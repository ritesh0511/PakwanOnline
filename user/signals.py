from django.core.mail import send_mail
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User

@receiver(post_save,sender=User)
def send_success_mail(sender,instance,created,*args,**kwargs):
    if created:
        subject = 'Welcome to Our Website'
        
        message = f'Hi {instance.first_name}\n\nThank you for Registering at our website'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [instance.email]
        print('mailed successfully')
        send_mail(subject,message,email_from,recipient_list)



from .models import User,UserProfile

@receiver(post_save,sender=User)
def create_user_profile_post_save_user(sender,instance,created=False,**kwargs):
    print(created)
    if created:
        UserProfile.objects.create(user=instance)
    else:
        try:
            userprofile = UserProfile.objects.get(user=instance)
            userprofile.save()
        except :
            UserProfile.objects.create(user=instance)