from django.contrib import admin
from .models import Course, Lecture, Product, Order, Coupon, UserDetails, BlogPost

class CourseAdmin(admin.ModelAdmin):
    class Media:
        js = ("tinymce.js",)
        
    list_display = ('short_name', 'short_description')

class LectureAdmin(admin.ModelAdmin):
    class Media:
        js = ("tinymce.js",)

    list_display = ('short_name', 'short_course', 'course_index')

class ProductAdmin(admin.ModelAdmin):
    class Media:
        js = ("tinymce.js",)
        
    list_display = ('product_name', 'price', 'stock')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'discounted_cost', 'status')

class CouponAdmin(admin.ModelAdmin):
    list_display = ('user', 'code', 'quantity')

class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ('userForeignKey', 'city', 'state')

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    class Media:
        js = ("tinymce.js",)

    list_display = ('title', 'publish_date', 'privacy', 'views')

# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(Lecture, LectureAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Coupon, CouponAdmin)
admin.site.register(UserDetails, UserDetailsAdmin)
# admin.site.register(BlogPost, BlogPostAdmin)