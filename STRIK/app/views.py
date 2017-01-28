# BEGIN DJANGO IMPORTS
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.template import loader
# END DJANGO IMPORTS

def index(request):
    return render(request, 'app/index.html')
