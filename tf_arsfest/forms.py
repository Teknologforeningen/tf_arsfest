from django.forms import ModelForm
from models import Guest


class RegistrationForm(ModelForm):
    class Meta:
        model = Guest
        
        
    