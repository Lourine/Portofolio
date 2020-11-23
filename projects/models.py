from django.db import models

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length =60)
    description = models.TextField()
    link = models.CharField(null = True,max_length =500)
    article_image = models.ImageField(upload_to = 'images/',blank = True)
    @classmethod
    def project_list(cls):
        
        projects = cls.objects.all()
        return projects
    def __str__(self):
        return self.title


class Skills(models.Model):
    name= models.CharField(max_length=60)
    image= models.ImageField(upload_to = 'images/', blank= True)

    @classmethod
    def skill_list(cls):
        
        skills = cls.objects.all()
        return skills
    def __str__(self):
        return self.name

    
