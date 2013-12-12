#from django.shortcuts import render
#from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from pages.models import Page

# Create your views here.



def list_of_all_pages(request):
    latest_pages_list = Page.objects.all().order_by('-name')
    context = {'latest_pages_list': latest_pages_list}
    return render(request, 'pages/page_list.html', context)
    
def details(request, pk):
    page = get_object_or_404(Page , name  = pk)
    uml_list = page.as_html()
    return render(request, 'pages/detail.html', {'page': page , 'uml_list' : uml_list})

    
 
    
    
