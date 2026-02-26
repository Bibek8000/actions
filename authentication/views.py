from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student
from django.contrib.auth.hashers import check_password
def dashboard(request): 
    if 'student_name' not in request.session:
        return redirect('login')
    
    
    name = request.session.get('student_name')  
    return render(request,'authentication/dashboard.html', {
        "student_name": name
    })
        
        

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            student = Student.objects.get(username=username)
            print(student)
            if check_password(password,student.password):
                request.session['student_name = student.name']
                return redirect('dashboard')
            else:
                return render(request,'authentication/login.html',{
                'error':"invalid from pass" })
        except:
            return render(request,'authentication/login.html',{
                'error':"invalid from except"
            })


    return render(request,'authentication/login.html')
