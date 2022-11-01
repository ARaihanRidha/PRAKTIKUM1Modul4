from calendar import c
from pickle import TRUE
from re import A
while (TRUE):

              print("Pilih program")
              print("1.Penjumlahan")
              print("2.Pengurangan")
              print("3.Perkalian")
              print("4.Pembagian")
              print("5.Exit")
              A=float(input("Masukkan Pilihan   :"))
              if A==5:
                break
              elif A>=6:
                print("Input anda salah,silahkan coba lagi")
                continue
              B=float(input("Masukkan nilai pertama  :"))
              C=float(input("Masukkan nilai kedua  :"))
              if A==1:
                W = (B+C)                
                print("Hasil penjumlahan antara",format(B,'.2f'),"dengan",format(C,".2f"),"adalah",format(W,'.2f'))                    
              elif A==2:
                Y = (B-C)                
                print("Hasil pengurangan antara",format(B,'.2f'),"dengan",format(C,".2f"),"adalah",format(Y,'.2f'))                    
              elif A==3:
                Z = (B*C)                
                print("Hasil perkalian antara",format(B,'.2f'),"dengan",format(C,".2f"),"adalah",format(Z,'.2f'))                    
              elif A==4:
                D = (B/C)                
                print("Hasil pembagian antara",format(B,'.2f'),"dengan",format(C,".2f"),"adalah",format(D,'.2f'))      
              
            
               
             
               
               
               

              
                

print("Terimakasih,telah menggunakan kalkulator Akhmad Raihan Ridha")            
              



 
