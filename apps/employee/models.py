from django.db import models

from managers import SampleManager

MONTH_CHOICES = (
    ('01', 'January'),
    ('02', 'February'),
    ('03', 'March'),
    ('04', 'April'),
    ('05', 'May'),
    ('06', 'June'),
    ('07', 'July'),
    ('08', 'August'),
    ('09', 'September'),
    ('10', 'October'),
    ('11', 'November'),
    ('12', 'December'),
    )


class Unit(models.Model):
    code = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=100)

    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class Designation(models.Model):
    name = models.CharField(max_length=40)

    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=40)

    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Status"

    def __unicode__(self):
        return self.name


class Employee(models.Model):
    code = models.CharField(max_length=10, null=True, blank=True, unique=True)
    name = models.CharField(max_length=100)

    designation = models.ForeignKey(Designation, null=True, blank=True)
    unit = models.ForeignKey(Unit, null=True, blank=True)
    status = models.ForeignKey(Status, default=1)

    date_of_birth = models.DateField(null=True, blank=True)
    date_of_joining = models.DateField(null=True, blank=True)

    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    comments = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    objects = SampleManager()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["name",]


class SalaryDetail(models.Model):
    employee = models.ForeignKey(Employee)
    year = models.IntegerField()
    month = models.CharField(max_length=2,
                              choices=MONTH_CHOICES)

    basic = models.PositiveSmallIntegerField()
    da = models.PositiveSmallIntegerField()
    hra = models.PositiveSmallIntegerField()
    allowance = models.PositiveSmallIntegerField(default=0)

    loss_of_pay = models.PositiveSmallIntegerField(default=0)

    repayment_of_loan = models.PositiveSmallIntegerField(default=0)

    @property
    def total_salary(self):
        return self.basic + self.da + self.hra + self.allowance

    @property
    def contribution_to_pf(self):
        """ Employee and Employer each contribute 12% of basic + da towards PF
        """
        return (self.cycle.basic + self.cycle.da) * 0.24

    @property
    def admin_charges(self):
        """ 1% of basic + da
        """

        if self.cycle.basic + self.cycle.da > 6500:
            return 65
        else:
            return (self.cycle.basic + self.cycle.da) * 0.01

    @property
    def total_remittence(self):
        return self.contribution_to_pf + self.repayment_of_loan

    @property
    def total_deductions(self):
        return self.contribution_to_pf + self.repayment_of_loan + self.admin_charges



    def __unicode__(self):
        return '%s : %s/%s' % (self.employee, self.month, self.year)
