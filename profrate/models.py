from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

SCHOOL_DEPARTMENTS = (
    ("English Department", "English Department"),
)

LETTER_GRADES = (
    ("A", "A"),
)

USER_TYPES = (
    ("Student", "Student"),
    ("Professor", "Professor"),
)

MAJORS = (
    ("Computer Science", "Computer Science"),
)

Countries = (

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
    department = models.CharField(max_length=200, choices=SCHOOL_DEPARTMENTS)
    score = models.FloatField(
        validators=[MinValueValidator(1.0), MaxValueValidator(5.0)],)
    take_again_perc = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)],)
    difficulty_lvl = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],)

    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)
    major = models.CharField(max_length=200, choices=MAJORS, null=True)
    type = models.CharField(max_length=200, choices=USER_TYPES)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class ProfRating(models.Model):
    prof = models.ForeignKey(Prof, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL, null=True)
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
    likes_num = models.IntegerField(
        validators=[MinValueValidator(0)], default=0)
    dislikes_num = models.IntegerField(
        validators=[MinValueValidator(0)], default=0)

    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "Rating of " + self.prof.first_name + self.prof.last_name + " by " + self.user.username


class SchoolRating(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reputation = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],)
    location = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],)
    opportunities = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],)
    facilities = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],)
    internet = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],)
    food = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],)
    clubs = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],)
    social = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],)
    happiness = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],)
    safety = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],)
    beauty = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],)
    comment = models.TextField()
    grade = models.CharField(max_length=1, choices=LETTER_GRADES)
    likes_num = models.IntegerField(
        validators=[MinValueValidator(0)], default=0)
    dislikes_num = models.IntegerField(
        validators=[MinValueValidator(0)], default=0)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "Rating of " + self.school.name + " by " + self.user.username
