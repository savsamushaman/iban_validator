A step by step guid to project setup

!IMPORTANT! - This setup is done on WINDOWS

1. Create your virtual environment

execute => python -m venv env

2. Activate your virtual environment

execute => /env/Scripts/activate

optional steps\*
Update your pip, setuptools and wheel, execute => python -m pip install --upgrade pip setuptools wheel

3. Install dependencies

execute => pip install -r requirements.txt

4. Start the server

cd into => iban_validator\iban_validator
execute => python manage.py makemigrations
execute => python manage.py migrate
optional\*) execute => python manage.py createsuperuser (to create the admin user)
execute => python manage.py runserver
