from django.shortcuts import redirect, render, HttpResponse

from .models import User
from .forms import registerForm


# Register
def registerUser(request):
    """
    New user registration. 'form' from here
    is used in registerUser template. When
    form is valid and saved, it triggers
    singals and print at terminal.
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
            return redirect("registerUser")
    else:
        form = registerForm()
    context = {"form": form}

    return render(request, "account/registerUser.html", context)
