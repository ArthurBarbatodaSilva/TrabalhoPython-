def menu_alunos(dados):
    print("------- Menu -------")
    print("1 => Cadastrar")
    print("2 => Excluir")
    print("3 => Listar")
    print("4 => Editar")
    print("5 => Fechar")
    print("--------------------")

    operacao = int(input("Digite o Comando:"))

    if operacao == 1:
        cadastrar(dados)
    elif operacao == 2:
        excluir_aluno(dados)
    elif operacao == 3:
        listar_aluno(dados)
    elif operacao == 4 :
         editar_aluno(dados)
    elif operacao ==  5:
        fechar = int(input("Voçê realmente quer fechar o programa?|1/sim|2/não|"))
        if fechar == 1:
            print("Programa encerrado")
        else:
            menu_alunos(dados)
    else:
        print("Comando Invalido")
        menu_alunos(dados)


def cadastrar(dados):
    print("\n------- Cadastrar Aluno -------")
    print("\nInsira os dados do aluno abaixo")
    id = input("Id:")
    Nome = input("Nome:")
    idade = int(input("Idade:"))
    cpf = input("CPF:")

    salvar(dados,id,Nome,idade,cpf)
    novo_cadastro =int(input("Você deseja cadastrar um novo aluno?|1/sim|2/não|"))

    if novo_cadastro == 1:
        cadastrar(dados)
    elif novo_cadastro == 2:
        menu_alunos(dados)
    else:
        print("comando invalido")
        menu_alunos(dados)

def listar_aluno(dados):
    for i in dados:
        print(i['id'] + ',' + i['nome'] + ',' + str(i['idade']) + ',' + i['CPF'])

    menu_alunos(dados)

def salvar(dados,id,nome,idade,cpf):
    dados.append({'id':id,'nome':nome,'idade':idade,'CPF':cpf })

def editar_aluno(dados):
    cod =input("Digite o Id do aluno:")

    for i in dados:
        if i['id'] == cod :
            i['nome'] = input("nome:")
            i['idade'] = input("idade:")
            i['CPF'] = input ("cpf:")

    menu_alunos(dados)

def excluir_aluno(dados):
   id = input ("Digite o Id do aluno que deseja excluir:")

   indice = 0
   while indice < len(dados):
    if dados[indice]['id'] == id:
        dados.remove (dados[indice])
        print("O cadastro foi removido")
    indice += 1
    menu_alunos(dados)

if __name__ == '__main__':
    dados =[]
    menu_alunos(dados)
