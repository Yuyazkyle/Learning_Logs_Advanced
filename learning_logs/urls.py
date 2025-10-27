'''URL for the learning_logs apps'''

from django.urls import path
from users import views as auth_view
from . import views

app_name = 'learning_logs'
urlpatterns = [
    #My HomePage
    path('', views.index, name = 'index'),
    #My Topic page
    path('topics/', views.topics, name = 'topics'),
    #My individual topic page
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #My page for new topics form
    path('new_topic/', views.new_topic, name='new_topic'),
    #My page for a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #My page for editing the topic
    path('edit_topic/<int:topic_id>/', views.edit_topic, name='edit_topic'),
    #My page for editing entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    #warn the user before topic deletion
    path('warning_delete_topic/<int:topic_id>/', views.warning_delete_topic, name="warning_delete_topic"),
    #delete the topic
    path('delete_topic/<int:topic_id>/', views.delete_topic, name="delete_topic"),
    #warn the user before entry deletion
    path('warning_delete_entry/<int:entry_id>/', views.warning_delete_entry, name="warning_delete_entry"),
    #delete the entry
    path('delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),
    # show all announced entries
    path('announcements/<int:topic_id>/', views.announcements, name='announcements'),

    # User app URL mapping
    path('login/', auth_view.login, name='login'),
    path('signup/', auth_view.signup, name='signup'),
    path('logout/', auth_view.log_out, name='logout'),
]