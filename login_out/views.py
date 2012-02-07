from django.contrib.auth import login,logout
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

def home(request):
    vars = { 'user', request.user }
    return render_to_response('main_page.html', vars)

@login_required
def login_req(request):
    return render_to_response('login_required.html', {})