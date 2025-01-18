from django import forms
from .models import PatientRegistration
from Coordinator.models import User
from receptionist.models import Consultation_details

class PatientRegistrationForm(forms.ModelForm):
    class Meta:
        model = PatientRegistration
        fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'gender', 'address', 'phone_number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].required = False



class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation_details
        fields = ['op_number', 'patient_name', 'date', 'symptoms', 'Diagnosis', 'prescription']
        widgets = {
            'symptoms': forms.Textarea(attrs={'rows': 3}),
            'Diagnosis': forms.Textarea(attrs={'rows': 3}),
            'prescription': forms.Textarea(attrs={'rows': 6, 'cols': 50, 'style': 'min-height: 150px;'}),
        }
    def clean_prescription(self):
        prescription_data = self.cleaned_data.get('prescription')
        if not prescription_data:
            return None  # Allow empty prescriptions
        try:
            if isinstance(prescription_data, str):
                return json.loads(prescription_data)
            return prescription_data
        except ValueError:
            raise forms.ValidationError("Prescription data must be a valid JSON format.")

#     def __init__(self, *args, **kwargs):
#         super(ConsultationForm, self).__init__(*args, **kwargs)
#         self.fields['doctor'].required = False
#  # Add other fields as needed


