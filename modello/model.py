import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._grafo = nx.Graph()
        self._nazioni=None

    def creaGrafo(self,anno):
        self._nazioni = DAO.getNazioni(anno)
        self.idMap = {}
        for v in self._nazioni:
            self.idMap[v.CCode] = v
        self._grafo.add_nodes_from(self._nazioni)
        self.addEdges(anno)

    def addEdges(self,anno):
        self._confini=DAO.getConfini(anno)
        for u,v in self._confini:
            u_inizio=self.idMap[u]
            u_fine=self.idMap[v]
            self._grafo.add_edge(u_inizio,u_fine)

    def numNodes(self):
        return self._grafo.number_of_nodes()
    def numEdges(self):
        return self._grafo.number_of_edges()

    def nazioni(self):
        return self._nazioni

    def componenentiConnesse(self):
        print(nx.number_connected_components(self._grafo))
        return len(list(nx.connected_components(self._grafo)))

    def getConnessa(self,codice):
        vo=self.idMap[codice]
        vicini=list(nx.neighbors(self._grafo,vo))
        return len(vicini)