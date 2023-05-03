from django.db import models
from django.conf import settings

# Create your models here.



class Booking(models.Model):

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

    category = models.CharField(max_length=4, choices=SLOTS)
    slot = models.IntegerField()
    

    def __str__(self):
        return f'{self.slot} {self.category}'
    


class Books(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    slot_from = models.DateTimeField()
    slot_to = models.DateTimeField()

    def __str__(self):
        return f'{self.user} has booked {self.booking} from {self.slot_from} till {self.slot_to}'
    