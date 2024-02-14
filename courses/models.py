from django.db import models

from common.utils import BaseModel
from django.contrib.auth.models import User


class Category(BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


BOSHLANGICH, ORTA, YUQORI = ("Boshlangich", "O`rta", "Yuqori")


class Course(BaseModel):
    DEGREE = (
        (BOSHLANGICH, BOSHLANGICH),
        (ORTA, ORTA),
        (YUQORI, YUQORI),
    )
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=128)
    buy_user = models.ManyToManyField(User, related_name="buy_course", blank=True)
    image = models.ImageField(upload_to='photos/course/')
    price = models.PositiveIntegerField(default=0)
    price_discount = models.IntegerField(default=0, null=True, blank=True)
    rating = models.FloatField(default=0)

    degree = models.CharField(max_length=128, choices=DEGREE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')

    # language = models.CharField(max_length=128)
    like = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Chapter(BaseModel):
    title = models.CharField(max_length=256)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='chapters')

    def __str__(self):
        return self.title


class Lesson(BaseModel):
    title = models.CharField(max_length=256)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='lessons')
    short_description = models.TextField()
    description = models.TextField()
    total_time = models.IntegerField(default=0)
    videos = models.FileField(upload_to='videos/course/')

    def __str__(self):
        return self.title


class LessonUser(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    time_watched = models.IntegerField(default=0)
    total_time = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user} - {self.lesson}"

    def is_finished(self):
        return self.total_time * 0.9 <= self.time_watched

    @property
    def status(self):
        if self.is_finished():
            return "finished"
        if self.time_watched > 0:
            return "in_progress"
        return "not started"


class LessonUserWatched(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(LessonUser, on_delete=models.CASCADE)

    from_time = models.IntegerField(default=0)
    to_time = models.IntegerField(default=0)


class CourseComment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments')
    rating = models.FloatField(default=0)
    description = models.TextField()

    def __str__(self):
        return f"comment by {self.user}"


class Complaint(BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class CauseOfComplaint(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cause')
    course = models.ManyToManyField(Course, related_name='complaints')
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE)
    cause = models.TextField()

    def __str__(self):
        return f"complaint by {self.user}"
