from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings

class Contact(models.Model):
    first_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2,"First name must be greater than 2 characters")]
    )
    last_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2,"Last name must be greater than 2 characters")]
    )
    email = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3,"email must be greater than 3 characters")]
    )
    text = models.TextField()
    picture = models.BinaryField(null=True, blank=True, editable=True)
    content_type = models.CharField(max_length=256, null=True, blank=True,
                                    help_text='The MIMEType of the file')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.first_name



