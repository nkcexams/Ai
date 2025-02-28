import pandas as pd
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination


data=pd.read_csv("ds4.csv")

model=BayesianNetwork([('age','Lifestyle'),('Gender','Lifestyle'),('Family','heartdisease'),
                       ('diet','cholestrol'),('Lifestyle','diet'),('cholestrol','heartdisease')])
model.fit(data,estimator=MaximumLikelihoodEstimator)

evidence = { var: int(input(f'Enter {var}: ')) for var in ['age', 'Gender', 'Family', 'diet', 'Lifestyle', 'cholestrol']}
q = VariableElimination(model).query(variables=['heartdisease'], evidence=evidence)
print(q)



