from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

from core.softdelete import SoftDelete

class User(AbstractBaseUser, SoftDelete):
    
    pass


