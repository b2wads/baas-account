class Calculadora:
    def abs(self, n: int) -> int:
        if n < 0:
            return -n
        return n

    def min(self, a: int, b: int) -> int:
        if a < b:
            print(f"a < b, retornando a: {a}")
            return a
        print(f"a > b, retornando b: {b}")
        return b

    def max(self, a: int, b: int) -> int:
        if a > b:
            return a
        return b


class Produto:
    id: str
    nome: str
    preco: int


class ListaDeProdutos:

    calc = Calculadora()

    def __init__(self, produto1, produto2):
        self.p1 = produto1
        self.p2 = produto2

    def menor_preco(self):
        return self.calc.min(self.p1.preco, self.p2.preco)

    def get_preco_atualizado(self, id: str) -> int:
        with HttpClientSession(
            f"https://api.americanas.com.br/product/{id}"
        ) as response:
            data = response.json()
            return data["preco"]
