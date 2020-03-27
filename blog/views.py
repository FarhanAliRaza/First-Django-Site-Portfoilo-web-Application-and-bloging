from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect


from .models import BlogPost


def blog_post_detail_view(request, slug):

    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog.html'
    context = {"object": obj}
    return render(request, template_name, context)







