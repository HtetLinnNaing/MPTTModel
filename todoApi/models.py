from django.db import models


# Create your models here.
class todo(models.Model):
    name = models.CharField(max_length=100, null=False)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "todo_list"
