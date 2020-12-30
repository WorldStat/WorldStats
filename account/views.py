from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse

def entry(request):
    if request.method == 'GET':
        return render(request, 'account/entry.html')
    elif request.method == 'POST':
        data = dict()
        _login = request.POST.get('login')
        _pass1 = request.POST.get('pass1')

        user = authenticate(request, username=_login, password=_pass1)
        if user is not None:
            data['color'] = 'green'
            data['message'] = "Login successful"
            login(request, user)
        else:
            data['color'] = 'red'
            data['message'] = "User not found"

        return render(request, 'account/entry_res.html', context=data)

def exit(request):
    logout(request)
    return redirect('main')

def profile(request):
    return render(request, 'account/profile.html')

def reg(request):
    if request.method == 'GET':
        return render(request, 'account/reg.html')
    elif request.method == 'POST':
        data = dict()
        _login = request.POST.get('login')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        email = request.POST.get('email')

        """
        # test:
        data['login'] = login
        data['pass1'] = pass1
        data['pass2'] = pass2
        data['email'] = email
        """
        if pass1 != pass2:
            data['color'] = 'red'
            data['message'] = "Passwords don't match"
        else:
            user = User.objects.create_user(_login, email, pass1)
            user.save()
            if user is None:
                data['color'] = 'red'
                data['message'] = "Registration is denied"
            else:
                data['color'] = 'green'
                data['message'] = "Registration is successful "
        return render(request, 'account/reg_res.html', context=data)

def ajax_reg(request):
    response = dict()
    _login = request.GET.get('login')

    try:
        User.objects.get(username=_login)
        response['mess'] = 'login taken'
    except User.DoesNotExist:
        response['mess'] = 'login available'

    return JsonResponse(response)