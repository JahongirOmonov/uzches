from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract=True

class User(BaseModel):
    fullname = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.fullname

class Book(BaseModel):
        
    class LanguageChoices(models.TextChoices):
        ENGLISH = 'en', 'English'
        UZBEK = 'uz', 'Uzbek'
        RUSSIAN = 'ru', 'Russian'

    class LevelChoices(models.TextChoices):
        BEGINNER = 'Boshlang`ich', 'Boshlang`ich'
        AMETOUR = 'Havaskor', 'Havaskor'
        PROFESSIONAL = 'Professional', 'Professional'

    title = models.CharField(max_length=128)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="books")
    description = models.TextField()
    publisher = models.CharField(max_length=64)
    page = models.IntegerField()
    level = models.CharField(max_length=12, choices=LevelChoices.choices , default=LevelChoices.BEGINNER)
    language = models.CharField(max_length=2, choices=LanguageChoices.choices, default=LanguageChoices.UZBEK)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_discounted = models.BooleanField(default=False)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    basket = models.ManyToManyField(User, through='Basket')
    image = models.ImageField(upload_to='images/')



    def __str__(self) -> str:
        return self.title

class Category(BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.title

class SavedBook(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.user.fullname} > {self.book.title}'

class RatingBook(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    value = models.FloatField()

    def __str__(self) -> str:
        return f'{self.user.fullname} > {self.book.title} > {self.value}'


class Basket(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='baskets')
    

    def __str__(self) -> str:
        return f'{self.user.fullname}'
    
class Legimitation(BaseModel):
    fullname = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=9)
    mail = models.EmailField()


