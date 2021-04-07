from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    picture=models.ImageField(default='profile_default.jpg',upload_to='profile_pictures')

    def __str__(self):
        return self.user.username

    def save(self,*args,**kwargs):
        super().save()
        image=Image.open(self.picture.path)
        output_size=(300,300)
        image.thumbnail(output_size)
        image.save(self.picture.path)


