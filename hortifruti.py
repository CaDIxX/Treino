class ListaCompras:
    def __init__(self, n_produtos: int) -> None:
        self.itens = [0 for _ in range(n_produtos)]

    def adicionar_item(self, posicao: int, item: str, preco: float) -> None:
        self.itens[posicao] = [item, preco]
    
    def listar_preco(self, num_item) -> None:
            print(self.itens[num_item][1])


def main() -> None:
    n_itens = int(input())
    lista_compra = ListaCompras(n_itens)

    for i in range(len(lista_compra.itens)):
        item = input()
        
        for j in range(len(lista_compra.itens)):
            if lista_compra.itens[j] == 0:
                continue

            if item == lista_compra.itens[j][0]:
                print("Produto já cadastrado")
                break
        
        preco = float(input())
        lista_compra.adicionar_item(i, item, preco)
    
    while True:
        hortifruti = input()

        if hortifruti == "Fim":
            break

        for m in range(len(lista_compra.itens)):
            if lista_compra.itens[m] == 0:
                continue

            if hortifruti in lista_compra.itens[m]:
                lista_compra.listar_preco(m)

            if m == -1:
                print("Produto não cadastrado.")


if __name__ == "__main__":
    main()

