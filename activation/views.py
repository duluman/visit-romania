from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect, Http404
from activation.models import Activation
from django.utils import timezone
from activation.helpers.utils import regenerate_activation
from users.forms import SetPassword
from django.contrib.auth import authenticate, login
from django.conf import settings
# Create your views here.


def activate(request, token):
    # token exists
    activation = get_object_or_404(Activation, token=token)

    # if user is active
    if activation.user.is_active:
        raise Http404

    # token invalid
    if activation.expires_at < timezone.now():
        if request.GET.get('resend'):
            regenerate_activation(activation)
            return HttpResponseRedirect(reverse('users:login'))

        return render(request, 'activation/activate.html', {
            'token': activation.token
        })

    if request.method == 'POST':
        form = SetPassword(activation.user, request.POST)

        if form.is_valid():
            user_with_password = form.save(commit=False)
            user_with_password.is_active = True
            user_with_password.save()

            activation.activated_at = timezone.now()
            activation.save()

            email = user_with_password.email
            # password = user_with_password.password
            password = form.cleaned_data['password']
            authenticate_user = authenticate(request, username=email, password=password)
            login(request, authenticate_user) #, backend='django.contrib.auth.backends.ModelBackend'
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = SetPassword(activation.user)

    return render(request, 'activation/set_password.html', {
        'form': form,
        'token': token
    })
