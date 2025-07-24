class Program:
    @staticmethod
    def main():
        cantidad_clientes=int(input("Cuantos clientes desea ingresar?"))
        clientes ={}
        for i in range(cantidad_clientes):
            print(f"\nCliente #: {i+1}")
            codigo_cliente=input("Ingrese codigo de cliente: ")
            nombre_cliente=input("Ingrese nombre del cliente: ")
            cantidad_destinos=int(input("Cuantos destinos desea registrar? (1-5)"))
            destinos = []
            for j in range(cantidad_destinos):
                destino=input(f"\nIngrese destino #: {j+1}")
                destinos.append(destino)

            clientes[codigo_cliente]={"nombre": nombre_cliente, "destinos_visitados":destinos}
        total_destinos=Program.contar_clientes(clientes)
    def contar_clientes(clientes, codigos=None, i=0):
        if codigos==None:
            codigos=list(clientes.keys())
        if i==len(codigos):
            return 0
        else:
            cliente=clientes[codigos[i]]
            destinos=len(cliente["destinos_visitados"])
            return destinos+Program.contar_clientes(clientes, codigos, i+1)