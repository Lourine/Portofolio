from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import contactView, successView

urlpatterns=[
    url(r'^$',views.project_list,name='projectList'),
    url(r'^$',views.skill_list,name='Skills'),
    url('contact/', contactView, name='contact'),
    url('success/', successView, name='success'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)