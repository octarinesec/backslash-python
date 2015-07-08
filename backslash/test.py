from sentinels import NOTHING

from .api_object import APIObject
from .error_container import ErrorContainer
from .lazy_query import LazyQuery
from .metadata_holder import MetadataHolder

class Test(APIObject, MetadataHolder, ErrorContainer):

    def report_end(self, duration=NOTHING):
        self.client.api.call_function('report_test_end', {'id': self.id, 'duration': duration})

    def mark_skipped(self):
        self.client.api.call_function('report_test_skipped', {'id': self.id})

    def mark_interrupted(self):
        self.client.api.call_function('report_test_interrupted', {'id': self.id})


    def edit_status(self, status):
        return self.client.api.call_function('edit_test_status', {'id': self.id, 'status': status})

    def query_errors(self):
        """Queries tests of the current session

        :rtype: A lazy query object
        """
        return LazyQuery(self.client, '/rest/errors', query_params={'test_id': self.id})
