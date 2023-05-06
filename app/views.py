from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    send_mail('New Django Send Mail Code Check Out', 
              'Hey. I have an updated django send mail code on my GitHub @AlbanusMuange1. Check it out and try to update it', 
              'albanusmuangemutunga@gmail.com',
              ['missiejoan04@gmail.com', 'felixjamesk27@gmail.com', 'omondicollins163@gmail.com'],
              fail_silently=False
              )
    return render(request, 'home.html')