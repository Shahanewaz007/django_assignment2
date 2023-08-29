from django.db import models


class ToDoModel(models.Model):
    
    taskTitle = models.CharField(max_length=30)
    taskDescription = models.TextField()
    is_complete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.taskTitle
