from django.contrib.auth import get_user_model
from rest_framework import serializers
from core.models import IBAN
from core.validations import validate_country_code, validate_iban_len, iban_is_valid, validate_iban_len_country_specific


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['url', 'username', 'email', 'groups']


class IBANSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = IBAN
        fields = ['iban', 'country_code', 'is_valid', 'validation_date']

        extra_kwargs = {
            'country_code': {'read_only': True},
            'is_valid': {'read_only': True},
            'validation_date': {'read_only': True},
        }
    
    def validate_iban(self, value:str):

        # replace the spaces in the input string
        value = value.replace(' ','')
        value = value.upper()

        # Do not change the order of the validations, if you do, expect bugs
        validations = [
            validate_iban_len,
            validate_country_code,
            validate_iban_len_country_specific,
        ]

        for validation in validations:
            validation(value)

        return value
    
    def validate(self, data):
        super().validate(data)

        # allow_invalid = False, will disable the storing of well formatted but invalid IBANs
        if iban_is_valid(data['iban']):
            # is_valid is false by default
            data['is_valid'] = True
        else:
            data['is_valid'] = False

        data['country_code'] = data['iban'][:2]
        

        return data