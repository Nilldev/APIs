
from flask import Flask, make_response, jsonify, request
from bd import Carros
#server= (___name___)




#@server.get('/pessoas')
#def buscar_pessoas():
 #   return 'Programaticamente falando'

app = Flask(__name__)


@app.route('/carros', methods=['GET'])
def get_carros():
    return make_response(

     jsonify(Carros)

    )

@app.route('/carros', methods=['POST'])
def creat_carro():
   carro= request.json
   return carro


app.run()


