from django.db import models

# Create your models here.
class reg(models.Model):
    Name=models.CharField(max_length=20)
    DOB=models.CharField(max_length=20)
    phone_no=models.IntegerField()
    Address=models.CharField(max_length=20)
    Email=models.CharField(max_length=120)
    state=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=50)
    Confirm_Password=models.CharField(max_length=50)

class employee(models.Model):
    name=models.CharField(max_length=20)
    gender_category=(
        ('male','male'),
        ('female','female'),
        ('prefer not to say','prefer not to say'),
    )
    gender=models.CharField(max_length=50,choices=gender_category,default='select',null=True)
    DOB=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    phone_no=models.IntegerField()
    Email=models.CharField(max_length=220)
    image=models.FileField()
    cv= models.FileField(upload_to='pdfs/', null=True, blank=True)
    Username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    Confirm_Password=models.CharField(max_length=20)
    licenses=models.FileField()

class complaint_table(models.Model):
    USER= models.ForeignKey(reg, default=1, on_delete=models.CASCADE)
    complaint = models.CharField(max_length=100)
    replydate = models.CharField(max_length=100)
    complaintdate = models.CharField(max_length=100)
    reply = models.CharField(max_length=100)





class add_waste(models.Model):
    WASTE_TYPE = [
        ('plastic', 'Plastic'),
        ('paper&cardboard', 'Paper&cardboard'),
        ('glass', 'Glass'),
        ('organic', 'Organic'),
        ('electronic', 'Electronic'),
        ('hazardous', 'Hazardous'),
    ]

    waste_type = models.CharField(max_length=20, choices=WASTE_TYPE)
    image = models.FileField()
    quantity = models.IntegerField()  # in kilograms
    price = models.IntegerField() # price per kilogram
    # total_price = models.IntegerField() # price per kilogram







#
# class book_now(models.Model):
#
#
#     User_details= models.ForeignKey(reg, default=1, on_delete=models.CASCADE)
#     phone_no=models.IntegerField()
#     waste_type_details =models.ForeignKey(add_waste, default=1,on_delete=models.CASCADE)
#     Quantity=models.ForeignKey(Quantity1,default=1,on_delete=models.CASCADE)
#     state=models.CharField(max_length=100)
#     city=models.CharField(max_length=100)
#     location = models.CharField(max_length=255, blank=True, null=True)  # Optional: to store location (address)
#     #
#     # def save(self, *args, **kwargs):
#     #     # Automatically calculate total price before saving
#     #     self.total_price = self.quantity * self.price_per_kg
#     #     super(Waste, self).save(*args, **kwargs)
#     #
#     # def __str__(self):
#     #     return f"Order for {self.name} ({self.waste_type})"



class our_employee(models.Model):
    name=models.CharField(max_length=20)
    gender_category=(
        ('male','male'),
        ('female','female'),
        ('prefer not to say','prefer not to say'),
    )
    gender=models.CharField(max_length=50,choices=gender_category,default='select',null=True)
    DOB=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    phone_no=models.IntegerField()
    Email=models.CharField(max_length=220)
    image=models.FileField()
    cv= models.FileField(upload_to='pdfs/', null=True, blank=True)
    Username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    Confirm_Password=models.CharField(max_length=20)
    licenses=models.FileField()

#
# class Order(models.Model):
#     customer = models.ForeignKey(reg, on_delete=models.CASCADE)
#     cart = models.ForeignKey(c, on_delete=models.CASCADE, null=True,blank=True)  # Adjust according to your requirements
#     product = models.ForeignKey(product, on_delete=models.CASCADE)
#     so_fname = models.CharField(max_length=20, null=False)
#     so_lname = models.CharField(max_length=20)
#     so_email = models.EmailField(null=False)
#     so_phone = models.IntegerField(null=False)
#     so_address = models.TextField(null=False)
#     so_district = models.CharField(max_length=20, null=False)
#     so_city = models.CharField(max_length=20, null=False)
#     so_pincode = models.IntegerField(null=False)
#     add_message = models.CharField(max_length=250)
#     order_status = (
#         ('Pending', 'Pending'),
#         ('Out For Shipping', 'Out For Shipping'),
#         ('Delivered', 'Delivered'),
#         ('Cancelled', 'Cancelled'),
#     )
#     status = models.CharField(max_length=150, choices=order_status, default='Pending')
#     quantity = models.IntegerField(null=False)
#     total_price = models.FloatField(null=False)
#     payment_mode = models.CharField(max_length=150, null=False)
#     payment_id = models.CharField(max_length=150, null=True)
#     order_id = models.CharField(max_length=150, null=False)
#     tracking_no = models.CharField(max_length=150, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     delivery_boy=models.ForeignKey(d_register,on_delete=models.CASCADE,null=True,)



class Quantity2(models.Model):
    User_details= models.ForeignKey(reg, default=1, on_delete=models.CASCADE)
    Waste=models.ForeignKey(add_waste, default=1, on_delete=models.CASCADE)
    total_price = models.IntegerField()
    Worker=models.ForeignKey(our_employee,on_delete=models.CASCADE,null=True,blank=True)
    so_fname = models.CharField(max_length=20, null=False)
    so_lname = models.CharField(max_length=20)
    so_email = models.EmailField(null=False)
    so_phone = models.IntegerField(null=False)
    so_address = models.TextField(null=False)
    so_district = models.CharField(max_length=20, null=False)
    so_city = models.CharField(max_length=20, null=False)
    so_pincode = models.IntegerField(null=False)
    order_status = (
        ('Pending', 'Pending'),
        ('pick up confirm', 'pick up confirm'),
        ('collected', 'collected'),
        ('Cancelled', 'Cancelled'),
    )
    status = models.CharField(max_length=150, choices=order_status, default='Pending')
    payment_mode = models.CharField(max_length=150, null=False)
    payment_id = models.CharField(max_length=150, null=True)
    order_id = models.CharField(max_length=150, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PasswordReset(models.Model):
    user = models.ForeignKey(reg, on_delete=models.CASCADE, null=True, blank=True)
    emp = models.ForeignKey(our_employee, on_delete=models.CASCADE, null=True, blank=True)
    # security
    token = models.CharField(max_length=4)