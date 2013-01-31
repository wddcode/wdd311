# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Feedback.whatever'
        db.add_column('feedback_feedback', 'whatever',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Feedback.whatever'
        db.delete_column('feedback_feedback', 'whatever')


    models = {
        'feedback.feedback': {
            'Meta': {'ordering': "('-created',)", 'object_name': 'Feedback'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'whatever': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['feedback']