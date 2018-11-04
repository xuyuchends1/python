import pandas as pd
from sklearn import linear_model

def linearModel(data):
    features=['x']
    label=['y']
    trainData=data[:15]
    testData=data[15:]
    model=trainModel(features,label)


def trainModel(trainData,features,label):
    model=linear_model.LinearRegression()
    model.fit(trainData[features],trainData[label])
    return model

data=pd.read_csv("JingTongShuJuKeXue/4/4.2.1.csv")

mdoel=linearModel(data)
pass