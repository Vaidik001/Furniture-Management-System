from django.contrib import admin
from .models import *
# Register your models here.

class showrole(admin.ModelAdmin):
    list_display = ['id','user_typename']

admin.site.register(role,showrole)

class showuser_detail(admin.ModelAdmin):
    list_display = ['id','u_name','u_dp','u_gender','u_email','u_phone','u_type','u_status','users']

admin.site.register(user_detail,showuser_detail)


class showfurniture(admin.ModelAdmin):
    list_display = ['id', 'cat_name', 'cat_picture', 'cat_desc', 'cat_added','furniture']


admin.site.register(furniture_category,showfurniture)


class showcountry(admin.ModelAdmin):
    list_display = ['id', 'country_name']


admin.site.register(country,showcountry)


class showstate(admin.ModelAdmin):
    list_display = ['id', 'country_id', 'state_name']


admin.site.register(state, showstate)


class showcity(admin.ModelAdmin):
    list_display = ['id', 'state_id', 'city_name']


admin.site.register(city, showcity)


class showuser_address(admin.ModelAdmin):
    list_display = ['id', 'u_id', 'building_name', 'street_name', 'city_name', 'pincode']


admin.site.register(user_address, showuser_address)


class showfeedback(admin.ModelAdmin):
    list_display = ['id', 'f_title', 'f_desc', 'f_by', 'f_on']


admin.site.register(feedback_details,showfeedback)

class showcomplain(admin.ModelAdmin):
    list_display = ['id', 'c_name', 'c_detail', 'c_photo','c_by','c_on','complain']


admin.site.register(complain_details,showcomplain)

class showbrand(admin.ModelAdmin):
    list_display = ['id','b_name','b_desc','b_logo','logo']

admin.site.register(brand,showbrand)

class shownew_furniture(admin.ModelAdmin):
    list_display = ['id','fu_model_name','n_brand','fu_desc','fu_price','fu_image','fu_type','available_qty','new_furniture']

admin.site.register(new_furniture,shownew_furniture)

class showoldfurniture(admin.ModelAdmin):
    list_display = ['id','o_name','o_brand','o_desc','o_price','o_image','o_type','o_available_qty','old_furniture']

admin.site.register(old_furniture,showoldfurniture)

class showrent_furniture(admin.ModelAdmin):
    list_display = ['id','r_f_name','r_brand','r_desc','r_price','r_image','r_type','r_available_qty','rent_furniture']

admin.site.register(rent_furniture,showrent_furniture)

class shownewfurniture_buying(admin.ModelAdmin):
    list_display = ['id','fu_id','user_id','booking_dt']

admin.site.register(new_furniture_buying,shownewfurniture_buying)

class showoldfurniture_buying(admin.ModelAdmin):
    list_display = ['id','o_fu_id','user_booking_id','o_booking_dt']

admin.site.register(old_furniture_buying,showoldfurniture_buying)

class showrentfurniture_order(admin.ModelAdmin):
    list_display = ['id','rent_f_name','rent_user_id','r_startdate','r_enddate','rent_bookdatetime']

admin.site.register(rentfurniture_order,showrentfurniture_order)









