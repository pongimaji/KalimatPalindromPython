print("## MENENTUKAN KALIMAT PALINDROM ##")
print("(*)kalimat palindrom adalah kalimat yang susunannya sama jika dibalik.")
print()
kalimat=input("Masukkan kalimat : ").lower()
hasil=''
i=len(kalimat)-1
while (i>=0):
	hasil+=kalimat[i]
	i=i-1
if(kalimat==hasil):
	print("Kalimat termasuk Palindrom")
else:
	print("Kalimat tidak termasuk Palindrom")