# shop_database
To start the project you need to:
1. Install VisualStudioCode, aswell as Python (follow some tutorial from youtube.com)
2. Open Windows search field or VisualStudioCode terminal and type: pip3 install django
3. Download this repository through CODE green button and clicking Download ZIP.
4. Open it in VS Code.
5. Now type in VS code terminal:
```
python manage.py makemigrations 
python manage.py migrate
python manage.py createsuperuser (allows you to login to django admin panel "http://localhost:8000/admin/")
python manage.py runserver 8000 (8000 is localhost port)
```
To open consumer site you can use the following links:
```
http://localhost:8000/shop/user_login/ - RECOMENDED TO USE ONLY THIS!!!!!
http://localhost:8000/shop/shop/
http://localhost:8000/shop/added_to_cart/
http://localhost:8000/shop/adress/
```
If you want to open the whole database I recommend to install in VSC the following extension - SQLite. Now if u click CTRL+SHIFT+P and write SQLite: Open Database, you can select database to open. It should appear in left lower corner as SQ Lite Explorer. Then go down the list of tables and find ones that you want to check.
