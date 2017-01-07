from django.db import models

from researchers.models import Role
from .utils import generate_uid


class Project(models.Model):
    unique_id = models.CharField(
        max_length=8,
        unique=True,
        default=generate_uid)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    sources = models.ManyToManyField(
        'researchers.Source',
        related_name='projects',
        blank=True)
    protocols = models.ManyToManyField(
        'protocols.Protocol',
        related_name='projects',
        blank=True)
    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_participants_by_role(self):
        participants_by_role = list()
        for role_value, role_label in Role.ROLES:
            if self.roles.filter(role=role_value).exists():
                participants_by_role.append(
                    (
                        role_label,
                        self.roles.filter(
                            role=role_value).order_by('researcher')
                    )
                )
        return participants_by_role
