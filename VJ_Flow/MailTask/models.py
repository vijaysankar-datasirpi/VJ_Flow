from django.db import models

class ScheduledTask(models.Model):
    task_name = models.CharField(max_length=255)
    run_at = models.DateTimeField()
    is_executed = models.BooleanField(default=False)