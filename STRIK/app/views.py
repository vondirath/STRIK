# BEGIN DJANGO IMPORTS
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.template import loader
# END DJANGO IMPORTS
from .models import Posts
from .forms import PostForm

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

def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            post_date = timezone.now()
            image_name = form.cleaned_data['image_name']
            sale = form.cleaned_data['sale']
            featured = form.cleaned_data['featured']
            price = form.cleaned_data['price']
            temporary_price = form.cleaned_data['temporary_price']
            return HttpResponseRedirect('app/index.html')
    else:
        form = PostForm()
    
    return render(request, 'app/new_post.html', {'form': form})
