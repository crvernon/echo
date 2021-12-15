import os
import unittest
import pkg_resources

import pandas as pd

import echo.fetch as fetch


class TestFetch(unittest.TestCase):
    """Tests for fetch setter data behavior."""

    # expected outcome from the get_data query
    COMP_DF = pd.DataFrame({'field_0': [0.24567706373560583, 0.07098094248317988],
                            'field_1': [0.3781703789954739, 0.4314911397341613],
                            'field_2': [0.0335912327489154, 0.7304099284940675]})

    def test_get_data(self):
        """Ensure data stream read is functioning as expected."""

        # get glob path for data files
        data_dir = pkg_resources.resource_filename('echo', 'tests/data')
        glob_path = os.path.join(data_dir, 'file_*.csv')

        # get data from file query
        df = fetch.get_data(glob_path=glob_path, alternative_idx=0)

        # compare outputs
        pd.testing.assert_frame_equal(TestFetch.COMP_DF, df)
