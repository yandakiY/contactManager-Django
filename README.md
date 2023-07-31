# Contacts Manager

Contacts Manager is a web application developed with Django, a Python-based web development framework.
The main goal of this app is to organize saved contacts votes.

## Features

The features of application : 
- Add new contacts
- Add others numbers to a contact saved
- Update properties of a contact (name , email , numbers)
- Delete a contact
- Delete all contacts
- View contacts deleted, in a section , "contacts deleted"
- Restore a contact
- Restore all contacts
- Implementation Error Page

## Screenshots
<img src="/images/index.png" alt="Page Index" width="600" height="500">
<img src="/images/update.png" alt="Page Index" width="250" height="500">
<img src="/images/addNumber.png" alt="Page Index" height="500">
<img src="/images/listsdeleted.png" alt="Page Index" width="400" height="500">

## Installation

1.Clone the GitHub repository:

```bash
  git clone https://github.com/yandakiY/contactManager-Django.git
```

2.Perform database migrations :

```bash
  python manage.py migrate

```

3.Start the development server:

```bash
  python manage.py runserver

```

4.Access the application in your browser at :
```bash
  http://localhost:8000/
```
## License

[MIT](https://choosealicense.com/licenses/mit/)


## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)
 - [Writing your first Django application](https://docs.djangoproject.com/en/4.2/intro/tutorial01/)