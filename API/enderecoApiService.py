import http.client
import json
import os
import pandas
class EncerecoApiService:
    def consultarEderecoIbge(self,cep=None):
        apiViaCep=http.client.HTTPSConnection("viacep.com.br")

        while True:
            cep=input("digite o CEP para consultar o endereço: ")
            os.system("cls")
            apiViaCep.request("GET",f"/ws/{cep}/json/")
            response=apiViaCep.getresponse()
            data=response.read().decode("utf-8")
            endereco=json.loads(data)

            endereco_simples=[{"logradouro":endereco.get("logradouro"),"bairro":endereco.get("bairro"),"localidade":endereco.get("localidade"),"uf":endereco.get("uf"),}]
            tabela=pandas.DataFrame(endereco_simples)
            print(tabela)

servico=EncerecoApiService()
servico.consultarEderecoIbge()