import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB

w = ['sunny','sunny','overcast','rainy','rainy','rainy','overcast','sunny','sunny','rainy','sunny','overcast','overcast','rainy']
t = ['hot','hot','hot','mild','cool','cool','cool','mild','cool','mild','mild','mild','hot','mild']
p = ['no','no','yes','yes','yes','no','yes','no','yes','yes','yes','yes','yes','no']

le_w, le_t, le_p = LabelEncoder(), LabelEncoder(), LabelEncoder()
X = np.column_stack((le_w.fit_transform(w), le_t.fit_transform(t)))
y = le_p.fit_transform(p)

model = GaussianNB().fit(X, y)
new_example = np.array([[le_w.transform(['sunny'])[0], le_t.transform(['mild'])[0]]])
print("Predicted Play Decision:", "Yes" if model.predict(new_example)[0] else "No")

