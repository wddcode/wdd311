from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

from cms.models import CMSPlugin

class Room(models.Model):

    name = models.CharField(verbose_name=_('Room Name'), max_length=40, null=False, blank=True)
    description = models.CharField(max_length=600, null=True, blank=True)
    
    # meta
    class Meta:
        verbose_name = _('Room')
        verbose_name_plural = _('Rooms')
        ordering = ('name', )

    def __unicode__(self):
        return "%s" % self.name

    @models.permalink
    def get_absolute_url(self):
        return ('room-detail', [self.pk])
    
""""""



class Entry(models.Model):

    message = models.CharField(verbose_name=_('Chat Message'), max_length=600, null=False, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    room = models.ForeignKey(Room, null=True, blank=True)
    
    # meta
    class Meta:
        verbose_name = _('Entry')
        verbose_name_plural = _('Entries')
        ordering = ('-created', )

    
    def __unicode__(self):
        return "%s" % self.created



class RoomPlugin(CMSPlugin):    
    room = models.ForeignKey('wdd.Room', related_name='plugins')
    def __unicode__(self):
        return "%s" % self.room.name
