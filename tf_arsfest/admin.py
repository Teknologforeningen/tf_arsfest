# --coding: UTF-8 --
import csv
from django.contrib import admin
from django.utils.encoding import smart_str, smart_unicode
from django.http import HttpResponse
from models import Guest, Event, GuestType, Registration
from views import send_registration_email

admin.site.register(GuestType) 

def resend_invoice_email(modeladmin, request, queryset):
    '''
    Skickar epost med räkningen pånytt till valda registreringar.
    '''
    for registration in queryset:
        data = registration.get_dictionary()
        send_registration_email(data)
    
 
def export_guests_as_csv(modeladmin, request, queryset):
    """ 
    Exportta alla gäster som hör till de valda eventsen.
    
    Based on http://djangosnippets.org/snippets/2712/
    """
    opts = modeladmin.model._meta

    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=%s.csv' % (unicode(opts).replace('.', '_'))
    writer = csv.writer(response)
    
    # Namn på fälten som gås igenom för vaje gäst. Tas från models.py
    field_names = ['name', 'allergies', 'nonalcoholic']
    field_labels = ['Par', 'Namn', 'Allergier/Dieter', 'Alkoholfri', 'Övrigt']
    
    #Skriv ut columnernas namn
    writer.writerow([smart_str(label) for label in field_labels])
 
    # Föv varhe fest
    for obj in queryset:
        guests = Guest.objects.filter(event__name=obj.name)
        for guest in guests:
            
            # Finns det en avec?
            avec = False
            try:
                registration = Registration.objects.get(guest=guest)
            except:
                try:
                    registration = Registration.objects.get(avec=guest)
                    avec=True
                except:
                    continue
            
            fields = [smart_str(getattr(guest, field)) for field in field_names]
            
            # Ersätt True med "Alkoholfri" och False med tom sträng
            if fields[2] == "False":
                fields[2] = "Alkoholfri"
            else:
                fields[2] = ""
            
            # Om avecen är vald som bordsdam/herre så sätts denne i samma grupp
            # Detta görs så att tableplanner programmet skall sätta dom nära varandra
            if avec and not getattr(registration, 'avecbutton'):
                fields.insert(0, str(registration.pk)+'b')
            else:
                fields.insert(0, registration.pk)
                
            fields.append(smart_str(getattr(registration, 'misc')))
                
            writer.writerow(fields)
    return response    


def prep_field(obj, field):
    """ Returns the field as a unicode string. If the field is a callable, it
    attempts to call it first, without arguments.
    """
    if '__' in field:
        bits = field.split('__')
        field = bits.pop()
 
        for bit in bits:
            obj = getattr(obj, bit, None)
 
            if obj is None:
                return ""
 
    attr = getattr(obj, field)
    output = attr() if callable(attr) else attr
    return unicode(output).encode('utf-8') if output else ""
 
 
def export_csv_action(description="Export as CSV", fields=None, exclude=None, header=True):
    """ This function returns an export csv action. """
    def export_as_csv(modeladmin, request, queryset):
        """ Generic csv export admin action.
        Based on http://djangosnippets.org/snippets/2712/
        """
        opts = modeladmin.model._meta
        field_names = [field.name for field in opts.fields]
        labels = []
 
        if exclude:
            field_names = [f for f in field_names if f not in exclude]
 
        elif fields:
            field_names = [field for field, _ in fields]
            labels = [label for _, label in fields]
 
        response = HttpResponse(mimetype='text/csv')
        response['Content-Disposition'] = 'attachment; filename=%s.csv' % (
                unicode(opts).replace('.', '_')
            )
 
        writer = csv.writer(response)
 
        if header:
            writer.writerow(labels if labels else field_names)
 
        for obj in queryset:
            writer.writerow([prep_field(obj, field) for field in field_names])
        return response
    export_as_csv.short_description = description
    return export_as_csv

class EventModelAdmin(admin.ModelAdmin):
    actions = [export_guests_as_csv]
 
admin.site.register(Event, EventModelAdmin)

class GuestAdmin(admin.ModelAdmin):
    list_filter = ('event__name',)
    
admin.site.register(Guest, GuestAdmin)

class RegistrationAdmin(admin.ModelAdmin):
    '''
    Custom admin funktioner för registreringar.
    '''
    list_filter = ('event__name',)
    
    # Bestäm vad som exportas från registreringarna
    actions = [
        export_csv_action("Export Registrations as CSV",
            fields=[
                    ('event', 'Fest'),
                    ('name', 'Förening/Post'),
                    ('solennakt', 'Solenn Akt'),
                    ('greeting', 'Hälsning'),
                    ('misc', 'Övrigt'),
                    ('avecbutton', 'Avec är par?'),
                    ('guest__name', 'Gäst'),
                    ('guest__allergies', 'Allergier/Diet'),
                    ('guest__nonalcoholic', 'Alkoholfri'),
                    ('avec__name', 'Avec'),
                    ('avec__allergies', 'Avec allergier'),
                    ('avec__nonalcoholic', 'Avec alkoholfri'),
            ],
            header=True
        ), resend_invoice_email]
    
admin.site.register(Registration, RegistrationAdmin)

