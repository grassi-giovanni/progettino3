# Importiamo db dall'app principale per poterlo utilizzare in questo file
from app import db

# Definiamo il modello per la tabella ListaSpesa
class ListaSpesa(db.Model):
    # Definiamo la struttura della tabella
    id = db.Column(db.Integer, primary_key=True)  # id come chiave primaria unica
    elemento = db.Column(db.String(100), nullable=False)  # elemento non può essere nullo

    # Metodo per rappresentare l'oggetto in formato leggibile
    def __repr__(self):
        return f"<ListaSpesa {self.elemento}>"