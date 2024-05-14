import flet as ft


from UI.view import View
from modello.model import Model
class Controller:
    def __init__(self, view:View, model:Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the modello, which implements the logic of the program and holds the data
        self._model = model
        self._anno=None



    def leggiAnno(self,e):
        anno=self._view._txtAnno.value
        try:
            self._anno=int(anno)
        except ValueError:
            self._view.create_alert("NON hai inserito un numero")
            self._view.update_page()
            return
        if self._anno<1816 or self._anno>2016:
            self._view.create_alert("NUmero inserito non compreso nell'intervallo 1816-2016")
            self._view.update_page()
            return

    def handleCalcola(self, e):
        self._model.creaGrafo(self._anno)

        pass
