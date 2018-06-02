from flask import render_template,redirect, request
from lister import app
from sqlalchemy import func
from lister.extensions import db
from lister.forms import mainForm
from lister.models.database import Agencias


@app.route('/', methods=['GET','POST'])
def index():
    form = mainForm()
    if form.validate_on_submit() and request.method == 'POST':
        agen = form.agencia.data
        est = form.estado.data
        mun = form.cidade.data
        banco = Agencias.query.filter(Agencias.municipio.ilike('%'+mun+'%'),Agencias.uf == est,Agencias.nomeinstituicao.ilike('%'+agen+'%'))
        return render_template('results.html', banco = banco, mun = mun)
    return render_template('home.html',form=form)

@app.route('/results')
def results():
    return render_template('results.html')
