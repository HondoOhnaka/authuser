from django.contrib.auth import login,logout
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

def home(request):
    return render_to_response('main_page.html', RequestContext(request))

@login_required
def login_req(request):
    vars = RequestContext(request, { 'user', request.user } )
    return render_to_response('login_required.html', vars)