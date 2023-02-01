from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
)


# Create new user & superuser
class UserManager(BaseUserManager):
    # user
    def create_user(
        self,
        first_name,
        last_name,
        username,
        email,
        password=None,
    ):
        if not email:
            raise ValueError("User must have an email address")

        if not username:
            raise ValueError("User must have a username")

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)

        user.save(using=self._db)
        return user

    # superuser from user inst above
    def create_superuser(
        self, first_name, last_name, username, email, password=None
    ):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.superadmin = True

        user.save(using=self._db)
        return user


# Custom user model class for db
class User(AbstractBaseUser):
    RESTAURANT = 1
    CUSTOMER = 2

    roleChoices = {
        (RESTAURANT, "Restaurant"),
        (CUSTOMER, "Customer"),
    }

    # table fields for user in db
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=12, blank=True)
    role = models.PositiveIntegerField(
        choices=roleChoices, blank=True, null=True
    )
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    # indicate this user model to be used, not built-in user model
    # also state this update in settings.py, to tell django
    objects = UserManager()

    def __str__(self):
        return self.email

    # admin & superadmin access permissions
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
