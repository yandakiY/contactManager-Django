from django.shortcuts import render , HttpResponseRedirect , get_object_or_404
from django.views import generic
from .models import Person, NumberTel
from django.utils import timezone
from django.urls import reverse
from django.utils.html import escape

# Create your views here.
class IndexView(generic.ListView):
    # model = Person
    template_name = "managerContact/index.html"
    context_object_name = "persons"
    
    def get_queryset(self):
        return Person.objects.all().order_by("-date_creation").filter(views=True)


def addNumberView(request, person_id):
    # Get item person by id
    person = Person.objects.get(pk=person_id)
    return render(request , "managerContact/addNumber.html", {"person":person})
    

def updateContactView(request , person_id):
    # get item person which correspond to id
    person = Person.objects.get(id=person_id)
    return render(request , "managerContact/updateContact.html" , {"person":person})


class ContactDeletedView(generic.ListView):
    # model = Person
    template_name = "managerContact/contactDeleted.html"
    context_object_name = "persons"
    
    def get_queryset(self):
        return Person.objects.all().order_by("-date_creation").filter(views=False)


def addPerson(request):
    # get property name , email, and number
    # name
    name = request.POST.get('name_person')
    # email
    email = request.POST.get('email')
    # number_tel
    number_tel = request.POST.get('number_tel')
    
    # Save Person
    contact , created = Person.objects.get_or_create(name_person=name , email=email , date_creation=timezone.now())
    
    # get the last element of contact and add number
    last_contact = Person.objects.last()
    # use numbertel_set, for add a number for a Person
    last_contact.numbertel_set.create(other_number=number_tel)
    
    
    if not created:
        return render(request , "managerContact/index.html" , {"message_error":"Contacts already present"})
    
    return HttpResponseRedirect(reverse("managerContact:index" , args=()))


def addOtherNumber(request , person_id):
    # get the element who correspond to id
    person = get_object_or_404(Person , pk = person_id)
    
    new_number = request.POST.get('new_number_tel')
    
    # add number to this person
    person.numbertel_set.create(other_number=new_number)
    # redirection to index
    return HttpResponseRedirect(reverse('managerContact:index' , args=()))

def updateContact(request , person_id):
    # get the item which correspond 
    # change name , email and numbers 
    person = get_object_or_404(Person , id=person_id)
    
    person.name_person = escape(request.POST.get('name_person'))
    
    person.email = escape(request.POST.get('email'))
    person.save()
    
    # get all numbers associate to this person
    # browse each number 
    # update and save
    
    # get all numbers from form
    for i , number in enumerate(person.numbertel_set.all() , start=1):
        # input from formulaire in htmk file
        input = request.POST.get(f'number{i}')
        # 
        # person.numbertel_set.get(other_number=number).other_number = input 
        # delete the number present
        person.numbertel_set.get(other_number=number).delete()
        # and create a new number with the value which come to the form in html file
        person.numbertel_set.create(other_number=input)
        # person.save()
        
        # print(f'Depuis Forms: {input} Database {number} , index:{i}')
    
    
    # Save , first change
    # person.save()
    
    # redirection to index
    return HttpResponseRedirect(reverse("managerContact:index" , args=()))


def removeContact(request , person_id):
    
    # lists of id in database and IndexView (only Contact with views eq True)
    lists_id = [p.id for p in Person.objects.all() if p.views == True]
    print(lists_id)
    
    if(person_id in lists_id):
        # get item who correspond
        person = Person.objects.get(id = person_id)
        # change value property views
        person.views = False
        # save changement
        person.save()
        # redirection to index
        return HttpResponseRedirect(reverse('managerContact:index' , args=()))
    
    return render(request , "managerContact/error400.html")
    # pass

def removeAll(request):
    # lists of id in database and IndexView (only Contact with views eq True)
    lists_id = [p.id for p in Person.objects.all() if p.views == True]
    print(lists_id)
    
    if len(lists_id) == 0:
        # Nothing
        # redirectio to home page
        return HttpResponseRedirect(reverse("managerContact:index" , args=()))
    
    # browse each element list id and delete
    for id in lists_id:
        person = Person.objects.get(id = id)
        # delete
        person.views = False
        # save
        person.save()
    # redirect to home page
    return HttpResponseRedirect(reverse("managerContact:index" , args=()))
    

# def removeAllContact(request , person_id):
#     # get item who correspond to id
#     # Lists of contact in database
#     lists_id = [p.id for p in Person.objects.all()]
    
#     if (person_id in lists_id):
#         person = Person.objects.get(id=person_id)
        
#         # delete
#         person.delete()
        
#         return HttpResponseRedirect(reverse('managerContact:index' , args=()))
#     # else:
    
#     return HttpResponseRedirect("Error 404")

def deleteContact(request , person_id):
    # get item who correspond to id
    # Lists of contact in database
    lists_id = [p.id for p in Person.objects.all() if p.views == False]
    
    if (person_id in lists_id):
        person = Person.objects.get(id=person_id)
        
        # delete
        person.delete()
        
        return HttpResponseRedirect(reverse('managerContact:ContactDeletedView' , args=()))
    
    return render(request , "managerContact/error400.html")


def deleteAllContact(request):
    # get lists of all id
    lists_id = [p.id for p in Person.objects.all() if p.views == False]
     
    
    if len(lists_id) == 0:
        return render(request , "managerContact/error400.html")
    else:
        # browse each element, and delete
        for id in lists_id:
            person = Person.objects.get(id = id)
            # delete
            person.delete()
            
    return HttpResponseRedirect(reverse('managerContact:ContactDeletedView' , args=()))


def restoreContact(request , person_id):
    # get lists of all id
    lists_id = [p.id for p in Person.objects.all() if p.views == False]
    
    if (person_id in lists_id):
        person = Person.objects.get(id = person_id)
        # change property views
        person.views = True
        # save that
        person.save()
        # redirect to
        return HttpResponseRedirect(reverse('managerContact:ContactDeletedView' , args=()))
        
    else:
        return render(request , "managerContact/error400.html")

def restoreAllContact(request):
    
    # get lists of all id
    lists_id = [p.id for p in Person.objects.all() if p.views == False]
    
    if len(lists_id) == 0:
        return render(request , "managerContact/error400.html")
    else:
        
        for id in lists_id:
            person = Person.objects.get(id = id)
            # delete
            person.views = True
            # save
            person.save()
            
    return HttpResponseRedirect(reverse('managerContact:ContactDeletedView' , args=()))
    