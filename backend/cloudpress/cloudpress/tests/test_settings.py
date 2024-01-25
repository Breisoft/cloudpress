from django.test import TestCase, override_settings
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from unittest.mock import patch


class TestSettings(TestCase):

    # Test development settings
    def test_development_settings(self):
        # Ensure DEBUG is True in development
        self.assertTrue(settings.DEBUG)
        # Check that the development SECRET_KEY is set
        self.assertEqual(
            settings.SECRET_KEY, 'INSECURE-DEV-#+#hzfhl*s3!5ymy^ky4j)gltsh0*(s!$od6am@9-tzidy3+w')
        # Check the development database is sqlite3
        self.assertEqual(
            settings.DATABASES['default']['ENGINE'], 'django.db.backends.sqlite3')

    # Test production settings
    @patch.dict('os.environ', {
        'PROD': 'True',
        'DJANGO_SECRET_KEY': 'fake_production_secret_key',
        'name': 'prod_db',
        'user': 'prod_user',
        'pass': 'prod_pass',
        'host': 'prod_host',
        'port': 'prod_port',
        'DJANGO_ALLOWED_HOSTS': 'example.com'
    })
    def test_production_settings(self):
        # Reload settings to apply the patched environment variables
        with self.assertRaises(ImproperlyConfigured):
            # This should raise an error due to missing DJANGO_SECRET_KEY
            settings._setup()

        # With DJANGO_SECRET_KEY set, we should not get an error
        settings._setup()
        self.assertFalse(settings.DEBUG)
        # Check that the production SECRET_KEY is not the development key
        self.assertNotEqual(
            settings.SECRET_KEY, 'INSECURE-DEV-#+#hzfhl*s3!5ymy^ky4j)gltsh0*(s!$od6am@9-tzidy3+w')
        # Check that the production database is postgresql
        self.assertEqual(
            settings.DATABASES['default']['ENGINE'], 'django.db.backends.postgresql')
        # Check that ALLOWED_HOSTS is correctly set from environment variable
        self.assertIn('example.com', settings.ALLOWED_HOSTS)

        # Ensure that all required database settings are present
        self.assertEqual(settings.DATABASES['default']['NAME'], 'prod_db')
        self.assertEqual(settings.DATABASES['default']['USER'], 'prod_user')
        self.assertEqual(
            settings.DATABASES['default']['PASSWORD'], 'prod_pass')
        self.assertEqual(settings.DATABASES['default']['HOST'], 'prod_host')
        self.assertEqual(settings.DATABASES['default']['PORT'], 'prod_port')

    # More tests could be added to cover other settings...
