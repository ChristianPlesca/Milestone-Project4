from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    message_subject = forms.CharField(required=True)
    message_content = forms.CharField(required=True, widget=forms.Textarea)
    

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_email'].label = "Your email:"
        self.fields['phone_number'].label = "Phone Number:"
        self.fields['message_subject'].label = "Subject:"
        self.fields['message_content'].label = "Your Enquiry/Message:"