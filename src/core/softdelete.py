from django.utils import timezone
from django.db import models


class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

    def delete(self, *args, **kwargs):
        return self.get_queryset().update(is_deleted=True, delete_at=timezone.now())

    def hard_delete(self, *args, **kwargs):
        return super().get_queryset().delete(*args, **kwargs)

    def restore(self, *args, **kwargs):
        return self.get_queryset().update(is_deleted=False, delete_at=None)


class SoftDelete(models.Model):
    is_deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(blank=True, null=True)

    objects = SoftDeleteManager()
    all_objects = models.Manager()  # Include deleted objects

    class Meta:
        abstract = True
