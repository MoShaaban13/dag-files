from airflow import DAG
from dags.operator.custom_kubernetes_pod_operator import CustomKubernetesPodOperator
from airflow.utils.dates import days_ago

with DAG(
    dag_id="simple_custom_print_dag",
    start_date=days_ago(1),
    schedule_interval=None,
    catchup=False,
) as dag:

    print_task = CustomKubernetesPodOperator(
        task_id="print_task",
        namespace="default",  # Set your namespace
        image="ubuntu",  # Use a lightweight image
        cmds=["bash", "-c"],
        arguments=["echo 'Hello from Custom Kubernetes Pod!'"],  # Command to execute
        resources={'request_memory': '256Mi', 'limit_memory': '256Mi', 'request_cpu': '0.5', 'limit_cpu': '0.5'},
        is_delete_operator_pod=True,  # Cleanup the pod after execution
        dag=dag
    )

