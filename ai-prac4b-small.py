import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix


df=pd.read_csv('diabetes.csv')
print(df.head())

X=df.drop('Outcome',axis=1)
y=df['Outcome']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)

clf=DecisionTreeClassifier(random_state=42)
clf.fit(X_train,y_train)

y_pred=clf.predict(X_test)

accuracy = accuracy_score(y_test,y_pred)
print(f"accuracy:{accuracy*100:.2f}%")

print("\nclassification report:")
print(classification_report(y_test,y_pred))
print("\n confusion matrix:")
print(confusion_matrix(y_test,y_pred))

plt.figure(figsize=(200,80))
plot_tree(clf,feature_names=X.columns,class_names=["No Diabetes","Diabetes"])
plt.title("Decision tree classifier")
plt.show()





