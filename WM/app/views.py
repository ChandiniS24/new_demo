from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

import random
from . models import *
from datetime import datetime
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect



#############index########
def index(re):
    return  render(re,"index.html")

def login(re):
    if re.method == 'POST':
        a = re.POST['n1']
        b = re.POST['n2']
        try:
            x = reg.objects.get(Username=a)
            if x.Password == b:
                re.session['user'] = a
                return redirect(user)
            else:
                return HttpResponse("invalid")
        except Exception:
            try:
                y = our_employee.objects.get(Username=a)
                if y.password == b:
                    re.session['worker'] = a
                    return redirect(worker)
                else:
                    return HttpResponse("invalid password")
            except:
                if a == "admin" and b == "admin":
                    re.session['admin'] = a
                    return redirect(admin)
                else:
                    return HttpResponse("username incorrect")
    return render(re, 'login.html')






def about(re):
    return render(re, "about.html")

def services(re):
    return  render(re,"services.html")


#########userregister###########


def user_r(re):
    if re.method == 'POST':
        a = re.POST['n1']
        b = re.POST['n2']
        c = re.POST['n3']
        d = re.POST['n4']
        e = re.POST['n5']
        f = re.POST['n6']
        g = re.POST['n7']
        h = re.POST['n8']
        i = re.POST['n9']
        j = re.POST['n10']
        k = re.POST['n11']
        try:
            reg.objects.get(Username=b)
            return HttpResponse("username is already taken")
        except:
            if j == k:
                reg.objects.create(Name=a, Username=b, DOB=c ,phone_no=d,Address=e,state=f,city=g,location=h, Email=i, Password=j, Confirm_Password=k).save()
                return render(re, 'register.html')
            else:
                return HttpResponse("error")
    return render(re, 'register.html')

def user(re):
    if 'user' in re.session:
        return render(re,'user.html')
    return redirect(login)

def view_profile(re):
    if 'user' in re.session:
        data = reg.objects.get(Username=re.session['user'])
        return render(re, 'viewu_profile.html', {'user': data})
    return redirect(login)

def edit_profile(re):
    if 'user' in re.session:
        data = reg.objects.get(Username=re.session['user'])
        return render(re, 'edit_profile.html', {'user': data})
    return redirect(login)

def edit_view(re):
    if 'user' in re.session:
        if re.method=='POST':
            a = re.POST['name']
            b = re.POST['address']
            c = re.POST['email']
            d = re.POST['username']
            reg.objects.filter(Username=re.session['user']).update(Name=a, Address=b, Email=c, Username=d)
            return redirect(view_profile)
            return render(re,'edit_profile.html')
        return redirect(login)

def complaint(re):
    if 'user' in re.session:
        user = reg.objects.get(Username=re.session['user'])
        res=complaint_table.objects.filter(USER=user)
        return render(re,'usercomplaint.html',{'user':res})
    return redirect(login)



def complaint_view(re):
    if 'user' in re.session:
        complaint = re.POST['textfield']
        obj=complaint_table()
        obj.complaint=complaint
        obj.complaintdate=datetime.now().strftime("%Y-%m-%d")
        obj.reply='pending'
        obj.replydate='pending'
        obj.USER=reg.objects.get(Username=re.session['user'])
        obj.save()
        return HttpResponse("<script>alert('added');window.location='viewcomplaint'</script>")
    return redirect(login)


def viewcomplaint(re):
    if 'user' in re.session:
        user = reg.objects.get(Username=re.session['user'])
        res=complaint_table.objects.filter(USER=user)
        return render(re, 'viewcomplaint.html',{'user':res})
    return redirect(login)

def display(re):
    if 'user' in re.session:
        data=add_waste.objects.all()
        return render(re,'add.html',{'data':data})
    return redirect(login)
#
# def booking(request, id):
#     if 'user' in request.session:
#         user = reg.objects.get(Username=request.session['user'])
#         data = add_waste.objects.get(pk=id)
#
#         if request.method == 'POST':
#             # Get the form values from the POST request
#             phone_no = request.POST['phone_no']
#             state = request.POST['state']
#             city = request.POST['city']
#             location = request.POST.get('location', '')
#             quantity = int(request.POST.get('quantity'))
#             price_per_kg = data.price  # Price per kg from the data
#             total_price = quantity * price_per_kg
#
#             # Create the booking in the Quantity1 model
#             booking = Quantity2(
#                 User_details=user,
#                 Waste=data,
#                 total_price=total_price,
#                 state=state,
#                 city=city,
#                 location=location,
#                 phone_no=phone_no
#             )
#             booking.save()
#
#             # Optionally, redirect to a payment page or confirmation page
#             return redirect(payment, price=total_price)  # Change this to your payment view
#
#         return render(request, 'book_now.html', {'data': data, 'user': user})
#
#     return redirect('login')  # If user is not logged in, redirect to login page
# If the user is not logged in, redirect to the login page
#
#
# def confirmation(re,id):
#     if 'user' in re.session:
#         user = reg.objects.get(Username=re.session['user'])
#         data = add_waste.objects.get(pk=id)




import razorpay #pip install razorpay
# def payment(re,price):
#     if 'user' in re.session:
#         u =reg.objects.get(Username=re.session['user'])
#         s = Quantity2.objects.filter(User_details=u)
#         t = price*100
#         return render(re, "payment.html", {'amount':t})






#     return render(re, "payment.html")
#
# def booking(re, id):
#     if 'user' in re.session:
#         user = reg.objects.get(Username=re.session['user'])
#         data = add_waste.objects.get(pk=id)
#
#         if re.method == 'POST':
#             # Get the quantity from the form
#             quantity =re.POST.get('quantity')  # Ensure it's a float for proper calculation
#             price_per_kg = data.price
#
#             # Calculate total price on the server-side (no JS needed)
#             total_price = quantity * price_per_kg
#             #
#             # Get other form data
#             # phone_no = re.POST.get('phone_no')
#             # state = re.POST.get('state')
#             # city = re.POST.get('city')
#             # location = re.POST.get('location', '')
#
#             # Create a new booking with all the details
#             booking = book_now(
#                 User_details=user,
#                 # phone_no=phone_no,
#                 waste_type_details=data,
#                 quantity=quantity,
#                 price_per_kg=price_per_kg,
#                 total_price=total_price,  # Save the calculated total price in the booking
#                 # state=state,
#                 # city=city,
#                 # location=location
#             )
#             booking.save()
#
#             # Pass the total_price to the payment view
#             return redirect('payment', id=booking.id)  # Pass the booking ID for payment processing
#
#         return render(re, 'book_now.html', {'user': user, 'data': data})
#
#     return redirect(login)


import razorpay  # pip install razorpay


# def payment(re, id):
#     if 'user' in re.session:
#         # Get the user details (optional)
#         u = reg.objects.get(Username=re.session['user'])
#
#         # Retrieve the booking based on the passed ID
#         booking =add_waste.objects.get(id=id)  # Get the booking record
#
#         # Use the total price from the booking record
#         total_price = booking.price *booking. quantity * 100  # Razorpay expects the price in paise (multiply by 100)
#
#         # Initialize the Razorpay client
#         return render(re, "payment.html", {'amount':total_price})
#     #
#     #     return render(re, "payment.html"
#     return render(re, "payment.html")
from django.urls import reverse
from django.urls import reverse

def booking(request, id):
    if 'user' in request.session:
        user = reg.objects.get(Username=request.session['user'])
        data = add_waste.objects.get(pk=id)

        # Generate a unique order ID
        order_id = f"ORD{datetime.now().strftime('%Y%m%d%H%M%S')}{random.randint(100, 999)}"
        #
        if request.method == 'POST':
            # Get the form values from the POST request
            so_fname = request.POST["fname"]

            so_email = request.POST["email"]
            so_phone = request.POST["phone"]
            so_address = request.POST["address"]
            so_district = request.POST["district"]
            so_city = request.POST["city"]
            so_pincode = request.POST["pincode"]
            payment_mode = request.POST.get("payment_mode")
            status = "Pending"
            quantity = int(request.POST.get('quantity'))
            price_per_kg = data.price  # Price per kg from the data
            total_price = quantity * price_per_kg

            # Create the booking in the Quantity2 model
            booking = Quantity2(
                User_details=user,
                Waste=data,
                total_price=total_price,
                so_fname=so_fname,

                so_email=so_email,
                so_phone=so_phone,
                so_address=so_address,
                so_district=so_district,
                so_city=so_city,
                so_pincode=so_pincode,
                payment_mode=payment_mode,
                order_id=order_id,
                status=status
            )
            booking.save()

            # Redirect to the payment page and pass the total price
            return redirect(reverse(payment, kwargs={'price': total_price}))

        return render(request, 'book_now.html', {'data': data, 'user': user})

    return redirect('login')  # If user is not logged in, redirect to login page



def payment(request, price):
    if 'user' in request.session:
        user = reg.objects.get(Username=request.session['user'])
        # Use the price directly from the URL
        total_price_in_paise = price * 100  # Razorpay expects price in paise (1 INR = 100 paise)

        # Create Razorpay order
        order_data = {
            'amount': total_price_in_paise,  # Total price in paise
            'currency': 'INR',
            'payment_capture': '1',  # Auto capture payment
        }
        # order = client.order.create(data=order_data)
        # order_id = order['id']

        return render(request, "payment.html", {'amount': total_price_in_paise})
    return redirect(login)






def view_orders(re):
    if 'user' in re.session:
        data = Quantity2.objects.all()
        return render(re,'order details.html',{'order' : data})
    return redirect(login)



##############admin############

def admin(re):
    if 'admin' in re.session:
        return render(re, 'admin.html')
    return redirect(login)

def user_view(re):
    if 'admin' in re.session:
        data = reg.objects.all()
        return render(re, 'user_profile.html', {'data': data})
    return redirect(login)

def viewcom(re):
    if 'admin' in re.session:
        shf=complaint_table.objects.all()
        return render(re,'complaint.html',{'data':shf})
    return redirect(login)

def add_W(re):
    if 'admin' in re.session:
        if re.method=='POST':
            a=re.POST['n1']
            b=re.POST['n2']
            c=re.POST['n3']
            d=re.FILES['n4']
            # total_price =b*c
            add_waste(waste_type=a,quantity=b,price=c,image=d).save()
            return redirect(add_W)
        return render(re,'add waste.html')
    return redirect(login)

def display_W(re):
    if 'admin' in re.session:
        data =add_waste.objects.all()
        return render(re, 'WM.html', {'data': data})
    return redirect(login)

def update(re,id):
    if 'admin' in re.session:
        x=add_waste.objects.get(pk=id)
        return render(re,'update.html',{'data':x})
    return redirect(login)


def update_view(re,id):
    if 'admin' in re.session:
        if re.method=='POST':
            a = re.POST['n']
            b = re.POST['n1']
            c = re.POST['n2']
            d=re.FILES['n3']
            add_waste.objects.filter(pk=id).update(waste_type=a,quantity=b,price=c,image=d)
            return redirect(display_W)
            return render(re,'update.html')
        return redirect(login)



def delete(re,id):
    if 'admin' in re.session:
        x = add_waste.objects.get(pk=id)
        x.delete()
        return redirect(display_W)
    return redirect(login)


def send_reply(re,complaint):
    if 'admin' in re.session:

        return render(re,'Send reply.html',{'complaint':complaint})
    return redirect(login)


def send_reply_post(re,id):
    if 'admin' in re.session:
        reply=re.POST['textarea']
        date = datetime.now().strftime("%d/%m/%y-%H:%M:%S")
        complaint_table.objects.filter(pk=id).update(reply=reply,replydate=date)
        return redirect(viewcom)
    return redirect(login)



def worker_view(re):
    if 'admin' in re.session:
        data =employee.objects.all()
        return render(re, 'worker_profile.html', {'data': data})
    return redirect(login)


def bio1(re,id):
    if 'admin' in re.session :
        data=employee.objects.get(pk=id)
        return render(re, 'bio data1.html', {'bio': data})
    return redirect(login)


def bio(re,id):
    if 'admin' in re.session :
        data=our_employee.objects.get(pk=id)
        return render(re, 'bio_data.html', {'bio': data})
    return redirect(login)




def approve(re,id):

    req=employee.objects.get(pk=id)
    our_emp= our_employee.objects.create(name=req.name, Username=req.Username, DOB=req.DOB, address=req.address, Email=req.Email, phone_no=req.phone_no,image=req.image,cv=req.cv,licenses=req.licenses,password=req.password,Confirm_Password=req.Confirm_Password,gender=req.gender)
    our_emp.save()
    req.delete()
    return redirect(worker_view)

def delete1(re,id):
    if 'admin' in re.session:
        x =employee.objects.get(pk=id)
        x.delete()
        return redirect(worker_view)
    return redirect(login)


def approved(re):
    if 'admin' in re.session:
        data =our_employee.objects.all()
        return render(re, 'approved_em.html', {'data': data})
    return redirect(login)

def admin_vieworders(re):
    if 'admin' in re.session:
        data = Quantity2.objects.all()
        worker=our_employee.objects.all()
        return render(re,'admin_vieworder.html',{'order' : data,'worker':worker})
    return redirect(login)

def admin_pass(re, sts):
    if re.method == "POST":
        st = get_object_or_404(Quantity2, id=sts)
        worker_id = re.POST.get('worker')

        if worker_id:
            worker_instance = get_object_or_404(employee, id=worker_id)
            st.worker = worker_instance  # Assign the instance, not the ID
            st.save()

        return redirect(admin_vieworders)


#########logout###########
def logout(re):
    if 'admin' in re.session or 'user' in re.session or 'worker' in re.session:
        re.session.flush()
        return redirect(login)
    return render(re,'index.html')


#############worker#########################



def worker(re):
    if 'worker' in re.session:
        return render(re, 'worker.html')
    return redirect(login)

def worker_r(re):
    if re.method == 'POST':
        a = re.POST['n1']
        b = re.POST['n2']
        c = re.POST['n3']
        d = re.POST['n4']
        e = re.POST['n5']
        f = re.POST['n6']
        g = re.FILES['n7']
        h = re.FILES['n8']
        i = re.FILES['n9']
        j=  re.POST['n10']
        k=re.POST['n11']
        l = re.POST['gender']
        try:
            employee.objects.get(Username=b)
            return HttpResponse("username is already taken")
        except:
            if j == k:
                employee.objects.create(name=a, Username=b, DOB=c, address=d, Email=e, phone_no=f,image=g,cv=h,licenses=i,password=j,Confirm_Password=k,gender=l).save()
                return render(re, 'worker-register.html')
            else:
                return HttpResponse("error")
    return render(re, 'worker-register.html')

def profile_view(re):
    if 'worker' in re.session:
        data = our_employee.objects.get(Username=re.session['worker'])
        return render(re, 'profile_worker.html', {'worker': data})
    return redirect(login)

def worker_management(re):
    if 'worker' in re.session:
        data = Quantity2.objects.all()
        return render(re,'worker_vieworder.html',{'order' : data})
    return redirect(worker)

def delivery_status(re,sts):
    if re.method == "POST":
        st = Quantity2.objects.get(id=sts)
        st.status= re.POST.get('status')
        st.save()
        return redirect(worker_management)

def Wedit_profile(re):
    if 'worker' in re.session:
        data = our_employee.objects.get(Username=re.session['worker'])
        return render(re, 'Wedit_profile.html', {'worker': data})
    return redirect(login)

def edit_view1(re):
     if 'worker' in re.session:
         if re.method == 'POST':
             a = re.POST['name']
             b = re.POST['address']
             c = re.POST['email']
             d = re.POST['phone_no']
             our_employee.objects.filter(Username=re.session['worker']).update(name=a, address=b, Email=c, phone_no=d)
             return redirect(profile_view)
             return render(re, 'Wedit_profile.html')
         return redirect(login)


    ##########################forgot password##################
def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # whois = request.POST.get('whois')
        try:
            user =reg.objects.get(Email=email)
        except reg.DoesNotExist:
            user = None

        try:
            emp = our_employee.objects.get(Email=email)
        except our_employee.DoesNotExist:
            emp = None

        if not user and not emp:
            return HttpResponse(
                 f"<script>alert('Email id not registered'); window.history.back();</script>",
                 content_type="text/html",
                 )


        if user:
            # Generate and save a unique token for the user
            token = get_random_string(length=4)
            PasswordReset.objects.create(user=user, token=token)
        else:
            # Generate and save a unique token for the employee
            token = get_random_string(length=4)
            PasswordReset.objects.create(emp=emp, token=token)

        # Send email with reset link
        reset_link = f'http://127.0.0.1:8000/reset/{token}'
        try:
            send_mail('Reset Your Password', f'Click the link to reset your password: {reset_link}',
                      'settings.EMAIL_HOST_USER', [email], fail_silently=False)
            return HttpResponse(
                f"<script>alert('We have sent you an email to change your current password'); window.history.back();</script>",
                content_type="text/html",
            )

        except:
            return HttpResponse(
                f"<script>alert('Network connection failed'); window.history.back();</script>",
                content_type="text/html",
            )

    return render(request, 'forget_password.html')


def reset_password(request, token):
    # Verify token and reset the password
    print(token)
    password_reset = PasswordReset.objects.get(token=token)
    # usr = User.objects.get(id=password_reset.user_id)
    if request.method == 'POST':
        new_password = request.POST.get('newpassword')
        repeat_password = request.POST.get('cpassword')

        if repeat_password == new_password:
            try:
                password_reset.user.Password = new_password
                password_reset.user.save()
            except:
                password_reset.emp.password = new_password
                password_reset.emp.save()

            # password_reset.delete()
            return redirect(login)
        else:
            return HttpResponse(
                f"<script>alert('Please recheck both your password'); window.history.back();</script>",
                content_type="text/html",
            )

    return render(request, 'reset_password.html', {'token': token})