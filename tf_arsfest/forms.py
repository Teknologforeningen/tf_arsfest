from django.forms import ModelForm
from models import *


class RegistrationForm(ModelForm):
    class Meta:
        model = Participant
        
        
    