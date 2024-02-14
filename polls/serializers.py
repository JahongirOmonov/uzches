from rest_framework import serializers
from .models import SavedBook, Book, RatingBook, Basket, Legimitation
from django.db.models import Avg

class SavedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedBook
        fields = ['user', 'book']

class BookSerializer(serializers.ModelSerializer):
    category=serializers.StringRelatedField(source = 'category.title')
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['title',
                  'image', 
                  'price', 
                  'discount_price', 
                  'level', 'category', 
                  'publisher', 
                  'average_rating' ]

    def get_average_rating(self, obj):
        ratings = RatingBook.objects.filter(book=obj)
        average_rating = ratings.aggregate(avg_rating=Avg('value'))['avg_rating']
        return average_rating
    
class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title',
                  'discount_price',
                  'price',
                  'image',
                  'level',
                  'publisher',
                  'page',
                  'created_at',
                  'description'
                  ]
        

class BookRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'title',
            'image',
            'publisher'
        ]


class BooksAndroidSerializer(serializers.ModelSerializer):
    category=serializers.StringRelatedField(source = 'category.title')
    class Meta:
        model = Book
        fields = ['title',
                  'discount_price',
                  'price',
                  'image',
                  'level',
                  'publisher',
                  'category'
                  ]
        

class BookBasketSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(source = 'user.fullname')
    title=serializers.StringRelatedField(source = 'books.title')
    image=serializers.StringRelatedField(source = 'books.image')
    price=serializers.StringRelatedField(source = 'books.price')
    discount_price=serializers.StringRelatedField(source = 'books.discount_price')
    class Meta:
        model=Basket
        fields = ['title', 'image', 'price', 'discount_price', 'user']


class LegimitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Legimitation
        fields = '__all__'

