startnumber=int(input("put even start number: "))
endnumber=int(input("put even end number: "))
# if startnumber%2 !=0:
#     print("yeet")
#     startnumber=startnumber+1
for i in range(startnumber,endnumber):
    if i % 2 == 0:
        print(i)