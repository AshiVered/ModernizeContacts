import re
import quopri

input_file = "original.vcf"
output_file = "contacts_converted_utf8.vcf"

def unfold_lines(text):
    """
    מאחד שורות עם המשך (כמו בגוגל):
    1. שורות שמתחילות ברווח או טאב
    2. שורות שנשברו באמצע רצף קידוד (נגמרות ב- '=')
    """
    # מאחד שבירות רכות (quoted-printable soft line breaks)
    text = re.sub(r"=\r?\n", "", text)
    # מאחד שורות שמתחילות ברווח
    text = re.sub(r"\r?\n[ \t]", "", text)
    return text

def decode_quoted_printable_field(line):
    # מנקה תגיות ופותח את הקידוד
    line = re.sub(r"CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:", "", line)
    decoded = quopri.decodestring(line).decode("utf-8", errors="ignore")
    return decoded

def convert_vcard(vcard_text):
    vcard_text = unfold_lines(vcard_text)
    vcard_text = vcard_text.replace("VERSION:2.1", "VERSION:3.0")
    vcard_text = vcard_text.replace("TEL;CELL:", "TEL;TYPE=CELL:")

    # מפענח FN ו-N
    vcard_text = re.sub(
        r"(FN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:)(.+)",
        lambda m: "FN:" + decode_quoted_printable_field(m.group(2)),
        vcard_text
    )
    vcard_text = re.sub(
        r"(N;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:)(.+)",
        lambda m: "N:" + decode_quoted_printable_field(m.group(2)),
        vcard_text
    )

    # תיקון FN/N אם הסדר הפוך
    match_n = re.search(r"^N:(.*)$", vcard_text, re.MULTILINE)
    match_fn = re.search(r"^FN:(.*)$", vcard_text, re.MULTILINE)
    if match_n:
        n_parts = match_n.group(1).split(";")
        while len(n_parts) < 5:
            n_parts.append("")
        last, first = n_parts[0].strip(), n_parts[1].strip()
        if match_fn:
            fn = match_fn.group(1).strip()
            if not fn or (first and last and fn == f"{last} {first}"):
                new_fn = f"FN:{first} {last}".strip()
                vcard_text = re.sub(r"^FN:.*$", new_fn, vcard_text, flags=re.MULTILINE)

    # מוסיף קטגוריה
    if "CATEGORIES:" not in vcard_text:
        vcard_text = vcard_text.strip() + "\nCATEGORIES:יובא בתאריך 2.11,myContacts\n"

    return vcard_text.strip() + "\nEND:VCARD\n"

# קריאת כל התוכן
with open(input_file, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

# מאחד שבירות שורה
content = unfold_lines(content)
cards = content.split("END:VCARD")

converted = []
for c in cards:
    c = c.strip()
    if not c:
        continue
    converted.append(convert_vcard(c))

with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(converted))

print(f"✅ נוצר קובץ תקין בשם: {output_file}")
