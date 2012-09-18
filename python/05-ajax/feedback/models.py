from django.db import models
from django.utils.translation import ugettext as _


class Feedback(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=256)
    comment = models.TextField()
    
    created = models.DateTimeField(auto_now_add=True)
    
    # meta
    class Meta:
        verbose_name = _('Feedback')
        verbose_name_plural = _('Feedbacks')
        ordering = ('-created', )

    def __unicode__(self):
        return "%s : %s" % (self.created, self.name)

    @models.permalink
    def get_absolute_url(self):
        return ('feedback-feedback-detail', [self.pk])

