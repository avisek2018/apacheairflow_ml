import pandas as pd
import pickle

from sklearn.model_selection import train_test_split

from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier



def train_dtree(ti):
    json_data = ti.xcom_pull(task_ids='feature_engineering')
    df = pd.read_json(json_data)

    #Separate Target and Features
    x=df.iloc[:,:-1]
    y=df.iloc[:,-1]

    X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.3, random_state=100)

    dt_model = DecisionTreeClassifier(criterion = "entropy", random_state = 100)
    dt_model.fit(X_train, y_train)

    # save the model to disk
    filename = '/home/avisek/airflow/outputs/models/dt_model.sav'
    pickle.dump(dt_model, open(filename, 'wb'))

    #Save the Train Dataset
    train_df = pd.concat([X_train,y_train], axis=1)
    train_df.to_csv('/home/avisek/airflow/outputs/train_df.csv', index=False)

    #Save the Test Dataset
    test_df = pd.concat([X_test,y_test], axis=1)
    test_df.to_csv('/home/avisek/airflow/outputs/test_df.csv', index=False)

    return test_df.to_json()

def train_rfc(ti):
    json_data = ti.xcom_pull(task_ids='feature_engineering')
    df = pd.read_json(json_data)

    #Separate Target and Features
    x=df.iloc[:,:-1]
    y=df.iloc[:,-1]

    X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.3, random_state=100)
    
    # creating a RF classifier
    rfc_model = RandomForestClassifier(n_estimators = 100) 
    rfc_model.fit(X_train, y_train)

    # save the model to disk
    filename = '/home/avisek/airflow/outputs/models/rfc_model.sav'
    pickle.dump(rfc_model, open(filename, 'wb'))

    #Save the Train Dataset
    train_df = pd.concat([X_train,y_train], axis=1)
    train_df.to_csv('/home/avisek/airflow/outputs/train_df.csv', index=False)

    #Save the Test Dataset
    test_df = pd.concat([X_test,y_test], axis=1)
    test_df.to_csv('/home/avisek/airflow/outputs/test_df.csv', index=False)

    return test_df.to_json()