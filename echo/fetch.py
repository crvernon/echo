import duckdb


def get_data(slurm_idx, data_dir):
    """Get data from a pool of CSV files containing our desired values to use when setting.

    In this case data_dir is a glob path, so /my/path/my_files_*.csv where * is wild.

    """

    # get all records associated with the sample matching the slurm_array_idx
    sql = f"""
    SELECT
        field_0
        ,field_1
        ,field_2
    FROM
        '{data_dir}'
    WHERE
        sample = {slurm_idx};
    """

    return duckdb.query(sql).df()
