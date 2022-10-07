from django.db import models


class Note(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return str(self.id) + ". " + self.title