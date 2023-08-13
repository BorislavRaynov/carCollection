from django.core.exceptions import ValidationError

def check_valid_year(value):
    if not 1980 <= value <= 2049:
        raise ValidationError('Year must be between 1980 and 2049')