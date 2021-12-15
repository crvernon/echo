import duckdb


def get_data(glob_path):
    """Get data from a pool of CSV files containing our desired values to use when setting.

    In this case data_dir is a glob path, so /my/path/my_files_*.csv where * is wild.

    TODO:  build proper docstring

    """

    # get slurm task id from environment; natively this will be type str
    slurm_task_idx = os.environ["SLURM_ARRAY_TASK_ID"])

    # get all records associated with the sample matching the slurm_array_idx
    sql = f"""
    SELECT
        field_0
        ,field_1
        ,field_2
    FROM
        '{glob_path}'
    WHERE
        sample = {slurm_task_idx}
    ORDER BY
        field_1;
    """

    return duckdb.query(sql).df()
