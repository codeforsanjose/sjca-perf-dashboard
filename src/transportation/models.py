from django.db import models

class OpExpByService(models.Model):
    order = models.IntegerField(default=0)
    service = models.CharField(max_length=500)
    formattedYear = models.CharField(max_length=20)
    value = models.FloatField()
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order"]
        verbose_name_plural = "Department of Transportation - Expenditures by service"

    def __unicode__(self):
        return str(self.service) + ": " + str(self.value)

class AuthPosition(models.Model):
    year = models.IntegerField(default=0)
    formattedYear = models.CharField(max_length=20)
    value = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["year"]
        verbose_name_plural = "Department of Transportation - Authorized Positions"

    def __unicode__(self):
        return str(self.formattedYear) + ": " + str(self.value)

class OpExpenditure(models.Model):
    year = models.IntegerField(default=0)
    formattedYear = models.CharField(max_length=20)
    category = models.CharField(max_length=50)
    value = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["year", "value"]
        verbose_name_plural = "Department of Transportation - Operating Expenditures"

    def __unicode__(self):
        return str(self.formattedYear) + ": " + str(self.value)

class ModeOfCommute(models.Model):
    year = models.IntegerField(default=0, verbose_name="order")
    formattedYear = models.CharField(max_length=20, verbose_name="mode of commute")
    category = models.CharField(max_length=50)
    value = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["year", "value"]
        verbose_name_plural = "Department of Transportation - Mode of Commute"

    def __unicode__(self):
        return str(self.formattedYear) + ": " + str(self.value)

class SignalActivity(models.Model):
    year = models.IntegerField(default=0)
    formattedYear = models.CharField(max_length=20)
    category = models.CharField(max_length=50)
    value = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["year", "value"]
        verbose_name_plural = "Department of Transportation - Signal Activities"

    def __unicode__(self):
        return str(self.formattedYear) + ": " + str(self.value)

class RoadwayMarking(models.Model):
    year = models.IntegerField(default=0)
    formattedYear = models.CharField(max_length=20)
    value = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["year"]
        verbose_name_plural = "Department of Transportation - Roadway Markings"

    def __unicode__(self):
        return str(self.formattedYear) + ": " + str(self.value)

# parking - START
class ParkingDowntown(models.Model):
    year = models.IntegerField(default=0)
    formattedYear = models.CharField(max_length=20)
    value = models.FloatField()
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["year"]
        verbose_name_plural = "Department of Transportation - Parking at Downtown facilities"

    def __unicode__(self):
        return str(self.formattedYear) + ": " + str(self.value)

class ParkingCitation(models.Model):
    year = models.IntegerField(default=0)
    formattedYear = models.CharField(max_length=20)
    value = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["year"]
        verbose_name_plural = "Department of Transportation - Parking Citations"

    def __unicode__(self):
        return str(self.formattedYear) + ": " + str(self.value)

# parking - END

# street maintenance - START
class StreetLandscape(models.Model):
    year = models.IntegerField(default=0)
    formattedYear = models.CharField(max_length=20)
    value = models.FloatField()
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["year"]
        verbose_name_plural = "Department of Transportation - Street Landscapes"

    def __unicode__(self):
        return str(self.formattedYear) + ": " + str(self.value)

class SidewalkRepair(models.Model):
    year = models.IntegerField(default=0)
    formattedYear = models.CharField(max_length=20)
    value = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["year"]
        verbose_name_plural = "Department of Transportation - Sidewalk Repairs"

    def __unicode__(self):
        return str(self.formattedYear) + ": " + str(self.value)

# street maintenance - END

# storm drainage - START
class StreetSweeping(models.Model):
    year = models.IntegerField(default=0)
    formattedYear = models.CharField(max_length=20)
    category = models.CharField(max_length=50)
    value = models.FloatField()
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["year", "value"]
        verbose_name_plural = "Department of Transportation - Street Sweeping"

    def __unicode__(self):
        return str(self.formattedYear) + ": " + str(self.value)

class StormCall(models.Model):
    year = models.IntegerField(default=0)
    formattedYear = models.CharField(max_length=20)
    value = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["year"]
        verbose_name_plural = "Department of Transportation - Storm Calls"

    def __unicode__(self):
        return str(self.formattedYear) + ": " + str(self.value)

class DrainRequest(models.Model):
    year = models.IntegerField(default=0)
    formattedYear = models.CharField(max_length=20)
    value = models.FloatField(default=None, null=True, blank=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["year"]
        verbose_name_plural = "Department of Transportation - Drain Requests"

    def __unicode__(self):
        return str(self.formattedYear) + ": " + str(self.value)

# storm drainage - END

# pavement maintenance - START
class StreetRepair(models.Model):
    year = models.IntegerField(default=0)
    formattedYear = models.CharField(max_length=20)
    value = models.FloatField(default=None, null=True, blank=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["year"]
        verbose_name_plural = "Department of Transportation - Street Repair Ratings"

    def __unicode__(self):
        return str(self.formattedYear) + ": " + str(self.value)

class PavementIndexArea(models.Model):
    year = models.IntegerField(default=0, verbose_name="order")
    formattedYear = models.CharField(max_length=20, verbose_name="area")
    value = models.FloatField(default=None, null=True, blank=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["year", "value"]
        verbose_name_plural = "Department of Transportation - Pavement Index by Area"

    def __unicode__(self):
        return str(self.formattedYear) + ": " + str(self.value)

class PavementIndexSJ(models.Model):
    year = models.IntegerField(default=0)
    formattedYear = models.CharField(max_length=20)
    value = models.FloatField(default=None, null=True, blank=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["year", "value"]
        verbose_name_plural = "Department of Transportation - Pavement Index San Jose"

    def __unicode__(self):
        return str(self.formattedYear) + ": " + str(self.value)

class Pothole(models.Model):
    year = models.IntegerField(default=0)
    formattedYear = models.CharField(max_length=20)
    value = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["year"]
        verbose_name_plural = "Department of Transportation - Potholes filled"

    def __unicode__(self):
        return str(self.formattedYear) + ": " + str(self.value)

class RoadFunding(models.Model):
    year = models.IntegerField(default=0, verbose_name="order")
    formattedYear = models.CharField(max_length=40, default=None, null=True, blank=True)
    category = models.CharField(max_length=50)
    value = models.FloatField(default=None, null=True, blank=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["year", "value"]
        verbose_name_plural = "Department of Transportation - Funding needed to fix roads"

    def __unicode__(self):
        return str(self.category) + ": " + str(self.value)

# pavement maintenance - END
