from django.db import models

from django.contrib.auth.models import User
from django.utils.translation import ugettext as _



class Entry(models.Model):
    
    
    message = models.CharField(verbose_name=_('Chat Message'),max_length=600, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    
    
    # meta
    class Meta:
        verbose_name = _('Entry')
        verbose_name_plural = _('Entries')
        ordering = ('-created', )
    
    def __unicode__(self):
        return "%s" % self.created
