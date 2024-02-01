from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    if request.method =='POST':
        fullName = request.POST['Name']
        email = request.POST['Email']
        password = request.POST['Password']
        confirmpassword = request.POST['ConfirmPass']
        if len(fullName) <= 4:
            return render(request, 'login/index.html', {'error_message': 'Name is too sohrt'})
        if not fullName.isalnum():
              return render(request, 'login/index.html', {'error_message': 'Name must be written in Alpha Numeric '})
        if not '@' in email and email.count('@') == 1 and email.index('@') > 0 and email.index('@') < len(email) - 1:
              return render(request, 'login/index.html', {'error_message': 'Incorrect Email Format'})
        if User.objects.filter(email=email).exists():
            return render(request, 'login/index.html', {'error_email_message': 'Email already exists'})
        # if password!= "(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}":
        #     return render(request, 'login/index.html', {'error_password_message': 'Password must be at least 8 characters long, contain one lowercase letter, one uppercase letter, and one digit.'})
        if password!= confirmpassword:
            return render(request, 'login/index.html', {'error_conf_pass': 'Password and Confirm Password do not match'})
        else:
            myUser = User.objects.create_user(fullName , email, password )
            myUser.save()
            return redirect('login-page')
        
    return render(request,"login/index.html")


def loginPage(request):
    if request.method =='POST':
        name = request.POST['Name']
        password = request.POST['Password']
        user= authenticate(request, username=name ,password= password )
        if user is not None:
           login(request, user)
           return redirect('home-page')
        else:
            return render(request, 'login/loginpage.html', {'error_message': 'Incorrect Username or Password'})
    return render(request,"login/loginpage.html")

#@login_required(login_url='login-page') #// 1 method
@login_required  #2 Method
def homePage(request):
    return render(request,"login/home.html")

#custom
def custom_page_not_found_view(request, exception):
    return render(request, 'login/404.html', {}, status=404)
# def custom_page_not_found(request, exception):
#     return render(request, 'login/404.html', {}, status=404)
# def error_404(request, exception):
#     return render(request, 'login/404.html', status=404)

 
