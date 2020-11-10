from django.db import models
from django.contrib.auth.models import AbstractUser
from content.models import Classe

# Create your models here.
class CustomUser(AbstractUser):
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, null=True)
    profile_image = models.ImageField(upload_to="profile_pics", null=True, blank=True)
    email = models.EmailField()
    val_pos = models.IntegerField(default=0)
    val_neg = models.IntegerField(default=0)

    def __str__(self):
        return self.username

    def get_val_ratio(self):
        tot = self.val_pos + self.val_neg
        if tot:
            ratio_pos = round((self.val_pos/tot) * 100,2)
            ratio_neg = round((self.val_neg/tot) * 100,2)

            ratio_pos = str(ratio_pos)+"%"
            ratio_neg = str(ratio_neg)+"%"

            return ratio_pos, ratio_neg

        return "0%", "0%"
