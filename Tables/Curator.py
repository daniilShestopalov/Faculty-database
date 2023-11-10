from django.db import models

class Curator(models.Model):
    curator_id = models.AutoField(primary_key=True)
    curator_second_name = models.CharField(max_length=45)
    curator_first_name = models.CharField(max_length=45)
    curator_middle_name = models.CharField(max_length=45, null=True, default=None)
    curator_contact_number = models.BigIntegerField(unique=True)

    def __str__(self):
        return f"{self.curator_second_name} {self.curator_first_name} {self.curator_middle_name if self.curator_middle_name else ''}".strip()
