from django.db import models
from django.utils.translation import gettext as _
from modules.fusion.models import User

class LeaveCategory(models.TextChoices):
    CL = 'CL', _('Casual Leave')
    RH = 'RH', _('Restricted Holiday')
    SCL = 'SCL', _('Special Conduct Leave')
    EL = 'EL', _('Earned Leave')
    COL = 'COL', _('Compensatory Off Leave')
    VL = 'VL', _('Vacation Leave')

class LeaveRequest(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leave_requests')
    category = models.CharField(max_length=3, choices=LeaveCategory.choices)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Leave Request')
        verbose_name_plural = _('Leave Requests')
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.employee.username} - {self.get_category_display()} from {self.start_date} to {self.end_date}'
