from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models


class CustomUser(AbstractUser):
    pass


class IBAN(models.Model):
    # Montenegro IBANs are 22char long
    # but in the future we may want to store IBANs from other countries
    # Shortest IBAN --> Norway 15char, Longest --> Malta 34
    iban = models.CharField(max_length=34, validators=[MinLengthValidator(15)])
    country_code = models.CharField(max_length=2)
    is_valid = models.BooleanField(default=False)
    validation_date = models.DateField(auto_now_add=True, blank=True)