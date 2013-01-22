from django.contrib import admin
from models import Guest, Event, GuestType, Registration

admin.site.register(Registration)
admin.site.register(Guest)
admin.site.register(Event)
admin.site.register(GuestType)
