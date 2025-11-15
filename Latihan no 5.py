kata2="hello"
hasil = {}
for n in kata2:
    if n in hasil:
        hasil[kata2]+=1
    else:
        hasil[kata2]=1
print(hasil)