# views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})

def contact_success(request):
    return HttpResponse('Thank you for your message. We will get back to you shortly.')
