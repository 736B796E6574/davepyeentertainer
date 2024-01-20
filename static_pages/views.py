from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
from .models import Event  # Import the Event model

def index(request):
    # Fetch events from the database
    events = Event.objects.all()
    
    # Pass events to the template
    return render(request, 'index.html', {'events': events})

def contact_confirmation(request):
    return render(request, 'contact-confirmation.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('your-name')
        email = request.POST.get('your-email')
        phone = request.POST.get('your-phone')  # Get the phone number from the form
        message = request.POST.get('your-message')

        if not name or not email or not message:
            # Add your error message or handling here
            return HttpResponse("Please fill all the fields in the form.")

        email_body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"  # Include the phone in the email body

        try:
            send_mail(
                subject=f"New contact form submission from {name}",
                message=email_body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            # Redirect or send a success message after sending the email
            return redirect('contact_confirmation')
        except Exception as e:
            # Add your error handling here
            return HttpResponse(f"Error sending email: {str(e)}")

    return render(request, 'contact.html')
