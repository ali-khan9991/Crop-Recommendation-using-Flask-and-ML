import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import *
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import warnings
import pickle
warnings.filterwarnings("ignore")

df = pd.read_csv('Crop_recommendation.csv')
x = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
y = np.array(x)
y = df['label']
y = np.array(y)
X_train,X_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 0)
clf = RandomForestClassifier(n_estimators=230,criterion='entropy',max_depth=6,max_features=1,min_samples_leaf=1).fit(X_train,y_train)
pickle.dump(clf,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))
