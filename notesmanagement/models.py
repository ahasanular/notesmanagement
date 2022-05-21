from django.db import models
from django.utils import timezone # importing timezone to get the data entry time.

class NotesManagement(models.Model):
    created_by = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(max_length=255, null=True)
    created_from = models.CharField(max_length=255, null=True)
    modified_by = models.CharField(max_length=255, null=True)
    modified_at = models.DateTimeField(max_length=255, null=True)
    modified_from = models.CharField(max_length=255, null=True)
    is_archived = models.BooleanField(default=False)
    archived_by = models.CharField(max_length=255, null=True)
    archived_at = models.DateTimeField(max_length=255, null=True)
    archived_from = models.CharField(max_length=255, null=True)

    class Meta:
        abstract = True


def history_time_info(sender, instance, *args, **kwargs):
    if instance._state.adding:
        instance.created_at = timezone.now()
    else:
        instance.modified_at = timezone.now()
        if instance.is_archived and not instance.archived_at:
            instance.archived_at = timezone.now()
