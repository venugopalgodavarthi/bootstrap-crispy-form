from django.urls import path
from myapp import views
urlpatterns=[
    path("",views.registerview),
    path("base/",views.baseview),
]