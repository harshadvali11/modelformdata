from django.shortcuts import render

# Create your views here.

from app.forms import *
from django.http import HttpResponse
def insert_topic(request):
    TF=TopicForm()
    d={'form':TF}
    if request.method=='POST':
        form_data=TopicForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('inserted')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    WF=WebpageForm()
    d={'form':WF}
    if request.method=='POST':
        form_data=WebpageForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('webpage is inserted')
    return render(request,'insert_webpage.html',d)













