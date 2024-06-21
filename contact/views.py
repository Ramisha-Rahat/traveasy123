from django.shortcuts import render
from.models import saveContact

# Create your views here.
def contact(request):
    
  
    return render(request, 'contact/contact.html')


def savecontact(request):
    response=''
    if request.method=="POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        subject= request.POST.get('subject')
        message= request.POST.get('message')
        
        data=saveContact(name=name , email=email , subject=subject , message=message)
        data.save()
        response = 'Message Sent'
        
    return render(request, 'contact/contact.html',{'response':response})     
    