`A step by step guid to project setup`

!IMPORTANT! - This setup is done on WINDOWS

1.  Create your virtual environment

        python -m venv env

2.  Activate your virtual environment

        /env/Scripts/activate

        (optional) Update your pip, setuptools and wheel,
        python -m pip install --upgrade pip setuptools wheel

3.  Install dependencies

        pip install -r requirements.txt

4.  Start the server

        cd iban_validator
        python manage.py makemigrations
        python manage.py migrate
        (optional) python manage.py createsuperuser (to create the admin user)
        python manage.py runserver

`For a list of API endpoints, go to (or send GET request to): http://127.0.0.1:8000/api/`

For a list of previously validated IBAN numbers send a GET request to http://127.0.0.1:8000/api/ibans/

To validate your IBAN number send a POST request to http://127.0.0.1:8000/api/ibans/.

`Requests examples`

{
"iban": "ME25505000012345678951"
}

It is possible to turn off the saving of the IBAN to the database,
just set the "commit" field to false

{
"iban": "ME25505000012345678951"
"commit": false
}

`Response examples`

Response will contain the following fields [iban[string], is_valid[boolean], errors[list]]

If the IBAN is valid:

{
"iban": "ME25505000012345678951",
"is_valid": true,
"errors": []
}

If the IBAN is invalid:

{
"iban": "XE25505000012345678952",
"is_valid": false,
"errors": [
"Invalid country code. Only IBANs originating from Montenegro are allowed. Valid country codes: ME."
]
}

`For details about the IBAN validation, check /iban_validator/core/validations.py !`
