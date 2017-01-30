# BEGIN DJANGO IMPORTS
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.template import loader
# END DJANGO IMPORTS
from .models import Posts

def index(request):
    latest_post_list = Posts.objects.order_by('-post_date')[:10]
    context = {'latest_post_list' : latest_post_list}
    return render(request, 'app/index.html', context)
