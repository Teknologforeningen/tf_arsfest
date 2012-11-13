from django.db import models


class Participant(models.Model):
    # Name
    name = models.CharField(max_length=90, verbose_name="Namn")
    
    # Email
    email = models.EmailField(verbose_name="E-post adress")
    
    # Phone
    phone = models.CharField(max_length=20, verbose_name="Telefonnummer")
    
    # Allergies
    allergies = models.TextField(verbose_name="Allergier")
    
    # Student or not
    type = models.ForeignKey('ParticipantType', verbose_name="Deltagartyp")
    
    # Avec
    avec = models.ForeignKey('Participant', verbose_name="Avec", null=True, blank=True)
    
class Event(models.Model):
    # Date&Time
    date = models.TimeField()
    
    
class ParticipantType(models.Model):
    # Name of type
    name = models.CharField(max_length=50)