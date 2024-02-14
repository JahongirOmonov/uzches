from django.urls import path
from .views import ( 
                    BookListApiView, 
                    SavedBookGenericView,
                    BookDetailApiView,
                    BookRecommendationListApiView,
                    BookSearchListApiView,
                    BooksAndroidListApiView,
                    TotalPriceApiView,
                    BookBasketListApiView,
                    LegimitationListApiView
                    )

urlpatterns = [
    # path('save-book/', SavedBookView.as_view()),
    path('save-book-gen/', SavedBookGenericView.as_view()),
    path('libraries/', BookListApiView.as_view()),
    path('book-detail/<int:pk>', BookDetailApiView.as_view()),
    path('book-recommend/', BookRecommendationListApiView.as_view()),
    path('book-search/', BookSearchListApiView.as_view()),
    path('books-android/', BooksAndroidListApiView.as_view()),
    path('total-price/<int:id>/', TotalPriceApiView.as_view()),
    path('basket-user-list/<int:id>/', BookBasketListApiView.as_view()),
    path('legimitation/', LegimitationListApiView.as_view())
]


