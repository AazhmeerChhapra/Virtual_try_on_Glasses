from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View

import random
from django.http import HttpResponse
from rest_framework import generics
from store.models.FielsToBeSent import FieldsToBeSent 
from django.shortcuts import render,redirect
from store.serializiers.FieldsToBeSentSerializers import FieldsToBeSentSerializers
from django.core.mail import send_mail,EmailMessage
from .forms import UserRegistrationForm,OtpForm
class Signup (View):
    
    def get(self, request):
        return render (request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get ('firstname')
        last_name = postData.get ('lastname')
        phone = postData.get ('phone')
        email = postData.get ('email')
        password = postData.get ('password')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        customer = Customer (first_name=first_name,
                             last_name=last_name,
                             phone=phone,
                             email=email,
                             password=password)
        error_message = self.validateCustomer (customer)

        if not error_message:
            number=random.randrange(1000,9999)
            msg=EmailMessage('otp code',f'<p>Your code is { number }</p>','aazhmeerchhapra@gmail.com',[email])
            msg.content_subtype="html"                                          # ^^^^^^^^^
            msg.send()                                                          # |||||||||
            print('the number generated is =====>>>',number)                   # enter your email here
            request.session['user_data'] = {
                'first_name': first_name,
                'last_name': last_name,
                'phone': phone,
                'email': email,
                'password': password,
                'otp': number,
            }
            return redirect('otpform')
            
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render (request, 'signup.html', data)
    

    def validateCustomer(self, customer):
        error_message = None
        if (not customer.first_name):
            error_message = "Please Enter your First Name !!"
        elif len (customer.first_name) < 3:
            error_message = 'First Name must be 3 char long or more'
        elif not customer.last_name:
            error_message = 'Please Enter your Last Name'
        elif len (customer.last_name) < 3:
            error_message = 'Last Name must be 3 char long or more'
        elif not customer.phone:
            error_message = 'Enter your Phone Number'
        elif len (customer.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len (customer.password) < 5:
            error_message = 'Password must be 5 char long'
        elif len (customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists ():
            error_message = 'Email Address Already Registered..'
        # saving

        return error_message
    
    
def otp_form(request):
    if request.method=='POST':
        form=OtpForm(request.POST)
        if form.is_valid():
            token_number=form.cleaned_data.get('token_number')
            user_data = request.session.get('user_data')
            if user_data and token_number == user_data['otp']:
                customer = Customer(
                    first_name=user_data['first_name'],
                    last_name=user_data['last_name'],
                    phone=user_data['phone'],
                    email=user_data['email'],
                    password=user_data['password']
                )
                customer.password = make_password(customer.password)
                customer.register()

                # Clear session data
                del request.session['user_data']

                FieldsToBeSent.objects.create(number=user_data['otp'])
                return redirect("homepage")
            else:
                return ("Wrong OTP fill the form again")
    else:
        form=OtpForm()
    return render(request,'otp.html',{'form':form})

class FieldsToBeSentViews (generics.ListCreateAPIView):
    queryset=FieldsToBeSent.objects.all()
    serializer_class=FieldsToBeSentSerializers
    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)
    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)
