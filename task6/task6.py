def task(csvString):
  from io import StringIO
  import csv
  import numpy as np
  import json
  f = StringIO(csvString)
  reader = csv.reader(f, delimiter=',')
  out = []
  for row in reader:
    out.append(row)
  out=np.array(out).T
  def get_table(out, col):
    table=np.zeros(np.array(out).shape)
    for i in range(table.shape[1]):
      for j in range(table.shape[0]):
        if (out[i][col]<out[j][col]):
          table[i,j]=1
        elif (out[i][col]==out[j][col]):
          table[i,j]=0.5
        else:
          table[i,j]=0
    return table
  tables=[]
  for i in range(len(out)):
    tables.append(get_table(out,i))
  X=np.zeros((len(out),len(out)))
  for i in range(len(out)):
    X+=tables[i]
  X=X/len(out)
  k0=np.array([1/len(out)]*len(out))
  eps=0.001
  Y=X.dot(k0)
  lya1=(np.ones(len(out))).dot(Y)
  k1=1/lya1*Y
  while (abs(max(k1-k0))>=eps):
    k0=k1
    Y=X.dot(k0)
    lya1=(np.ones(len(out))).dot(Y)
    k1=1/lya1*Y
  for i in range(len(k1)):
    k1[i]=round(k1[i],3)
  return(json.dumps(k1.tolist()))
