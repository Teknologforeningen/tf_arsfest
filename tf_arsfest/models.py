# --coding: UTF-8 --
from django.db import models

class Guest(models.Model):
    # Name
    name = models.CharField(max_length=90, verbose_name="Namn")
    
    # Email
    email = models.EmailField(verbose_name="E-post adress")
    
    # Phone
    phone = models.CharField(max_length=20, verbose_name="Telefonnummer")
    
    # Allergies
    allergies = models.TextField(verbose_name="Allergier", blank=True)
    
    # Student or not
    type = models.ForeignKey('GuestType', verbose_name="Deltagartyp")
    
    # Alkoholfri
    nonalcoholic = models.BooleanField(verbose_name="Alkoholfri", default=False)
    
    # Silliz
    silliz = models.BooleanField(verbose_name="Sillfrukost")
    
    def __unicode__(self):
        return self.name
    
        
class Registration(models.Model):
    
    # Förening
    name = models.CharField(max_length=150, verbose_name="Förening", blank=True, null=True)
    
    # Deltar i solenn-akt
    solennakt = models.BooleanField(verbose_name="Deltar i solenn akt", default=False)
    
    # Framför hälsning
    greeting = models.BooleanField(verbose_name="Vill framföra hälsning", default=False)
    
    # Gäst
    guest = models.OneToOneField(Guest, related_name="guest", unique=True)
    
    # Avec
    avec = models.OneToOneField(Guest, blank=True, null=True, related_name="avec", unique=True)
    
    avecbutton = models.BooleanField(verbose_name="Avec")
    # Avec boolean
    
    def __unicode__(self):
        return self.name
    
class Event(models.Model):
    # Date&Time
    date = models.TimeField()
    
    # Name
    name = models.CharField(max_length=120, verbose_name="Händelsens namn")
    
    # Platser
    places = models.PositiveIntegerField(verbose_name="Max antal gäster")
    
    def __unicode__(self):
        return self.name
    
class GuestType(models.Model):
    
    # Name of type
    name = models.CharField(max_length=50, verbose_name="Namn (t.ex. studerande)")
    
    # Price
    price = models.PositiveIntegerField(verbose_name="Pris")
    
    def __unicode__(self):
        return "%s (%de)" % (self.name, self.price)
    
class Invoice(models.Model):
    reference_number = models.PositiveIntegerField(verbose_name="Referensnummer")
    sum = models.FloatField(verbose_name="Summa")