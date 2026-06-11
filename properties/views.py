from django.shortcuts import render, redirect, get_object_or_404
from properties.models import allproperties
from formapp.models import Realtors
from properties.forms import PropertiesForm, PropertyEditForm
from django.core.paginator import Paginator
from properties.models import PropertyBooking, visit

# Create your views here.


def property_detail(request,id=0): 
    detail = allproperties.objects.get(id=id) 
    property = allproperties.objects.get(id=id)
    rooms = property.rallproperties.all()
    kitchens = property.kallproperties.all()
    bathrooms = property.ballproperties.all()
    balcony = property.baallproperties.all()
    livingareas = property.lallproperties.all()

     
    return render(request, "properties/property_details.html", {'detail':detail,'rooms':rooms,'kitchens':kitchens,'bathrooms':bathrooms,'balcony':balcony,
    'livingareas':livingareas} )


def dashboard_details(request):
    
    realtors=Realtors.objects.get(user=request.user)
    if realtors:
        details = allproperties.objects.filter(realtorname=realtors)
        paginator=Paginator(details,1)
        page=request.GET.get('pg')
        details=paginator.get_page(page)
    # else:
    #     details= []
        return render(request, "realtors/dashboard.html",{'details':details,'realtors':realtors})
    


def add_new_property(request):
    if request.method=='POST':
        form = PropertiesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  
            return redirect('dashboard')
        else:
            print(form.errors)   
    else:
        form=PropertiesForm()
    return render(request, 'properties/add_property.html', {'form':form})


def propertyEdit(request, id=0):
    form1=get_object_or_404(allproperties,id=id)
    if request.method=='POST':
        form1=PropertiesForm(request.POST,request.FILES,instance=form1)
        if form1.is_valid():
            form1.save()   
            return redirect('dashboard')
    else:
        form1=PropertyEditForm(instance=form1)  
        return render(request, "properties/property_edit.html", {'form1':form1})
        

def book_property(request,id):

    property_obj = get_object_or_404(allproperties,id=id)

    emi = None
    error = None

    if request.method == "POST":

        booking_type = request.POST.get("booking_type")

        loan_amount = request.POST.get("loan_amount")
        tenure = request.POST.get("tenure")

        property_price = float(property_obj.price)

        if loan_amount:
            loan_amount = float(loan_amount)

            if loan_amount > property_price:
                error = "Loan amount should not exceed property price"

            else:

                tenure = int(tenure)

                # interest rates
                if tenure == 1:
                    rate = 16
                elif tenure == 2:
                    rate = 15
                elif tenure == 5:
                    rate = 13
                elif tenure == 10:
                    rate = 11

                r = (rate / 12) / 100
                n = tenure * 12
                p = loan_amount

                emi = (p * r * (1 + r) ** n) / ((1 + r) ** n - 1)

                PropertyBooking.objects.create(
                    
                    property=property_obj,
                    booking_type=booking_type,
                    loan_amount=loan_amount,
                    tenure=tenure,
                    emi_amount=emi
                )

    return render(request,'properties/calculator.html',{
        'property':property_obj,
        'emi':emi,
        'error':error
    })


def AllProperties(request):
    property_type=request.GET.get('types')
    properties=[]
    
    if property_type=='buy':
        properties=allproperties.objects.filter(property_type='BUY')
    elif property_type=='rental':
        properties = allproperties.objects.filter(property_type='RENTAL')
    else:
        properties=allproperties.objects.all()
    
    return render(request,'allproperties.html',{'properties':properties})


def visit_property(request,id):
    detail=get_object_or_404(allproperties,id=id)
    submitted=False
    if request.method=='POST':
        visit_date=request.POST.get('visit_date')
        visit_time=request.POST.get('visit_time')

        visit.objects.create(
            user=request.user,
            area=detail,
            time=visit_time,
            date=visit_date
        )
        submitted=True
    return render(request,"visit.html",{'detail':detail,'submitted':submitted})





def book_advance(request,id):
    property_detail=get_object_or_404(allproperties,id=id)
    property_price=property_detail.price
    realtor_charge=property_price*0.015
    advance=property_price*0.10
    return render(request,'properties/bookadvance.html',{'property_detail':property_detail,'realtor_charge':realtor_charge,'advance':advance})


