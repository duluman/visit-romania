
from users.forms import ContactForm

from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import get_template
from django.shortcuts import render


def contact(request):
    form = ContactForm(request.POST)
    print("*"*10)
    print(form)
    print("*" * 10)
    if form.is_valid():
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        email_template = get_template('users/contact.html')

        email_content = email_template.render(
            {

                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'subject': subject,
                'message': message,
            }
        )
        print("*" * 10)
        print(email_content)
        print("*" * 10)
        mail = EmailMultiAlternatives(
            'New contact message',
            email_content,
            settings.EMAIL_HOST_USER,
            [email]
        )
        mail.content_subtype = 'html'
        mail.send()




