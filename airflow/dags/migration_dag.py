from airflow.providers.docker.operators.docker import DockerOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.decorators import task, dag
from datetime import datetime
from docker.types import Mount

@dag(
    # owner="pneuma",
     start_date=datetime.now(),
     catchup=False)
def migrate_docker_dag():
    start_task = DummyOperator(
        task_id='start_task'
        )

    end_task = DummyOperator(
        task_id='end_task'
        )   
    migration_task = DockerOperator(
        task_id='migrate_data',
        image='pneuma/data_migration:v1.0.0',
        container_name="data_migration",
        docker_url='unix://var/run/docker.sock',
        network_mode='dwh-network',
        
    )
    start_task >> migration_task >> end_task



dag = migrate_docker_dag()
