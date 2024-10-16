from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    dag_id='pod_stay_alive_ubuntu_5_minutes',
    default_args=default_args,
    description='A DAG to run a pod with ubuntu image that stays alive for at least 5 minutes',
    schedule_interval=None,
    catchup=False,
)

# Define the KubernetesPodOperator task to run the ubuntu image
stay_alive_pod = KubernetesPodOperator(
    namespace='default',
    image="ubuntu:latest",  # Using the Ubuntu image
    cmds=["bash", "-c"],  # Command to execute
    arguments=["echo 'Pod will stay alive for 5 minutes' && sleep 300"],  # Sleep for 5 minutes (300 seconds)
    labels={"purpose": "stay-alive"},
    name="stay-alive-pod-ubuntu",
    task_id="stay_alive_pod_task_ubuntu",
    get_logs=True,  # Retrieve logs from the pod
    is_delete_operator_pod=True,  # Delete the pod after completion
    dag=dag,
)

stay_alive_pod
