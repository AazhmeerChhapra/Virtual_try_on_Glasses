from django.shortcuts import render , redirect , HttpResponseRedirect, HttpResponse
from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import View
from django.core.mail import send_mail,EmailMessage
from store.models.FielsToBeSent import FieldsToBeSent 
from django.contrib.auth.hashers import make_password


from .forms import UserRegistrationForm,OtpForm

import random


class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get ('return_url')
        return render (request, 'login.html')

    def post(self, request):
        email = request.POST.get ('email')
        password = request.POST.get ('password')
        customer = Customer.get_customer_by_email (email)
        error_message = None
        if customer:
            flag = check_password (password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                print(customer.first_name)

                if Login.return_url:
                    return HttpResponseRedirect (Login.return_url)
                else:
                    Login.return_url = None
                    return redirect ('homepage')
            else:
                error_message = 'Invalid !!'
        else:
            error_message = 'Invalid !!'

        print (email, password)
        return render (request, 'login.html', {'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('login')

def forget_password_link(request):
    #  email = request.GET.get('email')
    #  print("email is ", email)
    #  if email is None:
    #      return HttpResponse('Please Go back and enter email')
    #  else:
    #   number=random.randrange(1000,9999)
    #   msg=EmailMessage('otp code',f'<p>Your code is { number }</p>','aazhmeerchhapra@gmail.com',[email])
    #   msg.content_subtype="html"                                          # ^^^^^^^^^
    #   msg.send()                                                          # |||||||||
    #   print('the number generated is =====>>>',number)    
    #   request.session['user_data'] = {
    #              'otp': number,
    #          }              
      return render(request,'forget_password.html')

def forget_password(request):
    email = request.POST.get('email')
    print("email is ", email)
    if email is None:
         return HttpResponse('Please Go back and enter email')
    else:
      number=random.randrange(1000,9999)
      msg=EmailMessage('otp code',f'<p>Your code is { number }</p>','aazhmeerchhapra@gmail.com',[email])
      msg.content_subtype="html"                                          # ^^^^^^^^^
      msg.send()                                                          # |||||||||
      print('the number generated is =====>>>',number)    
      request.session['user_data'] = {
                 'email':email,
                 'otp': number
             }  
      return redirect('otpverify')          



def verify_otp(request):
    if request.method=='POST':
        form=OtpForm(request.POST)
        if form.is_valid():
            token_number=form.cleaned_data.get('token_number')
            user_data = request.session.get('user_data')
            if user_data and token_number == user_data['otp']:
                data = {}
                data['email'] = user_data['email']
                # Clear session data
                del request.session['user_data']

                FieldsToBeSent.objects.create(number=user_data['otp'])
                return render(request, 'change_password.html', data)
            else:
                return ("Wrong OTP fill the form again")
    else:
        form=OtpForm()
    return render(request,'otp.html',{'form':form})
    

def change_password(request):
    if request.method=='POST':
        email = request.POST.get('email')
        customer = Customer.get_customer_by_email(email)
        password = request.POST.get('password')
        confirm_password = request.POST.get('password_confirm')
        if password == confirm_password:
            customer.password = make_password(password)
            customer.save()
            return redirect("login")
    else:
        return request

            
