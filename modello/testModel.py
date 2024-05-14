from modello.model import Model
myModel=Model()
myModel.creaGrafo(2000)

print(myModel.numNodes())
print(myModel.numEdges())
myModel.componenentiConnesse()

print(myModel.getConnessa(232))