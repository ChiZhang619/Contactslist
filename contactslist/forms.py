from django import forms
from contactslist.models import Contact
from django.core.files.uploadedfile import InMemoryUploadedFile
from contactslist.humanize import naturalsize
from django.core.exceptions import ValidationError

class CreateForm(forms.ModelForm):
    max_upload_limit = 2 * 1024 * 1024
    max_upload_limit_text = naturalsize(max_upload_limit)


    picture = forms.FileField(required=False, label='File to Upload <= '+max_upload_limit_text)
    upload_field_name = 'picture'


    class Meta:
        model = Contact
        fields = ['first_name', 'last_name','email','text', 'picture']  # Picture is manual


    def clean(self):
        cleaned_data = super().clean()
        ad = cleaned_data.get('picture')
        if ad is None:
            return
        if len(ad) > self.max_upload_limit:
            self.add_error('picture', "File must be < "+self.max_upload_limit_text+" bytes")


    def save(self, commit=True):
        instance = super(CreateForm, self).save(commit=False)

        f = instance.picture   
        if isinstance(f, InMemoryUploadedFile):
            bytearr = f.read()
            instance.content_type = f.content_type
            instance.picture = bytearr 

        if commit:
            instance.save()

        return instance


