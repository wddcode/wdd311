from django.contrib import admin

from wdd.models import *

class EntryAdmin(admin.ModelAdmin):
    
    list_display = ('created', 'user', 'room',)
    list_filter= ('user', 'room',)
    
    date_hierarchy = 'created'


admin.site.register(Entry, EntryAdmin)

class RoomAdmin(admin.ModelAdmin):
    
    list_display = ('name',)

admin.site.register(Room, RoomAdmin)













