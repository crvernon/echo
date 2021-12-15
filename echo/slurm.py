import os

import echo.config as cfg
from echo.config import Config


def slurm_header


def run_slurm(config_file: '' = str, params: {} = dict):
    """Create and optionally submit a SLURM job script."""

    # instantiate a config instance
    job = Config()

    # update default params with data from the config file if passed
    if len(config_file) > 0:
        new_params = cfg.read_yaml(config_file)
        job.params = new_params

    # account for any additional parameter updates
    job.params = params

    # construct script; deindent is required to properly construct script
    slurm_script = f"""#!/bin/bash
#SBATCH --job-name={job.params.get('job_name')}
#SBATCH --partition={job.params.get('partition')}
#SBATCH --account={job.params.get('account')}
#SBATCH --output={job.params.get('output')}
#SBATCH --error={job.params.get('error')}
#SBATCH --nodes={job.params.get('nodes')}
#SBATCH --ntasks={job.params.get('ntasks')}
#SBATCH --cpus-per-task={job.params.get('cpus_per_task')}
#SBATCH --time={job.params.get('time')}
#SBATCH --array={job.params.get('array')}

echo "My SLURM_ARRAY_JOB_ID is $SLURM_ARRAY_JOB_ID."
echo "My SLURM_ARRAY_TASK_ID is $SLURM_ARRAY_TASK_ID"
echo "Executing on the machine:" $(hostname)

module load git/2.31.1
module load java/1.8.0_31
module load R/4.0.2
module load python/3.7.0
module load gcc/10.2.0

source /rcfs/projects/GCAM/pyenv3.7.0/bin/activate

STARTTIME=`date +%s`

LD_PRELOAD=/rcfs/projects/GCAM/GCAM-libraries/lib/boost/libboost_python37.so.1.76.0 python {job.params.get('python_script')} {job.params.get('data_dir')}

ENDTIME=`date +%s`
RUNTIME=$((ENDTIME-STARTTIME))
echo "Run completed in $RUNTIME seconds."
"""

    # write output script to file
    with open(job.params.get('output_job_script'), 'w') as out:
        out.write(slurm_script)

    if job.params.submit_job:
        cmd = f"sbatch {job.params.get('output_job_script')}"
        print(cmd)

        os.system(cmd)


if __name__ == "__main__":

    param_dict = {'job_name': 'gcam_test',
                  'partition': 'short',
                  'account': 'gcam',
                  'output': 'slurm-%A.%a.out',
                  'error': 'slurm-%A.%a.err',
                  'nodes': 1,
                  'ntasks': 1,
                  'cpus_per_task': 1,
                  'mem_per_cpu': '4G',
                  'time': '00:10:00',
                  'array': '0-1',
                  'mail_type': 'all',
                  'mail_user': '',
                  'python_script': '/people/d3y010/test_gcamwrapper/test.py',
                  'output_job_script': '/people/d3y010/test_gcamwrapper/gcam_test.sl',
                  'submit_job': True,
                  'data_dir': '/people/d3y010/test_gcamwrapper/data/file_*.csv'}

    run_slurm(params=param_dict)
