#from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from pages.models import Page

def list_of_all_pages(request):
    text_string = "<ol>\n"
    for page in Page.objects.all():
        text_string += "<li>" + page.name + "</li>\n" 
    text_string += "</ol>\n"
    return HttpResponse( text_string) 
    
    
