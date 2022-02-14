from typing import Any
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base
import pandas as pd
import os


# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'randomized_chart_data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
Chart_Data = db.Table('Chart_Data',db.metadata, autoload=True, autoload_with=db.engine)
Observation_Type = db.Table('Observation_Type', db.metadata, autoload=True, autoload_with=db.engine)
Result_Status = db.Table('Result_Status', db.metadata, autoload=True, autoload_with=db.engine)
Unit_Of_Measure = db.Table('Unit_Of_Measure', db.metadata, autoload=True, autoload_with=db.engine)
id=1;

@app.route('/chartdata', methods=['GET'])
def get_chartdata():

#@app.route('/')
#def index():
  results = db.session.query(Chart_Data) 
  results1 =db.session.query(Observation_Type)
  results2=db.session.query(Result_Status)
  results3=db.session.query(Unit_Of_Measure)
  df1=pd.DataFrame(results)
  df2=pd.DataFrame(results1)
  df2.rename(columns={'Id': 'Observation_Type_Id', 'Name': 'Observation_Type_Name'}, inplace=True)
  df3=pd.DataFrame(results2)
  df3.rename(columns={'Id': 'Result_Status_Id', 'Name': 'Result_Status_Name'}, inplace=True)
  
  df4=pd.DataFrame(results3)
  df4.rename(columns={'Id': 'Unit_Of_Measure_Id', 'Name': 'Unit_Of_Measure_Name'}, inplace=True)
  #print(df2.head())
  result =  pd.merge(df1, df2, how="outer", on=["Observation_Type_Id"])
  result1 =  pd.merge(result, df3, how="outer", on=["Result_Status_Id"])
  result2 =  pd.merge(result1, df4, how="outer", on=["Unit_Of_Measure_Id"])
  result3 = result2[['Id','CHARTTIME','VALUENUM','ERROR','WARNING','STOPPED','Observation_Type_Name','Result_Status_Name','Unit_Of_Measure_Name']]
  #df_filtered = result3[result3.Id == 3]
 # print(result3.to_json(orient='table'))
  #print(df4.head())

  return result3.to_json(orient='index') 

@app.route('/chartdata/<id>', methods=['GET'])
def get_product(id):
  results = db.session.query(Chart_Data)
  results1 =db.session.query(Observation_Type)
  results2=db.session.query(Result_Status)
  results3=db.session.query(Unit_Of_Measure)
  df1=pd.DataFrame(results)
  df2=pd.DataFrame(results1)
  df2.rename(columns={'Id': 'Observation_Type_Id', 'Name': 'Observation_Type_Name'}, inplace=True)
  df3=pd.DataFrame(results2)
  df3.rename(columns={'Id': 'Result_Status_Id', 'Name': 'Result_Status_Name'}, inplace=True)
  
  df4=pd.DataFrame(results3)
  df4.rename(columns={'Id': 'Unit_Of_Measure_Id', 'Name': 'Unit_Of_Measure_Name'}, inplace=True)
  #print(df2.head())
  result =  pd.merge(df1, df2, how="outer", on=["Observation_Type_Id"])
  result1 =  pd.merge(result, df3, how="outer", on=["Result_Status_Id"])
  result2 =  pd.merge(result1, df4, how="outer", on=["Unit_Of_Measure_Id"])
  result3 = result2[['Id','CHARTTIME','VALUENUM','ERROR','WARNING','STOPPED','Observation_Type_Name','Result_Status_Name','Unit_Of_Measure_Name']]
  df_filtered = result3[result3.Id == 3]
 # print(result3.to_json(orient='table'))
  #print(df4.head())

  return df_filtered.to_json(orient='index') 
  #id=int(id)
  #results = db.session.query(Chart_Data,Observation_Type,Result_Status,Unit_Of_Measure).filter(Chart_Data.c.Observation_Type_Id == Observation_Type.c.Id).filter(Chart_Data.c.Result_Status_Id == Result_Status.c.Id).filter(Chart_Data.c.Unit_Of_Measure_Id == Unit_Of_Measure.c.Id)
  
  #df1=pd.DataFrame(results)
  #df_filtered = df1[df1.Id == id]
  #df2 = df1.query('Id==id')
  #DF2= df1[df1.Id == id]
  #id1=df1[['Observation_Type_Id']]
  #id1=id1['Observation_Type_Id'].iloc[0]
  #results1 =db.session.query(Observation_Type).filter_by(Id = id1)
  #df2=pd.DataFrame(results1)
  #id2=df1[['Result_Status_Id']]
  #results2=db.session.query(Result_Status)
 # results3=db.session.query(Unit_Of_Measure)
  #df2=pd.DataFrame(results1)
  #df2.rename(columns={'Id': 'Observation_Type_Id', 'Name': 'Observation_Type_Name'}, inplace=True)
  #df3=pd.DataFrame(results2)
  #df3.rename(columns={'Id': 'Result_Status_Id', 'Name': 'Result_Status_Name'}, inplace=True)
  
  #df4=pd.DataFrame(results3)
  #df4.rename(columns={'Id': 'Unit_Of_Measure_Id', 'Name': 'Unit_Of_Measure_Name'}, inplace=True)
  #print(df2.head())
  #result =  pd.merge(df1, df2, how="outer", on=["Observation_Type_Id"])
  #result1 =  pd.merge(result, df3, how="outer", on=["Result_Status_Id"])
  #result2 =  pd.merge(result1, df4, how="outer", on=["Unit_Of_Measure_Id"])
  #result3 = result2[['Id','CHARTTIME','VALUENUM','ERROR','WARNING','STOPPED','Observation_Type_Name','Result_Status_Name','Unit_Of_Measure_Name']]
  #print(results)
  #print(id1)
  #print(results1)
  #print(id2['Result_Status_Id'])
  #print(results)
  #print(DF2)
  #print(df1.head())
  #print(df_filtered.head())
  #rslt_df = result3[result3['Id']==id] 
  #print(rslt_df)
  #return ''
  #onify(product)



# Run Server
if __name__ == '__main__':
  app.run(debug=True)