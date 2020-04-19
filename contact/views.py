from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from .forms import ContactForm
from django.core.mail import send_mail
from antique_shop.settings import EMAIL_HOST_USER


def contact(request):
    contact_class = ContactForm

    if request.method == 'POST':
        contact_form = contact_class(request.POST)

        if contact_form.is_valid():
            phone_number = contact_form.cleaned_data['phone_number']
            sender_subject = contact_form.cleaned_data['message_subject']
            sender_name = contact_form.cleaned_data['contact_name']
            sender_email = contact_form.cleaned_data['contact_email']
            

            message = "{0} has sent you a new message:\nFrom Email: {1}\nFrom Phone Number: {2}\n\n{3}".format(sender_name,sender_email,phone_number, contact_form.cleaned_data['message_content'])
            send_mail('You have recived a New Enquiry!!!', message, sender_email, [EMAIL_HOST_USER])

            messages.success(request, "Thanks for your Enquiry your message was successfully sent!")
            return redirect('contact')
        else:
            messages.error(request, "Your message was not sent. Please try again.")
            return redirect(reverse('contact'))

    return render(request, "contact.html", {'contact_form': contact_class})