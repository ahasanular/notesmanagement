from django.db import models
from notesmanagement.models import NotesManagement
from notesmanagement.models import history_time_info
from django.db.models.signals import pre_save


class ContentManagement(NotesManagement):
    heading = models.CharField(max_length=255)
    body = models.TextField()


    def __str__(self):
        return '[ ' + str(self.id) + '] ' + self.heading


pre_save.connect(history_time_info, sender=ContentManagement)