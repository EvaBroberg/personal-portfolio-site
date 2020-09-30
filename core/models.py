from django.db import models

# About model

class About(models.Model):
    short_description = models.TextField(default='SOME STRING')
    description       = models.TextField(default='SOME STRING')
    image             = models.ImageField(upload_to="about")

    class Meta:
        verbose_name        = "About me"
        verbose_name_plural = "About me"

    def __str__(self):
        return "About me"


# Skills model

class Skills(models.Model):
    skills = models.TextField(default='SOME STRING')

    class Meta:
        verbose_name        = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return self.skills


# Experience model

class Experience(models.Model):
    experience = models.TextField(default='SOME STRING')

    class Meta:
        verbose_name        = "Experience"
        verbose_name_plural = "Experience"

    def __str__(self):
        return self.experience


# Recent work model 

class RecentWork(models.Model):
    title = models.CharField(max_length=100, verbose_name="Work title")
    image = models.ImageField(upload_to="works")

    def __str__(self):
        return self.title

