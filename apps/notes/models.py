from __future__ import unicode_literals

from django.db import models

class NoteManager(models.Manager):
    def validate(self, data):
        errors = []

        if not data['text']:
            errors.append('no text given')

        if errors:
            return (False, errors)
        else:
            new_note = self.create( text=data['text'] )
            return (True, new_note)

    def remove(self, id):
        id = int(id)
        try:
            note = self.get(id=id)
            note.delete()
        except:
            pass


class Note(models.Model):
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = NoteManager()

    def __str__(self):
        return self.text
