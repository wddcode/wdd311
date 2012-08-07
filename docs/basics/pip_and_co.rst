**********
Quickstart Session
**********

You need to define a :class:`~cms.models.fields.PlaceholderField` on the model you would like to
use::

    from django.db import models
    from cms.models.fields import PlaceholderField

    class MyModel(models.Model):
        # your fields
        my_placeholder = PlaceholderField('placeholder_name')
        # your methods