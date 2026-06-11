from django.shortcuts import render, get_object_or_404, redirect
from properties.models import allproperties
from booking.models import BookingModel, Book, Agreement
from booking.forms import AgreementFrom
from django.http import HttpResponse
from django.db.transaction import commit


# Create your views here.



def booking_property(request,id):
    book=get_object_or_404(allproperties,id=id)
    submitted=False
    rent=book.price
    advance=rent*4
    min_token=advance*0.10
    if request.method=='POST':
        token=int(request.POST.get('token'))
        if token>=min_token:
            # Book.objects.create(
            #     user=request.user,
            #     property=book,
            #     rent_amount=rent,
            #     advance_amount=advance,
            #     token_advance=token,
            #     status=True

            # )
            Book.objects.create(
                user=request.user,
                property=book,
                rentamount=rent,

                advance_amount=advance,

                token=token,

                status=True

            )
            return redirect('success')


        submitted=True

    return render(request,'book.html',{'book':book,'submitted':submitted,'rent':rent,'advance':advance})


def booking_success(request):

    return render(
        request,
        'success.html'
    )




def book_property(request,id):

    property_detail = get_object_or_404(allproperties,id=id)
    if request.method == "POST":

        token = int(request.POST.get('token'))
        rent = property_detail.price
        
        if rent is None:
            return HttpResponse("property price is missing")
        

        advance = rent * 4
        min_token = advance * 0.10
        # VALIDATION
        if token < min_token:

            return render(request,'book.html',{
                'book':property_detail,
                'advance':advance,
                'error':'Token advance must be minimum 10% of advance amount'
            })

        booking = BookingModel.objects.create(
            user=request.user,
            property_detail=property_detail,
            token=token,
            advance=advance,
            owner_name=property_detail.owner_name,
            property_name=property_detail.property_type,
            area=property_detail.area,
            rent=rent
        )

        return render(request,'success.html',{
            'booking':booking
        })

    return render(request,'book.html',{
        'book':property_detail,
        'advance':advance
    })


def agreement_detail(request, id):

    form_detail = get_object_or_404(allproperties, id=id)

    if request.method == "POST":

        agreement = Agreement.objects.create(
            property_detail=form_detail,
            first_party_name=request.POST.get('owner_name'),
            owner_phone=request.POST.get('owner_phone'),
            email=request.POST.get('owner_email'),
            address=request.POST.get('owner_address'),
            stamp_papper_price=request.POST.get('stamp_paper'),
            secondary_party_name=request.POST.get('second_party_name'),
            secondary_phone=request.POST.get('second_party_phone'),
            secondart_email=request.POST.get('second_party_email'),
            secondary_address=request.POST.get('second_party_address'),
            advance_amount=request.POST.get('advance_paid')
        )

        return redirect('agreementdetail', id=agreement.id)

    return render(request, 'agreement.html', {
        'form_detail': form_detail
    })


def agreement_creation(request, id):

    agreement = get_object_or_404(Agreement, id=id)

    return render(
        request,
        'agreementdetail.html',
        {'agreement': agreement}
    )