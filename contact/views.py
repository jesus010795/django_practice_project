from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm


def contact(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid:
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            email_message= EmailMessage(
                "Nobre empresa: Nuevo mensaje contacto",
                "De {}, <{}> \n\n Escribio: \n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["bep_95@hotmail.com", "bep010795@gmail.com"],
                reply_to=[email]
            )
            try:
            #Suponemos que todo ha ido bien, redireccionamos
                email_message.send()
                return redirect(reverse('contact')+'?ok')
            except Exception:
                import traceback
                traceback.print_exc()
                #Si algo sale mal
                return redirect(reverse('contact')+'?fail')

    return render(request, 'contact/contact.html', { 'form': contact_form})