from django.urls import path

from . import views

app_name = 'broadcast'
urlpatterns=[
    # Broadcast index page
    path('index/', views.index, name='index'),
    # Broadcast topic page
    path('topics/', views.topics, name='topics'),
    # Add Broadcast topic page
    path('add_topic/', views.add_topic, name='add_topic'),
    # Admin and staff entry view
    path('topic/<int:topic_id>/', views.topic, name='topic'),
    # Add entry
    path('add_entry/<int:topic_id>/',
          views.add_entry, name='add_entry'),
    # Delete Topic
    path('delete_topic/<int:topic_id>/',
          views.delete_topic, name='delete_topic'),
    # Delete Entry
    path('delete_entry/<entry_id>/',
          views.delete_entry, name='delete_entry'),
    # Edit topic
    path('edit_topic/<int:topic_id>/', views.edit_topic, name='edit_topic'),
    # Edit entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    # Delete all broadcast entry at once
    path('flush_entries/<int:topic_id>/', views.flush_entries, name="flush_entries")
]