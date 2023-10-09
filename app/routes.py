from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import Mercadoria

@app.route('/')
def index():
    mercadorias = Mercadoria.query.all()
    return render_template('index.html', mercadorias=mercadorias)

# Rota para adicionar uma nova mercadoria
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        preco = request.form['preco']
        mercadoria = Mercadoria(nome=nome, descricao=descricao, preco=preco)
        db.session.add(mercadoria)
        db.session.commit()
        flash('Mercadoria adicionada com sucesso!', 'success')
        return redirect(url_for('index'))
    return render_template('add.html')

# Rota para editar uma mercadoria existente
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    mercadoria = Mercadoria.query.get(id)
    if request.method == 'POST':
        mercadoria.nome = request.form['nome']
        mercadoria.descricao = request.form['descricao']
        mercadoria.preco = request.form['preco']
        db.session.commit()
        flash('Mercadoria atualizada com sucesso!', 'success')
        return redirect(url_for('index'))
    return render_template('edit.html', mercadoria=mercadoria)

# Rota para ver os detalhes de uma mercadoria
@app.route('/view/<int:id>')
def view(id):
    mercadoria = Mercadoria.query.get(id)
    return render_template('view.html', mercadoria=mercadoria)

# Rota para deletar uma mercadoria
@app.route('/delete/<int:id>')
def delete(id):
    mercadoria = Mercadoria.query.get(id)
    db.session.delete(mercadoria)
    db.session.commit()
    flash('Mercadoria deletada com sucesso!', 'success')
    return redirect(url_for('index'))
