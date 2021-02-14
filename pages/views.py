# from django.http import HttpResponse
from django.shortcuts import render
# from django.views.generic import TemplateView


# Create your views here.
def home_page_view(request):
    # return HttpResponse("Hello, world!")
    context = {
        'blog_entries': [
            {
                'title': 'Hello, world!',
                'body': 'I have created my first template in Django!'
            },
            {
                'title': 'A title',
                'body': 'And a description.'
            }
        ]
    }
    return render(request, 'index.html', context)


# class AboutView(TemplateView):
#     template_name = "about.html"
