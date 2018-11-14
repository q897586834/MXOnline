from django.shortcuts import render
from .models import UserMessage
from django.db import models

# Create your views here.
def getform(request):
    if request.method == "POST":
        name = request.POST.get('name',"")
        message = request.POST.get('name', "")
        address = request.POST.get('name', "")
        email = request.POST.get('name', "")
        user_message = UserMessage()
        user_message.createuser(name=name,message=message,address=address,email=email,object_id="1")
    return render(request,'message_form.html')
