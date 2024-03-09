from django.db import models

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Subject(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    organization = models.ForeignKey(Organization, related_name='organization_subject', on_delete=models.CASCADE, default=1)
    tutors = models.ManyToManyField("Users.Tutor", related_name='tutors_subject')

    def __str__(self):
        return f"{self.title}-{self.organization.name}"
    
class Ticket(models.Model):
    student = models.ForeignKey("Users.Student", on_delete=models.CASCADE, related_name='student_ticket', default=1)
    tutor = models.ForeignKey("Users.Tutor", on_delete=models.CASCADE, related_name='tutor_ticket', default=1)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, related_name='subject_ticket', default=1)
    session_time = models.DurationField(help_text='Duration of the session in [DD] [HH:[MM:]]ss[.uuuuuu] format')

    def __str__(self):
        return f"{self.subject.title} session for {self.student.name} with {self.tutor.name}"
    