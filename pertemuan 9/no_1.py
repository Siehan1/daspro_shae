def Deretfibonacci(n):
    pertama, selanjutnya = 0, 1 
    hasil = 0 
    
    for i in range(n): 
        print(f"Deret ke-{i+1}: {hasil}")
        pertama, selanjutnya = selanjutnya, hasil
        hasil = pertama + selanjutnya
        
inputbilangan = int(input("Masukan jumlah bilangan: "))
Deretfibonacci(inputbilangan)