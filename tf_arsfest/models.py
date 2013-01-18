# --coding: UTF-8 --
from django.db import models


class Participant(models.Model):
    # Name
    name = models.CharField(max_length=90, verbose_name="Namn")
    
    # Email
    email = models.EmailField(verbose_name="E-post adress")
    
    # Phone
    phone = models.CharField(max_length=20, verbose_name="Telefonnummer")
    
    # Allergies
    allergies = models.TextField(verbose_name="Allergier", blank=True)
    
    # Student or not
    type = models.ForeignKey('ParticipantType', verbose_name="Deltagartyp")
    
    # Avec
    avec = models.OneToOneField('Participant', verbose_name="Avec", null=True, blank=True)
    
    def __unicode__(self):
        return self.name
    
class Event(models.Model):
    # Date&Time
    date = models.TimeField()
    
    # Name
    name = models.CharField(max_length=120, verbose_name="Händelsens namn")
    
    def __unicode__(self):
        return self.name
    
class ParticipantType(models.Model):
    
    # Name of type
    name = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.name
    
class Invoice(models.Model):
    reference_number = models.PositiveIntegerField()
    sum = models.FloatField()