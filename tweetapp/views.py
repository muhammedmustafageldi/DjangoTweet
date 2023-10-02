from django.shortcuts import render, redirect
from . import models
from datetime import datetime
import time
from django.urls import reverse, reverse_lazy
from tweetapp.forms import AddTweetForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create your views here.

def feeds(request):
    tweets_list = models.Tweet.objects.order_by('-time_unix').all()
    tweets_context = {"tweets": tweets_list} 
    return render(request, "tweetapp/feeds.html", context=tweets_context)

@login_required(login_url="/login")
def add_tweet(request):
    if request.method == "POST":
        tweet = request.POST["tweet"]

        current_time = str(datetime.now().strftime("%d-%m-%Y %H:%M"))
        time_unix = time.time()
        tweet_object = models.Tweet(username=request.user, body=tweet, time=current_time, time_unix=time_unix)
        tweet_object.save()

        return redirect(reverse('tweetapp:feeds'))
    else:
        return render(request, "tweetapp/add_tweet.html")
    

def add_tweet_by_form(request):
    if request.method == "POST":
        form = AddTweetForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data['nickname_input']
            body = form.cleaned_data['body_input']
        return redirect(reverse('tweetapp:feeds'))
    else:
        form = AddTweetForm()
        return render(request,'tweetapp/add_tweet_by_form.html',context={'form': form})    
    

@login_required
def delete_tweet(request, id):
    tweet = models.Tweet.objects.get(pk=id)
    if request.user == tweet.username:
        models.Tweet.objects.filter(id=id).delete()
        return redirect(reverse('tweetapp:feeds'))

def sign_up_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        # Is the username unique?
        if User.objects.filter(username=username).exists():
            error_message = 'This username is already exists.'
            return render(request, 'registration/sign_up.html', {'error_message': error_message})

        # Check if the passwords match
        if password == password_confirmation:
            user = User.objects.create_user(username=username, password=password)   
            login(request, user)
            return redirect(reverse('tweetapp:feeds'))
        else:
            error_message = "Password confirmation does not match."
            return render(request, 'registration/sign_up.html', {'error_message': error_message})    
    else:
        return render(request, 'registration/sign_up.html')          