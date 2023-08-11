import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime, timedelta
from airflow.utils.dates import days_ago

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from read_input_data import read_csv_file
from transform_data import remove_null_values, analyze_data, feature_engg
from model_train import train_dtree, train_rfc
from score_model import test_dtree, test_rfc
#from explain_model import explain_rfc

default_args = {
   'owner': 'avisek'
}

with DAG(
    dag_id = 'python_pipeline',
    description = 'Running a Python pipeline',
    default_args = default_args,
    start_date = days_ago(1),
    schedule_interval = '@once',
    tags = ['python', 'transform', 'pipeline']
) as dag:
    
    read_csv_file = PythonOperator(
        task_id='read_csv_file',
        python_callable=read_csv_file
    )

    remove_null_values = PythonOperator(
        task_id='remove_null_values',
        python_callable=remove_null_values
    )
    
    analyze_data = PythonOperator(
        task_id='analyze_data',
        python_callable=analyze_data
    )

    feature_engineering = PythonOperator(
        task_id='feature_engineering',
        python_callable=feature_engg
    )

    model_training = PythonOperator(
        task_id='model_train',
        #python_callable=train_dtree
        python_callable=train_rfc
    )

    model_scoring= PythonOperator(
        task_id='model_scoring',
        #python_callable=test_dtree
        python_callable=test_rfc
    )

    # model_explain = PythonOperator(
    #     task_id='explain_model',
    #     python_callable=explain_rfc
    # )

read_csv_file >> remove_null_values >> analyze_data >> feature_engineering >> model_training >> model_scoring #>> model_explain


