import pandas as pd
import matplotlib.pyplot as plt

a=pd.read_csv("1.csv", delimiter=";",
              names=["Ticker", "Per", "Data", "Time", "Open", "High", "Low", "Close", "Vol"])
september21=pd.DataFrame({"sep_open": a["Open"][0:809],
              "sep_close": a["Close"][0:809],
              "sep_max": a["High"][0:809],
              "sep_min": a["Low"][0:809]})
october23=pd.DataFrame({"oct_open": a["Open"][809:1619],
              "oct_close": a["Close"][809:1619],
              "oct_max": a["High"][809:1619],
              "oct_min": a["Low"][809:1619]})
november21=pd.DataFrame({"nov_open": a["Open"][1619:2429],
              "nov_close": a["Close"][1619:2429],
              "nov_max": a["High"][1619:2429],
              "nov_min": a["Low"][1619:2429]})
december03=pd.DataFrame({"dec_open": a["Open"][2429:3239],
              "dec_close": a["Close"][2429:3239],
              "dec_max": a["High"][2429:3239],
              "dec_min": a["Low"][2429:3239]})

dio=pd.concat([september21, october23, november21, december03])

dio.boxplot()
plt.legend(dio, loc=2, ncol=2)
plt.show()