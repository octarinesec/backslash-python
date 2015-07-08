from sentinels import NOTHING

from .api_object import APIObject
from .error_container import ErrorContainer
from .lazy_query import LazyQuery
from .metadata_holder import MetadataHolder

class Session(APIObject, MetadataHolder, ErrorContainer):

    def report_end(self, duration=NOTHING):
        self.client.api.call_function('report_session_end', {'id': self.id, 'duration': duration})

    def report_test_start(self, name, file_name=NOTHING, class_name=NOTHING, test_logical_id=NOTHING):
        return self.client.api.call_function(
            'report_test_start',
            {'session_id': self.id,
             'name': name,
             'class_name': class_name,
             'file_name': file_name,
             'test_logical_id': test_logical_id})


    def add_subject(self, name, product=NOTHING, version=NOTHING, revision=NOTHING):
        return self.client.api.call_function(
            'add_subject',
            {'session_id': self.id, 'name': name, 'product': product, 'version': version, 'revision': revision})

    def edit_status(self, status):
        return self.client.api.call_function('edit_session_status', {'id': self.id, 'status': status})

    def query_tests(self):
        """Queries tests of the current session

        :rtype: A lazy query object
        """
        return LazyQuery(self.client, '/rest/sessions/{0}/tests'.format(self.id))

    def query_errors(self):
        """Queries tests of the current session

        :rtype: A lazy query object
        """
        return LazyQuery(self.client, '/rest/errors', query_params={'session_id': self.id})
