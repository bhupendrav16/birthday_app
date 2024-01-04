from django.shortcuts import render
from datetime import date 
from .smtp import send_message
# Create your views here.


def home(request):
    if request.method == "POST":
        username = request.POST.get('name')
        birthday = request.POST.get('birthday')
        date_of_joining =request.POST.get('date_of_joining')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        day = str(date.today())
        # print(birthday)
        if birthday == day:
            send_message(email,username)
            return render(request, "home/home.html",{'username':username})
        return render(request,"home/home.html" , {'username':username , 'birthday':birthday, 'date_of_joining':date_of_joining,'phone':phone,'email':email,'day':day})
    
    return render(request,"home/home.html")
    

def register(request):

    return render(request,"home/register.html")
    