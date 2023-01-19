from django.test import TransactionTestCase
from django.test.runner import DiscoverRunner
from unittest.suite import TestSuite
class UnitTestRunner(DiscoverRunner):
    def setup_databases(self, **kwargs):
        pass
    def teardown_databases(self, old_config, **kwargs):
        pass
    def is_unittest(self, test):
        return not issubclass(test.__class__, TransactionTestCase)