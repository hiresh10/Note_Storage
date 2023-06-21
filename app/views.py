from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Note, UserMaster
from app.serializers import Noteserializer
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.contrib.auth import logout




class NoteViewSet(viewsets.ViewSet):
    def list(self, request):
        notes = Note.objects.all()
        serializer = Noteserializer(notes, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        note = get_object_or_404(Note, pk=pk)
        serializer = Noteserializer(note)
        return Response(serializer.data)

    def create(self, request):
        serializer = Noteserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def update(self, request, pk=None):
        note = get_object_or_404(Note, pk=pk)
        serializer = Noteserializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        note = get_object_or_404(Note, pk=pk)
        note.delete()
        return Response(status=204)


def Index(request):
    return render(request, 'app/index.html')

def SignupPage(request):
    return render(request, 'app/signup.html')

def Register(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        gender = request.POST['gender']

        user = UserMaster.objects.filter(email=email)
        if user:
            message = "User already exists!!"
            return render(request,'app/signup.html',{'msg':message})

        else: 
            if password==cpassword:
                newuser = UserMaster.objects.create(name=name,email=email,password=password,gender=gender)
                message = 'Signup Successfull!!'
                return render(request,'app/login.html', {'msg':message})
            else:
                message = "Password Missmatch!!"
                return render(request,'app/signup.html',{'msg':message})
    else:
        message="Bad request"
        return render(request,'app/index.html',{'msg':message})


def LoginPage(request):
    return render(request, 'app/login.html')


def Loginuser(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            user = UserMaster.objects.get(email=email)
            if user.password == password:
                request.session['user_id'] = user.id
                request.session['user_email'] = user.email
                request.session['name'] = user.name
                request.session['gender'] = user.gender
                message = "Login Successful!"
                return render(request, 'app/home.html', {'msg': message})
            else:
                message = "Incorrect Password"
                return render(request, 'app/login.html', {'msg': message})
        except ObjectDoesNotExist:
            message = "User does not exist"
            return render(request, 'app/login.html', {'msg': message})
    else:
        return render(request, 'app/login.html')

def Home(request):
    notes = Note.objects.all()
    return render(request, 'app/home.html', {'notes': notes})

def Profile(request):
    return render(request,'app/profile.html')

def Post_notepage(request):
    return render(request,'app/post_note.html')




def Post_note(request):
    if request.method == "POST":
        name = request.POST['user_name']
        content = request.POST['note_content']
        note_type = request.POST['note_type']
        note_file = request.FILES.get('note_file')

        note = Note.objects.create(name=name,content=content,type=note_type,note_file=note_file,)
        note.save()

        message = "Note Posted Successfully!"
        return render(request, 'app/home.html', {'msg': message})

    return render(request, 'app/post_note.html', {'user_email': request.user.email})


def Notes(request):
    all_notes = Note.objects.all()
    return render(request, 'app/notes.html', {'all_notes': all_notes})

def get_users(request):
    users = UserMaster.objects.all()
    user_list = [{'name': user.name} for user in users]
    return JsonResponse({'users': user_list})


def logout_view(request):
    logout(request)
    return redirect('index')

def AdminLoginPage(request):
    return render(request,'admin/admin_login.html')

def Aminlogin(request):
    username = request.POST['username']
    password = request.POST['password']

    if username == "admin" and password == "admin":

        request.session['username'] = username
        request.session['password'] = password
        return render(request,'admin/adminhome.html')

    else:
        message = "Username and password not match"
        return render(request,"admin/admin_login.html",{'msg':message})
    
def Userlist(request):
    users = UserMaster.objects.all()
    return render(request, 'admin/userlist.html', {'users': users})

def UserDelete(request,pk):
    user = UserMaster.objects.get(pk=pk)
    user.delete()

    return redirect('userlist')

def NoteList(request):
    note = Note.objects.all()
    return render(request, 'admin/noteinfo.html', {'note': note})

def NoteDelete(request,pk):
    note = Note.objects.get(pk=pk)
    note.delete()
    return redirect('notelist')

def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect('index')