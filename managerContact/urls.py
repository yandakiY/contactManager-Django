from . import views
from django.urls import path

app_name = "managerContact"
urlpatterns = [
    path('' , views.IndexView.as_view() , name="index"),
    path('addPerson' , views.addPerson , name="addPerson")
]
