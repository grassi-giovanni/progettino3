from flask import Flask, render_template, request, redirect, url_for
from models import db, ListaSpesa

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lista_spesa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    items = ListaSpesa.query.all()
    return render_template('index.html', items=items)

@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    elemento = request.form.get('elemento')
    if elemento:
        nuovo_elemento = ListaSpesa(elemento=elemento)
        db.session.add(nuovo_elemento)
        db.session.commit()
    return redirect(url_for('home'))

@app.route('/svuota', methods=['POST'])
def svuota():
    ListaSpesa.query.delete()
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/rimuovi/<int:id>', methods=['POST'])
def rimuovi(id):
    elemento = ListaSpesa.query.get(id)
    if elemento:
        db.session.delete(elemento)
        db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
