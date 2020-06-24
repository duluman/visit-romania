from users.models import Profile
from django.conf import settings
from django.db.models.signals import post_save
# for payments
import stripe
from payments.models import StripeCustomer


def create_user_profile(sender, instance, created, **kwargs):

    if created:
        Profile.objects.create(user=instance)


def create_stripe_customer(sender, instance, created, **kwargs):
    if created:
        customer = stripe.Customer.create(
            email=instance.email,
            name=f'{instance.first_name} {instance.last_name}',
            api_key=settings.STRIPE_SECRET_KEY
        )

        StripeCustomer(user=instance, customer_id=customer['id']).save()


post_save.connect(create_user_profile, sender=settings.AUTH_USER_MODEL)
post_save.connect(create_stripe_customer, sender=settings.AUTH_USER_MODEL)
#
# from users.models import MyUserManager
# from helpers.emails import send_register_email
# from users.models import MyUser
# from django.db.models.signals import pre_save
# def generate_random_password(sender, instance, *args, **kwargs):
#     if not instance.pk:
#
#         email = instance.email
#         first_name = instance.first_name
#         last_name = instance.last_name
#
#         generated_password = MyUserManager().make_random_password()
#         print(f'email: {email} - password: {generated_password}')
#
#         send_register_email(first_name, last_name, email, generated_password)
#
#         instance.set_password(generated_password)

# pre_save.connect(generate_random_password, sender=MyUser)

