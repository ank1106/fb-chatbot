from django.conf.urls import url
from .views import FacebookAPI


urlpatterns = [
    url(r'^fb/$', FacebookAPI.as_view()),

]
