import pandas as pd
from sklearn.model_selection import train_test_split
import acquire as ak 

def prep_iris(i):
    a = i
    
    a = a.drop(columns=['species_id','measurement_id'])
    a = a.drop(columns=['species_id.1'])
    a = a.rename(columns ={'species_name':'species'})
    return a 

def prep_titanic():
    
    a = ak.get_titanic_data()
    a = a.drop(columns=['passenger_id','embarked', 'deck', 'class'])
 
    return a 


def prep_telco(i):
    a = i
    a = a.drop(columns=['contract_type_id.1', 'contract_type_id', 'internet_service_type_id.1' , 'payment_type_id.1', 'payment_type_id', 'internet_service_type_id', 'customer_id'])
 
    return a 

def train_val_test(df, strat, seed = 55):
    train, val_test = train_test_split(df, train_size = 0.7,
                                      random_state = seed,
                                      stratify = df[strat])
    val, test = train_test_split(val_test, train_size=0.5,
                                random_state = seed,
                                stratify = val_test[strat])
    return train, val, test


def ret_dum(x):
    x = pd.get_dummies(x)
    return x