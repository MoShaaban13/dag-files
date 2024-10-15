from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from airflow.utils.dates import days_ago

with DAG(
    dag_id="simple_print_dag",
    start_date=days_ago(1),
    schedule_interval=None,
    catchup=False,
) as dag:

    print_task = KubernetesPodOperator(
        task_id="print_task",
        name="print-pod",
        namespace="default",  # Set your namespace
        image="ubuntu",  # Use a lightweight image
        cmds=["bash", "-c"],  # Use bash to execute commands
        arguments=["echo 'Hello from Kubernetes Pod!'"],  # The command to execute
        resources={
            "request_memory": "256Mi",  # Request memory
            "limit_memory": "256Mi",  # Limit memory
            "request_cpu": "500m",  # Request CPU in millicores
            "limit_cpu": "500m",  # Limit CPU in millicores
        },
        dag=dag
    )

