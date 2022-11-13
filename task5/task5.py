def task(dataA,dataB):
  import numpy as np
  def mas(A):
    numb=[]
    for item in A:
      try:    
        numb.append(int(item))
      except:
        mas=[]
        for i in range(len(item)):
          mas.append(int(item[i]))
        numb.append(mas)
    return numb
  def get_table(numb):
    max=0
    for elem in numb:
      try:
        if elem>max:
          max=elem
      except:
        for i in elem:
          if i>max:
            max=i
    table = np.zeros((max,max)) 
    mas=np.zeros(max)
    for item in numb:
      try:
        mas[item-1]=1
        for j in range(max):
          if mas[j]==0:
            table[j,item-1]=0
          else:
            table[j,item-1]=1
      except:
        for elem in item:
          mas[elem-1]=1
        for elem in item:
          for j in range(max):
            if mas[j]==0:
              table[j,elem-1]=0
            else:
              table[j,elem-1]=1
    return table
  def back_string(arg):
    estimated=[]
    for item in arg:
      try:
        estimated.append(str(item+1))
      except:
        mas=[]
        for elem in item:
          mas.append(str(elem+1))
        estimated.append(mas)
    return estimated
  dataA=mas(dataA)
  dataB=mas(dataB)
  tableA=get_table(dataA)
  tableB=get_table(dataB)
  mergedTable=tableA*tableB+tableA.T*tableB.T
  no_diff=[]
  for i in range(mergedTable.shape[0]):
    no_diff.append([])
  for j in range(mergedTable.shape[1]):
    for i in range(mergedTable.shape[0]):
      if (mergedTable[i][j]==0 or mergedTable[i][j]==2) and i!=j:
        no_diff[j].append(i)
  for i in range(len(no_diff)):
    for item in no_diff[i]:
      for j in range(len(no_diff)):
        if item in no_diff[j]:
          if i not in no_diff[j]:
            no_diff[j].append(i)
          if j not in no_diff[i]:
            no_diff[i].append(j)
  colorful=[0]*len(no_diff)
  color=1
  for i in range(len(colorful)):
    if colorful[i]==0:
      if len(no_diff[i])!=0:
        for item in no_diff[i]:
          colorful[item]=color
      else:
        colorful[i]=color      
      color+=1
  diff=[]
  for i in range(1,color):
    diff.append(colorful.index(i))
  tableMult=tableA*tableB
  table_count=[0]*len(diff)
  for j in range(len(diff)):
    for i in range(tableMult.shape[0]):
      table_count[j]+=tableMult[i,diff[j]]
  pairs=[]
  for i in range(len(table_count)):
    pairs.append([table_count[i],diff[i]])
  pairs.sort(key = lambda x:x[0], reverse=False)
  experts=[]
  for item in pairs:
    if len(no_diff[item[1]])!=0:
      experts.append(sorted(no_diff[item[1]]))
    else:
      experts.append(item[1])
  return back_string(experts)
