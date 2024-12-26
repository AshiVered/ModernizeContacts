# ModernizeContacts - Contact Update Tool


**ModernizeContacts** is a tool to extract and merge contacts from an NBF file into a VCF file.
It uses 7zip to extract files and combines VCF files into one.
A detailed log file is generated for every action.


## Description

The tool extracts VCF files from an NBF archive, merges them into one, and saves the merged file to a selected folder.
A log file is created for tracking the process.

If you want to skip all the following steps, simply download the zip file from the releases page, extract it, and run it.

## System Requirements

- Python 3.x
- 7zip (7z.exe)
- Tkinter (for GUI)
- Windows OS


## Installation & Usage

### 1. Install Python & PyInstaller

Ensure Python is installed (https://python.org).
Then install PyInstaller:
pip install pyinstaller


### 2. Compile the Script

Run this command to compile to .exe:
pyinstaller --onefile --windowed --icon=res/icon.ico ModernizeContacts.py


### 3. Running the Software

After compiling, run the .exe from the 'dist' folder.
Select the NBF file, choose the save folder, and click "Run" to start the extraction and merging process.


## Log File

A log file will be created detailing each action during the process.


## Contributor

Feel free to open an Issue or submit a Pull Request.


---

# ModernizeContacts


הוא כלי לחילוץ ואיחוד אנשי קשר מקובץ NBF לקובץ VCF.
הכלי עושה שימוש ב-7zip לחילוץ קבצים ומאחד את קבצי ה-VCF לקובץ אחד.
קובץ לוג מפורט נוצר לכל פעולה.


## תיאור

הכלי מחלץ קבצי VCF מתוך ארכיון NBF, מאחד אותם לקובץ אחד ושומר את הקובץ המאוחד בתיקייה שנבחרה.
קובץ לוג נוצר למעקב אחרי התהליך.

אם אתה רוצה לדלג על כל השלבים הבאים, פשוט הורד את קובץ הzip מדף השחרורים, חלץ והרץ.

## דרישות מערכת

- Python 3.x
- 7zip (7z.exe)
- Tkinter (ל-GUI)
- מערכת הפעלה Windows


## התקנה ושימוש

### 1. התקנת Python ו-PyInstaller

יש לוודא ש-Python מותקן (https://python.org).
לאחר מכן יש להתקין את PyInstaller:
pip install pyinstaller


### 2. קימפול של הסקריפט

להריץ את הפקודה הבאה כדי לקמפל ל-.exe:
pyinstaller --onefile --windowed --icon=res/icon.ico ModernizeContacts.py


### 3. הרצת התוכנה

לאחר הקומפילציה, יש להריץ את הקובץ .exe מתוך תיקיית 'dist'.
יש לבחור את קובץ ה-NBF, לבחור את תיקיית השמירה וללחוץ על "Run" כדי להתחיל בתהליך החילוץ והאיחוד.


## קובץ לוג

קובץ לוג ייווצר כדי לפרט את כל הפעולות שבוצעו במהלך התהליך.


## תורמים

אל תהססו לפתוח Issue או לשלוח Pull Request.

