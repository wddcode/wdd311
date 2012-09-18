# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Feedback.comment'
        db.alter_column('feedback_feedback', 'comment', self.gf('django.db.models.fields.TextField')(default=None))

        # Changing field 'Feedback.email'
        db.alter_column('feedback_feedback', 'email', self.gf('django.db.models.fields.EmailField')(default=None, max_length=256))

    def backwards(self, orm):

        # Changing field 'Feedback.comment'
        db.alter_column('feedback_feedback', 'comment', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Feedback.email'
        db.alter_column('feedback_feedback', 'email', self.gf('django.db.models.fields.EmailField')(max_length=256, null=True))

    models = {
        'feedback.feedback': {
            'Meta': {'ordering': "('-created',)", 'object_name': 'Feedback'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['feedback']