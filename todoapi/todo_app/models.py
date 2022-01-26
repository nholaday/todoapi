from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=200, blank=False)
    completed = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
