#include <stdlib.h>
#include <stdio.h>
#include "grafo.h"

struct verticeListaAdjacencia {
    int peso; //peso do vértice até o próximo
    struct verticeListaAdjacencia *prox;
};

typedef struct verticeListaAdjacencia Vertice;

struct ListaAdjacencia {
    Vertice *inicio;
};

typedef struct ListaAdjacencia Lista;

struct grafo {
    string nome; //nome do grafo
    int n; //número de vértices
    int m; //número de arestas
    Lista* lista; //lista de adjacência
};

typedef struct grafo Grafo;
