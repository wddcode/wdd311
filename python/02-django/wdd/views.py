from django.views.generic import DetailView, ListView, FormView, UpdateView
from django.views.generic.detail import SingleObjectTemplateResponseMixin
from django.shortcuts import get_object_or_404, render_to_response

from django.http import HttpResponse, HttpResponseForbidden, Http404
from django.template import RequestContext

import json
from django.core import serializers



from wdd.models import Entry, Room


class RoomList(ListView):
    model = Room













class RoomDetail(DetailView):
    model = Room

    def get_context_data(self, **kwargs):
        context = super(RoomDetail, self).get_context_data(**kwargs)
        context['entries'] = Entry.objects.filter(room=self.object)
        return context



def home(request):
    data = {}
    return render_to_response('wdd/home.html', data, context_instance=RequestContext(request))


def chat(request, room=None, mimetype='json'):
    
    #entries = Entry.objects.all()
    
    #entries = Entry.objects.filter(user__id__gte=1)
    entries = Entry.objects.filter(user__username='ohrstrom')
        
    if mimetype == 'json':
        js = serializers.get_serializer("json")()
        data = js.serialize(entries, ensure_ascii=False)
        
        return HttpResponse(data, mimetype="application/json")
    
    if mimetype == 'html':
        
        return render_to_response('wdd/chat.html', {'entries': entries})
        # return HttpResponse('HTML', mimetype="text/html")



    