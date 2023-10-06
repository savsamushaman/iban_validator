from django.contrib.auth import get_user_model
from rest_framework import serializers
from core.models import IBAN
from core.validations import validate_country_code, validate_iban_len, iban_is_valid, validate_iban_len_country_specific


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['url', 'username', 'email', 'groups']


class GetIBANSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = "__all__"
        model = IBAN

class PostIBANSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IBAN
        fields = ['iban', 'is_valid']
        extra_kwargs = {
            'is_valid': {'read_only': True},
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

        # add the allow_invalid = True keyword argument to the iban_is_valid function
        # to enable the storing of well formatted but invalid IBANs
        if iban_is_valid(data['iban']):
            data['is_valid'] = True
        else:
            data['is_valid'] = False

        data['country_code'] = data['iban'][:2]
        

        return data