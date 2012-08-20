from django.contrib import admin

from wdd.models import *

class EntryAdmin(admin.ModelAdmin):
    
    list_display = ('created', 'user',)
    list_filter= ('user',)
    
    date_hierarchy = 'created'


admin.site.register(Entry, EntryAdmin)













