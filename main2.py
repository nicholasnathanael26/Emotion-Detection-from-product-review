import text2emotion as te
import pandas as pd
from matplotlib import pyplot as plt

#mengambil data dari excel yang kami buat
base = pd.read_csv("D:/INFORMATIKA/semester 5/AI/TUBES/test/TUGAS_AI.csv")
base.head()

#mengeluarkan hasil yang ada di kolom review di dalam excel
dpyears = base.Review
list = dpyears.head(100)

banyakData = int(input("masukkan banyak data yang akan dicari: "))

#perulangan untuk mengeluarkan data review
for i in range(banyakData):
    text = list[i]
    #Call to the function
    res=te.get_emotion(text)
    persen = te.get_percent_emotion(text)
    print (persen)

# data=list()
# text = input('Masukkan Review : ')
# res = te.get_emotion(text)
# persen = te.get_percent_emotion(text)
#
# for k,v in res.items():
#     data.append(v)
#
# print(persen)
# emotions = ['HAPPY','ANGRY','SUPRISE','SAD','FEAR']
#
# fig = plt.figure(figsize=(10,7))
# plt.pie(data, labels=emotions, normalize=False)
# plt.show()