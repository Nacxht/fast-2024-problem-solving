barang = {
    "Golok" : 20
}

def tampilBarang():
    ask = input("\n1. Tampilkan dari terbesar\n2. Tampilkan dari terkecil\n\nPilih : ")
    if (ask == "1"):
        data = short(True)
    else:
        data = short(False)
    print("----------------")
    count = 0
    for i in data:
        if (data[i] != 0):
            count += 1
            print(f"{i} | jumlah : {data[i]}")
    if (count == 0):
        print("Barang Kosong")
    print("----------------")
    
def chekAvailabeKeys(keys):
    for i in barang:
        if i == keys:
            return True
    return False

def checkMax(plus = 0):
    size = 0
    for i in barang:
        size += barang[i]
    size += plus
    if (size > 250):
        return False
    else:
        return True
        
def short(bigger):
    res = {}
    data = []
    for i in barang:
        if (data):
            for j in range(len(data)):
                if (bigger):
                    condition = barang[i] > data[j]["val"]
                else:
                    condition = barang[i] < data[j]["val"]    
                if (condition):
                    data.insert(j,{"keys":i,"val":barang[i]})
                elif(j == len(data)-1):
                    data.append({"keys":i,"val":barang[i]})
        else:
            data.append({"keys":i,"val":barang[i]})
    for i in data:
        res.update({
            i["keys"]:i["val"]
        })
    return res
                
                

def tambahBarang():
    nama = input("\nMasukkan nama Barang :")
    jumlah = int(input("Masukkan jumlah Barang : "))
    if (chekAvailabeKeys(nama)):
        barang[nama] = barang[nama] + jumlah
    else :
        if (checkMax(jumlah)):
            barang.update({
                nama : jumlah
            })
        else:
            print("\n::Melebihi batas maksimal (250)::\n")
            
def cariBarang():
    ask = input("\nMasukkan Nama Barang : ")
    this = ""
    for i in barang:
        if (i == ask):
            this = ask
    if (this):
        print(f"({this}) Jumlah : {barang[this]}")
        ask = input("Ingin menghapusnya (y/n)")
        if (ask == "y" or ask == "Y"):
            print(barang[this])
            if (barang[this] > 0):
                barang[this] = 0
            else:
                del barang[this]
    else:
        print("Maaf, Barang tidak tersedia")
    
def distribute():
    ask = input("\nMasukkan Nama Barang : ")
    this = ""
    for i in barang:
        if (i == ask):
            this = ask
    if (ask):
        print(f"Barang : ({this}) => {barang[this]}")
        ask =  int(input("Masukan jumlah distribusi : "))
        if(ask <= barang[this]):
            barang[this] -= ask
        else:
            print("Stock tidak cukup!")
    else:
        print("Barang Tidak Ada!")
    

while True:
    print("---Menu---\n1. Tambah Barang\n2. Tampil Barang\n3. Cari Barang\n4. Distribusi Barang")
    ask = input("Masukkan Perintah : ")
    if (ask == "1"):
        tambahBarang()
    elif(ask == "2"):
        tampilBarang()
    elif(ask == "3"):
        cariBarang()
    elif(ask == "4"):
        distribute()