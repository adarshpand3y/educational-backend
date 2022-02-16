from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    one_line_description = models.CharField(max_length=300, blank=True, default="", help_text=('Describe the course in one but unforgettable line. Max 300 characters'))
    description = models.TextField(unique=True)
    image_url = models.CharField(max_length=200, default="", help_text=('Enter Image URL within 200 characters.'))
    high_price = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    slug = models.SlugField(blank=True, unique=True, help_text=('Leave this parameter empty, it will get generated automatically.'))

    @property
    def short_name(self):
        return truncatechars(self.name, 50)
    
    @property
    def short_description(self):
        return truncatechars(self.one_line_description, 50)

    def __str__(self):
        return truncatechars(self.name, 50)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Course, self).save(*args, **kwargs)

class Lecture(models.Model):
    name = models.CharField(max_length=100, unique=True)
    one_line_description = models.CharField(max_length=300, blank=True, default="", help_text=('Describe the lecture in one but unforgettable line. Max 300 characters'))
    description = models.TextField(unique=True)
    youtube_url = models.CharField(max_length=100, unique=True)
    course_index = models.IntegerField(unique=True)
    course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.SET_NULL)
    slug = models.SlugField(blank=True, unique=True, help_text=('Leave this parameter empty, it will get generated automatically.'))

    @property
    def short_name(self):
        return truncatechars(self.name, 50)
    
    @property
    def short_course(self):
        return truncatechars(self.course, 50)

    def __str__(self):
        return truncatechars(self.name, 50)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Lecture, self).save(*args, **kwargs)

class Product(models.Model):
    product_name = models.CharField(max_length=50, unique=True)
    high_price = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    short_description = models.TextField(help_text='Write a brief description of the product here.')
    description = models.TextField(help_text='This area holds the HTML to show on the product page.')
    image1 = models.TextField(max_length=200, default="")
    image2 = models.TextField(max_length=200, default="")
    image3 = models.TextField(max_length=200, default="")
    slug = models.SlugField(blank=True, help_text=('Leave this parameter empty, it will get generated automatically.'))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.product_name

class Order(models.Model):
    order_choices = [
        ("OPS", 'Order Placed Successfully'),
        ("S", 'Shipped'),
        ("OFD", 'Out For Delivery'),
        ("D", 'Delivered'),
        ]
    items = models.TextField(help_text=(f"Customer's Orders"))
    total_cost = models.IntegerField(default=0)
    code_applied = models.CharField(default="", max_length=20)
    discounted_cost = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text=(f"User who placed this order."))
    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    address1 = models.CharField(max_length=100, default="")
    address2 = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=50, default="")
    state = models.CharField(max_length=50, default="")
    pincode = models.CharField(max_length=50, default="")
    landmark = models.CharField(max_length=50, default="")
    ordered_at = models.DateTimeField(auto_now_add=True, help_text=(f"Do NOT change this date and time field."))
    last_changed_at = models.DateTimeField(auto_now=True, help_text=(f"Do NOT change this date and time field."))
    status = models.CharField(max_length=5, choices=order_choices, default="Order Placed Successfully", help_text=(f"Change this only when you are sure. This sends an email to the user regarding the update."))

    def __str__(self):
        return f"Order Id: {self.id}"

class Coupon(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=20)
    discount_percentage = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    description = models.CharField(max_length=100)
    val = models.FloatField(blank=True, help_text="Do NOT change this field. It gets updated automatically.")

    @property
    def user(self):
        return self.user

    def save(self, *args, **kwargs):
        self.val = self.discount_percentage/100
        super(Coupon, self).save(*args, **kwargs)

    def __str__(self):
        return f"Coupon: {self.name}"

class UserDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.IntegerField(default=0)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=50)
    pincode = models.IntegerField()
    landmark = models.CharField(max_length=50)

    @property
    def user(self):
        return self.user

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name_plural = "User Details"

class BlogPost(models.Model):
    title = models.CharField(max_length=256, help_text=('Write the title within 200 characters.'))
    description = models.TextField(help_text='Write a desctiprion of this blog in a few sentences')
    body = models.TextField(help_text=('Your main content goes here.'))
    views = models.IntegerField(default=0, help_text=('This statistic is for your reference, do not change it.'))
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    privacy = models.CharField(max_length=10, choices=[("PRIVATE", 'Private'), ("PUBLIC", 'Public')], default="PRIVATE", help_text=('Public posts will appear to everyone and private posts only to you. Change this to private instead of deleting a post.'))
    slug = models.SlugField(blank=True, help_text=('Leave this parameter empty, it will get generated automatically.'))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title