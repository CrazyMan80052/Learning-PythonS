startnumber=int(input("put odd start number: "))
endnumber=int(input("put end number: "))
for i in range(startnumber,endnumber):
    if i % 2 != 0:
        print(i)