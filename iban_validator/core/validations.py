from rest_framework import serializers
from core.utils import iban_is_genuine

# Move this to settings.py ?
ALLOWED_COUNTRIES = {
    'ME': 22,
}


### Validations of the field 'iban' ###

def validate_country_code(iban:str) -> None:
    """Validates the country code of IBAN number"""
    country_code = iban[:2]
    
    if not country_code.isalpha():
        raise serializers.ValidationError("The first two characters of the IBAN must be the country code (example: ME)")
    
    if country_code not in ALLOWED_COUNTRIES.keys():
        # optional check, can be deleted if other countires are added
        raise serializers.ValidationError('Invalid country code. Only IBANs originating from Montenegro are allowed')

    return True


def validate_iban_len(iban:str) -> None:
    # validates the len of the IBAN number, assuming the spaces were removed beforehand
    if len(iban) < 15:
        raise serializers.ValidationError("Ensure this field has at least 15 characters. (Spaces don't count as characters)")

def validate_iban_len_country_specific(iban:str) -> None:
    country_code = iban[:2]
    expected_iban_len = ALLOWED_COUNTRIES.get(country_code)

    if expected_iban_len != len(iban):
        raise serializers.ValidationError(f"IBANs originating from {country_code} should be {expected_iban_len} characters long. IBAN is {len(iban)} characters long.")
    
    return True



####################################
# Quote from the challenge:
#
# Validation history: 
# Implement a feature that stores and provides access to the history of validated IBANs. 
# The API should offer an endpoint to retrieve a list of validated IBANs along with their **validation status** and timestamps.

# The fact that the stored model instance has a **validation status** lets me think that IBANs that are formatted OK but !not valid! are allowed to be stored
# I will implement this check with a switch that allows this feature to be turned on and off

def iban_is_valid(iban:str, allow_invalid=False) -> None:
    """Check if the IBAN number is valid, and not a random one"""
    if not iban_is_genuine(iban):
        if not allow_invalid:
            raise serializers.ValidationError({"iban": "The IBAN is invalid",})
        return False
    return True
