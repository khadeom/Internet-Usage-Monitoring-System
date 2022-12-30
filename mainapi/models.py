from django.db import models

# Create your models here.


class UserData(models.Model):
    username = models.CharField(max_length=255)
    mac_address = models.CharField(max_length=17)
    start_time = models.DateTimeField()
    usage_time = models.DurationField()
    upload = models.PositiveIntegerField()
    download = models.PositiveIntegerField()
    end_time = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Calculate end time based on start time and usage time
        self.end_time = self.start_time + self.usage_time
        super().save(*args, **kwargs)


