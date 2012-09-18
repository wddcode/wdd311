from django.conf.urls.defaults import *
from feedback.views import *

urlpatterns = patterns('',

    url(r'^$', FeedbackList.as_view(), name='feedback-feedback-list'),
    url(r'^add/$', FeedbackCreate.as_view(), name='feedback-feedback-add'),
    url(r'^(?P<pk>\d+)/$', FeedbackDetail.as_view(), name='feedback-feedback-detail'),

)