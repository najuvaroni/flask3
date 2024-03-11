from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app= Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/biblioteca'
db = SQLAlchemy(app)

class livro (db.Model):
    id_livro = db.Column(db.Integer, primary_key= True,autoincrement=True )
    titulo = db.Column(db.String(100))
    autor = db.Column(db.String(254))
    ano_publicado = db.Column(db.Integer)

@app.route('/')
def index():
    livros = livro.query.all()
    return render_template('cadastro_livros.html', outro=livros)

app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo livro')

app.route('/criar', methods=['POST'])
def criar():
    titulo = request.form['titulo']
    autor = request.form['autor']
    ano_publicado = request.form['ano_publicado']

    livros = livro.query.filter_by(titulo=titulo).first()
    if livros:
        flash('livro já existente')
        return redirect(url_for('novo'))

    novo_livro = livro(titulo=titulo, autor=autor, ano_publicado=ano_publicado)
    db.session.add(novo_livro)
    db.session.commit()
    return redirect(url_for('index'))

if __name__  == '__main__':
    app.run()