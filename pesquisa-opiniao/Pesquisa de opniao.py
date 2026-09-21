
excelente = 0
bom = 0
ruim = 0

for i in range(1,11):
    nome= input("qual o seu nome?")
    idade= int(input("qual a sua idade?"))
    opniao= int(input("qual a sua opnião (1: EXCELENTE, 2: BOM e 3: RUIM)"))

    match opniao:
        case 1:
            excelente += 1
        case 2:
            bom += 1
        case 3:
            ruim += 1    
        case _:
            print("Numero não válido, por favor fale novamente!")
        
print(f"valor final de  {excelente}  opniões EXCELENTE")
print(f"valor final de  {bom}  opniões BOM")
print(f"valor final de  {ruim}  opniões RUIM")
