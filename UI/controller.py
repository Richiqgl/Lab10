import flet as ft
import networkx as nx

from UI.view import View
from modello.model import Model
class Controller:
    def __init__(self, view:View, model:Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the modello, which implements the logic of the program and holds the data
        self._model = model
        self._anno=None

    def leggiAnno(self):
        anno=self._view._txtAnno.value
        try:
            annoIntero=int(anno)
        except ValueError:
            self._view.create_alert("NON hai inserito un numero")
            self._view.update_page()
            return None
        if annoIntero<1816 or annoIntero>2016:
            self._view.create_alert("NUmero inserito non compreso nell'intervallo 1816-2016")
            self._view.update_page()
            return None
        return annoIntero

    def handleCalcola(self, e):
        self._anno=self.leggiAnno()
        if self._anno is None:
            return
        self._model.creaGrafo(self._anno)
        componentiConnesse=self._model.componenentiConnesse()
        self._view._txt_result.controls.append(ft.Text("Grafo correttamente creato"))
        self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {componentiConnesse} componenti connesse"))
        for v in self._model.nazioni():
            numero=self._model.getConnessa(v.CCode)
            self._view._txt_result.controls.append(ft.Text(f"{v.StateNme} -- {numero} vicini."))
        self._view.update_page()


