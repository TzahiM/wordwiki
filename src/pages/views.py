#from django.shortcuts import render
#from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import UpdateView, CreateView
from pages.models import Page

# Create your views here.
class PageCreate(CreateView):
    model = Page

    fields = ['name', 'header', 'body_text']
    template_name = 'pages/page_create_form.html'

class PageUpdate(UpdateView):
    model = Page

    fields = ['name', 'header', 'body_text']
    template_name = 'pages/page_update_form.html'


def list_of_all_pages(request):
    latest_pages_list = Page.objects.all().order_by('-name')
    context = {'latest_pages_list': latest_pages_list}
    return render(request, 'pages/page_list.html', context)
    


def details(request, pk):
    page = get_object_or_404(Page , name  = pk)
    uml_list = page.as_html()
    return render(request, 'pages/detail.html', {'page': page , 'uml_list' : uml_list})

    
 
    
    
