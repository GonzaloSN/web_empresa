from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage

# Create your views here.

def contact(request):
        contact_form = ContactForm()
    
        if request.method == 'POST':
            contact_form = ContactForm(data=request.POST)
            if contact_form.is_valid():
                name = request.POST.get('name', '')
                email = request.POST.get('email', '')
                content = request.POST.get('content', '')
                #Enviamos el correo y redireccionamos
                email = EmailMessage(
                    #asunto
                    'Delicias de la UCA: Nuevo mensaje de contacto',
                    #cuerpo
                    'De {} <{}>\n\nEscribió:\n\n{}'.format(name, email, content),
                    #email origen
                    'no-contestar@inbox.mailtrap.io',
                    #email destino
                    ['Gonzaloooooo96@gmail.com'],
                    reply_to=[email]
                )
                try:
                    email.send()
                    #Todo ha ido bien
                    return redirect(reverse('contact')+'?ok')
                except:
                    #Algo no ha ido bien
                    return redirect(reverse('contact')+'?fail')
        return render(request, 'contact/contact.html', {'form':contact_form})

#def contact(request):
 #   contact_form = ContactForm()
#
 #   if request.method == 'POST':
  #      contact_form = ContactForm(data=request.POST)
   #     if contact_form.is_valid():
    #        name = request.POST.get('name', '')
     #       email = request.POST.get('email', '')
      #      content = request.POST.get('content', '')
       #     #Si todo sale bien..
        #    return redirect(reverse('contact')+'?ok')
    #return render(request, 'contact/contact.html', {'form':contact_form})