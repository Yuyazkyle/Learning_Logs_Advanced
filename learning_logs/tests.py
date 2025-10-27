from django.test import TestCase
from models import Topic, Entry

topic = Topic.objects.filter

# These are the attributes assigned to the user objects
'''django.core.exceptions.FieldError: Cannot resolve 
keyword 'name' into field. 
Choices are: btopic, date_joined, email, first_name, 
groups, id, is_active, is_staff, is_superuser, 
last_login, last_name, logentry, password, 
topic, user_permissions, username
'''