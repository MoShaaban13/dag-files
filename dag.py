from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from airflow.utils.dates import days_ago

with DAG(
    dag_id="dag_with_pod_operator",
    start_date=days_ago(1),
    schedule_interval=None,
    catchup=False,
) as dag:
    
    task_create_pod = KubernetesPodOperator(
        task_id="create_pod",
        name="example-pod",
        namespace="default",
        image="ubuntu",
        cmds=["bash", "-cx"],
        arguments=["echo", "Hello World"],
    )

