from django.contrib import admin
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


# Experience model

class Experience(models.Model):
    experience = models.TextField(blank=True)

    class Meta:
        verbose_name        = "Experience"
        verbose_name_plural = "Experience"

    def __str__(self):
        return self.experience


# Recent work model 

class RecentWork(models.Model):
    title            = models.CharField(max_length=100, verbose_name="Work title")
    client           = models.TextField(verbose_name="Client", blank=True)
    description      = models.TextField(verbose_name="Work description", blank=True)
    work_description = models.TextField(verbose_name="Work responsibilities", blank=True)
    image            = models.ImageField(upload_to="works")
    code             = models.URLField(("code"), max_length=128, db_index=True, blank=True)
    demo             = models.URLField(("demo"), max_length=128, db_index=True, blank=True)
    site             = models.URLField(("site"), max_length=128, db_index=True, blank=True)


    def __str__(self):
        return self.title


class Duties(models.Model):
    description = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.description


class Journey(models.Model):
    image          = models.ImageField(upload_to="journey")
    date           = models.CharField(max_length=100, verbose_name="date", blank=True)

    company_image   = models.ImageField(upload_to="journey", verbose_name="company image")
    company_page    = models.TextField(verbose_name="company page", blank=True)
    company_name    = models.TextField(verbose_name="company name", blank=True)
    job_title       = models.TextField(verbose_name="job title", blank=True)
    job_date        = models.CharField(max_length=100, verbose_name="job date", blank=True)
    duties          = models.ManyToManyField(Duties,related_name='duties',blank=True)

    company_image2   = models.ImageField(upload_to="journey", verbose_name="company image",blank=True)
    company_page2    = models.TextField(verbose_name="company page", blank=True)
    company_name2    = models.TextField(verbose_name="company name", blank=True)
    job_title2       = models.TextField(verbose_name="job title", blank=True)
    job_date2        = models.CharField(max_length=100, verbose_name="job date", blank=True)
    duties2          = models.ManyToManyField(Duties, related_name='duties2',blank=True)

    company_image3   = models.ImageField(upload_to="journey", verbose_name="company image",blank=True)
    company_page3    = models.TextField(verbose_name="company page", blank=True)
    company_name3    = models.TextField(verbose_name="company name", blank=True)
    job_title3       = models.TextField(verbose_name="job title", blank=True)
    job_date3        = models.CharField(max_length=100, verbose_name="job date", blank=True)
    duties3          = models.ManyToManyField(Duties, related_name='duties3',blank=True)


    class Meta:
        verbose_name        = "Journey"
        verbose_name_plural = "Journey"

    def __str__(self):
        return self.date


class AllWork(models.Model):
    title            = models.CharField(max_length=100, verbose_name="Work title")
    client           = models.TextField(verbose_name="Client", blank=True)
    description      = models.TextField(verbose_name="Work description", blank=True)
    work_description = models.TextField(verbose_name="Work responsibilities", blank=True)
    image            = models.ImageField(upload_to="works")
    code             = models.URLField(("code"), max_length=128, db_index=True, blank=True)
    demo             = models.URLField(("demo"), max_length=128, db_index=True, blank=True)
    site             = models.URLField(("site"), max_length=128, db_index=True, blank=True)


    def __str__(self):
        return self.title






    




