from django import forms
from django.db.models import F
from .models import Property, PropertyUtility, PropertyNearby, PropertyImage
from apps.helper.models import Utility, Nearby


class PropertyForm(forms.ModelForm):
    utilities = forms.ModelMultipleChoiceField(
        queryset=Utility.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Utilities"
    )
    nearby = forms.ModelMultipleChoiceField(
        queryset=Nearby.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Nearby Places"
    )
    images = forms.FileField(
        widget=forms.FileInput(attrs={'accept': 'image/*'}),
        required=False,
        label="Property Images"
    )

    class Meta:
        model = Property
        fields = [
            "title",
            "description",
            "type",
            "status",
            "location",
            "price",
            "area",
         ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add CSS classes to form fields
        self.fields['title'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Enter property title'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-textarea',
            'placeholder': 'Describe your property in detail'
        })

        self.fields['type'].widget.attrs.update({
            'class': 'form-select'
        })
        
        self.fields['type'].choices = [("", "Select Type")] + list(self.fields['type'].choices)[1:]

        self.fields['status'].widget.attrs.update({
            'class': 'form-select'
        })
        
        self.fields['status'].choices = [("", "Select Status")] + list(self.fields['status'].choices)[1:]

        self.fields['location'].widget.attrs.update({
            'class': 'form-select'
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-number',
            'placeholder': '0.00'
        })

        self.fields['area'].widget.attrs.update({
            'class': 'form-number',
            'placeholder': '0.00'
        })

        self.fields['images'].widget.attrs.update({
            'class': 'form-input',
            'accept': 'image/*'
        })

        # Pre-populate utilities and nearby if editing
        if self.instance.pk:
            self.fields['utilities'].initial = self.instance.utilities.all()
            self.fields['nearby'].initial = self.instance.nearby.all()

    def clean_images(self):
        images = self.files.getlist('images') if self.files else []
        # Validate each image
        for image in images:
            if image.size > 5242880:  # 5MB limit
                raise forms.ValidationError(f"{image.name} exceeds 5MB limit.")
        return images

    def save(self, commit=True):
        instance = super().save(commit=commit) # Save the property instance first to get an ID for related models
        
        if commit:
            # Clear existing utilities and nearby
            PropertyUtility.objects.filter(property=instance).delete()
            PropertyNearby.objects.filter(property=instance).delete()

            # Add selected utilities and update popularity counts
            for utility in self.cleaned_data['utilities']:
                PropertyUtility.objects.create(property=instance, utility=utility)
                Utility.objects.filter(pk=utility.pk).update(count=F('count') + 1)

            # Add selected nearby places and update popularity counts
            for nearby_item in self.cleaned_data['nearby']:
                PropertyNearby.objects.create(property=instance, nearby=nearby_item)
                Nearby.objects.filter(pk=nearby_item.pk).update(count=F('count') + 1)

            # Save uploaded images to the property
            for image_file in self.cleaned_data.get('images', []):
                PropertyImage.objects.create(property=instance, image=image_file)

        return instance
        
        
        
    