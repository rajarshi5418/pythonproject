2


from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

validate = URLValidator()
value = request.GET.get('url', None)

if value:        
    try:
        validate(value)
    except ValidationError:
        print("no")