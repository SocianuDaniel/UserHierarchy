from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator


class UserManager(BaseUserManager):
    """Mamager for users"""

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('User must provide an email ....')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """create superusers """
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the System"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'


class CommonUserAbstract(models.Model):
    """Base abstract model for costumised users"""
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="%(class)s_user")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    level = models.PositiveIntegerField(
        _('user level'),
        validators=[MinValueValidator(0), MaxValueValidator(5)]
        )

    class Meta:
        abstract = True


class OwnerManager(models.Manager):
    def create_owner(self, email, password=None, **extra_fields):
        user = get_user_model().objects.create_user(
            email, password, **extra_fields
            )
        if not user:
            raise ValueError(_('error creating the user'))
        print(**extra_fields)
        level = 1
        owner = self.model(user=user, level=level, **extra_fields)
        owner.save(using=self._db)
        return owner


class Owner(CommonUserAbstract):
    level = models.PositiveBigIntegerField(
        _("user level"),
        editable=False,
        default=1
        )
    objects = OwnerManager()
