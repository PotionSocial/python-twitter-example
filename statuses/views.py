from django.shortcuts import render, redirect
from django.conf import settings
import requests
from .forms import StatusForm, UserSelectorForm

default_headers = {
    'API-KEY': settings.API_KEY,
    'API-SECRET': settings.API_SECRET,
    'Content-Type': 'application/json',
}


def get_user_id(request):
    # Get current user id or sets it with latest available user
    if "current_user_id" in request.session:
        return request.session['current_user_id']
    else:
        url = settings.PROJECT_URL + '/public-api/v1/users'
        response = requests.get(url, headers=default_headers)
        json_response = response.json()
        users = json_response['items']
        request.session['current_user_id'] = users[0]['id']


def select_current_user(request):
    if request.POST:
        user_id = request.POST.get('user_id')
        request.session['current_user_id'] = user_id

    return redirect('statuses_index')


def statuses_index(request):
    get_user_id(request)
    url = settings.PROJECT_URL + '/public-api/v1/statuses'

    status_form = StatusForm(None)
    user_selector_form = UserSelectorForm(
        initial={'user_id': request.session['current_user_id']})

    response = requests.get(
        url + f"?for_user_id={request.session['current_user_id']}", headers=default_headers)
    json_response = response.json()
    statuses = json_response['items']
    print(statuses)

    return render(request, 'statuses_index.html', locals())


def create_status(request):
    get_user_id(request)

    url = settings.PROJECT_URL + '/public-api/v1/statuses'
    form = StatusForm(request.POST or None)
    if form.is_valid():
        message = form.cleaned_data['message']
        form_response = requests.post(url, headers=default_headers, json={
            'message': message,
            'user_id': request.session['current_user_id']
        })

    return redirect('statuses_index')


def delete_status(request, status_id):
    url = f'{settings.PROJECT_URL}/public-api/v1/statuses/{status_id}'
    response = requests.delete(url, headers=default_headers)
    json_response = response.json()

    return redirect('statuses_index')


def like_status(request, status_id):
    url = f'{settings.PROJECT_URL}/public-api/v1/statuses/{status_id}/like'
    response = requests.put(url, headers=default_headers, json={
                            'user_id': request.session['current_user_id']})
    json_response = response.json()

    print(json_response)

    return redirect('statuses_index')


def unlike_status(request, status_id):
    url = f'{settings.PROJECT_URL}/public-api/v1/statuses/{status_id}/unlike'
    response = requests.put(url, headers=default_headers, json={
                            'user_id': request.session['current_user_id']})
    json_response = response.json()

    return redirect('statuses_index')
