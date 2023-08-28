from django.contrib import admin
from .models.product import Products
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from .models.QuizResponse import QuizResponse
# from .models.FavoriteItem import FavoriteItems
# from .models.FielsToBeSent import FieldsToBeSent


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

# Register your models here.
admin.site.register(Products,AdminProduct)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(QuizResponse)
# admin.site.register(FavoriteItems)


# admin.site.register(FieldsToBeSent)



# username = Rehman, email = , password = 1234
# username = Ahmer001, email = , password = rawalpindi@10


