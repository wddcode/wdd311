##########
Quickstart Session
##########

You need to define a :function:`~cms.models.fields.PlaceholderField` on the model you would like to use::

    from django.db import models
    from cms.models.fields import PlaceholderField

    class MyModel(models.Model):
        # your fields
        my_placeholder = PlaceholderField('placeholder_name')
        # your methods
        

        
**********
easy_install & PIP
**********


==========
Install PIP
==========

::

    sudo easy_install PIP


==========
Install virtualenv
==========

::

    sudo pip install virtualenv
    
    
==========
Model Example | ``models/model.py``
==========

* this is shjdhfks dflskjhdf lsdkfjh slkdjfh http://example.com/ 
* a list

  * with a nested list
  * and some subitems

* and here the parent list continues

::

	from django.db import models
	from django.contrib.contenttypes.models import ContentType
	from django.contrib.contenttypes import generic
	
	VOTE_CHOICES = (
	    (+1, '+1'),
	    (-1, '-1'),
	)
	
	class Vote(models.Model):
	    
	    token = models.CharField(max_length=50)
	    vote = models.SmallIntegerField(choices=VOTE_CHOICES)
	
	    # generic foreign key to the model being voted upon
	    content_type = models.ForeignKey(ContentType)
	    object_id = models.PositiveIntegerField()
	    content_object = generic.GenericForeignKey('content_type', 'object_id')
	
	    class Meta:
	        app_label = 'arating'
	        verbose_name = _('Vote')
	        verbose_name_plural = _('Votes')
	        unique_together = (('token', 'content_type', 'object_id'),)
	
	
	    def __unicode__(self):
	        return '%s from %s on %s' % (self.get_vote_display(), self.token,
	                                     self.content_object)