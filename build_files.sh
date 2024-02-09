pip install --upgrade pip
pip install -r requirements.txt 
pip install --root-user-action=ignore

python manage.py collectstatic
