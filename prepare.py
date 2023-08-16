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


# Splits data into train test val
# strat should be my target variable in quotatoin marks
def train_val_test(df, strat, seed = 55):
    train, val_test = train_test_split(df, train_size = 0.7,
                                      random_state = seed,
                                      stratify = df[strat])
    val, test = train_test_split(val_test, train_size=0.5,
                                random_state = seed,
                                stratify = val_test[strat])
    return train, val, test


# Get dummy where x is dataframe 
def ret_dum(x):
    x = pd.get_dummies(x)
    return x


def theometrics(TP, TN, FP, FN):
    accuracy = (TP + TN) / (TP + TN + FP + FN)
    recall = TP / (TP + FN)
    true_positive_rate = TP / (TP + FN)
    false_positive_rate = FP / (FP + TN)
    true_negative_rate = TN / (TN + FP)
    false_negative_rate = FN / (FN + TP)
    precision = TP / (TP + FP)
    f1_score = 2 * (precision * recall) / (precision + recall)
    support = TP + FN
    data = {
        'Metric': ['Accuracy', 'Recall', 'True Positive Rate', 'False Positive Rate', 'True Negative Rate', 'False Negative Rate', 'Precision', 'F1-Score', 'Support'],
        'Value': [accuracy, recall, true_positive_rate, false_positive_rate, true_negative_rate, false_negative_rate, precision, f1_score, support]
    }
    theometrics = pd.DataFrame(data)
    return theometrics


def cm_funk(y_train,y_train_pred):
    cm = confusion_matrix(y_train, y_train_pred)
    tn, fp, fn, tp = cm.ravel()

    accuracy = (tp + tn)/(tn + fp + fn + tp)

    true_positive_rate = tp/(tp + fn)
    false_positive_rate = fp/(fp + tn)
    true_negative_rate = tn/(tn + fp)
    false_negative_rate = fn/(fn + tp)

    precision = tp/(tp + fp)
    recall = tp/(tp + fn)
    f1_score = 2*(precision*recall)/(precision+recall)

    support_pos = tp + fn
    support_neg = fp + tn

    output = {
    'metric' : ['accuracy', 'true_positive_rate', 'false_positive_rate', 'true_negative_rate', 'false_negative_rate', 'precision', 'recall', 'f1_score', 'support_pos', 'support_neg']
    ,'score' : [accuracy, true_positive_rate, false_positive_rate, true_negative_rate, false_negative_rate, precision, recall, f1_score, support_pos, support_neg]
}

    return pd.DataFrame(output)