import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import tensorflow as tf

def testing(ts):
    add = ts
    for i in range ts:
        pass

def toint(da):
    temp = ""
    for i in range(10):
        if i == 4 or i == 7:
            pass
        else:
            temp += da[i]
    return int(temp)

data = pd.read_csv("data/EA.csv")

#data handeling
op = []
cl  = []
low = []
high = []
close = []
da = []

for i in data:
    op.append(data["Open"].tolist())
   # cl.append(data["Close"].tolist())
    low.append(data["Low"].tolist())
    high.append(data["High"].tolist())


nodate = data["Date"].count()

for i in range(nodate):
    temp = toint(data["Date"][i])
    da.append(temp)
    cl.append(data["Close"][i])

agdate = pd.DataFrame(list(zip(da , cl)) , columns = ["DATE" , "CLOSE"])


#testcase





#basic graph
def basic():
    pass
#dat-close graph

def date_close():
    plt.plot(agdate["DATE"] , agdate["CLOSE"])
    plt.show()


#chart creating


#k-line chart

#20days mean graph
twenty_days_mean = []
for i in range(nodate):



#30 days mean graph

#50 days mmean graph



#candle chart

#volume chart

#testing
print(agdate.iloc[0:10])
