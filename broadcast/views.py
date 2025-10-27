from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseBadRequest
from django.contrib.auth.models import User

from .models import BTopic, BEntry
from .forms import BTopicForm, BEntryForm

def check_requesting_user(request):
    '''checks the request to see if user is staff or
    superuser'''
    if request.user.is_superuser or request.user.is_staff:
        return True
    else:
        raise Http404

def check_numberof_topics():
    '''To avoid a lot of Brodcasts, we limit the broadcasts
    to 2 for now, later me may upgrade it into a different
    tab ang tag it as announcement'''
    btopics = BTopic.objects.all()
    if len(btopics) >= 2:
        return True

def index(request):
    '''checks if user is a superuser before returning 
    the broadcast index page'''
    if check_requesting_user(request):
        return render(request, 'broadcast/index.html')
  
def topics(request):
    '''If user is superuser or staff, returns the broadcast
    topic page'''
    if check_requesting_user(request):
        topics = BTopic.objects.all()
        context={'topics':topics}
        return render(request,'broadcast/topics.html', context)

def add_topic(request):
    '''This should serve up the Topic broadcast only if
    the user is a staff or superuser and the number of
    pre-existing topics is less than or equal to 2'''
    if check_requesting_user(request):
        if not check_numberof_topics():
            if request.method != 'POST':
                form = BTopicForm()
            else:
                form = BTopicForm(request.POST)
                if form.is_valid():
                    newbtopic = form.save(commit=False)
                    newbtopic.owner = request.user
                    newbtopic.save()
                    return redirect('broadcast:topics')
            context = {'form':form}
            return render(request, 'broadcast/add_topic.html', context)
        
        else:
            raise Http404()
  
def topic(request, topic_id):
    '''Get all the broadcast entry for a particular
     topic for staff'''
    if check_requesting_user(request):
        topic = BTopic.objects.get(id=topic_id)
        entrys = topic.bentry_set.order_by('-date_added')

        context={'topic':topic, 'entrys':entrys}
        return render(request, 'broadcast/topic.html', context)
  
def add_entry(request, topic_id):
    '''Add broadcast entry and associate it with
     a particular topic'''
    if check_requesting_user(request):
        topic = BTopic.objects.get(id=topic_id)
        if request.method != 'POST':
            form = BEntryForm()
        else:
            form = BEntryForm(request.POST)
            if form.is_valid():
                add_topic = form.save(commit=False)
                add_topic.owner =topic
                add_topic.save()
                return redirect('broadcast:topic', topic.id)
        context = {'topic':topic, 'form':form}
        return render(request, 'broadcast/add_entry.html', context)
    
def delete_topic(request, topic_id):
    '''Delete the requested topic'''
    if check_requesting_user(request):
        topic = BTopic.objects.get(id=topic_id)
        topic.delete()
        return redirect('broadcast:topics')

def delete_entry(request, entry_id):
    '''Delete the requested entry'''
    if check_requesting_user(request):
        entry = BEntry.objects.get(id=entry_id)
        topic_id = entry.owner.id
        entry.delete()
        return redirect('broadcast:topic', topic_id)
    
def edit_topic(request, topic_id):
    '''Edit the requested topic'''
    if check_requesting_user(request):
        topic = BTopic.objects.get(id=topic_id)
        if request.method!='POST':
            form = BTopicForm(instance=topic)
        else:
            form = BTopicForm(instance=topic, data=request.POST)
            if form.is_valid():
                edit = form.save(commit=False)
                edit.owner = request.user
                edit.save()
                return redirect('broadcast:topic', topic_id)
        context = {'form':form, 'topic':topic}
        return render(request, 'broadcast/edit_topic.html', context)

def edit_entry(request, entry_id):
    '''Edit the requested entry'''
    if check_requesting_user:
        entry = BEntry.objects.get(id=entry_id)
        topic = entry.owner
        if request.method != 'POST':
            form = BEntryForm(instance=entry)
        else:
            form = BEntryForm(instance=entry, data=request.POST)
            if form.is_valid():
                edit = form.save(commit=False)
                edit.owner.id = topic.id
                edit.save()
                return redirect('broadcast:topic', topic.id)
        context = {'form':form, 'entry':entry}
        return render(request, 'broadcast/edit_entry.html', context)

def flush_entries(request, topic_id):
    '''Delete all entries of a particular topic'''
    if check_requesting_user(request):
        topic = BTopic.objects.get(id=topic_id)
        entry = topic.bentry_set.all()
        entry.delete()
        return redirect('broadcast:topic', topic_id)