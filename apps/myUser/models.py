from django.db import models

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, telphone, nickName, password=None):
        """
        Creates and saves a User with the given telphone, nickName and password.
        """
        if not telphone:
            raise ValueError('Users must have an telphone number')

        user = self.model(
            telphone=telphone,
            nickName=nickName,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, telphone, nickName, password):
        """
        Creates and saves a superuser with the given telphone, nickName and password.
        """
        user = self.create_user(telphone,
            password=password,
            nickName=nickName
        )
        user.is_admin = True
        user.save(using=self._db)
        return user



class MyUser(AbstractBaseUser):
    telphone = models.CharField(
        verbose_name='telephone number',
        max_length=20,
        unique=True,
    )
    nickName = models.CharField(max_length=32,unique=True,)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    email = models.EmailField(max_length=254,unique=True,null=True,blank=True)
    avatar = models.CharField(max_length=256,null=True,blank=True)
    useSex_choices = (("male", u"男"),
                      ("female", u"女"),
                      )
    sex = models.CharField(choices=useSex_choices, max_length=16, default="male")
    friens = models.ManyToManyField('self',blank=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'telphone'
    REQUIRED_FIELDS = ['nickName']

    def get_full_name(self):
        # The user is identified by their email address
        return self.telphone

    def get_short_name(self):
        # The user is identified by their email address
        return self.telphone

    def __str__(self):              # __unicode__ on Python 2
        return self.nickName

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
        

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin









