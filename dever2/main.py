from flask import Flask, request, render_template
from flaskext.mysql import MySQL
from bd import *



# Instanciando a app Flask
app = Flask(__name__)
# Instanciar o objeto MySQL
mysql = MySQL()
# Ligar o MYSQL ao Flask
mysql.init_app(app)

# Configurando o acesso ao MySQL
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'faculdade'

# Rota para /
@app.route('/')
def principal():
    cursor  = mysql.get_db().cursor()
    return render_template('menu.html', professores=listarProfessores(cursor))


@app.route('/detalhar/<prof>')
def exibir(prof):
    cursor = mysql.get_db().cursor()
    return render_template('informacoes.html', professor= exibirPofessor(cursor, nome=prof))



@app.route('/consulta', methods=['GET', 'POST'])
def exibirConsulta():
    if  request.method == 'POST':
        parametro = request.form.get('parametro')

        cursor = mysql.get_db().cursor()

        titulacao = consultarTitulacao(cursor, parametro)

        if titulacao is None:
            return render_template('menu.html',erro='Valor incorreto')

        else:
            cursor = mysql.get_db().cursor()
            return render_template('consultatitulacao.html', consulta=consultarTitulacao(cursor, parametro))
    return



@app.route('/consultacic')
def consultacic():
    cursor = mysql.get_db().cursor()
    return render_template('consultacic.html', dados=consultarapenascomputacao(cursor))





# Rodando a app
if __name__ == '__main__':
    app.run(debug=True)
