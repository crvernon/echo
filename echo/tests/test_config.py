import unittest

from echo.config import Config


class TestConfig(unittest.TestCase):
    """Tests for fetch setter data behavior."""

    NEW_PARAMS = {'job_name': 'new_job', 'nodes': 10}

    def test_config(self):
        """Ensure config generator and setter are working correctly."""

        # instantiate a config instance
        job = Config()

        self.assertEqual('test', job.params.get('job_name'))
        self.assertEqual(1, job.params.get('nodes'))

        # update and reassess
        job.params = TestConfig.NEW_PARAMS

        self.assertEqual('new_job', job.params.get('job_name'))
        self.assertEqual(10, job.params.get('nodes'))
