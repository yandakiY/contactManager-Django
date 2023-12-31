from . import views
from django.urls import path

app_name = "managerContact"
urlpatterns = [
    path('' , views.IndexView.as_view() , name="index"),
    path('addPerson' , views.addPerson , name="addPerson"),
    path('addNumber/<int:person_id>' , views.addNumberView , name="addNumber"),
    path('addOtherNumber/<int:person_id>' , views.addOtherNumber , name="addOtherNumber"),
    path('updateContact/<int:person_id>' , views.updateContactView , name="updateContact"),
    path('updateContactForm<int:person_id>', views.updateContact , name="updateContactForm" ),
    path('removeContact/<int:person_id>' , views.removeContact , name="removeContact"),
    path('removeAll' , views.removeAll , name="removeAll"),
    path('deleteContact/<int:person_id>' , views.deleteContact , name="deleteContact"),
    path('deleteAll' , views.deleteAllContact , name="deleteAll"),
    path('ContactDeletedView' , views.ContactDeletedView.as_view() , name="ContactDeletedView"),
    path('restoreContact/<int:person_id>' , views.restoreContact , name="restoreContact"),
    path('restoreAll' , views.restoreAllContact , name="restoreAll")
]
