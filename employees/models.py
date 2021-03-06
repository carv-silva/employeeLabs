from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=256)
    # budget = models.FloatField()
    # budget = models.FloatField(null=False, blank=False, default=None)
    budget = models.DecimalField(max_digits=15, default=0, decimal_places=2)
    description = models.CharField(max_length=25)
    # employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    startDate = models.DateField(null=True, blank=False)
    terminationDate = models.DateField(null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Payroll(models.Model):
    month = models.DateField(null=True, blank=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    gross_salary = models.DecimalField(
        max_digits=15, default=0, decimal_places=2)
    taxes = models.DecimalField(max_digits=15, default=0, decimal_places=2)
    net_salary = models.DecimalField(
        max_digits=15, default=0, decimal_places=2)
    BENEFITS = (
        ('MP', 'Medical plan'),
        ('DP', 'Dental plan'),
        ('GY', 'Gym'),
        ('N', 'None')
    )
    benefits = models.CharField(max_length=2, choices=BENEFITS, blank=False,
                                null=False, default='N')

    '''def save(self, tax_salary=gross_salary, *args, **kwargs):
        tax = (tax_salary / 100) * 11
        return super(Payroll, self).save(*args, **kwargs)'''

    ''' def tax_gross_salary(tax):
            tax = (tax / 100) * 11
            return tax

    def save(self, gross_salary, *args, **kwargs):
        self.gross_salary = (gross_salary / 100) * 11
        # gross_salary = (gross_salary / 100) * 11
        # super(gross_salary, self).save(*args, **kwargs)
        return self.gross_salary
        # self.gross_salary = (gross_salary / 100) * 11'''





