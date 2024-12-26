# ModernizeContacts


**ModernizeContacts** היא תוכנה שנועדה לחלץ אנשי קשר מקובץ NBF וליצור קובץ VCF מאוחד.
התוכנה משתמשת ב-7zip לחילוץ קבצים מתוך קובץ NBF ומבצעת מיזוג של קבצי ה-VCF שנמצאו.
בנוסף, התוכנה מאפשרת יצירת קובץ לוג מפורט לכל פעולה שהיא מבצעת.


## תיאור התוכנה

התוכנה מבצעת את הפעולות הבאות:
1. חילוץ קבצי VCF מקובץ NBF.
2. מיזוג קבצי ה-VCF לקובץ אחד.
3. שמירת הקובץ הממוזג בתיקייה שנבחרה.
4. יצירת קובץ לוג שמפרט את כל הפעולות.

היישום מציע ממשק גרפי (GUI) נוח שמאפשר לבחור את קובץ ה-NBF ואת תיקיית השמירה,
ולהתחיל את תהליך החילוץ והעיבוד.


## דרישות מערכת
- Python 3.x
- 7zip (7z.exe)
- Tkinter (לממשק הגרפי)
- מערכת הפעלה: Windows
"""

# -----------------------------------
## הוראות התקנה והפעלה

### 1. התקנת Python
"""
אם אין לך את Python מותקן, תוכל להוריד אותו מאתר הרשמי: 
https://www.python.org/downloads/
"""

### 2. התקנת PyInstaller
"""
להפוך את הקוד לקובץ .exe, יש להתקין את הכלי PyInstaller:
"""
# הרצת פקודת התקנה של PyInstaller:
"""
pip install pyinstaller
"""

### 3. הוראות קימפול לקובץ .exe
"""
כדי לקמפול את הקוד לקובץ .exe, הרץ את הפקודה הבאה בתיקיית הפרויקט:
"""
# הרצת פקודת קימפול:
"""
pyinstaller --onefile --windowed --icon=res/icon.ico ModernizeContacts.py
"""

### 4. הרצת התוכנה
"""
לאחר הקימפול, תוכל להריץ את קובץ ה-.exe שנמצא בתיקיית dist:
"""
# פקודת הרצה של התוכנה:
"""
dist/ModernizeContacts.exe
"""

# -----------------------------------
## שימוש בתוכנה
"""
1. הפעל את התוכנה על ידי לחיצה על קובץ ה-.exe.
2. בחר את קובץ ה-NBF שברצונך לחלץ.
3. בחר תיקייה שבה תישמר תוצאת החילוץ.
4. לחץ על כפתור "בצע" כדי להתחיל את התהליך.
5. לאחר סיום התהליך, יישמר קובץ VCF עם כל אנשי הקשר בתיקייה שנבחרה.

בנוסף, תוכל להציג את המידע אודות התוכנה על ידי לחיצה על כפתור ה-"i".
"""

# -----------------------------------
## קובץ לוג
"""
התוכנה יוצרת קובץ לוג שכולל את כל הפעולות שבוצעו.
קובץ הלוג נשמר באותו מיקום שבו נמצאים קבצי התוכנית ומכיל מידע על תהליך החילוץ,
כולל כל קובץ VCF שנמצא והפעולות שבוצעו.
"""

# -----------------------------------
## פיתוח
"""
אם ברצונך לתרום לפרויקט או לדווח על בעיות, אתה מוזמן לפתוח Issue או לשלוח Pull Request.
"""


# ModernizeContacts - Contact Update Tool

"""
**ModernizeContacts** is a tool designed to extract contacts from an NBF file and create a merged VCF file.
The software uses 7zip to extract files from the NBF and merges any found VCF files into a single one.
Additionally, the tool creates a detailed log file for every action it performs.
"""

# -----------------------------------
## תוכן התוכנה / Software Description
"""
The software performs the following actions:
1. Extracts VCF files from the NBF file.
2. Merges the VCF files into a single one.
3. Saves the merged file to the selected directory.
4. Creates a detailed log file with all actions performed.

The application provides an easy-to-use GUI interface that allows you to select the NBF file and the save folder,
and then start the extraction and processing process.
"""
# -----------------------------------

## דרישות מערכת / System Requirements
"""
- Python 3.x
- 7zip (7z.exe)
- Tkinter (for the GUI interface)
- Operating system: Windows
"""

# -----------------------------------
## הוראות התקנה והפעלה / Installation and Usage Instructions

### 1. התקנת Python / Installing Python
"""
If you don't have Python installed, you can download it from the official website: 
https://www.python.org/downloads/
"""

### 2. התקנת PyInstaller / Installing PyInstaller
"""
To compile the script into an .exe file, you need to install PyInstaller:
"""
# Install PyInstaller using the command:
"""
pip install pyinstaller
"""

### 3. הוראות קימפול לקובץ .exe / Compiling to .exe
"""
To compile the script into an .exe file, run the following command in the project folder:
"""
# Run the compilation command:
"""
pyinstaller --onefile --windowed --icon=res/icon.ico ModernizeContacts.py
"""

### 4. הרצת התוכנה / Running the Software
"""
After compiling, you can run the .exe file located in the 'dist' folder:
"""
# Run the software using:
"""
dist/ModernizeContacts.exe
"""

# -----------------------------------
## שימוש בתוכנה / How to Use the Software
"""
1. Launch the software by clicking on the .exe file.
2. Select the NBF file you want to extract contacts from.
3. Select the folder where the result will be saved.
4. Click the "Run" button to begin the process.
5. After the process is complete, the merged VCF file will be saved to the selected directory.

Additionally, you can view the software information by clicking the "i" button.
"""

# -----------------------------------
## קובץ לוג / Log File
"""
The software creates a log file that includes all the actions performed.
The log file is saved in the same location as the program files and contains information about the extraction process,
including each VCF file found and the actions performed.
"""

# -----------------------------------
## Contributor
"""
If you want to contribute to the project or report issues, feel free to open an Issue or submit a Pull Request.
"""

