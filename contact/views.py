from django.template.loader import get_template
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from .forms import ContactForm
from django.core.mail import send_mail

def contact(request):
    contact_class = ContactForm

    if request.method == 'POST':
        contact_form = contact_class(request.POST)

        if contact_form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            message_subject = request.POST.get('message_subject', '')
            message_content = request.POST.get('message_content', '')
            send_mail(
                message_subject,
                message_content,
                contact_email,
                ['cristiplesca1993@gmail.com'],
                fail_silently=False,
                )

            messages.success(request, "Your message was successfully sent!")
            return redirect('contact')
        else:
            messages.error(request, "Your message was not sent. Please try again.")
            return redirect(reverse('contact'))

    return render(request, "contact.html", {'contact_form': contact_class})