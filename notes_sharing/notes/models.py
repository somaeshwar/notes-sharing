from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(max_length=100)
    semester = models.IntegerField()

    def __str__(self):
        return f"{self.name} (Sem {self.semester})"


class Notes(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='notes/')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    download_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title
