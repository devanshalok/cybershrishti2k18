from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import contact_us as cu
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import datetime

import smtplib
from email.mime.text import MIMEText


class Template(generic.TemplateView):
    template_name="bot/index.html"

# class TryTemplate(generic.TemplateView):
#     template_name="bot/modaltemp.html"

def contactus(request):

    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']

        val=0
        count=0
        error_name=''
        error_message=''
        error_email=''
        error_phone=''
        if name=='':
            error_name="Please enter your name."
            count+=1

        if email=='':
            error_email="Please enter your email address."
            count+=1

        if phone=='':
            error_phone="Please enter your phone number."
            count+=1
        else:
            if len(phone)<10 or len(phone)>11:
                error_phone="Please enter a valid contact number"
                count+=1

        if message=='':
            error_message="Please enter a message."
            count+=1

        if count==0:
            entry=cu(name=name,email=email,phone=phone,message=message)
            entry.save()      
            val=0
            print('====================================================================== %d'%val)
            return render(request,'bot/child.html',{'error_name':error_name,'error_phone':error_phone,'error_message':error_message,'error_email':error_email,'val':val}) 
        if count>0:
            val=1
            return render(request,"bot/child.html",{'error_name':error_name,'error_phone':error_phone,'error_message':error_message,'error_email':error_email,'val':val,'name_val':name,'email_val':email,'phone_val':phone,'message_val':message})

    else:
        return render(request,"bot/index.html")

def redirect(request):
    return HttpResponseRedirect('/home')

    # class Template(generic.TemplateView):
    #     template_name="bot/index.html"












# def sendmail(request):
    
#     if request.method=='POST':
#         name=request.POST['name']
#         email=request.POST['email']
#         phone=request.POST['phone']
#         message=request.POST['message']

#         count=0
#         error_name=''
#         error_message=''
#         error_email=''
#         error_phone=''
#         if name=='':
#             error_name="Please enter your name."
#             count+=1

#         if email=='':
#             error_email="Please enter your email address."
#             count+=1

#         if phone=='':
#             error_phone="Please enter your phone number."
#             count+=1
#         else:
#             if len(phone)<10 or len(phone)>10:
#                 error_phone="Please enter a valid contact number"
#                 count+=1

#         if message=='':
#             error_message="Please enter a message."
#             count+=1

#         if count==0:
#             body=message                                        #pass the html syntax
#             sender="aman.parmar17@gmail.com"
#             receiver="itsourearth2016@gmail.com"

#             msg=MIMEText(body)
#             msg["From"]=sender
#             msg["To"]=receiver
#             msg["Subject"]="contact made"

#             ss=smtplib.SMTP("smtp.gmail.com",587)
#             ss.starttls()
#             ss.login("aman.parmar17@gmail.com","aman.parmar17")

#             ss.send_message(msg)
#             print("mail sent")
#             ss.quit()

#             return HttpResponseRedirect('/home') 
#         return render(request,"bot/child.html",{'error_name':error_name,'error_phone':error_phone,'error_message':error_message,'error_email':error_email})

#     else:
#         return render(request,"bot/index.html")

    