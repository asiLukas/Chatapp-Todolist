from django.db import models
from django.utils import timezone
import django.utils.timezone
from django.urls import reverse


class ToDoList(models.Model):
    item = models.CharField(max_length=20)
    comments = models.TextField(blank=True, null=True)
    created = models.DateField(default=django.utils.timezone.now)
    deadline = models.CharField(max_length=20)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.item

    def get_absolute_url(self):
        return reverse('todolist:detail_list', kwargs={'id': self.id})


'''class Items(models.Model):
    todolsdfist = models.ForeignKey(ToDoList, on_delete=models.CASCADE, default=20)
    todo = models.CharField(max_length=100)
    deadline = models.DateField(default=django.utils.timezone.now)
    complete = models.BooleanField(default=False)

    class Meta:
        ordering = ['deadline']

    def __str__(self):
        return self.todo

    def get_absolute_url(self):
        return reverse('todolist:detail_list', kwargs={'id': self.id})
'''
