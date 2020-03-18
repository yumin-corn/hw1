import csv 
compare_0 = -999.000
compare_1 = -999.000
compare_2 = -999.000
compare_3 = -999.000
compare_4 = -999.000
min_0 = -999.000
min_1 = -999.000
min_2 = -999.000
min_3 = -999.000
min_4 = -999.000
a0 = 0
a1 = 0
a2 = 0
a3 = 0
a4 = 0
s0 = 0
s1 = 0
s2 = 0
s3 = 0
s4 = 0
i  = 0

# 開啟 CSV 檔案
t = 0
with open('106000130.csv', newline='') as csvfile:

  # 讀取 CSV 檔案內容
  rows = csv.reader(csvfile)
 # cols = sheet1.ncols

  
  for row in rows:
     length = len(row)
     for i in range(length):
        if row[i] == 'WDSD':
          t = i
     
 # print(t)
k=0
with open('106000130.csv', newline='') as csvfile:

  # 讀取 CSV 檔案內容
  rows = csv.reader(csvfile)
  for row in rows:
      #print(7777) 
      if row[0]=='C0A880':
         if row[t] != '-99.000' and row[t] != '-999.000':
            if a0 == 0:
               compare_0 = float(row[t])
               min_0     = float(row[t])
               a0 = 1
            if compare_0 < float(row[t]):
               compare_0 = float(row[t])
            if min_0 > float(row[t]):
               min_0 = float(row[t])
         else:
            s0 = 1
      if row[0]=='C0F9A0':
         if row[t] != '-99.000' and row[t] != '-999.000':
           # print(row[t])
            if a1 == 0:
               compare_1 = float(row[t])
               min_1     = float(row[t])
               a1 = 1
            
            if compare_1<float(row[t]):
               compare_1 = float(row[t])
             #  print(compare_1)
            if min_1 > float(row[t]):
               min_1 = float(row[t])
            #   print(min_1)
         else:
            s1 = 1
  #    print(min_1,compare_1,k)
 #     k=k+1
      if row[0]=='C0G640':
         if row[t] != '-99.000' and row[t] != '-999.000':
            if a2 == 0:
               compare_2 = float(row[t])
               min_2     = float(row[t])
               a2 = 1
            if compare_2 < float(row[t]):
               compare_2 = float(row[t])
            if min_2 > float(row[t]):
               min_2 = float(row[t])
         else:
            s2 = 1
      if row[0]=='C0R190':
         if row[t] != '-99.000' and row[t] != '-999.000':
            if a3 == 0:
               compare_3 = float(row[t])
               min_3     = float(row[t])
               a3 = 1
            if compare_3 < float(row[t]):
               compare_3 = float(row[t])
            if min_3 > float(row[t]):
               min_3 = float(row[t])
         else:
            s3 = 1
      if row[0]=='C0X260':
         if row[t] != '-99.000' and row[t] != '-999.000':
            if a4 == 0:
               compare_4 = float(row[t])
               min_4     = float(row[t])
               a4 = 1
            if compare_4 < float(row[t]):
               compare_4 = float(row[t])
            if min_4 > float(row[t]):
               min_4 = float(row[t])
         else:
            s4 = 1
            
#print(min_1)
#print(compare_1)


if min_0 == -999.000 or compare_0 == -999.000 or s0 == 1:
    compare_0 = 'None'
else :
    compare_0 = compare_0-min_0
ll = [['C0A880',compare_0]]

if min_1 == -999.000 or compare_1 == -999.000 or s1 == 1:
    compare_1 = 'None'
else :
   # print(compare_1)
    compare_1 = compare_1-min_1
   # print(min_1)
if min_2 == -999.000 or compare_2 == -999.000 or s2 == 1:
    compare_2 = 'None'
else :
    compare_2 = compare_2-min_2

if min_3 == -999.000 or compare_3 == -999.000 or s3 == 1:
    compare_3 = 'None'
else :
    compare_3 = compare_3-min_3

if min_4 == -999.000 or compare_4 == -999.000 or s4 == 1:
    compare_4 = 'None'
else :
    compare_4 = compare_4-min_4
    
ll.append(['C0F9A0',compare_1])
ll.append(['C0G640',compare_2])
ll.append(['C0R190',compare_3])
ll.append(['C0X260',compare_4])
print(ll)

