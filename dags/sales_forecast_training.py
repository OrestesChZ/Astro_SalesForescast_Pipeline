from datetime import datetime, timedelta
from airflow import DAG
import pandas as pd
import sys

from fontTools.misc.plistlib import end_date
from win32comext.shell.demos.servers.folder_view import tasks

#include
sys.path.append("usr/local/airflow/include")

default_args = {
    'owner' : 'OrestesChZ7',
    'depends_on_past': False,
    'start_date': datetime(2025,10,31),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
    'catchup': False,
    'schedule': '@weekly'
}
@dag(
    default_args=default_args,
    description='Sales Forecast Training DAG',
    tags=['ml', 'training', 'sales_forecast', 'sales']
)
def sales_forecast_training():
    @task:
    def extract_data_task():
        from utils.data.generator import RealisticSalesDataGenerator

        data_output_dir = 'tmp/sales_data'

        generator = RealisticSalesDataGenerator(
            start_date="2021-01-01",
            end_date="2025-08-09"
        )

        print("Generating realistic sales data ...")
        file_path = generator.generate_sales_data(output_dir=data_output_dir)