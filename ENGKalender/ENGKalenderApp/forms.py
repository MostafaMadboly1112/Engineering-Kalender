from django import forms


class AvailForm(forms.Form):
   
    SLOTS=(
        ('DA1','DATA Slot 1'), 
        ('DA2','DATA Slot 2'), 
        ('DA3','DATA Slot 3'), 
        ('DA4','DATA Slot 4'), 
        ('DA5','DATA Slot 5'), 
        ('VO1','VOIC Slot 1'),    
        ('VO2','VOIC Slot 2'),    
        ('VO3','VOIC Slot 3'),    
    )

    category = forms.ChoiceField(choices=SLOTS, required=True)
    slot_from = forms.DateTimeField(required=True,  input_formats=["%Y-%m-%d &H:%M", ])
    slot_to = forms.DateTimeField(required=True,  input_formats=["%Y-%m-%d &H:%M", ])


