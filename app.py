print("Programa Expresso\m")
print("1 Cadastrar Restaurante")
print("2 Listar Restaurante")
print("3 Ativar Restaurante")
print("4 Sair\n")

input("Escolha uma opção")

opcao_digitada =int(input("Escolha uma opção:"))
print("Você selecionou a opção:", opcao_digitada,"\n")

if(opcao_digitada==1):
    print("Você escolheu cadastrar um restaurante\n")
elif(opcao_digitada==2):
    print("Você escolheu listar os restaurantes do app\n")
elif(opcao_digitada==3):
    print("Você escolheu ativar um restaurante\n")
else:
    print("Você escolheu sair do programa\n")