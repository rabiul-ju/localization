from django.shortcuts import render
from .forms import LoginFrom, RegistrationForm
from .helper import Helper
from django.utils.translation import LANGUAGE_SESSION_KEY
from django.utils import translation
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext, ugettext


# Create your views here.


def login(request):
    """
    Here first check the session. If session has data than redirect to
    home page. else redirect to loging page.
    :param request:
    :return:
    """
    helper = Helper()
    message = False
    if request.method == "GET":
        try:
            token = request.session["token"]
            user = helper.users(token)
            if user is not None:
                context = {
                    'user': user,
                    'message': message
                }
                return render(request, 'home.html', context)
        except:
            request.session[LANGUAGE_SESSION_KEY] = "en"
            translation.activate(request.session[LANGUAGE_SESSION_KEY])
            request.session["token"] = None
            pass

    if request.method == "POST":
        message = True
        form = LoginFrom(request.POST)
        if form.is_valid():  # All validation rules pass
            token = helper.login(form.cleaned_data)
            user = helper.users(token)
            # comment the below line code when real api is implemented.
            # currently default user is sent for every time.
            user = {"email":"yourname@gmail.com", "id": 1001}
            if user is not None:
                context = {
                    'user': user,
                    'message': message
                }
                request.session["token"] = token
                return render(request, 'home.html', context)

    form = LoginFrom()
    request.session["token"] = None
    context_dict = {
        'form': form,
        "message": message,
    }

    return render(request, 'login.html', context=context_dict)


def logout(request):
    request.session["token"] = None
    return render(request, 'login.html')


def registration(request):
    helper = Helper()
    message = False
    if request.method == "POST":
        message = True
        form = RegistrationForm(request.POST)
        if form.is_valid():
            success = helper.registraion(form.cleaned_data)
            # comment the below line when called it from real api.
            # now success is always true
            success = True
            if success:
                return render(request, 'login.html', {"success": success})

    form = RegistrationForm()
    context = {
        'form': form,
        'message': message
    }
    return render(request, 'registration.html', context)


def home(request):
    helper = Helper()
    try:
        token = request.session["token"]
        user = helper.users(token)
        if user is not None:
            context = {
                'user': user
            }
            return render(request, 'home.html', context)
    except:
        pass

    return render(request, 'login.html')


def change_language(request):
    reverse_url = request.POST["next"]
    translation.activate(request.POST["language"])
    request.session[LANGUAGE_SESSION_KEY] = request.POST["language"]
    return redirect(reverse_url)
