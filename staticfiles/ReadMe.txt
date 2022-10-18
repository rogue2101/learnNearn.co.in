1.Create environment-py -m venv env
2.Activate env - env\Scripts\activate.bat
3. Install django - pip install django
4. Create project-django-admin startproject TPS
5.Go to TPS by "cd TPS" the make app - django-admin startapp resume
6. Add app "resume" to settings.py 
7.Create admin - py manage.py createsuperuser
    Username (leave blank to use 'acer'): admin
    Email address: admin@gmail.com
    Password:admin
8. Create model then migrate and register in admin.py file
9. Register your models -
    from .models import Profile
    admin.site.register(Profile)
    10. id should be same as model fields...then only it will work
11. add template in settings.py dir
12. import view in urls.py


To delete all data of tables created by models:

First, install django-turncate using your terminal/command line:
pip install django-truncate
Add "django_truncate" to your INSTALLED_APPS in the settings.py file:
INSTALLED_APPS = [
    ...
    'django_truncate',
]
Use this command in your terminal to delete all data of the table from the app.
python manage.py truncate --apps app_name --models table_name





* To logout 
simply put a function in views: def logout(request): auth.logout(request) return render(request, "home/index.html")
import in the start in views: from django.contrib.auth.models import User, auth
and in urls add the path: path('logout', views.logout, name='logout'),

*To change user signin and sign out use:
{% if request.user.is_authenticated %}
    <a href="{% url 'logout' %}" class="nav-item nav-link active">Signout</a>
{% else %}
    <a href="detail.html" class="dropdown-item">Signup</a>
{% endif %}

wkhtmltox-0.12.6-1.msvc2015-win64.exe