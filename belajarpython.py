#for letter in "python":
    #print(letter)

#n = 4
#i = "halo"
#while i != "selesai":
    #i = input("isi selsai kalau udah selesai:")

#mylist = [1,2,3] 
#mytuple = (4, 5, 6) #tupple tdiak bisa diubah (tambah)
#myset = {7, 8, 9}
#print(mylist[0])
#print(mytuple[1])
#print(7 in myset)

#mylist.append(0)
#mylist.insert(1, "tada")
#print(mylist)
#myset.add(11)
#print(myset)

data = (10, [20, 30, 40], 60)
print(type(data))
data[1][1]=300
data[1].append(60)
print(data)