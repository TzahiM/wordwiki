#from django.shortcuts import render
#from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from pages.models import Page

def list_of_all_pages(request):
    
#    text_string = "<ul>\n"
#    for page in Page.objects.order_by('-name'):
#        text_string += "<li>" + page.name + "</li>\n" 
#    text_string += "</ull>\n"
#    return HttpResponse( text_string)
    latest_pages_list = Page.objects.all().order_by('-name')
    context = {'latest_pages_list': latest_pages_list}
    return render(request, 'pages/page_list.html', context)
    
    
 
    
    
