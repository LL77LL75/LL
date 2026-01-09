list1 = [9, 6, 3, 25, 21, 8, 23, 1, 17, 14]
list2 = [37, 39, 41, 29, 9, 25, 43, 21, 3, 42]
list3 = [24, 8, 10, 22, 45, 34, 28, 39, 3, 32]
list4 = [15, 21, 8, 32, 46, 44, 37, 20, 27, 22]
list5 = [11, 38, 4, 28, 24, 41, 15, 10, 45, 14]
lists = [list1,list2,list3,list4,list5]
for i in lists:
  for a in range(len(i)-1):
      if i[a] > i[a+1]:
        z = i[a]
        i[a] = i[a+1]
        i[a+1] = z
        pass
for i in lists:
   print(i)