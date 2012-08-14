from django.views.generic import DetailView, ListView, FormView, UpdateView
from django.views.generic.detail import SingleObjectTemplateResponseMixin
from django.shortcuts import get_object_or_404, render_to_response

from django.http import HttpResponse, HttpResponseForbidden, Http404
from django.template import RequestContext

import json


def home(request):
    
    data = {}

    return render_to_response('wdd/home.html', data, context_instance=RequestContext(request))
