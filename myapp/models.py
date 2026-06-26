from random import choices
from tkinter.constants import CASCADE

from django.db import models
from django.db.models import CharField, ForeignKey
from django.utils.safestring import mark_safe

# Create your models here.
role=[
    ('1','User'),
    ('2','Buyer',),
    ('3','Seller'),
    ('4','Rent')
]
gender=[
    ('1','Male'),
    ('2','Female')
]
status=[
    ('1','Active'),
    ('2','Inactive')
]
qty=[
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
    ('8','8'),
    ('9','9'),
    ('10','10'),
    ('11','11'),
    ('12','12'),
    ('13','13'),
    ('14','14'),
    ('15','15'),
    ('16','16'),
    ('17','17'),
    ('18','18'),
    ('19','19'),
    ('20','20')


]
class role(models.Model):
    user_typename=models.CharField(max_length=30,choices=role)

    def __str__(self):
        return self.user_typename

class user_detail(models.Model):
    u_name=models.CharField(max_length=30)
    u_dp=models.ImageField(upload_to='user')
    u_gender=models.CharField(max_length=10,choices=gender)
    u_email=models.EmailField()
    u_phone=models.BigIntegerField()
    u_type=models.ForeignKey(role,on_delete=models.CASCADE)
    u_status=models.CharField(max_length=10,choices=status)

    def __str__(self):
        return self.u_name

    def users(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.u_dp.url))

    users.allow_tags = True

class furniture_category(models.Model):
    cat_name=models.CharField(max_length=30)
    cat_picture=models.ImageField(upload_to='furniture')
    cat_desc=models.TextField()
    cat_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cat_name

    def furniture(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.cat_picture.url))

    furniture.allow_tags = True

class country(models.Model):
    country_name=models.CharField(max_length=30)

    def __str__(self):
        return self.country_name

class state(models.Model):
    country_id=models.ForeignKey(country,on_delete=models.CASCADE)
    state_name=models.CharField(max_length=30)

    def __str__(self):
        return self.state_name

class city(models.Model):
    state_id=models.ForeignKey(state,on_delete=models.CASCADE)
    city_name=models.CharField(max_length=30)

    def __str__(self):
        return self.city_name

class user_address(models.Model):
    u_id=models.ForeignKey(user_detail,on_delete=models.CASCADE)
    building_name=models.CharField(max_length=30)
    street_name=models.CharField(max_length=30)
    city_name=models.ForeignKey(city,on_delete=models.CASCADE)
    pincode=models.IntegerField()

class feedback_details(models.Model):
    f_title=models.CharField(max_length=20)
    f_desc=models.TextField()
    f_by=models.ForeignKey(user_detail,on_delete=models.CASCADE)
    f_on=models.DateTimeField(auto_now_add=True)


class complain_details(models.Model):
    c_name=models.CharField(max_length=30)
    c_detail=models.TextField()
    c_photo=models.ImageField(upload_to='complain')
    c_by=models.ForeignKey(user_detail,on_delete=models.CASCADE)
    c_on=models.DateTimeField(auto_now_add=True)

    def complain(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.c_photo.url))

    complain.allow_tags = True

class brand(models.Model):
    b_name=models.CharField(max_length=30)
    b_desc=models.TextField()
    b_logo=models.ImageField(upload_to='logo')

    def logo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.b_logo.url))

    logo.allow_tags = True

    def __str__(self):
        return self.b_name

class new_furniture(models.Model):
    fu_model_name=models.CharField(max_length=30)
    n_brand=models.ForeignKey(brand,on_delete=models.CASCADE)
    fu_desc=models.TextField()
    fu_price=models.IntegerField()
    fu_image=models.ImageField(upload_to='new furniture')
    fu_type=models.ForeignKey(furniture_category,on_delete=models.CASCADE)
    available_qty=models.CharField(max_length=20,choices=qty)

    def __str__(self):
        return self.fu_model_name

    def new_furniture(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.fu_image.url))

    new_furniture.allow_tags = True

class old_furniture(models.Model):
    o_name=models.CharField(max_length=30)
    o_brand=models.ForeignKey(brand,on_delete=models.CASCADE)
    o_desc=models.TextField()
    o_price=models.IntegerField()
    o_image=models.ImageField(upload_to='old furniture')
    o_type=models.ForeignKey(furniture_category,on_delete=models.CASCADE)
    o_available_qty=models.CharField(max_length=20,choices=qty)

    def __str__(self):
        return self.o_name

    def old_furniture(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.o_image.url))

    old_furniture.allow_tags = True

class rent_furniture(models.Model):
    r_f_name=models.CharField(max_length=30)
    r_brand=models.ForeignKey(brand,on_delete=models.CASCADE)
    r_desc=models.TextField()
    r_price=models.IntegerField()
    r_image=models.ImageField(upload_to='rent furniture')
    r_type=models.ForeignKey(furniture_category,on_delete=models.CASCADE)
    r_available_qty=models.CharField(max_length=20,choices=qty)

    def __str__(self):
        return self.r_f_name

    def rent_furniture(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.r_image.url))

    rent_furniture.allow_tags = True

class new_furniture_buying(models.Model):
    fu_id=models.ForeignKey(new_furniture,on_delete=models.CASCADE)
    user_id=models.ForeignKey(user_detail,on_delete=models.CASCADE)
    booking_dt=models.DateTimeField(auto_now_add=True)

class old_furniture_buying(models.Model):
    o_fu_id=models.ForeignKey(old_furniture,on_delete=models.CASCADE)
    user_booking_id=models.ForeignKey(user_detail,on_delete=models.CASCADE)
    o_booking_dt=models.DateTimeField(auto_now_add=True)

class rentfurniture_order(models.Model):
    rent_f_name=models.ForeignKey(rent_furniture,on_delete=models.CASCADE)
    rent_user_id=models.ForeignKey(user_detail,on_delete=models.CASCADE)
    r_startdate=models.DateField()
    r_enddate=models.DateField()
    rent_bookdatetime=models.DateTimeField(auto_now_add=True)


















