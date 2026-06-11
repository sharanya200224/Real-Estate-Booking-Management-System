from django.shortcuts import render,redirect
from formapp.forms import UserForm, UserProfileForm, UserUpdateForm, RealtorForm, EnquiryForm,UserProfileFormUpdateForm,RealtorProfileForm,RealtorUpdateForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from properties.models import allproperties
from formapp.models import Realtors
from booking.models import Book,BookingModel



from properties.models import visit

# Create your views here.
def registration(request):
    registered=False
    if request.method=='POST':
        form1=UserForm(request.POST)
        form2=UserProfileForm(request.POST,request.FILES)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.save()
            
            profile=form2.save(commit=False)
            profile.user=user
            profile.save()
            registered=True
        
    else:
        form1=UserForm()
        form2=UserProfileForm()
    context={
        'form1':form1,
        'form2':form2,
        'registered':registered
    }
    return render(request,"registration.html",context)

def user_login(request):
    if request.method=='POST':
        Username=request.POST['username']
        password=request.POST['password']
        # to print in cmd
        # print(username)
        # print(password)
        user=authenticate(username=Username,password=password)
        #//--------------form.username=login.username-----------//
        if user:
            if Realtors.objects.filter(user=user).exists():
                realtor=Realtors.objects.get(user=user)
                if realtor.is_approved:
                    login(request,user) 
                    return redirect("dashboard")
                else:
                    return HttpResponse("realtor not approved")
            else:
                if user.is_active :
                    login(request,user)
                    return redirect('home')
                else:
                    return HttpResponse("User is not active")
        else:
            return HttpResponse("Please check your Credentials")
    return render(request,"login.html")


@login_required(login_url="login")
def home(request):
    properties=allproperties.objects.all()
    realtor_property = Realtors.objects.all()
    
    is_realtor = Realtors.objects.filter(user=request.user).exists() if request.user.is_authenticated else False
    return render(request,"home.html",{'properties':properties,'realtor_property':realtor_property,'is_realtor':is_realtor})


@login_required(login_url="login")
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url="login")
def profile(request):
    is_realtor=Realtors.objects.filter(user=request.user).exists()
    realtor=None
    if is_realtor:
        realtor = Realtors.objects.get(user=request.user)
        properties = allproperties.objects.filter(realtorname=realtor)
        return render(request, "profile.html", {
            "is_realtor": True,
            "realtor": realtor,
            "properties":properties
        })
    
    booking = visit.objects.filter(user=request.user)
    books = Book.objects.filter(user=request.user)
    latestbooking=BookingModel.objects.filter(user=request.user).order_by ('-booking_date','-booking_time')[:1]
    return render(request, 'profile.html',{'booking':booking,'books':books,'latestbooking':latestbooking})


@login_required(login_url="login")
@login_required(login_url='login')
def user_update(request):

    is_realtor = Realtors.objects.filter(user=request.user).exists()

    if is_realtor:

        realtor = Realtors.objects.get(user=request.user)

        if request.method == "POST":
            form = UserUpdateForm(request.POST, instance=request.user)
            form3 = RealtorUpdateForm(
                request.POST,
                request.FILES,
                instance=realtor
            )

            if form.is_valid() and form3.is_valid():
                form.save()
                form3.save()
                return redirect('profile')

        else:
            form = UserUpdateForm(instance=request.user)
            form3 = RealtorUpdateForm(instance=realtor)

    else:

        if request.method == "POST":
            form = UserUpdateForm(request.POST, instance=request.user)
            form3 = UserProfileFormUpdateForm(
                request.POST,
                request.FILES,
                instance=request.user.userdata
            )

            if form.is_valid() and form3.is_valid():
                form.save()
                form3.save()
                return redirect('profile')

        else:
            form = UserUpdateForm(instance=request.user)
            form3 = UserProfileFormUpdateForm(
                instance=request.user.userdata
            )

    return render(
        request,
        "update.html",
        {
            'form': form,
            'form3': form3
        }
    )


def realtor_reg(request):
    registered=False
    if request.method=='POST':
        form3=RealtorForm(request.POST)
        form4=RealtorProfileForm(request.POST,request.FILES)
        if form3.is_valid() and form4.is_valid():
            user=form3.save()
            user.set_password(user.password)
            user.save()
            
            profile=form4.save(commit=False)
            profile.user=user
            profile.save()
            registered=True
        
    else:
        form3=RealtorForm()
        form4=RealtorProfileForm()
    context={
        'form3':form3,
        'form4':form4,
        'registered':registered
    }
    return render(request,"realtorreg.html",context)


def realtor_detail(request):
    return render(request, "realtors/realtordetail.html")

def realtor_dashboard(request):
    return render(request, "realtors/dashboard.html")


def enquiry(request):
    submited=False
    if request.method=='POST':
        enquiry=EnquiryForm(request.POST)
        if enquiry.is_valid():
            enquiry.save()
            submited=True
            # messages.success(request,"thank for enquiry our team will get back you soon")      
    else:
        enquiry=EnquiryForm()
    return render(request,'enquiry.html', {'enquiry':enquiry,"submited":submited})




def search(request,area=None):
    allpop=allproperties.objects.all()
    area=request.GET.get('area')
    result=allproperties.objects.filter(area=area)
    return render(request,"search.html",{'result':result,'allpop':allpop})