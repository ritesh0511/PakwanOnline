from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.core.validators import RegexValidator,FileExtensionValidator
from django.contrib.auth.models import PermissionsMixin
#from django.contrib.gis.geos import Point
#from django.contrib.gis.db import models as gismodels


# Create your models here.

class UserManger(BaseUserManager):
    
    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError('users must have an email address')
        user = self.model(email = self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_admin(self,email,password=None,**extra_fields):
        return self.create_user(email,password,**extra_fields,is_staff= True,is_superuser=True,is_admin=True)


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractBaseUser,PermissionsMixin,TimestampedModel):
    class Role(models.TextChoices):
        VENDOR = ('vendor','Vendor')
        CUSTOMER = ('customer','Customer')

     
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=10,unique=True)
    role = models.CharField(max_length=20,choices=Role.choices)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_join = models.DateField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'email'

    objects = UserManger()

    def __str__(self):
        return self.email


class Address(TimestampedModel):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    city = models.CharField(max_length=20,blank=True,null=True)
    state = models.CharField(max_length=20,blank=True,null=True)
    pin_code = models.CharField(max_length=20,blank=True,null=True)
    country = models.CharField(max_length=20,blank=True,null=True)
    latitude = models.CharField(max_length=20,blank=True,null=True)
    longitude = models.CharField(max_length=20,blank=True,null=True)
    #location = gismodels.PointField(blank=True,null=True,srid=4326)

    def __str__(self):
        return f'{self.city}, {self.state}, {self.country}, {self.pin_code}'


class UserProfile(TimestampedModel):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    profile_picture = models.ImageField(upload_to='profile_image',blank=True,null=True,validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png'])])
    cover_photo  = models.ImageField(upload_to='cover_photo',blank=True,null=True,validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png'])])

    def __str__(self) -> str:
        return self.user.email
    
