class Program:
    @staticmethod
    def main():
        cantidad_clientes=int(input("Cuantos clientes desea ingresar?: "))
        clientes ={}
        for i in range(cantidad_clientes):
            print(f"\nCliente #: {i+1}")
            codigo_cliente=input("Ingrese codigo de cliente: ")
            nombre_cliente=input("Ingrese nombre del cliente: ")
            cantidad_destinos=int(input("Cuantos destinos desea registrar? (1-5)"))
            destinos = []
            for j in range(cantidad_destinos):
                destino=input(f"\nIngrese destino #{j+1}: ")
                destinos.append(destino)

            clientes[codigo_cliente]={"nombre": nombre_cliente, "destinos_visitados":destinos}
        print("=================LISTA DE CLIENTES REGISTRADOS=================")
        for codigo, datos in clientes.items():
            print(f"\nCodigo de cliente: {codigo}, Nombre: {datos["nombre"]}, Destinos visitados: ")
            for destinos in datos["destinos_visitados"]:
                print(f"- {destinos}")

        print(f"El cliente con mas destinos visitados es: {Program.cliente_con_mas_destinos(clientes)}")
        total_destinos=Program.contar_clientes(clientes)
        print(f"\nEl total de destinos registrado es de: {total_destinos}")
    @staticmethod
    def contar_clientes(clientes, codigos=None, i=0):
        if codigos is None:
            codigos=list(clientes.keys())
        if i==len(codigos):
            return 0
        else:
            cliente=clientes[codigos[i]]
            destinos=len(cliente["destinos_visitados"])
            return destinos+Program.contar_clientes(clientes, codigos, i+1)
    @staticmethod
    def cliente_con_mas_destinos(clientes):
        max_destinos = -1
        cliente_mas_viajero = None

        for codigo, datos in clientes.items():
            cantidad = len(datos["destinos_visitados"])
            if cantidad > max_destinos:
                max_destinos = cantidad
                cliente_mas_viajero = (codigo, datos["nombre"], cantidad)

        return cliente_mas_viajero
Program.main()