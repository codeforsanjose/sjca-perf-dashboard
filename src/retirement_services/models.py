from django.db import models

class RSOpExpenditure(models.Model):
    year = models.IntegerField(default=0)
    formattedYear = models.CharField(max_length=20)
    value = models.FloatField(default=None, null=True, blank=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["year"]
        verbose_name_plural = "Retirement Services - Operating Expenditures"

    def __unicode__(self):
        return str(self.formattedYear) + ": " + str(self.value)

class RSAuthPosition(models.Model):
    year = models.IntegerField(default=0)
    formattedYear = models.CharField(max_length=40, default=None, null=True, blank=True)
    value = models.FloatField(default=None, null=True, blank=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["year"]
        verbose_name_plural = "Retirement Services - Authorized Positions"

    def __unicode__(self):
        return str(self.formattedYear) + ": " + str(self.value)


class RSRetireeBenefits(models.Model):
    year = models.IntegerField(default=0)
    formattedYear = models.CharField(max_length=40,
                                     default=None,
                                     null=True,
                                     blank=True)
    category = models.CharField(max_length=50)
    value = models.FloatField(default=None, null=True, blank=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["year"]
        verbose_name_plural = "Retirement Services - Retiree Benefits"

    def __unicode__(self):
        return u'%s (%s): - %s' % (self.category,
                                   self.formattedYear,
                                   self.value)


class RSFederatedFundedPercent(models.Model):
    year = models.IntegerField(default=0)
    formattedYear = models.CharField(max_length=40,
                                     default=None,
                                     null=True,
                                     blank=True)
    category = models.CharField(max_length=50)
    value = models.FloatField(default=None, null=True, blank=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["year"]
        verbose_name_plural = "Retirement Services - Federated Funded Status"

    def __unicode__(self):
        return u'%s (%s): - %s' % (self.category,
                                   self.formattedYear,
                                   self.value)


class RSPoliceAndFireFundedPercent(models.Model):
    year = models.IntegerField(default=0)
    formattedYear = models.CharField(max_length=40,
                                     default=None,
                                     null=True,
                                     blank=True)
    category = models.CharField(max_length=50)
    value = models.FloatField(default=None, null=True, blank=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["year"]
        verbose_name_plural = ("Retirement Services"
                               " - Police and Fire Funded Status")

    def __unicode__(self):
        return u'%s (%s): - %s' % (self.category,
                                   self.formattedYear,
                                   self.value)
