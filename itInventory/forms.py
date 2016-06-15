from django import forms
from .models import inventory




class itemForm(forms.ModelForm):
    machine = forms.CharField(label='Machine', max_length=100, required=False)
    room = forms.CharField(label='Room', max_length=100, required=False)
    mac = forms.CharField(label='MAC', max_length=100, required=True, error_messages={'required': 'MAC Address is required.'})
    ip = forms.CharField(label='IP', max_length=100, required=False)
    vlan = forms.CharField(label='VLAN', max_length=100, required=False)
    manufacturer = forms.CharField(label='Manufacturer', max_length=100, required=False)
    model = forms.CharField(label='Model', max_length=100, required=False)
    serial = forms.CharField(label='Serial', max_length=100, required=True, error_messages={'required': 'Serial is required.'})
    user = forms.CharField(label='User', max_length=100, required=False)
    os = forms.CharField(label='OS', max_length=100, required=False)
    department = forms.CharField(label='Department', max_length=100, required=False)
    sponsor = forms.CharField(label='Sponsor', max_length=100, required=False)
    notes = forms.CharField(label='Notes', max_length=100, required=False)

    def process(self):
        a = self.cleaned_data

        item = inventory(machine=a.get('machine'), room=a.get('room'), mac=a.get('mac'), ip=a.get('ip'), vlan=a.get('vlan'),
                         manufacturer=a.get('manufacturer'), model=a.get('model'), serial=a.get('serial'), user=a.get('user'), os=a.get('os'),
                         department=a.get('department'), sponsor=a.get('sponsor'), notes=a.get('notes'))
        item.save()

    class Meta:
        model = inventory
        fields = ['machine','room','mac','ip','vlan','manufacturer','model','serial','user','os','department','sponsor','notes']



class searchForm(forms.Form):
    CHOICES=[('', 'Search by...'),('Machine','Machine'),('Serial','Serial'), ('MAC Address', 'MAC Address'), ('IP Address','IP Address'), ('User', 'User'), ('Department', 'Department')]
    search = forms.CharField(label='Search', max_length=200, required=True, error_messages={'required': 'Please enter a search term.'})
    choices = forms.ChoiceField(label="Search By", choices=CHOICES, required=True, error_messages={'required': 'Please select an option.'})

    class Meta:
        model = inventory
        widgets = {
            'search': forms.Textarea(attrs={'cols':20})
        }



