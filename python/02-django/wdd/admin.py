from django.contrib import admin

from wdd.models import *

class EntryAdmin(admin.ModelAdmin):	
    
    list_display = ('created', 'user', 'room')
    list_filter = ('user',)

    date_hierarchy = 'created'


class RoomAdmin(admin.ModelAdmin):

    list_display = ('name', )

admin.site.register(Entry, EntryAdmin)
admin.site.register(Room, RoomAdmin)













