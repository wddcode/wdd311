from django.contrib import admin
from feedback.models import *

"""
class FeedbackAdmin(admin.ModelAdmin):	
    list_display = ('created', 'name', 'email')
    list_filter = ('name',)
    date_hierarchy = 'created'

admin.site.register(Feedback, FeedbackAdmin)
"""

admin.site.register(Feedback)












