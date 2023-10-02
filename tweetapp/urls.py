from django.urls import path
from . import views

app_name = 'tweetapp'

urlpatterns = [
    path("",views.feeds,name="feeds"),
    path("add_tweet/",views.add_tweet, name="add_tweet"),
    path("add_tweet_by_form/", view=views.add_tweet_by_form, name="add_tweet_by_from"),
    path("signup/", view=views.sign_up_view, name="signup"),
    path("deletetweet/<int:id>", view=views.delete_tweet, name="delete_tweet")
]