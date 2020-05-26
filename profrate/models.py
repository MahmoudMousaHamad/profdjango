from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


SCHOOL_DEPARTMENTS = (
    ("English Department", "English Department"),
)

LETTER_GRADES = (
    ("A", "A"),
)


class School(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    website = models.CharField(max_length=200)

    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Prof(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    department = models.CharField(max_length=18, choices=SCHOOL_DEPARTMENTS)
    score = models.FloatField(
        validators=[MinValueValidator(1.0), MaxValueValidator(5.0)],)
    take_again_perc = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)],)
    difficulty_lvl = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],)

    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.first_name + " " + self.last_name


class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)


class ProfRating(models.Model):
    prof = models.ForeignKey(Prof, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    quality = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],)
    difficulty = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],)
    course_name = models.CharField(max_length=200)
    for_credit = models.BooleanField(default=True)
    attendence_req = models.BooleanField(default=True)
    take_again = models.BooleanField(default=False)
    textbook_req = models.BooleanField(default=True)
    comment = models.TextField()
    grade = models.CharField(max_length=1, choices=LETTER_GRADES)
    likes_num = models.IntegerField(validators=[MinValueValidator(0)],)
    dislikes_num = models.IntegerField(validators=[MinValueValidator(0)],)

    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "Rating of " + self.prof.__str__ + " by " + self.user.__str__
