import logging

from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactForm
from .models import Education, Project, Skill

logger = logging.getLogger(__name__)


def _send_contact_notification(contact_message):
    """Email the portfolio owner while keeping the visitor's email as Reply-To."""
    if not settings.EMAIL_HOST_USER or not settings.EMAIL_HOST_PASSWORD:
        raise RuntimeError('Email credentials are not configured.')

    subject = f'Portfolio contact: {contact_message.subject}'
    body = (
        'You received a new message from your portfolio website.\n\n'
        f'Name: {contact_message.name}\n'
        f'Email: {contact_message.email}\n'
        f'Subject: {contact_message.subject}\n\n'
        'Message:\n'
        f'{contact_message.message}\n\n'
        'This message is also saved in Django Admin.'
    )

    email = EmailMessage(
        subject=subject,
        body=body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[settings.PORTFOLIO_OWNER_EMAIL],
        reply_to=[contact_message.email],
    )
    email.send(fail_silently=False)


def home(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        contact_message = form.save()

        try:
            _send_contact_notification(contact_message)
        except Exception:
            # The database copy is retained even if Gmail/SMTP is temporarily unavailable.
            logger.exception('Unable to send portfolio contact notification email.')
            messages.warning(
                request,
                'Thanks! Your message was saved successfully. Email notification is temporarily unavailable.',
            )
        else:
            messages.success(request, 'Thanks! Your message has been received.')

        return redirect('home')

    context = {
        'skills': Skill.objects.all(),
        'projects': Project.objects.all(),
        'education': Education.objects.all(),
        'form': form,
    }
    return render(request, 'core/home.html', context)


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'core/project_detail.html', {'project': project})
