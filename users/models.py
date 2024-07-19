from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    image = models.ImageField(default= 'default.jpg', upload_to= 'profile_pics')

    def __str__(self):
        return(f'{self.user.username} Profile')
    

 #defining save method to resize our images   
    def save(self):
        #overide the default save
        super().save()

        #assig the variable img to the image uploaded
        img = Image.open(self.image.path)

        #check if the image size is greater than 300 pixels the we resize
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)

            #saving the resized image on the same path
            img.save(self.image.path)

            




