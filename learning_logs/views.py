from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Topic, Entry
from .form import TopicForm, EntryForm
from broadcast.models import BTopic, BEntry

def get_for_usertopic(request, topic_id):
    '''used in cases where we would still want to access other
    attribute of that topic'''
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    else:
        return topic

def get_for_userentry(request, entry_id):
    '''used to get for user entry and check if it belongs to 
    the requesting user'''
    entry = Entry.objects.get(id=entry_id)
    if entry.topic.owner != request.user:
        raise Http404
    else:
        return entry
    
def index(request):
    '''Homepage'''
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    '''Topic page'''
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    broadcast = BTopic.objects.all()
    context = {'topics':topics, 'broadcast':broadcast}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    '''Individual topic and entry'''
    topic = get_for_usertopic(request, topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic' : topic, 'entries' : entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    '''New topic form'''
    if request.method != 'POST':
        #display a blank form
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            newtopic = form.save(commit=False)
            newtopic.owner = request.user
            newtopic.save()
            return redirect('learning_logs:topics')
    
    #store and render the blank form in if condition or
    #if the result on else --if valid return false, a blank form again
    context = {'form':form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    '''Add a new entry for a particular topic'''
    topic = get_for_usertopic(request, topic_id)
    if request.method != 'POST':
        #create a blank form
        form = EntryForm()

    else:
        #Form made is submitted, request is post
        form = EntryForm(request.POST)

        if form.is_valid():
            '''if submitted for is valid'''
            newentry = form.save(commit=False)
            newentry.topic = topic
            newentry.save()
            return redirect('learning_logs:topic', topic_id)
    
    #for a requested or invalid form
    context = {'topic':topic, 'form':form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    '''modify an entry for a topic'''
    entry = get_for_userentry(request,entry_id)
    topic = entry.topic
    topic = get_for_usertopic(request, topic.id)
    if request.method != 'POST':
        #create a blank form
        form = EntryForm(instance=entry)
    else:
        #Form is submitted, post request
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.topic = topic
            edit.save()
            return redirect('learning_logs:topic', topic.id)
    
    context = {'form':form, 'topic':topic, 'entry':entry}
    return render(request, 'learning_logs/edit_entry.html', context)

@login_required
def edit_topic(request, topic_id):
    '''Edit the names of the topic'''
    topic = get_for_usertopic(request, topic_id)
    if request.method != 'POST':
        form = TopicForm(instance=topic)
    else:
        form = TopicForm(instance=topic, data=request.POST)
        if form.is_valid():
            edittopic=form.save(commit=False)
            edittopic.owner = request.data
            edittopic.save()
            return redirect('learning_logs:topic', topic.id)
    context = {'form':form, 'topic':topic}
    return render(request, 'learning_logs/edit_topic.html', context)

@login_required
def warning_delete_topic(request, topic_id):
    '''Warning message before for delete action'''
    topic = get_for_usertopic(request, topic_id)
    context={"topic":topic}
    return render(request, 'learning_logs/warning_delete_topic.html', context)

@login_required
def delete_topic(request, topic_id):
    '''Delete the topic'''
    topic=get_for_usertopic(request, topic_id)
    topic.delete()
    return redirect('learning_logs:topics')

@login_required
def warning_delete_entry(request, entry_id):
    '''Warning message before entry deletion'''
    entry = get_for_userentry(request, entry_id)
    topic = entry.topic
    context = {"entry":entry, "topic":topic}
    return render(request, 'learning_logs/warning_delete_entry.html', context)

@login_required
def delete_entry(request, entry_id):
    '''Delete the entry'''
    entry = get_for_userentry(request, entry_id)
    topic = entry.topic
    entry.delete()
    return redirect('learning_logs:topic', topic.id)

@login_required
def announcements(request, topic_id):
    '''show all broadcasted entires for each topic'''
    topic = BTopic.objects.get(id=topic_id)
    entry = topic.bentry_set.all()
    context={'entrys':entry}
    return render(request, 'learning_logs/announcements.html', context)