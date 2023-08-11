import pandas as pd
import matplotlib.pyplot as plt

def remove_null_values(ti):
    json_data = ti.xcom_pull(task_ids='read_csv_file')
    df = pd.read_json(json_data)    
    df = df.dropna()
    print(df)
    return df.to_json()

def analyze_data(ti):
    json_data = ti.xcom_pull(task_ids='remove_null_values')    
    df = pd.read_json(json_data)
    print(df.describe())
    df.hist(figsize=(20,15))
    plt.savefig('/home/avisek/airflow/outputs/heart_hist.png')

    #Log the count of people affected by heart disease
    not_hv_hd = df[(df['HeartDisease']==0)]
    normal = not_hv_hd.count()[1]
    print("The number of healthy people are: ", normal)

    hv_hd = df[(df['HeartDisease']==1)]
    sick = hv_hd.count()[1]
    print("The number of people sufferring from heart disease are: ", sick)

    #Separate Target and Features
    x=df.iloc[:,:-1]
    y=df.iloc[:,-1]
    #Log the Uniques values for all categorical variables
    obj=x.select_dtypes(include='object')
    count_values = {}
    for col in obj.columns:
        #get the unique values and their counts for the current column
        counts = x[col].value_counts()
        #convert the counts to a dictionary and add it to the main dictionary
        count_values[col] = counts.to_dict()
    #Print the Unique values in Log
    for key, value in count_values.items():
        print(f"{key}:")
        for sub_key, sub_value in value.items():
            print(f"  {sub_key}: {sub_value}")

    return df.to_json()


def feature_engg(ti):
    json_data = ti.xcom_pull(task_ids='analyze_data')
    df = pd.read_json(json_data)    
    #Separate Target and Features
    x=df.iloc[:,:-1]
    y=df.iloc[:,-1]

    #Convert the Categorical Vars to Numeric by One Hot Encoding
    cat_vars = ['Sex',
                'ChestPainType',
                'RestingECG',
                'ExerciseAngina',
                'ST_Slope']

    x = pd.get_dummies(data = x,
                            prefix = cat_vars,
                            columns = cat_vars)
    
    df = pd.concat([x,y], axis=1)
    print(df.head())
    return df.to_json()