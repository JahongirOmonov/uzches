from django.contrib import admin

from .models import Basket, Book, Category, RatingBook, SavedBook, User
admin.site.register(User)
admin.site.register(Book)
admin.site.register(Category)
# admin.site.register(Library)
admin.site.register(Basket)
admin.site.register(RatingBook)
admin.site.register(SavedBook)