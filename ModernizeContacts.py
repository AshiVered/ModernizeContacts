import os
import subprocess
import shutil
import stat
import tkinter as tk
from tkinter import filedialog, messagebox, Toplevel
import webbrowser

# נתיב לתיקיית המשאבים
RESOURCE_FOLDER = "res"
ICON_PATH = os.path.join(RESOURCE_FOLDER, "icon.ico")
SEVEN_ZIP_PATH = os.path.join(RESOURCE_FOLDER, "7z.exe")

def find_vcf_files(root_folder):
    """חיפוש קבצי VCF בתיקייה ובתת-תיקיות"""
    vcf_files = []
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.endswith(".vcf"):
                vcf_files.append(os.path.join(root, file))
    return vcf_files

def on_rm_error(func, path, exc_info):
    """מטפל בשגיאות מחיקה על ידי שינוי הרשאות"""
    os.chmod(path, stat.S_IWRITE)  # הסרת קריאה בלבד והוספת כתיבה
    func(path)

import logging

# הגדרת קובץ הלוג
log_file = "process_log.txt"
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_nbf(file_path, save_path):
    extracted_folder = "extracted_nbf"
    try:
        # בדיקה אם 7z.exe קיים בתיקיית המשאבים
        if not os.path.exists(SEVEN_ZIP_PATH):
            messagebox.showerror("שגיאה", "7z.exe לא נמצא בתיקיית המשאבים.")
            logging.error("7z.exe לא נמצא בתיקיית המשאבים.")
            return
        
        # יצירת תיקיה זמנית לחילוץ
        os.makedirs(extracted_folder, exist_ok=True)
        
        # חילוץ קובץ NBF באמצעות 7z.exe
        result = subprocess.run(
            [SEVEN_ZIP_PATH, "x", file_path, "-o" + extracted_folder],
            capture_output=True,
            text=True
        )
        logging.info(f"7z STDOUT:\n{result.stdout}")
        logging.info(f"7z STDERR:\n{result.stderr}")
        #אם התוכנה קורסת - לשמור לוג מפורט
        if result.returncode != 0:
            error_filename = f"7z_error_{int(__import__('time').time())}.txt"
            with open(error_filename, "w", encoding="utf-8") as f:
                f.write("פקודה:\n")
                f.write(" ".join([SEVEN_ZIP_PATH, "x", file_path, "-o" + extracted_folder]) + "\n\n")
                f.write("STDOUT:\n")
                f.write(result.stdout + "\n")
                f.write("STDERR:\n")
                f.write(result.stderr + "\n")
                f.write(f"\nקוד חזרה: {result.returncode}\n")
            logging.error(f"שגיאה בהרצת 7z, ראה קובץ שגיאה: {error_filename}")
            messagebox.showerror("שגיאת 7z", f"שגיאה בחילוץ הקובץ.\nראה פרטים בקובץ:\n{error_filename}")
            return

        logging.info(f"חולץ קובץ NBF מ-{file_path}")
        
        # חיפוש קבצי VCF בתיקייה המחולצת
        vcf_files = find_vcf_files(extracted_folder)
        logging.info(f"נמצאו {len(vcf_files)} קבצי VCF בתיקייה המחולצת.")
        
        if not vcf_files:
            messagebox.showerror("שגיאה", "לא נמצאו קבצי VCF בתיקייה המחולצת.")
            logging.warning("לא נמצאו קבצי VCF בתיקייה המחולצת.")
            return
        
        # איחוד קבצי VCF
        combined_vcf_path = os.path.join(save_path, "extracted.vcf")
        with open(combined_vcf_path, "wb") as combined_vcf:  # פתיחה כקובץ בינארי
            for vcf_file in vcf_files:
                with open(vcf_file, "rb") as vcf:  # קריאה כקובץ בינארי
                    shutil.copyfileobj(vcf, combined_vcf)  # העתקת התוכן בינארית
                    logging.info(f"קובץ VCF נוסף: {vcf_file}")
        
        # הודעה על הצלחה והצגת מספר אנשי הקשר
        messagebox.showinfo("הצלחה", f"חולצו {len(vcf_files)} אנשי קשר.\nקובץ VCF נשמר בהצלחה בנתיב:\n{combined_vcf_path}")
        logging.info(f"חולצו {len(vcf_files)} אנשי קשר. הקובץ נשמר בנתיב: {combined_vcf_path}")
        
    except subprocess.CalledProcessError as e:
        messagebox.showerror("שגיאה בהרצת פקודה", f"{e}")
        logging.error(f"שגיאה בהרצת פקודה: {e}")
    except Exception as e:
        messagebox.showerror("שגיאה כללית", f"{e}")
        logging.error(f"שגיאה כללית: {e}")
    finally:
        # ניקוי התיקיה המחולצת עם טיפול בשגיאות הרשאה
        if os.path.exists(extracted_folder):
            for root, dirs, files in os.walk(extracted_folder, topdown=False):
                for name in files:
                    file_path = os.path.join(root, name)
                    os.chmod(file_path, stat.S_IWRITE)  # שינוי הרשאות קובץ
                    os.remove(file_path)
                    logging.info(f"נמחק קובץ: {file_path}")
                for name in dirs:
                    dir_path = os.path.join(root, name)
                    os.chmod(dir_path, stat.S_IWRITE)  # שינוי הרשאות תיקייה
                    os.rmdir(dir_path)
                    logging.info(f"נמחק תיקייה: {dir_path}")
            os.rmdir(extracted_folder)
            logging.info(f"נמחקה התיקיה הזמנית: {extracted_folder}")




def select_nbf_file():
    """פתיחת חלון לבחירת קובץ NBF"""
    file_path = filedialog.askopenfilename(title="בחר קובץ NBF", filetypes=[("NBF Files", "*.NBF")])
    if file_path:
        nbf_file_var.set(file_path)

def select_save_folder():
    """פתיחת חלון לבחירת תיקייה לשמירה"""
    folder_path = filedialog.askdirectory(title="בחר תיקייה לשמירה")
    if folder_path:
        save_folder_var.set(folder_path)

def run_extraction():
    """הרצת תהליך החילוץ והעיבוד"""
    nbf_file = nbf_file_var.get()
    save_folder = save_folder_var.get()
    if not nbf_file:
        messagebox.showerror("שגיאה", "יש לבחור קובץ NBF.")
        return
    if not save_folder:
        messagebox.showerror("שגיאה", "יש לבחור תיקייה לשמירה.")
        return
    process_nbf(nbf_file, save_folder)

def open_about():
    """פתיחת חלון 'אודות'"""
    about_window = Toplevel(root)
    about_window.title("About")
    about_window.geometry("300x200")
    about_window.iconbitmap(ICON_PATH)  # טעינת האייקון לחלון
    
    tk.Label(about_window, text="ModernizeContacts", font=("Arial", 14, "bold")).pack(pady=5)
    tk.Label(about_window, text="v1.0", font=("Arial", 10)).pack(pady=5)
    tk.Label(about_window, text="A.I.V Dev", font=("Arial", 10)).pack(pady=10)

    # שורה לחיצה עבור GitHub
    github_label = tk.Label(
        about_window,
        text="GitHub",
        font=("Arial", 10, "underline"),
        fg="blue",
        cursor="hand2"
    )
    github_label.pack()
    github_label.bind("<Button-1>", lambda e: webbrowser.open("https://github.com/AshiVered/ModernizeContacts"))

    # שורה לחיצה עבור icons8
    icons8_label = tk.Label(
        about_window,
        text="Icons by icons8",
        font=("Arial", 10, "underline"),
        fg="blue",
        cursor="hand2"
    )
    icons8_label.pack()
    icons8_label.bind("<Button-1>", lambda e: webbrowser.open("https://icons8.com"))


# יצירת חלון GUI
root = tk.Tk()
root.title("ModernizeContacts")
root.iconbitmap(ICON_PATH)  # הגדרת האייקון לחלון הראשי
# משתנים לאחסון הנתיבים שנבחרו
nbf_file_var = tk.StringVar()
save_folder_var = tk.StringVar()

# רכיבי ממשק
btn_width = 15  # רוחב לחצנים אחיד

tk.Label(root, text="קובץ NBF:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
tk.Entry(root, textvariable=nbf_file_var, state="readonly", width=50).grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="בחר קובץ", command=select_nbf_file, width=btn_width).grid(row=0, column=2, padx=5, pady=5)

tk.Label(root, text="תיקייה לשמירה:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
tk.Entry(root, textvariable=save_folder_var, state="readonly", width=50).grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text="בחר תיקייה", command=select_save_folder, width=btn_width).grid(row=1, column=2, padx=5, pady=5)

tk.Button(root, text="בצע", command=run_extraction, width=btn_width).grid(row=2, column=0, columnspan=3, pady=10)

# לחצן מידע
tk.Button(root, text="i", command=open_about, font=("Arial", 10, "bold")).grid(row=3, column=0, sticky="w", padx=5, pady=5)

# הרצת לולאת ה-GUI
root.mainloop()