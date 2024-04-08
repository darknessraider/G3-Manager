from django import forms

class PartRegisterForm(forms.Form):
    your_name = forms.CharField(label="Your Name", max_length=30)
    part_name = forms.CharField(label="Part Name", max_length=30)
    part_number = forms.IntegerField(label="Part Number")
    priority = forms.IntegerField(label="Priority")


class ElectricalReviewForm(forms.Form):
    name = forms.CharField(label="Electrical Reviewer")
    approved = forms.BooleanField(label="Approved")
