from django.contrib import admin
from .models import Type, Time, Ticket, Janr, Regisser, Concert, Place

admin.site.register(Regisser)
admin.site.register(Type)
admin.site.register(Time)
admin.site.register(Ticket)
admin.site.register(Janr)
admin.site.register(Concert)
admin.site.register(Place)
