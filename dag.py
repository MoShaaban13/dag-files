from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from airflow.utils.dates import days_ago
from datetime import timedelta
from kubernetes.client import V1ResourceRequirements

with DAG(
    dag_id="dag_with_pod_operator",
    start_date=days_ago(1),
    schedule_interval=None,
    catchup=False,
) as dag:

    resource_requirements = V1ResourceRequirements(
        requests={
            "cpu": "0.5",  # Requesting half a core
            "memory": "500Mi",  # Requesting 0.5 GB of memory
        },
        limits={
            "cpu": "0.5",  # Limiting to half a core
            "memory": "500Mi",  # Limiting to 0.5 GB of memory
        },
    )

    task_create_pod = KubernetesPodOperator(
        task_id="create_pod",
        name="example-pod",
        namespace="default",
        image="ubuntu",
        cmds=["bash", "-cx"],
        arguments=["echo", "Hello World"],
        execution_timeout=timedelta(minutes=10),  # Set timeout to 10 minutes
        resources=resource_requirements,  # Pass the resource requirements
    )

