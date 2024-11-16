from django.db import models
from cloudinary.models import CloudinaryField


class Certifications(models.Model):
    certificate_img = CloudinaryField('certificates')
    certificate_link = models.URLField()
    certificate_title = models.CharField(max_length=150, verbose_name="certificate title")
    offer_by = models.CharField(max_length=150, verbose_name="certificate offer")

    def __str__(self):
        return self.certificate_title
    
    

class Projects(models.Model):
    project_img = CloudinaryField('projects')
    project_link = models.URLField()
    project_title = models.CharField(max_length=150, verbose_name="project title")
    project_associate = models.CharField(max_length=150, verbose_name="project associated with")
    project_skills_gain = models.CharField(max_length=150, verbose_name="project skills")
    
    def __str__(self):
        return self.project_title