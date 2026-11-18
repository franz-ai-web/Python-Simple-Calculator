print("== SIMPLE CALCULATOR ==")

angka1 = float(input("Input The First Number : "))
print("\n1.\tPlus\n2.\tMinus\n3.\tMultiply\n4.\tDivide\n")
opsi = int(input("Input The Option : "))
angka2 = float(input("Input The Second Number : "))

if opsi == 1:
    hasil = angka1 + angka2
elif opsi == 2:
    hasil = angka1 - angka2
elif opsi == 3:
    hasil = angka1 * angka2
elif opsi == 4:
    hasil = angka1 / angka2
else:
    hasil = None

print("Hasilnya adalah :",hasil)