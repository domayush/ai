import numpy as np
import pandas as pd
import csv 
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination

heartDisease = pd.read_csv('heart.csv')
heartDisease = heartDisease.replace('?',np.nan)

print('Sample instances from the dataset are given below\n')
print(heartDisease.head())

print('\n--------------------------------------------------------------------------------\n')



print('\nAttributes and datatypes\n')
print(heartDisease.dtypes)

print('\n--------------------------------------------------------------------------------\n')

model= BayesianNetwork([('age','heartdisease'),('gender','heartdisease'),('exang','heartdisease'),('cp','heartdisease'),('heartdisease','restecg'),('heartdisease','chol')])
print('\nLearning CPD(conditional probability distribution) using Maximum likelihood estimators')
model.fit(heartDisease,estimator=MaximumLikelihoodEstimator)

print('\nInferencing with Bayesian Network:')
HeartDiseasetest_infer = VariableElimination(model)

print('\n 1. Probability of HeartDisease given evidence :-  gender ')
print(model.get_cpds('gender'))


print('\n--------------------------------------------------------------------------------\n')

print('\n 2. Probability of HeartDisease given evidence :-  cp ')
q2=HeartDiseasetest_infer.query(variables=['heartdisease'],evidence={'cp':2})
print(q2)

print('--------------------------------------------------------------------------------')

print('\n 3. Probability of HeartDisease given evidence :- restecg')
q1=HeartDiseasetest_infer.query(variables=['heartdisease'],evidence={'restecg':0})
print(q1)

