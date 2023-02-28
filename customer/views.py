from django.shortcuts import redirect, render
from .models import User
from .forms import registerForm
from django.contrib import messages


# Register
def registerUser(request):
    """
    New user registration. 'form' from here is 
    used in registerUser template. When form is 
    valid and saved, it triggers singals and 
    print at terminal.
    """
    if request.method == "POST":
        form = registerForm(request.POST)
        if form.is_valid():
            # method 1 - create user from form
            # password = form.cleaned_data['password']
            # user = form.save(commit=False)
            # user.set_password(password)
            # user.role = User.CUSTOMER
            # user.save()
            # return redirect("registerUser")

            # method 2 - create user from model
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password,
            )
            user.role = User.CUSTOMER
            user.save()
            messages.success(
                request, "Success! Your account is registered"
            )
            return redirect("registerUser")

        # handle any field errors
        else:
            print(form.errors)
    else:
        form = registerForm()
    context = {"form": form}

    return render(request, "customer/registerUser.html", context)


"""
Able to access and use messages object here
in all templates due to the below in settings.py
'django.contrib.messages.context_processors.messages'

whatever is returned through context_processors is 
accessible in all template files
"""
