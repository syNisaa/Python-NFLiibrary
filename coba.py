coba = ["hallo","haii","4",4]

menu = coba[-1]-1
print(menu)
f = open('NFLibrary/buku.txt','w+')
for each_line in f:
    data = each_line.strip()
    if data[:6] == "IND761":
        stok = data[-1]+1
        data[-1] == stok
        f.write(stok+"\n")
    else:
        pass
f.close()