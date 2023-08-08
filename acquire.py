import os
import pandas as pd
from env import get_connection


def get_titanic_data():
    filename = 'titanic_data.csv'
    
    if os.path.isfile(filename):
        return pd.read_csv(filename)

    else:
        url = get_connection('titanic_db')
        query = '''
        
        SELECT *
        FROM passengers
        ;
        '''

        titanic_data = pd.read_sql(query,url)
        titanic_data.to_csv(filename,index=0)
        return titanic_data

def get_iris_data():
    filename = 'iris_data.csv'

    if os.path.isfile(filename):
        return pd.read_csv(filename)

    else:
        url = get_connection('iris_db')
        query = '''
        
        SELECT *
        FROM measurements
        JOIN species ON measurements.species_id = species.species_id
        ;
        '''

        iris_data = pd.read_sql(query,url)
        iris_data.to_csv(filename,index=0)
        return iris_data

def get_telco_data():
    filename = 'telco_data.csv'

    if os.path.isfile(filename):
        return pd.read_csv(filename)
        
    else:
        url = get_connection('telco_churn')
        query = '''
        
        SELECT *
        FROM customers
        LEFT JOIN contract_types ON customers.contract_type_id = contract_types.contract_type_id
        LEFT JOIN internet_service_types ON customers.internet_service_type_id = internet_service_types.internet_service_type_id
        LEFT JOIN payment_types ON customers.payment_type_id = payment_types.payment_type_id
        ;
        '''

        telco_data = pd.read_sql(query, url)
        telco_data.to_csv(filename,index=0)
        return telco_data