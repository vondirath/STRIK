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
    """
        This renders the index view sorting every post by
        the posting date only not time of day.
    """
    latest_post_list = Posts.objects.order_by('-post_date')[:10]
    context = {'latest_post_list' : latest_post_list}
    return render(request, 'app/index.html', context)

def item_detail(request, post_id):
    """
        This renders each item view by taking the post_id
        given through the GET request.
    """
    post = get_object_or_404(Posts, pk=post_id)
    context = {'post': post}
    return render(request,'app/item_page_view.html', context)
