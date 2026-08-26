import os ,time

while True:
     senha = input("Cadastre a senha: ")
     if(len(senha) ==4 and senha.isdigit()):
          print("senha cadastrada com sucesso")
          break
     else:
          print("senha invalida")
          time.sleep(3)  
          os.system("cls ar clear")