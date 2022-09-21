from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=70)
    first_name=models.CharField(max_length=70)
    last_name=models.CharField(max_length=70)
    email=models.EmailField()


class page(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    page_name=models.CharField(max_length=70)
    page_cat=models.CharField(max_length=70)
    page_publish_date=models.DateField()


class post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post_title=models.CharField(max_length=70)
    post_cat=models.CharField(max_length=70)
    post_publish_date=models.DateField()


class song(models.Model):
    user=models.ManyToManyField(User)
    song_name=models.CharField(max_length=80)
    song_duration=models.IntegerField()

    def written_by(self):
        return ','.join(str(p) for p in self.user.all())



