import gcamwrapper as gw

import echo.fetch as fetch


def gcam_worker(slurm_idx, data_dir):
    """Fake model

    """

    gcam = gw.Gcam("configuration_ref.xml", "/people/pralitp/test-framework/exe")
    gcam.run_to_period(1)
    query = gw.get_query("land", "land_allocation")
    ret = gcam.get_data(query, {"region": ['=', 'USA'], "year": ['<=', '1990']})

    # set would happen here
    setter_data = fetch.get_data(slurm_idx, data_dir)
    print(setter_data)

    del gcam

    return ret.head()
