from django import forms
from django.conf import settings
import requests


class StatusForm(forms.Form):
    message = forms.CharField(
        label='subject', widget=forms.Textarea(attrs={'class': "form-control", 'rows': 3, 'placeholder': "What are you thinking?"}))


class UserSelectorForm(forms.Form):
    url = settings.PROJECT_URL + '/public-api/v1/users'
    response = requests.get(url, headers={
        'API-KEY': settings.API_KEY,
        'API-SECRET': settings.API_SECRET,
        'Content-Type': 'application/json',
    })
    json_response = response.json()
    user_choices = map(
        lambda u: [u['id'], u['nickname']], json_response['items'])

    user_id = forms.CharField(
        label='',
        max_length=3,
        widget=forms.Select(choices=user_choices, attrs={'onchange': 'user_selector_form.submit();',
                                                         'class': "form-control"}),
    )
