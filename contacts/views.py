from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mass_mail

def contact (requset):
    if requset.method == 'POST':
        listing_id = requset.POST['listing_id']
        listing = requset.POST['listing']
        name = requset.POST['name']
        email = requset.POST['email']
        phone = requset.POST['phone']
        message = requset.POST['message']
        user_id = requset.POST['user_id']
        realtor_email = requset.POST['realtor_email']    

        if requset.user.is_authenticated:
            user_id = requset.user.id
            has_contacted=Contact.objects.filter(user_id=user_id, listing_id=listing_id)
            if has_contacted:
                messages.error(requset,'You have already made an inquiry for this listing')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)

        contact.save()

        mail1 =(
            'SUCCESS INQUIRY',
            'Hello! ' + name + '.You have already made an inquiry for '+listing,'.'
            'chimera@finance.co',
            [email],      
        )

        mail2 =(
            'INQUIRY MAIL',
            listing + ' of inquiry has been recived. Please check the admin panel for more infomation.',
            'chimera@finanace.co',
            [realtor_email],
        )

        send_mass_mail((mail1,mail2),fail_silently=False)
        messages.success(requset,'Your request has been submitted, a realtor will get back to you very soon')
        return redirect('/listings/'+listing_id)
