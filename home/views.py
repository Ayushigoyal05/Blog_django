from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from blogin.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def home(request):
	return render(request, 'home/home.html')

def about(request):
	return render(request, 'home/about.html')

def contact(request):
	if request.method=='POST':
		name=request.POST['name']
		email=request.POST['email']
		phone=request.POST['phone']
		desc=request.POST['desc']
		if len(name)<2 or len(phone)<10 or len(email)<11 or len(desc)<4:
				messages.warning(request, 'Please fill the form correctly')
		else:
				messages.success(request, 'Your form has been sent successfully')
		#the variable contactss is a random variable.
				contactss=Contact(name=name, email=email, phone=phone, desc=desc)
				contactss.save()

	return render(request, 'home/contact.html')


def search(request):
	query=request.GET['query']
	if len(query)>75:  #this to provide security to searching algo so by long query one can not guess it
		all=Post.objects.none()
	else:
		alltitle=Post.objects.filter(title__icontains=query)
		allcontent=Post.objects.filter(content__icontains=query)
		all=alltitle.union(allcontent)

	if all.count()==0:
		messages.warning(request, 'Please enter query properly')

	pars={'all':all,'query':query}
	return render(request,'home/search.html',pars)


def loginhandle(request):
	if request.method=='POST':
		loginusername=request.POST['uname']
		loginpassword=request.POST['upassword']
		user=authenticate(username=loginusername, password=loginpassword)
		if user is not None:
			login(request,user)
			messages.success(request,"Successfully logged in")
			return redirect('/')
		else:
			messages.error(request,"Invalid credentials,check again")
			return redirect('/')
	return HttpResponse("handle login")

def logouthandle(request):
	logout(request)
	messages.success(request,"Successfully logged out")
	return redirect('/')
	
		
	    
	

def signuphandle(request):
	if request.method=='POST':
		username=request.POST['name']
		email=request.POST['email']
		fname=request.POST['fname']
		lname=request.POST['lname']
		password=request.POST['password']
		cpassword=request.POST['cpassword']
		if password==cpassword:
			myuser=User.objects.create_user(username, email, password)
			myuser.first_name=fname
			myuser.last_name=lname
			myuser.save()
			messages.success(request,"Your account is successfully created")
		else:
			messages.warning(request,"Passwords do not match")

		

		return redirect('/')


	else:
		return HttpResponse("Error 404 not found")
# Create your views here.
