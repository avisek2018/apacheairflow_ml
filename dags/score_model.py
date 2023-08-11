import pandas as pd
import pickle
import json

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score


def test_dtree(ti):
    #Get the test Set
    json_data = ti.xcom_pull(task_ids='model_train')
    test_df = pd.read_json(json_data)
    #Separate Target and Features
    X_test=test_df.iloc[:,:-1]
    y_test=test_df.iloc[:,-1]

    #Read the training Set
    train_df = pd.read_csv('/home/avisek/airflow/outputs/train_df.csv')
    #Separate Target and Features
    X_train=train_df.iloc[:,:-1]
    y_train=train_df.iloc[:,-1]

    # load the model from disk
    filename = '/home/avisek/airflow/outputs/models/dt_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    y_pred = loaded_model.predict(X_test)
    print("Predicted Values:")
    print(y_pred)

    print("Confusion Matrix: ",
        confusion_matrix(y_test, y_pred))
      
    print ("Accuracy : ",
    accuracy_score(y_test,y_pred)*100)

    print('F1 score:', f1_score(y_test, y_pred, average='weighted'))
    print('Recall:', recall_score(y_test, y_pred, average='weighted'))
    print('Precision:', precision_score(y_test, y_pred, average='weighted'))
      
    print("Report : ",
    classification_report(y_test, y_pred))

    performance  = {}
    keys={'Confusion Matrix', 'Accuracy'}
    values = [confusion_matrix(y_test, y_pred), accuracy_score(y_test,y_pred) ]
    for i in keys:
        for x in values:
            performance[i] = x

    return json.dumps(performance)

def test_rfc(ti):
    #Get the test Set
    json_data = ti.xcom_pull(task_ids='model_train')
    test_df = pd.read_json(json_data)
    #Separate Target and Features
    X_test=test_df.iloc[:,:-1]
    y_test=test_df.iloc[:,-1]

    #Read the training Set
    train_df = pd.read_csv('/home/avisek/airflow/outputs/train_df.csv')
    #Separate Target and Features
    X_train=train_df.iloc[:,:-1]
    y_train=train_df.iloc[:,-1]

    # load the model from disk
    filename = '/home/avisek/airflow/outputs/models/rfc_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    y_pred = loaded_model.predict(X_test)
    print("Predicted Values:")
    print(y_pred)

    print("Confusion Matrix: ",
        confusion_matrix(y_test, y_pred))
      
    print ("Accuracy : ",
    accuracy_score(y_test,y_pred)*100)

    print('F1 score:', f1_score(y_test, y_pred, average='weighted'))
    print('Recall:', recall_score(y_test, y_pred, average='weighted'))
    print('Precision:', precision_score(y_test, y_pred, average='weighted'))
      
    print("Report : ",
    classification_report(y_test, y_pred))

    performance  = {}
    keys={'Confusion Matrix', 'Accuracy'}
    values = [confusion_matrix(y_test, y_pred), accuracy_score(y_test,y_pred) ]
    for i in keys:
        for x in values:
            performance[i] = x

    return json.dumps(performance)