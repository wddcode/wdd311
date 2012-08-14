from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

class Blog(models.Model):
    name = models.CharField(max_length=200)
    
    # meta
    class Meta:
        verbose_name = _('Artist')
        verbose_name_plural = _('Artists')
        ordering = ('name', )
    
    def __unicode__(self):
        return self.name
