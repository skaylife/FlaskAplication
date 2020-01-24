## Monitor info
##### 1. Библиотеки

PyFladesk 1.1  ` pip install PyFladesk ` 
##### 2. Pyintaller Билд из py to exe

Windows:
` pyinstaller -w -F --add-data "templates;templates" --add-data "static;static" app.py `
Linux: 
` pyinstaller -w -F --add-data "templates:templates" --add-data "static:static" app.py `
