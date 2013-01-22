from django.forms import ModelForm
from models import Registration, Guest


class RegistrationForm(ModelForm):
    class Meta:
        model = Registration
        exclude = ('guest', 'avec')
        
class GuestForm(ModelForm):
    class Meta:
        model = Guest
        
        
    