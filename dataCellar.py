import pandas as pd

substanceInfo = pd.read_pickle("./substanceInfo.pkl");
# substanceInfo.head()
# substanceInfo.columns
# substanceInfo.index.values.tolist()

dataDict_N30DAYsubhistYN = pd.read_pickle("./dataDict_N30DAYsubhistYN.pkl");
# dataDict_N30DAYsubhistYN.head()
# dataDict_N30DAYsubhistYN.columns
# dataDict_N30DAYsubhistYN.index.values.tolist()


dataDict_N30DAYsubhistAPD = pd.read_pickle("./dataDict_N30DAYsubhistAPD.pkl");
# dataDict_N30DAYsubhistAPD.head()
# dataDict_N30DAYsubhistAPD.columns
# dataDict_N30DAYsubhistAPD.index.values.tolist()
