Working copy of https://docs.djangoproject.com/en/3.0/intro/tutorial01/


In a separate terminal from the running site, do the following.

$ cd
$ ./ngrok tls -region=us -hostname=www.avinyet.com -key ~/avinet.rsaprivatekey.pem -crt ~/avinet.fullchaincert.pem 8000

(my_django_environment) ganymede:mysite mbk$ python manage.py createsuperuser
Username (leave blank to use 'mbk'):
Email address: markkauffman2000@gmail.com
Password: Alan, etc.
Password (again):
Superuser created successfully.

(base) ganymede:mysite mbk$ workon my_django_environment
(my_django_environment) (base) ganymede:mysite mbk$
(my_django_environment) (base) ganymede:mysite mbk$ python manage.py shell
Python 3.7.4 (default, Dec  5 2019, 13:55:41)
[Clang 10.0.0 (clang-1000.10.44.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from django.shortcuts import render
>>> from django.contrib.auth import get_user_model
>>> all_users =  get_user_model().objects.all()
>>> all_users
<QuerySet [<User: mbk>, <User: mkauffman>]>
