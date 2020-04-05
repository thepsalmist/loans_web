from django.db import models


class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    client_title = models.CharField(max_length=100)
    image = models.ImageField(default="thumbnail.png", upload_to="Images")
    message = models.TextField()

    def __str__(self):
        return self.client_name


class About(models.Model):
    title = models.CharField(max_length=100, default="About us")
    body = models.TextField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message by {self.name}"


class Faq(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title
