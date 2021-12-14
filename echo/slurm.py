import os


def build_script(job_name='slurm-job',
                 partition='short',
                 account='gcam',
                 output=None,
                 error=None,
                 nodes=1,
                 ntasks=1,
                 cpus_per_task=1,
                 mem_per_cpu='4G',
                 time='00:10:00',
                 array=None,
                 mail_type='all',
                 mail_user='',
                 python_script='',
                 output_job_script='./slurm_script.sl',
                 submit_job=True,
                 data_dir='.'):
    """Create a SLURM job script."""

    slurm_script = f"""#!/bin/bash
#SBATCH --job-name={job_name}
#SBATCH --partition={partition}
#SBATCH --account={account}
#SBATCH --output={output}
#SBATCH --error={error}
#SBATCH --nodes={nodes}
#SBATCH --ntasks={ntasks}
#SBATCH --cpus-per-task={cpus_per_task}
#SBATCH --time={time}
#SBATCH --array={array}

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

LD_PRELOAD=/rcfs/projects/GCAM/GCAM-libraries/lib/boost/libboost_python37.so.1.76.0 python {python_script} $SLURM_ARRAY_TASK_ID {data_dir}

ENDTIME=`date +%s`
RUNTIME=$((ENDTIME-STARTTIME))
echo "Run completed in $RUNTIME seconds."
"""

    # write output script to file
    with open(output_job_script, 'w') as out:
        out.write(slurm_script)

    if submit_job:
        cmd = f"sbatch {output_job_script}"
        print(cmd)

        os.system(cmd)


if __name__ == "__main__":

    build_script(job_name='gcam_test',
                 partition='short',
                 account='gcam',
                 output='slurm-%A.%a.out',
                 error='slurm-%A.%a.err',
                 nodes=1,
                 ntasks=1,
                 cpus_per_task=1,
                 mem_per_cpu='4G',
                 time='00:10:00',
                 array='0-1',
                 mail_type='all',
                 mail_user='',
                 python_script='/people/d3y010/test_gcamwrapper/test.py',
                 output_job_script='/people/d3y010/test_gcamwrapper/gcam_test.sl',
                 submit_job=True,
                 data_dir='/people/d3y010/test_gcamwrapper/data/file_*.csv')


