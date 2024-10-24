import requests

url='http://localhost:3000/clientes'

class clientesApiService:
    def buscarClientes(self):
        response=requests.get(url)

        if response.status_code==200:
            users=response.json()
            print(users)
            return
        else:
            print("erro ao acessar API:", response.status_code)

    def buscarCliente(self,id=None,nome=None):
        if id is not None and nome is not None:
            response=requests.get(f'{url}?id={id}&nome={nome}')   
        elif id is not None:
            response=requests.get(f'{url}/{id}')   
        elif nome is not None:
            response=requests.get(f'{url}?nome={nome}')   
        else:
            self.buscarClientes()
            return  

        if response.status_code==200:
            users=response.json()
            print(users)
            return
        else:
            print("erro ao acessar API:", response.status_code)

    def adicionarCliente(self,nome):
        novo_cliente={"nome":nome}
        response=requests.post(url,json=novo_cliente)

        if response.status_code==201:
            print(f'{nome} foi adicionado a lista de clientes')
        else:
            print("erro ao acessar API:", response.status_code)

    def alterarCliente(self,id,nome):
        cliente_atualizado={"nome":nome}
        response=requests.put(f"{url}/{id}", json=cliente_atualizado)
        if response.status_code==200:
            print(f"{nome} foi atualizado a lista de clientes")
        else:
            print("erro ao atualizar o cliente: ", response.status_code)
    def removerCliente(self,id):
        response=requests.delete(f"{url}/{id}")
        if response.status_code==200:
            print(f"cliente do id {id} foi removido da lista de clientes")
        else:
            print("erro ao remover o cliente: ", response.status_code)

    
servico=clientesApiService()
# servico.adicionarCliente('Felipe')
# servico.buscarCliente(666)
# servico.buscarCliente(None,"galvao")
# servico.alterarCliente("a39c","galvao dos prazeres")
# servico.buscarCliente(3,"prazeres")
servico.removerCliente("3726")