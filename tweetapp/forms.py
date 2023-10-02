from django import forms

class AddTweetForm(forms.Form):
    nickname_input = forms.CharField(label="Nickname", max_length=50)
    body_input = forms.CharField(label="What do you think?", max_length=140)