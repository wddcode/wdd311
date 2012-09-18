from django import forms
from django.conf import settings
from django.utils.translation import ugettext as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import FormActions

from feedback.models import *


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        

    """
    def __init__(self, *args, **kwargs):

        super(FeedbackForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = "bulk_edit%s" % 'asd'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.form_tag = True

        layout = Layout(
            Fieldset(
                  'Your feedback',
                  Field('name'),
                  Field('email'),
                  Field('comment'),
            ),    
            FormActions(
                Submit('submit', 'Submit', css_class='btn btn-primary')
            ),
        )
        
        
        self.helper.add_layout(layout)
        """

    