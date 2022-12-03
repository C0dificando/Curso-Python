retirar = int(input("Cuanto retiras "))

if(retirar > 0 and retirar%100==0): #-,0,1,2,3,4,5.....,99
    print("Sacar dinero")
elif(retirar == 5000 or retirar ==3000):
    print("Ganaste un premio")
else:
    print("Debe ser mayor a 0 y multiplo de 100")

print(not(retirar == 1000))
'''elif(retirar != 9000):
    print("Sacar en caja")
else:
    print("NO paso nada")'''
