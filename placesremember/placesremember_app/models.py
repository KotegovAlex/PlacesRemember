from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Place(models.Model):
    """Model for storing records of visited places"""

    title = models.CharField(max_length=250, blank=False, verbose_name="Place Title")
    photo = models.ImageField(
        upload_to="photos/", blank=True, verbose_name="Place Photo"
    )
    content = models.TextField(default="", blank=True, verbose_name="Comment")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Creation Time")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Change Time")
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=False, verbose_name="User ID"
    )
    lon = models.FloatField(default=0.0)
    lat = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("place", kwargs={"place_id": self.pk})

    class Meta:
        verbose_name = "Place"
        ordering = ["id"]
