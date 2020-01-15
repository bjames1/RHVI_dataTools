import pandas as pd 

substanceInfo = pd.read_pickle("./substanceInfo.pkl");
# substanceInfo.head()
# substanceInfo.columns
# substanceInfo.index.values.tolist()

dataDict = pd.read_pickle("./dataDict.pkl");
# dataDict.head()
# dataDict.columns
# dataDict.index.values.tolist()
