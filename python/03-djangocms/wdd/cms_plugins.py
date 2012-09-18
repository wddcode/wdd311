from django.db import models
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool


from django.utils.translation import ugettext as _

from wdd.models import RoomPlugin as RoomPluginModel

@plugin_pool.register_plugin
class RoomPlugin(CMSPluginBase):
    model = RoomPluginModel
    name = _("Chat Plugin")
    render_template = "wdd/plugins/room.html"

    # meta
    class Meta:
        app_label = 'wdd'

    def render(self, context, instance, placeholder):
        
        context.update({
            'instance': instance,
            'object': instance.room,
            'placeholder': placeholder,
        })
        return context
