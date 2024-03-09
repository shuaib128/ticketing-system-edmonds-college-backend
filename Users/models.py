from django.db import models

# Create your models here.
class Tutor(models.Model):
    name = models.CharField(max_length=100)
    pronouns = models.CharField(max_length=50)  # Example: "he/him", "they/them", etc.
    photo = models.ImageField(upload_to='tutor_photos/', blank=True, null=True)
    tickets = models.ManyToManyField('tickets.Ticket', related_name='tickets_tutor', blank=True)


class Student(models.Model):
    name = models.CharField(max_length=100)
    pronouns = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.pronouns})-{self.id}"