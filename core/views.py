from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings
from .forms import AppointmentForm, SignUpForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Appointment  
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages

def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def services(request):
    return render(request, 'core/services.html')

def price(request):
    return render(request, 'core/price.html')

def gallery(request):
    return render(request, 'core/gallery.html')

def appointment(request):
    return render(request, 'core/appointment.html')

def page_not_found(request):
    return render(request, 'core/404.html')

# def contact(request):
#     return render(request, 'core/contact.html')

def cookies(request):
    return render(request, 'core/cookies.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('index')  # Redirect to a named URL
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def logout_view(request):
    auth_logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('index')  # Redirect to a named URL

@login_required
def profile_view(request):
    return render(request, 'profile.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Log the user in after successful signup
            messages.success(request, 'You have successfully signed up and are now logged in.')
            return redirect('index')  # Redirect to the named URL 'index'
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

# Account view
class AccountView(TemplateView):
    template_name = 'core/account.html'




from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from .forms import AppointmentForm
from .models import Appointment

def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment_message = form.save()

            service_location = "Home Service" if appointment_message.service_type == 'home' else "Office Visit"

            try:
                send_mail(
                    subject=f"New Appointment Request from {appointment_message.name}",
                    message=f"Preferred Date: {appointment_message.date}\n"
                            f"Preferred Time: {appointment_message.time}\n"
                            f"Service: {appointment_message.service}\n"
                            f"Service Type: {service_location}\n"
                            f"Address: {appointment_message.address}\n"
                            f"Phone: {appointment_message.phone}\n"
                            f"Additional Notes: {appointment_message.notes}",
                    from_email=appointment_message.email,
                    recipient_list=['uwajohn101@gmail.com'],  # Replace with your email
                    fail_silently=False,
                )
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            except Exception as e:
                # Log the exception (optional)
                print(f"An error occurred: {e}")
                messages.error(request, "There was an issue sending your message. Please try again later.")
                return redirect('appointment')

            # Provide user feedback
            messages.success(request, "Your appointment request has been sent successfully. We will get back to you as soon as possible. Thanks!")
            return redirect('appointment')  # Redirect to the same page or a thank you page
    else:
        form = AppointmentForm()

    return render(request, 'core/appointments.html', {'form': form})




def appointment_success(request):
    return render(request, 'core/appointment_success.html')


@login_required
def view_appointments(request):
    if not request.user.is_staff:
        messages.error(request, "You do not have permission to view this page.")
        return redirect('index')
    appointments = Appointment.objects.all().order_by('-requested_at')
    return render(request, 'core/view_appointments.html', {'appointments': appointments})

@login_required
def user_appointment_view(request):
    # Fetch appointments for the logged-in user and order by requested_at (most recent first)
    appointment = Appointment.objects.filter(email=request.user.email).order_by('-requested_at')
    return render(request, 'core/user_view_appointments.html', {'appointments': appointment})






def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()

            try:
                # Compose the full message including all the fields
                full_message = (
                    f"Name: {contact_message.name}\n"
                    f"Email: {contact_message.email}\n"
                    f"Phone: {contact_message.phone or 'N/A'}\n"
                    f"Subject: {contact_message.subject or 'No Subject'}\n"
                    f"Message:\n{contact_message.message}"
                )

                send_mail(
                    subject=f"New Contact Message from {contact_message.name}: {contact_message.subject or 'No Subject'}",
                    message=full_message,
                    from_email=contact_message.email,
                    recipient_list=['uwajohn101@gmail.com'],  # Replace with your email
                    fail_silently=False,
                )
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            except Exception as e:
                # Log the exception (optional)
                print(f"An error occurred: {e}")
                messages.error(request, "There was an issue sending your message. Please try again later.")
                return redirect('contact_us')

            # Provide user feedback
            messages.success(request, "Your message has been sent successfully, we will get back to you as soon as possible. Thanks!")
            return redirect('contact_us')  # Redirect to the same page or a thank you page
    else:
        form = ContactForm()

    return render(request, 'core/contact.html', {'form': form})



from .models import ContactMessage
@login_required
def view_contacts(request):
    contact_messages = ContactMessage.objects.all().order_by('-sent_at')  
    return render(request, 'core/view_contacts.html', {'contact_messages': contact_messages})
