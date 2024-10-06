
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

USER_LEVELS = (
    (0, _('Root')),
    (1, _('Owner')),
    (2, _('Supervisor'))
)


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


def validateEqual(value):
    if value != 1:

        raise ValidationError(
            _('%(value)s must be equal to 1  '),
            params={"value": value},
            )


class CommonUserAbstract(models.Model):
    """
        Base abstract model for costumised users
    """
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="%(class)s_user")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    level = models.PositiveIntegerField(
        _('user level'),
        validators=[validateEqual],
        choices=USER_LEVELS
        )

    class Meta:
        abstract = True


class OwnerManager(models.Manager):
    """
    owner model
    """

    def create_owner(self, email, password=None, **extra_fields):
        user = get_user_model().objects.create_user(
            email, password, **extra_fields
            )
        if not user:
            raise ValueError(_('error creating the user'))
        level = 1
        owner = self.model(user=user, level=level, **extra_fields)
        owner.save()
        return owner


class Owner(CommonUserAbstract):

    _owner_level = 1
    objects = OwnerManager()

    def save(self, force_insert=False, force_update=False):
        if self.level != USER_LEVELS[self._owner_level][0]:
            raise ValidationError('nu e bun')
        if self.user.is_superuser or self.user.is_staff:
            raise ValidationError(_('user must not be superuser or staff'))
        self.level = self._owner_level
        super(Owner, self).save(force_insert, force_update)
