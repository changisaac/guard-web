from django.conf.urls import url
from .views import FileView, FrameView, UserView

urlpatterns = [
    url(r'^frame/$', FrameView.as_view(), name='frame-create'),
    url(r'^upload/$', FileView.as_view(), name='file-upload'),
    url(r'^data/$', UserView.as_view(), name='user-request'),
]  
