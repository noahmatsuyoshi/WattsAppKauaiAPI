from django.db import models

# Create your models here.
class IssueType(models.Model):

    issueType = models.CharField(max_length=50)

    def __str__(self):
        return self.issueType