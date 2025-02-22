# Classe que implementa um nó de uma Árvore Binária de Busca.
class No:
    def __init__(self,valor):
        self.valor = valor
        self.filhoEsq = None
        self.filhoDir = None

# Classe que implementa uma ABB (Arvore Binaria de Busca).
class ABB:
    
    # Insere um valor na raiz da árvore.
    def __init__(self,valor):
        self.raiz = No(valor)
                
    # Cria um nó com um valor e o insere na árvore.
    def insere(self,valor):
        if (self.raiz == None):
            self.raiz = No(valor)
            return True
        atual = self.raiz

        while (True):
            
            # Caso o elemento "valor" já esteja na árvore, não o insere e devolve False.
            if (valor == atual.valor):
                print(str(valor) + " ja presente na arvore!")
                return False
            
            # Caso o elemento não esteja na árvore, ele é inserido e devolve True.
            if (valor < atual.valor):
                if (atual.filhoEsq == None):
                    atual.filhoEsq = ABB(valor)
                    return True
                else:
                    atual = atual.filhoEsq.raiz
            else:
                if (atual.filhoDir == None):
                    atual.filhoDir = ABB(valor)
                    return True
                else:
                    atual = atual.filhoDir.raiz
                    
    # Busca "valor" na árvore. Devolve True caso o "valor" seja encontrado; False caso contrário.            
    def busca(self,valor):
        atual = self
        while (atual != None):
            if (valor == atual.raiz.valor):
               return True
            if (valor < atual.raiz.valor):
               atual = atual.raiz.filhoEsq
            else:
               atual = atual.raiz.filhoDir
        return False             



# Função que recebe as entradas, organiza os dados e retorna a saída.
def resultados():
    
    # Entradas do arquivo csv e da quantidade de palavras a serem traduzidas.
    arquivo = input()
    quantidade = int(input())
    
    # Leitura do arquivo csv.
    arq = open(arquivo, "r+")
    
    # Organização do dicionário.
    l = list(arq)
    l1 = [i.replace("\n","") for i in l]
    l1 = [i.split(",") for i in l1]
    
    # Árvore de busca binária para as palavras em português.
    Tp = ABB("p")
    for i in l1:
        Tp.insere(i[0])

    # Árvore de busca binária para as palavras em inglês.
    Ti = ABB("i")
    for i in l1:
        Ti.insere(i[1])

    for i in range(quantidade):
        
        # Entrada das palavras a serem traduzidas.
        entrada = input()
        e = entrada.split()

        # Caso a entrada não informe o idioma, relatamos isso.
        if len(e) != 2:
            print("idioma nao informado")
            
        # Caso a entrada informe o idioma, buscamos a respectiva tradução na ABB adequada.
        else:
            if e[1] == "P":
                if Tp.busca(e[0]) == True:
                    for i in l1:
                        if i[0] == e[0]:
                            print(i[1])
                else:
                    print("traducao nao disponivel")
            if e[1] == "I":
                if Ti.busca(e[0]) == True:
                    for i in l1:
                        if i[1] == e[0]:
                            print(i[0])
                else:
                    print("traducao nao disponivel")        

resultados()

