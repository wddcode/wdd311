from django.contrib.auth.models import User
from django.db.models import Count

from tastypie import fields
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

from wdd.models import *

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'auth/user'
        excludes = ['email', 'password', 'is_superuser', 'is_active', 'is_staff', 'id']
        
class RoomResource(ModelResource):
    
    entries = fields.ToManyField('wdd.api.EntryResource', 'entry_set', null=True, related_name='entry')
    
    class Meta:
        queryset = Room.objects.all()
        resource_name = 'rooms'
        include_absolute_url = True

class EntryResource(ModelResource):
    
    user = fields.ForeignKey(UserResource, 'user', null=True, full=True)
    room = fields.ForeignKey(RoomResource, 'room', null=True, full=True)

    class Meta:
        queryset = Entry.objects.all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'entries'
        excludes = ['id',]
        authorization = DjangoAuthorization()
        filtering = {
            'user': ALL_WITH_RELATIONS,
            'room': ALL_WITH_RELATIONS,
            'created': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        }

    def obj_create(self, bundle, request, **kwargs):
        
        bundle.data['user'] = {'pk': request.user.pk}
        
        if 'room_id' in bundle.data:
            bundle.data['room'] = {'pk': bundle.data['room_id']}

        return super(EntryResource, self).obj_create(bundle, request, **kwargs)