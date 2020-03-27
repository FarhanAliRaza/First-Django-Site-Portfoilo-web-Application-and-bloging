from django.shortcuts import render

from django.shortcuts import render
from blog.models import BlogPost
from .forms import ContactForm
from.models import Message


def home_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
    qs = BlogPost.objects.all()
    template_name = 'index.html'
    context = {
        'object_list': qs,
        'form': form
    }
    return render(request, template_name, context)


