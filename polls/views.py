from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import SavedBook, Book,RatingBook, Legimitation
from rest_framework import generics
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework import filters
from .serializers import (SavedBookSerializer, 
                          BookSerializer, 
                          BookDetailSerializer,
                          BookRecommendationSerializer,
                          BooksAndroidSerializer,
                          BookBasketSerializer,
                          LegimitationSerializer
                          )
from django.db.models import Sum
from .models import User, Basket

# Create your views here.

# class SavedBookView(APIView):
#     def post(self, request, format=None):

#         serializer = SavedBookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SavedBookGenericView(GenericAPIView, CreateModelMixin):
    serializer_class = SavedBookSerializer
    queryset = SavedBook.objects.all()


class BookListApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer




class BookDetailApiView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer


class BookRecommendationListApiView(generics.ListAPIView):
    queryset = Book.objects.all()[:4]
    serializer_class = BookRecommendationSerializer


class BookSearchListApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookRecommendationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


class BooksAndroidListApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksAndroidSerializer



class TotalPriceApiView(APIView):

    def get(self, request, *args, **kwargs):
        # x=get_object_or_404(Basket, user__id=kwargs['id'])
        # user = BasketSerializer(x)

        

        user = User.objects.get(id=kwargs['id'])
        total_price = Basket.objects.filter(user=user).aggregate(total_price=Sum('books__price'))['total_price']
        if total_price is not None:
            return Response({'total_price':total_price})
        else:
            return Response({'error':'No books in the basket'})
        

class BookBasketListApiView(APIView):
    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=kwargs['id'])
        total_price = Basket.objects.filter(user=user).aggregate(total_price=Sum('books__price'))['total_price']
        if total_price is not None:
            all_data = Basket.objects.all()
            serializer = BookBasketSerializer(all_data, many=True)
            return Response(serializer.data)
        else:
            return Response({'error':'No books in the basket'})
        

class LegimitationListApiView(generics.ListAPIView):
    queryset = Legimitation.objects.all()
    serializer_class = LegimitationSerializer


        





