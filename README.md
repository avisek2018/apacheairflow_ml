# Creating a ML Pipeline with Apache Airflow
Apache Airflow is an open-source platform for developing, scheduling, and monitoring batch-oriented workflows for data engineering pipelines. It started at Airbnb in October 2014 as a solution to manage the company's increasingly complex workflows. Creating Airflow allowed Airbnb to programmatically author and schedule their workflows and monitor them. The main objective of Apache Airflow is to be a workflow manager. We can schedule individual tasks that we want to run as a part of our processing pipeline and specify dependencies between these tasks, all programmatically in Python and Airflow will automatically just manage these dependencies and make sure that our tasks are executed in the right order. 
Airflow is made up of several different components. The scheduler is what we use to schedule your workflows. Executors run our workflows. The metadata database holds additional information about our workflow and its components. And finally, the webserver is an interactive UI that we can use to manage your workflows. 

![Airflow Architechture](images/Airflow_Arch.jpg?raw=true)


The different components in Airflow come together to give us a nice workflow manager. When we use Apache Airflow, we define all of our workflows as directed-acyclic graphs (DAGs). The nodes in these graphs are the actual tasks that need to be executed. The edges connecting the different task nodes define the dependencies in our workflow. Here is a typical DAG diagram for Airflow –

![Sample DAG](images/Sample_Airflow_Dag.jpg?raw=true)

We'll be running Airflow on our local machine but Airflow works with distributed systems as well such as Apache Spark, Kubernetes, AWS, and other cloud platforms.  Airflow is widely used in data-related tasks such as building, extract, transform, and load pipelines. Here I will show you a specific use case for the machine learning pipeline.

## Install and Run Apache Airflow: 

Please follow this article to install apache airflow in Windows.

[How to Install Apache Airflow on Windows without Docker](https://www.freecodecamp.org/news/install-apache-airflow-on-windows-without-docker/)

An Airflow installation generally consists of the following components[from Airflow Documentation]:
 - A scheduler, which handles both triggering scheduled workflows, and submitting Tasks to the executor to run.
 - An executor, which handles running tasks. In the default Airflow installation, this runs everything inside the scheduler, but most production-suitable executors actually push task execution out to workers.
 - A webserver, which presents a handy user interface to inspect, trigger and debug the behaviour of DAGs and tasks.
 - A folder of DAG files, read by the scheduler and executor 
 - A metadata database, used by the scheduler, executor and webserver to store state.

