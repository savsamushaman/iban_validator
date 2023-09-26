import string

LETTERS = {ord(d): str(i) for i, d in enumerate(string.digits + string.ascii_uppercase)}

# for information how IBAN numbers are validated see:
# https://en.wikipedia.org/wiki/International_Bank_Account_Number#Validating_the_IBAN

def translate_iban(iban:str) -> str:
    """Translates letters to numbers"""
    return (iban[4:] + iban[:4]).translate(LETTERS)

def valid_iban(iban:str) -> bool:
    """Check the validity of the iban"""
    return int(translate_iban(iban)) % 97 == 1

def generate_iban_check_digits(iban) -> str:
    """Generate the check digits"""
    iban_number = translate_iban(iban[:2] + '00' + iban[4:])
    return '{:0>2}'.format(98 - (int(iban_number) % 97))

def iban_is_genuine(iban) -> bool:
    """Check if the iban is a genuine one, using the IBAN check digits"""
    if generate_iban_check_digits(iban) == iban[2:4] and valid_iban(iban):
        return True
    return False