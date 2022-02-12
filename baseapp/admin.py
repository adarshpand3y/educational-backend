from django.contrib import admin
from .models import Course, Lecture, Product, Order, Coupon, UserDetails

class CourseAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'short_description')

class LectureAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'short_course', 'course_index')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'discounted_cost', 'status')

class CouponAdmin(admin.ModelAdmin):
    list_display = ('user', 'code', 'quantity')

class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'state')

# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(Lecture, LectureAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Coupon, CouponAdmin)
admin.site.register(UserDetails, UserDetailsAdmin)