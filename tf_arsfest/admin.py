from django.contrib import admin
from models import Guest, Event, GuestType, Registration
import csv
from django.http import HttpResponse

admin.site.register(Registration)
admin.site.register(GuestType)

 
 
def export_as_csv(modeladmin, request, queryset):
    """ 
        Based on http://djangosnippets.org/snippets/2712/
    """
    opts = modeladmin.model._meta

    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=%s.csv' % (unicode(opts).replace('.', '_'))
    writer = csv.writer(response)
    
    field_names = ['name', 'allergies', 'nonalcoholic']
    field_labels = ['Namn', 'Allergier/Dieter', 'Alkoholfri', 'Avec']
    
    writer.writerow([unicode(label).encode('utf-8') for label in field_labels])
 
    for obj in queryset:
        guests = Guest.objects.filter(event__name=obj.name)
        for guest in guests:
            try:
                avec = Registration.objects.get(guest=guest).avec or Registration.objects.get(avec=guest).guest
            except:
                avec = None
            fields = [unicode(getattr(guest, field)).encode('utf-8') for field in field_names]
            fields.append(avec)
            writer.writerow(fields)
    return response

class EventModelAdmin(admin.ModelAdmin):
    actions = [export_as_csv]
 
admin.site.register(Event, EventModelAdmin)

class GuestAdmin(admin.ModelAdmin):
    list_filter = ('event__name',)
    
admin.site.register(Guest, GuestAdmin)
