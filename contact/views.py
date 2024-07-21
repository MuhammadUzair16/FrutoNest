# contact/views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()

            # Send an email notification
            subject = form.cleaned_data['subject']
            message = f"Name: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\nPhone: {form.cleaned_data['phone']}\n\nMessage:\n{form.cleaned_data['message']}"
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = [settings.EMAIL_HOST_USER]  # Your email or a list of emails

            try:
                send_mail(subject, message, from_email, to_email)
                messages.success(request, 'Thank you for your message. We will get back to you shortly.')
            except Exception as e:
                messages.error(request, 'An error occurred while sending your message. Please try again later.')

            return redirect('contact')  # Ensure this URL name matches your URL configuration
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
