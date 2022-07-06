from asyncio import gather
from time import sleep
from unicodedata import name
import numpy as np
import sys

#Classe que representa um vértice na lista de adjacência
class Vertice(object):

    #Ele guarda o seu índice, quantos vértices são adjacentes a ele,
    #e um dicionário que guarda os pesos das arestas incidentes
    def __init__(self, valor):
        self.indice = valor
        self.adjacentes = 0
        self.vizinhos = {}

    #Função que adiciona um vizinho ao vértice
    #Ela insere o peso da aresta na posição de índice "vizinho" do dicionário
    def add_vizinho(self, vizinho, peso):
        self.vizinhos[vizinho] = peso
        self.adjacentes += 1

    #Função que remove um vizinho do vértice
    def remove_vizinho(self, vizinho):
        del self.vizinhos[vizinho]
        self.adjacentes -= 1

    #Função que imprime a lista de adjacência do vértice
    def __str__(self):
        text = []
        for x in self.vizinhos:
            text.append('{} -> {} com peso: {}'.format(self.indice, x.indice, self.vizinhos[x]))
            text.append(', ')
        text = text[:-1]
        return ''.join(text)

    #Função que retorna o dicionário contendo os vizinhos
    #do vértice e o peso das arestas até eles
    def get_vizinhos(self):
        return self.vizinhos

    #Função que retorna os outros vértices que estão conectados ao vértice
    def get_coneccoes(self):
        return self.vizinhos.keys()

    #Função que retorna o peso de uma aresta até outro vértice
    def get_peso(self, vizinho):
        return self.vizinhos[vizinho]

#Classe que representa um grafo
class Grafo(object):

    #Ele guarda o seu nome, quantos vértices e quantas arestas o grafo possui,
    #e a lista e a matriz de adjacência do grafo
    #Ele adiciona 1 vértice no grafo ao ser criado
    def __init__(self, nome_Grafo):
        self.nome = nome_Grafo
        self.vertice = 0
        self.aresta = 0
        self.vertices = {}
        self.matrizVertices = []
        self.AddVertice(Vertice(1))

    #Função que verifica se o grafo existe
    def existe(self):
        try:
            self.nome
            return True
        except:
            print('Grafo não existe')

    #Função que adiciona um vértice com índice "vertice" ao grafo
    def AddVertice(self, vertice):
        if self.existe():
            self.vertices[vertice.indice] = vertice
            self.vertice += 1

    #Função que retorna um vértice com índice "indice" do grafo
    def get_vertice(self, indice):
        if self.existe():
            try:
                return self.vertices[indice]
            except KeyError:
                return None

    #Função que imprime a lista de adjacência do grafo
    def Grafo(self):
        if self.existe():
            for v in self:
                print('Vértice {}'.format(v.indice), end="")
                for w in v.get_coneccoes():
                    print(' -Peso {}-> Vértice {}'.format(v.get_peso(self.get_vertice(w.indice)), w.indice), end="")
                print('')

    #Função que retorna se o vértice de índice "indice" pertence ao Grafo
    def EVertice(self, indice):
        if self.existe():
            if self.get_vertice(indice) is not None:
                print('Vértice {} pertece ao Grafo {}'.format(indice, self.nome))
            else:
                print('Vértice {} não pertece ao Grafo {}'.format(indice, self.nome))

    def __contains__(self, indice):
        if self.existe():
            return indice in self.vertices

    #Função que adiciona uma aresta de peso "peso" saindo do vértice de índice
    #"indice_saida" e chegando ao vértice de índice "indice_chegada"
    def AddAresta(self, indice_saida, indice_chegada, peso):
        if self.existe():
            if indice_saida not in self.vertices or indice_chegada not in self.vertices:
                print('Um ou mais vértices não existem!')
                return 0
            self.vertices[indice_saida].add_vizinho(self.vertices[indice_chegada], peso)
            self.aresta += 1
    
    #Função que remove uma aresta de peso "peso" saindo do vértice de índice
    #"indice_saida" e chegando ao vértice de índice "indice_chegada",
    #se esta aresta existir
    def RemoveAresta(self, indice_saida, indice_chegada, peso):
        if self.existe():
            if indice_saida not in self.vertices or indice_chegada not in self.vertices:
                print('Um ou mais vértices não existem!')
                return 0
            if self.vertices[indice_saida].get_peso(self.vertices[indice_chegada]) != peso:
                print('Não existe aresta com peso {} do vértice {} para o vértice {}'.format(peso, indice_saida, indice_chegada))
                return 0
            self.vertices[indice_saida].remove_vizinho(self.vertices[indice_chegada])
            self.aresta -= 1
            print('Aresta removida com sucesso')
    
    #Função que retorna se existe uma aresta de peso "peso" saindo do vértice de
    #índice "indice_saida" e chegando ao vértice de índice "indice_chegada",
    def ExisteAresta(self, indice_saida, indice_chegada, peso):
        if self.existe():
            if indice_saida not in self.vertices or indice_chegada not in self.vertices:
                print('Um ou mais vértices não existem!')
                return 0
            if self.vertices[indice_saida].get_peso(self.vertices[indice_chegada]) != peso:
                print('Não existe aresta com peso {} do vértice {} para o vértice {}'.format(peso, indice_saida, indice_chegada))
                return 0
            print('Existe aresta com peso {} do vértice {} para o vértice {}'.format(peso, indice_saida, indice_chegada))

    #Função que muda o peso de uma aresta de peso "peso" para "novo_peso", saindo do vértice de índice
    #"indice_saida" e chegando ao vértice de índice "indice_chegada", se esta aresta existir
    def MudaPeso(self, indice_saida, indice_chegada, peso, novo_peso):
        if self.existe():
            if indice_saida not in self.vertices or indice_chegada not in self.vertices:
                print('Um ou mais vértices não existem!')
                return 0
            if self.vertices[indice_saida].get_peso(self.vertices[indice_chegada]) != peso:
                print('Não existe aresta com peso {} do vértice {} para o vértice {}'.format(peso, indice_saida, indice_chegada))
                return 0
            self.vertices[indice_saida].add_vizinho(self.vertices[indice_chegada], novo_peso)
            print('Peso mudado com sucesso')

    #Função que imprime todos os vértices e todas as arestas do grafo
    def ImprimeGrafo(self):
        if self.existe():
            print('Grafo {}:'.format(self.nome))
            print('Vértices: {}'.format([x.indice for x in self]))
            print('Arestas: ')
            for v in self:
                print(v)
    
    #def RecuperaPeso(self, indice_saida, indice_chegada):

    #Função que retorna se o grafo é simples ou não
    def GrafoSimples(self):
        if self.existe():
            for v in self:
                vetor = np.zeros((self.vertice), dtype=np.int)
                for w in v.get_coneccoes():
                    if v.indice == w.indice:
                        print('O Grafo {} não é simples'.format(self.nome))
                        return 0
                    vetor[w.indice-1] += 1
                    if vetor[w.indice-1] > 1:
                        print('O Grafo {} não é simples'.format(self.nome))
                        return 0
            print('O Grafo {} é simples'.format(self.nome))

    #def EArvore(self):

    #def EBipartido(self):

    #Função que retorna o complemento do grafo 
    def Complemento(self, grafo):
        if self.existe():
            for v in self:
                vetor = np.zeros((self.vertice), dtype=np.int)
                for w in v.get_coneccoes():
                    vetor[w.indice-1] = 1
                for j in range(self.vertice):
                    if vetor[j] == 0:
                        grafo.AddAresta(v.indice, j+1, 1)
            return grafo

    #Função que retorna se existe uma aresta saindo do vértice de
    #índice "indice_saida" e chegando ao vértice de índice "indice_chegada"
    def EAdj(self, indice_saida, indice_chegada):
        if self.existe():
            if indice_saida not in self.vertices or indice_chegada not in self.vertices:
                print('Um ou mais vértices não existem!')
                return 0
            for w in self.vertices[indice_saida].get_coneccoes():
                if w.indice == indice_chegada:
                    print('A aresta V{}V{} existe'.format(indice_saida, indice_chegada))
                    return 0
            print('A aresta V{}V{} não existe'.format(indice_saida, indice_chegada))

    #Função que retorna a lista de adjacência do vértice de índice "indice"
    def Adjacencia(self, indice):
        if self.existe():
            if indice not in self.vertices:
                print('Vértice não existe!')
                return 0
            print('Vértice {}'.format(indice), end="")
            for w in self.vertices[indice].get_coneccoes():
                print(' -Peso {}-> Vértice {}'.format(self.vertices[indice].get_peso(self.get_vertice(w.indice)), w.indice), end="")
            print('')

    #Função que retorna as arestas incidentes as vértice de índice "indice"
    def Incidencia(self, indice):
        if self.existe():
            if indice not in self.vertices:
                print('Vértice não existe!')
                return 0
            print('Arestas incidentes ao vértice {}: '.format(indice))
            i = 0
            for w in self.vertices[indice].get_coneccoes():
                if i == 0:
                    print('V{}V{}'.format(indice, w.indice), end="")
                else:
                    print(' ,V{}V{}'.format(indice, w.indice), end="")
                i = 1
            print('')

    #Função que constrói a matriz de adjacência do grafo
    def MatrizAdj(self):
        if self.existe():
            matriz = np.zeros((self.vertice, self.vertice), dtype=np.int)
            for v in self:
                for w in v.get_coneccoes():
                    matriz[v.indice-1][w.indice-1] = v.get_peso(self.get_vertice(w.indice))
            self.matrizVertices = matriz

    #Função que imprime a matriz de adjacência do grafo
    def ImprimeMatrizAdj(self):
        for i in range(self.vertice):
            for j in range(self.vertice):
                if j != self.vertice-1:
                    print('{}, '.format(self.matrizVertices[i][j]), end="")
                else:
                    print('{}'.format(self.matrizVertices[i][j]), end="")
            print('')

    #def Conexo(self):

    #Função que deleta as informações do grafo
    def del_grafo(self):
        if self.existe():
            del self.nome
            del self.vertice
            del self.aresta
            del self.vertices
            del self.matrizVertices

    #Função que retorna os vértices existentes no grafo
    def get_vertices(self):
        if self.existe():
            return self.vertices.keys()

    def __iter__(self):
        if self.existe():
            return iter(self.vertices.values())

#Função que cria um novo grafo com apenas um vértice
def NovoGrafo(nome_Grafo):
    g = Grafo(nome_Grafo)
    return g

#Função que remove o grafo da memória
def RemoveGrafo(g):
    g.del_grafo()

#Função que cria um novo grafo vazio e 
#transforma ele no complemento do grafo "g"
def Complemento(g):
    gc = NovoGrafo('{}_'.format(g.nome))
    for i in range(2, (g.vertice)+1):
        gc.AddVertice(Vertice(i))
    return g.Complemento(gc)

#Função para ler o arquivo de texto com o grafo
#Gera o grafo em forma de lista de adjacência
def LerArquivo(nome):
    arquivo = open("{}.txt".format(nome), "r")
    linha = arquivo.readline()
    parametros = linha.split()
    nome_Grafo = parametros[0]
    n_vertices = int(parametros[1])
    n_arestas = int(parametros[2])
    g = NovoGrafo(nome_Grafo)
    for i in range(2, n_vertices+1):
        g.AddVertice(Vertice(i))
    linha = arquivo.readline()
    linha = arquivo.readline()
    while linha:
        valores = linha.split()
        g.AddAresta(int(valores[0]), int(valores[1]), int(valores[2]))
        linha = arquivo.readline()
    arquivo.close()
    return g

#Função para ler o arquivo como entrada principal do código
def EntradaPricipal():
    nome = sys.argv[1]
    return LerArquivo(nome)

#Funções de Percursos

#criando uma classe pilha
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)


def DSF(G, vi):

    saida = {}  #Vai associar cada vertice ao vertice que o alcançou pela primeira vez
    cor = []    #Cor cinza para visitados, bracos não visitados e preto para os percorridos
    custo = []  #Custo é o custo para chegar aquele vertice

    for vertice in G:
        cor[vertice.indice] = 'branco'
        custo[vertice.indice] = float('inf')

    cor[vi.indice] = 'cinza'
    custo[vi.indice] = 0

    #Iniciando uma pilha (estrtura usado para busca em profundidade)
    pilha = Stack()

    #insere vi (raiz) na fila
    pilha.push(vi)

    while not pilha.isEmpty():

        #Pegar o ultimo elemento empilhado
        u = pilha.pop()

        for vertice in u.get_coneccoes():
            if (cor[vertice.indice] == 'branco'):
                custo[vertice.indice] = custo[u.indice] + u.get_peso(G.get_vertice(vertice.indice))
                saida[vertice.indice] = u
                cor[vertice.indice] = 'cinza'
                pilha.push(vertice)
        
        #Depois que o vertice 'u' é percorrido, muda para a cor 'preto'
        cor[u.indice] = 'preto'

    return saida


def BSF(G, vi):

    saida = {}  #Vai associar cada vertice ao vertice que o alcançou pela primeira vez
    cor = []    #Cor cinza para visitados, bracos não visitados e preto para os percorridos
    custo = []  #Custo é o custo para chegar aquele vertice

    for vertice in G:
        cor[vertice.indice] = 'branco'
        custo[vertice.indice] = float('inf')

    cor[vi.indice] = 'cinza'
    custo[vi.indice] = 0

    #Iniciando uma fila (estrtura usado para busca em largura), o que difere do código de DSF
    fila = []

    #insere vi (raiz) na fila
    fila.append(vi)

    while (len(fila) > 0):
        u = fila.popleft()

        for vertice in u.get_coneccoes():
            if (cor[vertice.indice] == 'branco'):
                custo[vertice.indice] = custo[u.indice] + u.get_peso(G.get_vertice(vertice.indice))
                saida[vertice.indice] = u
                cor[vertice.indice] = 'cinza'
                fila.append(vertice)
        
        #Depois que o u é percorrido, muda para a cor 'preto'
        cor[u.indice] = 'preto'

    return saida

#Caminhos Minimos

def Bellmanford(G, vi):

    #Função Relax - Atualizar a distancia e o prodecedor dos vertices alcançados por vi 
    def relax(u, v):
        if ((distancia[u.indice] != infinito) and ((distancia[u.indice] + u.get_peso(G.get_vertice(vertice.indice))) < distancia[v.indice])):
            distancia[v.indice] = distancia[u.indice] + u.get_peso(G.get_vertice(vertice.indice))
            pred[v.indice] = u.indice

    def verificaCiclosNetagtivos(u, v):
        if ((distancia[u.indice] != infinito) and ((distancia[u.indice] + u.get_peso(G.get_vertice(vertice.indice))) < distancia[v.indice])):
            return 1


    infinito = float('inf')
    distancia = []     #Distancia de vi a cada vertice
    pred = []   #predecessor de cada vértice

    #Inicializando as distancias

    for vertice in G:
        distancia[vertice.indice] = infinito
        pred[vertice.indice] = None

    distancia[vi.indice] = 0

    #Aplicando a ideia de "relax" para diminuir os valores de distancia

    for _ in range(G.vertice - 1):
        for u in G:
            for v in u.get_coneccoes(): # v é um vizinhos de u
                relax(u, v)

    #Verificando se existe ciclos negativos

    for u in G:
        for v in u.get_coneccoes(): # v é um vizinhos de u
            if(verificaCiclosNetagtivos()):
                print("Este grafo contém ciclos negativos")

    return distancia, pred

def CaminhoMinimoIJ(G, vi, vj):

    distancia, pred = Bellmanford(G, vi)

    inicio = vi.indice
    fim = vj.indice
    
    print("Caminho de ", vi.indice, " a ", vj.indice)

    while inicio != fim:
        pilha = Stack()
        pilha.push(pred[fim])
        fim = pred[fim]
    
    while not pilha.isEmpty():
        print(" > ", pilha.pop)

def CustoMinimo(G, v):
    
    distancia, pred = Bellmanford(G, v)

    print("Custos em relação a ", v.indice ,": ", distancia)


def CaminhoMinimo(G, v):
    
    distancia, pred = Bellmanford(G, v)

    for u in range(G.vertice):

        inicio = v.indice
        fim = u.indice

        print("Caminho de ", v.indice, " a ", u.indice)
        while inicio != fim:
            pilha = Stack()
            pilha.push(pred[fim])
            fim = pred[fim]
        
        while not pilha.isEmpty():
            print(" > ", pilha.pop)


def meu_switch():

    print("Bem Vindo! Escolha uma opção")
    print("1: NovoGrafo()")
    print("2: Grafo(G)")
    print("3: EVertice(G, v)")
    print("4: AddAresta(G, vi, vj , ω)")
    print("5: RemoveAresta(G, vi, vj , ω)")
    print("6: ExisteAresta(G, vi, vj , ω")
    print("7: MudaPeso(G, vi, vj , ω, ω′)")
    print("8: ImprimeGrafo(G)")
    print("9: RemoveGrafo(G)")
    print("10: RecuperaPeso(G, vi, vj)")
    print("11: GrafoSimples(G)")
    print("12: EArvore(G)")
    print("13: EBipartido(G)")
    print("14: Complemento(G)")
    print("15: EAdj(G, vi, vj)")
    print("16: Adjacencia(G, v)")
    print("17: Incidencia(G, v)")    
    print("18: MatrizAdj(G)")
    print("19: ImprimeMatrizAdj(G)")
    print("20: Conexo(G)")
    print("21: DFS(G, vi)")
    print("22: BFS(G, vi)")
    print("23: CaminhoMinimo(G, vi, vj)")    
    print("24: CustoMinimo(G, v)")
    print("25: CaminhoMinimo(G, v)")
    print()

    opcao = int(input("Informe um número de 1 a 25: "))

    print("----------------------------------------")

    if(opcao==1):
        valor = input("Informe o nome do grafo: ")
        g.NovoGrafo(valor)

    if(opcao==2):
        g.Grafo()

    if(opcao==3):
        valor = input("Informe o valor do vertice: ")
        g.EVertice(valor)

    if(opcao==4):
        valor1 = int(input("Informe o valor vertice vi: "))
        valor2 = int(input("Informe o valor vertice vj: "))
        valor3 = int(input("Informe o pedo da aresta vivj: "))
        
        g.AddAresta(valor1, valor2, valor3)

    if(opcao==5):
        valor1 = int(input("Informe o valor vertice vi: "))
        valor2 = int(input("Informe o valor vertice vj: "))
        valor3 = int(input("Informe o peso da aresta vivj: "))
        
        g.RemoveAresta(valor1, valor2, valor3)

    if(opcao==6):
        valor1 = int(input("Informe o valor vertice vi: "))
        valor2 = int(input("Informe o valor vertice vj: "))
        valor3 = int(input("Informe o peso da aresta vivj: "))
        
        g.ExisteAresta(valor1, valor2, valor3)

    if(opcao==7):
        valor1 = int(input("Informe o valor vertice vi: "))
        valor2 = int(input("Informe o valor vertice vj: "))
        valor3 = int(input("Informe o peso da aresta vivj: "))
        valor4 = int(input("Informe o novo peso da aresta vivj: "))
        
        g.MudaPeso(valor1, valor2, valor3, valor4)

    if(opcao==8):
        g.ImprimeGrafo()

    if(opcao==9):
        g.RemoveGrafo()
    
    if(opcao==10):
        g.RecuperaPeso()

    if(opcao==11):
        g.GrafoSimples()

    if(opcao==12):
        g.EArvore()
    
    if(opcao==13):
        g.EBipartido()
        
    if(opcao==14):
        g.Complemento()

    if(opcao==15):
        valor1 = int(input("Informe o valor vertice vi: "))
        valor2 = int(input("Informe o valor vertice vj: "))
        g.EAdj(valor1, valor2)

    if(opcao==16):
        valor1 = int(input("Informe o valor vertice v: "))
        g.Adjacencia(valor1)

    if(opcao==17):
        valor1 = int(input("Informe o valor vertice v: "))
        g.Incidencia(valor1)        

    if(opcao==18):
        g.MatrizAdj()

    if(opcao==19):
        g.ImprimeMatrizAdj()

    if(opcao==20):
        g.conexo()

    if(opcao==21):
        valor1 = int(input("Informe o valor vertice v: "))
        DSF(g, g.get_vertice(valor1))

    if(opcao==22):
        valor1 = int(input("Informe o valor vertice v: "))
        BSF(g, g.get_vertice(valor1)) 

    if(opcao==23):
        valor1 = int(input("Informe o valor vertice vi: "))
        valor1 = int(input("Informe o valor vertice vj: "))
        CaminhoMinimoIJ(g, g.get_vertice(valor1), .get_vertice(valor2)) 
    
    if(opcao==24):
        valor1 = int(input("Informe o valor vertice v: "))
        CustoMinimo(g, g.get_vertice(valor1)) 
    
        
    if(opcao==25):
        valor1 = int(input("Informe o valor vertice v: "))
        CaminhoMinimo(g, g.get_vertice(valor1)) 

    if(opcao>25 or opcao<1):
        print("Valor Inválido")


if __name__ == "__main__":

    g = None
    if sys.argv[1] is not None:
        g = EntradaPricipal()

    while True:
        meu_switch()
