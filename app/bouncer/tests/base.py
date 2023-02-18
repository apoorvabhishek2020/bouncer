"""
Base test Classes.
"""
import inspect

from google.cloud import ndb

from django.conf import settings
from django.test import (
    SimpleTestCase,
    override_settings,
)
from app.datastore import get_client

from bouncer import models

TEST_NAMESPACE = f'test_{settings.DATASTORE_NAMESPACE}'


@override_settings(DATASTORE_NAMESPACE=TEST_NAMESPACE)
class DatastoreTestCase(SimpleTestCase):
    """Base class for Datastore tests."""

    def _clear_entities(self):
        """Clear database entities."""
        classes = inspect.getmembers(models, inspect.isclass)
        models_classes = []
        for name, obj in classes:
            if issubclass(obj, ndb.Model):
                models_classes.append(obj)
        client = get_client()
        with client.context():
            for model in models_classes:
                ndb.delete_multi(model.query().iter(keys_only=True))

    def tearDown(self):
        """Clear entities after each test."""
        self._clear_entities()
