from django.core.mail import send_mail
from django.template.loader import render_to_string


from django.core.mail import send_mail
from django.core.mail import EmailMessage
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from real_estate.settings import EMAIL_HOST_USER

from .models import Enquiry


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def send_enquiry_email(request):
    data = request.data

    try:
        subject = data["subject"]
        name = data["name"]
        email = data["email"]
        message = data["message"]
        #code = get_random_str(6)
        
        #html_message = render_to_string("account/email/confirmation.html")
        email_from = EMAIL_HOST_USER
        recipient_list = [email,]


        send_mail(subject, message, email_from, recipient_list,  fail_silently=True)

        enquiry = Enquiry(name=name, email=email, subject=subject, message=message)
        enquiry.save()

        return Response({"success": "Your Enquiry was successfully submitted"})

    except:
        return Response({"fail": "Enquiry was not sent. Please try again"})
    
    
