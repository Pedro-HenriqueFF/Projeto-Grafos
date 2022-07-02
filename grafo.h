typedef struct verticeListaAdjacencia Vertice;
typedef struct ListaAdjacencia Lista;
typedef struct MatrizAdjacencia Matriz;
typedef struct grafo Grafo;

Grafo* NovoGrafo();
void Grafo(Grafo *);
int EVertice(Grafo *, Vertice *);
int AddAresta(Grafo *, Vertice *, Vertice *, int);
int RemoveAresta(Grafo *, Vertice *, Vertice *, int);
int ExisteAresta(Grafo *, Vertice *, Vertice *, int);
int MudaPeso(Grafo *, Vertice *, Vertice *, int, int);
void ImprimeGrafo(Grafo *);
void RemoveGrafo(Grafo *);
int RecuperaPeso(Grafo *, Vertice *, Vertice *);
int GrafoSimples(Grafo *);
int EArvore(Grafo *);
int EBipartido(Grafo *);
Grafo* Complemento(Grafo *)
int EAdj(Grafo *, Vertice *, Vertice *);
Lista* Adjacencia(Grafo *, Vertice *);
Lista* Incidencia(Grafo *, Vertice *);
Matriz* MatrizAdj(Grafo *);
void ImprimeMatrizAdj(Grafo *);
int Conexo(Grafo *);

void DFS(Grafo *, Vertice *);
void BFS(Grafo *, Vertice *);

void CaminhoMinimo(Grafo *, Vertice *, Vertice *);
void CustoMinimo(Grafo *, Vertice *);
void CaminhoMinimo(Grafo *, Vertice *);
