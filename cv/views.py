from django.shortcuts import render
from django.core.mail import EmailMessage
from django.contrib import messages
from products.models import Product


def home(request):
    temps = Product.objects.all()
    context = {
        'temps': temps,
    } 
    return render(request, 'home.html', context)

def contact(request):
    if request.method == 'POST':
        message = request.POST['message']
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']


        #send email
        mail_subject = name + ' sent a message from your Website.'
        message = message
        from_email = email

        send_email = EmailMessage(mail_subject, message, from_email, to=['info@regmotechnologies.co.ke', 'regmotech@gmail.com'])
        send_email.send()
        
        messages.success(request, name + ' your message has been sent. Thank you!')
   
    return render(request, 'contact.html')