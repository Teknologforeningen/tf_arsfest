from django.forms import ModelForm, RadioSelect
from models import Registration, Guest


class RegistrationForm(ModelForm):
    class Meta:
        model = Registration
        exclude = ('guest', 'avec', 'event', 'reference_number', 'sum')
        
class GuestForm(ModelForm):
    class Meta:
        model = Guest
        exclude = ('event')
        widgets = {'type': RadioSelect}
        
        
    