from django.views.generic import DetailView, ListView, FormView, UpdateView, CreateView
from django.views.generic.detail import SingleObjectTemplateResponseMixin
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseForbidden, Http404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.utils.functional import lazy 
from feedback.models import *
from feedback.forms import *

class FeedbackList(ListView):
    model = Feedback

class FeedbackDetail(DetailView):
    model = Feedback
    
"""
class FeedbackCreate(CreateView):
    template_name = 'feedback/feedback_create.html'
    form_class = FeedbackForm
    success_url = lazy(reverse, str)("feedback-feedback-list")  
"""