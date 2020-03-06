from django.conf.urls import url
from .views import FileView, FrameView

urlpatterns = [
    url(r'^frame/$', FrameView.as_view(), name='frame-create'),
    url(r'^upload/$', FileView.as_view(), name='file-upload'),
]  
