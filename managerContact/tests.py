from django.test import TestCase
from .models import Person , NumberTel
import datetime
from django.utils import timezone
from django.urls import reverse

# function for create a contact
def create_contact(name , views=True):
    return Person.objects.create(name_person=name , views=views , date_creation=timezone.now())

# Create your tests here.

class TestIndexView(TestCase):
    # check if we see only contacts with props views eq to True
    
    # we have only contacts with views = False
    def testContactFalse(self):
        create_contact(name="contac false"  , views=False)
        create_contact(name="contac false 1"  , views=False)
        # calls index
        response = self.client.get(reverse('managerContact:index'))
        # compare
        self.assertQuerysetEqual(response.context['persons'] , [])
    
    # we have a contact with views eq False and one with True
    def testContactViewTrueAndFalse(self):
        contact_true = create_contact(name="Contact true")
        create_contact(name="contact false"  , views=False)
        # calls index page
        response = self.client.get(reverse('managerContact:index'))
        # compare 
        self.assertQuerysetEqual(response.context['persons'] , [contact_true])
    
    # we have only contct with views eq to True
    def testManyContactViewsTrue(self):
        contact_true = create_contact(name="contact true" )
        contact_true1 = create_contact(name="contact true 1" )
        # calls index page
        response = self.client.get(reverse('managerContact:index'))
        # comapre
        self.assertQuerysetEqual(response.context['persons'] , [ contact_true ,contact_true1])
    

class TestUpdateNumber(TestCase):
    # check if person have props.views eq to True
    
    def testContactTrue(self):
        # create contact True
        contact_true = create_contact(name="contac true")
        # calls update Contact page
        response = self.client.get(reverse('managerContact:updateContact' , args=(contact_true.id,)))
        # use assert
        # self.assertContains(response , "Error")
        self.assertEqual(response.context['person'] , contact_true)
    
    def testContactFalse(self):
        # create contact True
        contact_false = create_contact(name="contac false" , views=False)
        # 
        # calls update Contact page
        response = self.client.get(reverse('managerContact:updateContact' , args=(contact_false.id,)))
        # use assert
        # self.assertContains(response , "Error")
        self.assertContains(response , 'Error')
        
class TestAddNumber(TestCase):
    
    def testAddNumberContactTrue(self):
        # create contact true 
        contact_true = create_contact(name="contact true")
        # add Number to contact true
        contact_true.numbertel_set.create(other_number="22222222")
        # calls page addNumber
        response = self.client.get(reverse('managerContact:addNumber' , args=(contact_true.id,)))
        # compare
        self.assertEqual(response.context['person'] , contact_true)
        
    
    def testAddNumberContactFalse(self):
        # create contact false
        contact_false = create_contact(name="contact false" , views=False)
        # add number 
        contact_false.numbertel_set.create(other_number="2222")
        # calls page addNumber
        response = self.client.get(reverse('managerContact:addNumber' , args=(contact_false.id,)))
        # compare contains
        self.assertContains(response , "Error")
        
        

class TestListContactDeleted(TestCase):
    
    # we have only contacts with views = False
    def testContactFalse(self):
        contact_false1 = create_contact(name="contac false"  , views=False)
        contact_false2 = create_contact(name="contac false 1"  , views=False)
        # calls index
        response = self.client.get(reverse('managerContact:ContactDeletedView'))
        # compare
        self.assertQuerysetEqual(response.context['persons'] , [contact_false1 , contact_false2])
    
    # we have a contact with views eq False and one with True
    def testContactViewTrueAndFalse(self):
        create_contact(name="Contact true")
        contact_false = create_contact(name="contact false"  , views=False)
        # calls index page
        response = self.client.get(reverse('managerContact:ContactDeletedView'))
        # compare 
        self.assertQuerysetEqual(response.context['persons'] , [contact_false])
    
    # we have only contct with views eq to True
    def testManyContactViewsTrue(self):
        create_contact(name="contact true")
        create_contact(name="contact true 1")
        # calls index page
        response = self.client.get(reverse('managerContact:ContactDeletedView'))
        # comapre
        self.assertQuerysetEqual(response.context['persons'] , [])
        
    