from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
)


# Create new user & superuser
class UserManager(BaseUserManager):
    # user
    def createUser(
        self, firstName, lastName, username, email, password=None
    ):
        if not email:
            raise ValueError("User must have an email address")

        if not username:
            raise ValueError("User must have a username")

        newUser = self.model(
            firstName=firstName,
            lastName=lastName,
            email=self.normalize_email(email),
            username=username,
        )
        newUser.set_password(password)
        newUser.save(using=self._db)
        return newUser

    # superuser from user instance
    def createSuperUser(
        self, firstName, lastName, username, email, password=None
    ):
        superUser = self.createUser(
            firstName=firstName,
            lastName=lastName,
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        superUser.is_admin = True
        superUser.is_active = True
        superUser.is_staff = True
        superUser.superadmin = True
        superUser.save(using=self._db)
        return superUser


# Create custom user model class
class User(AbstractBaseUser):
    RESTAURANT = 1
    CUSTOMER = 2

    roleOption = {
        (RESTAURANT, "Restaurant"),
        (CUSTOMER, "Customer"),
    }

    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=12, blank=True)
    role = models.PositiveIntegerField(
        options=roleOption, blank=True, null=True
    )

    # required fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username', 'firName', 'lastName']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, objective):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True