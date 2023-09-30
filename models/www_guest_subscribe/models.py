import uuid
from django.db import models
from django.utils import timezone
from models import BaseModelManager

class WWWGuestSubscribe(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    topics = models.JSONField(null=False, blank=False, default=list)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)
    deleted_at = models.DateTimeField(null=True, blank=False, default=None)

    objects = BaseModelManager()
    default_objects = models.Manager()

    class Meta:
        db_table = 'www_guest_subscribe'