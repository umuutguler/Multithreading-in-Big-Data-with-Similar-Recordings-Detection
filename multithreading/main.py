import csv
import time
import pandas as pd
import threading, queue
from TextComparison import Comparison
from Screen import Sc

baslangic_zamani = time.time()

df = pd.read_csv('rows.csv', engine='python')
data = df.head()

#Delete unwanted column
"""df.drop('Date received', axis=1, inplace=True)
df.drop('Sub-product', axis=1, inplace=True)
df.drop('Tags', axis=1, inplace=True)
df.drop('Sub-issue', axis=1, inplace=True)
df.drop('Consumer complaint narrative', axis=1, inplace=True)
df.drop('Company public response', axis=1, inplace=True)
df.drop('Consumer consent provided?', axis=1, inplace=True)
df.drop('Timely response?', axis=1, inplace=True)
df.drop('Company response to consumer', axis=1, inplace=True)
df.drop('Date sent to company', axis=1, inplace=True)
df.drop('Submitted via', axis=1, inplace=True)
df.drop('Consumer disputed?', axis=1, inplace=True)
df.to_csv("rows_2.csv")"""

i = 0
queue_ = queue.Queue()
queue_2 = queue.Queue()
product_list = []
issue_list = []
company_list = []
state_list = []
zip_list = []
complaintid_list = []

a = 0
with open("rows_2.csv") as dosyam:
    okuyucu = csv.reader(dosyam)
    for satir in okuyucu:
        product_list.insert(i, satir[1])
        issue_list.insert(i, satir[2])
        company_list.insert(i, satir[3])
        state_list.insert(i, satir[4])
        zip_list.insert(i, satir[5])
        complaintid_list.insert(i, satir[6])
        i += 1
        if i ==  100:
            break

product_list.pop(0)


for i in product_list:
    queue_.put(i)
    queue_2.put(i)

for i in issue_list:
    queue_.put(i)
    queue_2.put(i)

for i in company_list:
    queue_.put(i)
    queue_2.put(i)

for i in state_list:
    queue_.put(i)
    queue_2.put(i)

for i in zip_list:
    queue_.put(i)
    queue_2.put(i)

for i in complaintid_list:
    queue_.put(i)
    queue_2.put(i)

sonuc_benzerlik = []

def islem(threadName, queue_, queue_2):
    while not queue_.empty():
        item = queue_.get()
        while not queue_2.empty():
            item2 = queue_2.get()

            benzerlik_orani = Comparison.comparison(item, item2)
            sonuc_benzerlik.append(benzerlik_orani)

            queue_2.task_done()

        queue_.task_done()

for i in range(1):
    worker = threading.Thread(target=islem, args=(f"Thread-{i}", queue_, queue_2), daemon=True)
    worker.start()

queue_.join()
queue_2.join()
print("--- %s saniye ---" % (time.time() - baslangic_zamani))

Sc.sc(sonuc_benzerlik)



