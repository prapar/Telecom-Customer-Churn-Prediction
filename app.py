import joblib
from flask import Flask, jsonify, request, redirect, url_for, render_template
import json
import numpy as np
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
import warnings 
warnings.filterwarnings('ignore')
from xgboost import XGBClassifier
import flask
import os
app = Flask(__name__)

app.config["DEBUG"] = True
path = os.getcwd()+'/trained_models'

featureList = ['Customer ID','Age', 'Churn Score', 'CLTV', 'Monthly Charges', 'Number of Referrals', 'Satisfaction Score', 'Tenure in Months', 'Total Revenue', 'Number of Dependents', 'Avg Monthly GB Download', 'Contract', 'Dependents', 'Device Protection', 'Internet Type', 'Married', 'Senior Citizen', 'Multiple Lines', 'Offer', 'Online Backup', 'Online Security', 'Paperless Billing', 'Partner', 'Payment Method', 'Referred a Friend', 'Streaming Movies', 'Streaming Music', 'Streaming TV', 'Tech Support', 'Unlimited Data']

# Retrieve training model information
modelXGB = XGBClassifier()
modelXGB.load_model(path+'/modelXGB.txt')
best_t = joblib.load(path+'/best_t.pkl')    
ohe = joblib.load(path+'/ohe.pkl')
scaler = joblib.load(path+'/scaler.pkl')


@app.route('/')
def index():
    return flask.render_template('home.html')

def uploadFiles():    
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        global file_path
        file_path = os.getcwd()+'/input_files/'+uploaded_file.filename
        uploaded_file.save(file_path)
    return redirect(url_for('index'))

def validateData(data):
    '''
    Validations of the input values.
    '''
    flag = False
    errors = {}
    
    # Values of categorical features.
    val_Contract = ['Month-to-month', 'Two year', 'One year']
    val_Dependents = ['No', 'Yes']
    val_DeviceProtection = ['No internet service','No', 'Yes' ]
    val_InternetType = ['Fiber Optic', 'DSL', 'None', 'Cable' ]
    val_Married = ['No', 'Yes']
    val_SeniorCitizen = ['No', 'Yes']
    val_MultipleLines = ['No', 'Yes', 'No phone service']
    val_Offer = ['None', 'Offer B', 'Offer E', 'Offer D', 'Offer A', 'Offer C']
    val_OnlineBackup = ['No internet service','No', 'Yes' ]
    val_OnlineSecurity = ['No internet service','No', 'Yes' ]
    val_PaperlessBilling = ['No', 'Yes']
    val_Partner = ['No', 'Yes']
    val_PaymentMethod = ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)']
    val_ReferredaFriend = ['No', 'Yes']
    val_StreamingMovies = ['No internet service','No', 'Yes' ]
    val_StreamingMusic = ['No', 'Yes']
    val_StreamingTV = ['No internet service','No', 'Yes' ]
    val_TechSupport = ['No internet service','No', 'Yes' ]
    val_UnlimitedData = ['No', 'Yes']
    
    for index, row in data.iterrows(): 
        
        # Numeric Features
        if str(row['Customer ID'])=='nan':
            flag = True
            errors['CustID: '+str(row['Customer ID'])+' Customer ID'] = [' Must not be empty']

        if row['Age']<0 or row[ 'Age']>120:
            flag = True
            errors['CustID: '+str(row['Customer ID'])+' Age'] = [' Must be a value between 0 and 120']

        if row['Churn Score']<0 or row[ 'Churn Score']>100:
            flag = True
            errors['CustID: '+str(row['Customer ID'])+' Churn Score'] = [' Must be a value between 0 and 100']

        if row['CLTV'] < 0:
            flag = True
            errors['CustID: '+str(row['Customer ID'])+' CLTV'] = [' Must not be a negative value']             

        if row['Monthly Charges'] == '':
            flag = True
            errors['CustID: '+str(row['Customer ID'])+' Monthly Charges'] = [' Must not be empty']

        if row['Number of Referrals'] < 0:
            flag = True
            errors['CustID: '+str(row['Customer ID'])+' Number of Referrals'] = [' Must not be a negative value']  

        if row['Satisfaction Score']<1 or row[ 'Satisfaction Score']>5:
            flag = True
            errors['CustID: '+str(row['Customer ID'])+' Satisfaction Score'] = [' Must be a value between 1 and 5']    

        if row['Tenure in Months'] < 0:
            flag = True
            errors['CustID: '+str(row['Customer ID'])+' Tenure in Months'] = [' Must not be a negative value']  

        if row['Total Revenue'] == '':
            flag = True
            errors['CustID: '+str(row['Customer ID'])+' Total Revenue'] = [' Must not be empty']

        if row['Number of Dependents'] < 0:
            flag = True
            errors['CustID: '+str(row['Customer ID'])+' Number of Dependents'] = [' Must not be a negative value'] 

        if row['Avg Monthly GB Download'] < 0:
            flag = True
            errors['CustID: '+str(row['Customer ID'])+' Avg Monthly GB Download'] = [' Must not be a negative value']

            # Categorical Features

        if row['Contract'] not in val_Contract:
            flag = True
            errors['CustID: '+str(row['Customer ID'])+' Contract'] = [' Choose from: '+str(val_Contract)]

        if row['Dependents'] not in val_Dependents:
            flag = True
            errors['CustID: '+str(row['Customer ID'])+' Dependents'] = [' Choose from: '+str(val_Dependents)]

        if row['Device Protection'] not in val_DeviceProtection:
            flag = True
            errors['CustID: '+str(row['Customer ID'])+' Device Protection'] = [' Choose from: '+str(val_DeviceProtection)]

        if row['Internet Type'] not in val_InternetType:
            flag = True
            errors['CustID: '+str(row['Customer ID'])+' Internet Type'] = [' Choose from: '+str(val_InternetType)]

        if row['Married'] not in val_Married:
            flag = True
            errors['CustID: '+str(row['Customer ID'])+' Married'] = [' Choose from: '+str(val_Married)]

        if row['Senior Citizen'] not in val_SeniorCitizen:
            flag = True
            errors['CustID: '+str(row['Customer ID'])+' Senior Citizen'] = [' Choose from: '+str(val_SeniorCitizen)]

        if row['Multiple Lines'] not in val_MultipleLines:
            flag = True
            errors['CustID: '+str(row['Customer ID'])+' Multiple Lines'] = [' Choose from: '+str(val_MultipleLines)]

        if row['Offer'] not in val_Offer:
            flag = True
            errors['CustID: '+str(row['Customer ID'])+' Offer'] = [' Choose from: '+str(val_Offer)]

        if row['Online Backup'] not in val_OnlineBackup:
            flag = True
            errors['CustID: '+str(row['Customer ID'])+' Online Backup'] = [' Choose from: '+str(val_OnlineBackup)]

        if row['Online Security'] not in val_OnlineSecurity:
            flag = True
            errors['CustID: '+str(row['Customer ID'])+' Online Security'] = [' Choose from: '+str(val_OnlineSecurity)]

        if row['Paperless Billing'] not in val_PaperlessBilling:
            flag = True
            errors['CustID: '+str(row['Customer ID'])+' Paperless Billing'] = [' Choose from: '+str(val_PaperlessBilling)]

        if row['Partner'] not in val_Partner:
            flag = True
            errors['CustID: '+str(row['Customer ID'])+' Partner'] = [' Choose from: '+str(val_Partner)]

        if row['Payment Method'] not in val_PaymentMethod:
            flag = True
            errors['CustID: '+str(row['Customer ID'])+' Payment Method'] = [' Choose from: '+str(val_PaymentMethod)]

        if row['Referred a Friend'] not in val_ReferredaFriend:
            flag = True
            errors['CustID: '+str(row['Customer ID'])+' Referred a Friend'] = [' Choose from: '+str(val_ReferredaFriend)]

        if row['Streaming Movies'] not in val_StreamingMovies:
            flag = True
            errors['CustID: '+str(row['Customer ID'])+' Streaming Movies'] = [' Choose from: '+str(val_StreamingMovies)]

        if row['Streaming Music'] not in val_StreamingMusic:
            flag = True
            errors['CustID: '+str(row['Customer ID'])+' Streaming Music'] = [' Choose from: '+str(val_StreamingMusic)]

        if row['Streaming TV'] not in val_StreamingTV:
            flag = True
            errors['CustID: '+str(row['Customer ID'])+' Streaming TV'] = [' Choose from: '+str(val_StreamingTV)]

        if row['Tech Support'] not in val_TechSupport:
            flag = True
            errors['CustID: '+str(row['Customer ID'])+' Tech Support'] = [' Choose from: '+str(val_TechSupport)]

        if row['Unlimited Data'] not in val_UnlimitedData:
            flag = True
            errors['CustID: '+str(row['Customer ID'])+' Unlimited Data'] = [' Choose from: '+str(val_UnlimitedData)]

        if row['Zip Code'] == '':
            flag = True
            errors['CustID: '+str(row['Customer ID'])+' Zip Code'] = [' Must not be empty']

        if row['City'] == '':
            flag = True
            errors['CustID: '+str(row['Customer ID'])+' City'] = [' Must not be empty']
    return flag, errors

def getData(data):  
    
    df = data[featureList] # Extract features the model was trained with.
        
    # Read Zip and City - churn and stay rates from training.
    feature_dictionary_city = joblib.load(path+'/feature_dictionary_city.pkl')
    feature_dictionary_zip = joblib.load(path+'/feature_dictionary_zip.pkl')    
    
    # Engineered Features
    df['Electronic Check'] = data['Payment Method'].apply(lambda x : 'Yes' if x=='Electronic check' else 'No')
    df['Joined'] = data['Customer Status'].apply(lambda x : 'Yes' if x=='Joined' else 'No')
    df['Under65'] = data['Age'].apply(lambda x: 'Yes' if x<65 else 'No')
    df['MonthlyRevenue'] = data['Total Revenue']/data['Tenure in Months']
    df['ZipChurnRate'] =data['Zip Code'].apply(lambda x:0.5 if x not in (feature_dictionary_zip.keys()) else feature_dictionary_zip[x][1])
    df['ZipStayRate'] = data['Zip Code'].apply(lambda x:0.5 if x not in (feature_dictionary_zip.keys()) else feature_dictionary_zip[x][0])
    df['CityChurnRate'] = data['City'].apply(lambda x:0.5 if x not in (feature_dictionary_city.keys()) else feature_dictionary_city[x][1])
    df['CityStayRate'] = data['City'].apply(lambda x:0.5 if x not in (feature_dictionary_city.keys()) else feature_dictionary_city[x][0])   

    df.to_excel(os.getcwd()+'/output_files/df.xlsx',index=False)
    return df


@app.route('/', methods=['POST'])
def predict():
    
    uploadFiles()
    data = pd.read_csv(file_path)
    
    # Data Validation
    flag, errors = validateData(data)
    if(flag):
        return jsonify(errors)
    df = getData(data)

    result = pd.DataFrame(data = df['Customer ID'], columns = ['Customer ID'])
    df.drop(columns = 'Customer ID', axis = 1, inplace=True)        
    objLst = list(df.select_dtypes(include=['object']).columns.sort_values())
    numLst = list(df.select_dtypes(exclude=['object']).columns.sort_values())
    
    Xq_ohe = ohe.transform(df[objLst])
    Xq_cat = pd.DataFrame(Xq_ohe,columns=ohe.get_feature_names_out(objLst))
    
    Xq_scale = scaler.transform(df[numLst])
    Xq_num = pd.DataFrame(Xq_scale,columns=scaler.get_feature_names_out((numLst)))

    # Concat all features.
    Xq = pd.concat([Xq_cat,Xq_num], axis=1)
  
    predictionList = []
    prob = modelXGB.predict_proba(Xq)[:,1]
        
    for i in prob:
        if i>=best_t:
            # Probability >= best threshold
            predictionList.append('Yes') #1
        else:
            predictionList.append('No') #0
            
    result['Churn Risk'] = predictionList
    result.index += 1
    
    result.to_excel(os.getcwd()+'/output_files/result.xlsx',index=False)
    return render_template('results.html', tables = [result.to_html(header=True)], titles=[''])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)