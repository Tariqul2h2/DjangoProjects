from django.db import models


class MessageCategory(models.Model):
    title = models.CharField(max_length=50)
    pdfUpload = models.FileField(upload_to='uploads/%Y/%m/%d/')

    def __str__(self):
        return self.title


class Message(models.Model):
    message = models.TextField()
    # author = models.CharField(max_length=200)
    message_category = models.ForeignKey(
        'MessageCategory', on_delete=models.CASCADE
    )

    def __str__(self):
        if len(self.message) > 50:
            return self.message[:50] + "..."
        return self.message
