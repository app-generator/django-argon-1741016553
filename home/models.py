# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Users(models.Model):

    #__Users_FIELDS__
    user_id = models.IntegerField(null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    password_hash = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    role = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Users_FIELDS__END

    class Meta:
        verbose_name        = _("Users")
        verbose_name_plural = _("Users")


class Data(models.Model):

    #__Data_FIELDS__
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255, null=True, blank=True)
    file_type = models.CharField(max_length=255, null=True, blank=True)
    imported_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Data_FIELDS__END

    class Meta:
        verbose_name        = _("Data")
        verbose_name_plural = _("Data")


class Metrics(models.Model):

    #__Metrics_FIELDS__
    metric_id = models.IntegerField(null=True, blank=True)
    data_id = models.ForeignKey(Data, on_delete=models.CASCADE)
    metric_name = models.CharField(max_length=255, null=True, blank=True)
    metric_value = models.IntegerField(null=True, blank=True)
    calculated_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Metrics_FIELDS__END

    class Meta:
        verbose_name        = _("Metrics")
        verbose_name_plural = _("Metrics")



#__MODELS__END
