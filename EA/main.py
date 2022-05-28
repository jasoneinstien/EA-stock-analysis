import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

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
    cl.append(data["Close"].tolist())
    low.append(data["Low"].tolist())
    high.append(data["High"].tolist())


nodate = data["Date"].count()

print(nodate)

for i in range(nodate):
    temp = toint(data["Date"][i])
    da.append(temp)

agdata = pd.DataFrame

#chart creating


#k-line chart

#candle chart

#volume chart


#testing
#plt.plot(low , da)
#plt.plot(low , high)
#plt.show()

