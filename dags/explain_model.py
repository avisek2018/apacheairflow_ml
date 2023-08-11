import pickle
import shap
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def explain_rfc():
    #Read the test Set
    test_df = pd.read_csv('/home/avisek/airflow/outputs/test_df.csv')
    #Separate Target and Features
    X_test=test_df.iloc[:,:-1]
    y_test=test_df.iloc[:,-1]

    # load the model from disk
    filename = '/home/avisek/airflow/outputs/models/rfc_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))

    #shap.initjs()
    ex = shap.TreeExplainer(loaded_model)
    print(f"Average heart disease probability is {round(np.mean(y_test),4)}")
    shap_values = ex.shap_values(X_test)
    fig = shap.summary_plot(shap_values, X_test, max_display=30, show=False)
    plt.savefig("/home/avisek/airflow/outputs/rfc_shap_summary.png")
