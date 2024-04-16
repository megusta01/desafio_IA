class Objeto:
    def __init__(self, nome: str, peso: float, valor: float) -> None:
        self.nome = nome
        self.peso = peso
        self.valor = valor

    def valor_por_peso(self) -> float:
        return self.valor / self.peso

class backpackProblem:
    def __init__(self, objetos: list[Objeto], peso_maximo: float) -> None:
        self.objetos = objetos
        self.peso_maximo = peso_maximo
        self.solucoes = []

    def execucao(self):
        while self.objetos and not self.solucao_completa():
            objeto = self.escolherObjeto()

            if self.adicionar_objeto_se_possivel(objeto):
                self.solucoes.append(objeto)
                self.objetos.remove(objeto)
            else:
                self.objetos.remove(objeto)

        return self.solucoes

    def escolherObjeto(self) -> Objeto:
        return max(self.objetos, key=lambda objeto: objeto.valor_por_peso())

    def adicionar_objeto_se_possivel(self, objeto: Objeto) -> bool:
        peso_total = sum(solu_objeto.peso for solu_objeto in self.solucoes)
        return peso_total + objeto.peso <= self.peso_maximo

    def solucao_completa(self) -> bool:
        peso_total = sum(solu_objeto.peso for solu_objeto in self.solucoes)
        return peso_total == self.peso_maximo

    def calcular_peso_total(self) -> float:
        return sum(objeto.peso for objeto in self.solucoes)

    def calcular_valor_total(self) -> float:
        return sum(objeto.valor for objeto in self.solucoes)

if __name__ == "__main__":
    objetos = [
        Objeto("Notebook", 2.0, 1500),
        Objeto("Celular", 0.5, 800),
        Objeto("Teclado", 0.7, 1200),
        Objeto("Caixa de som portátil", 1.0, 500),
        Objeto("Tablet", 0.8, 900),
        Objeto("Headset", 0.3, 300),
        Objeto("Carregador", 0.2, 150),
        Objeto("Livro", 0.5, 200),
        Objeto("Bolsa para notebook", 1.5, 350),
        Objeto("Calculadora", 0.2, 100),
        Objeto("Mouse", 0.1, 50),
    ]

    problema_mochila = backpackProblem(objetos, peso_maximo=5)
    solucoes = problema_mochila.execucao()

    # Calculando os valores e pesos totais
    def calcular_valores_e_pesos(problema_mochila):
        valor_total = problema_mochila.calcular_valor_total()
        peso_total = problema_mochila.calcular_peso_total()
        return valor_total, peso_total

    valor_total, peso_total = calcular_valores_e_pesos(problema_mochila)

    print("\n========= Itens da Mochila =========")
    print("{:<25} | {:<10} | {:<15}".format("Nome do Item", "Peso (kg)", "Valor (R$)"))
    print("-" * 50)

    for objeto in solucoes:
        print(f"{objeto.nome:<25} | {objeto.peso:<10.2f} | {objeto.valor:<15.2f}")
    print("-" * 50)
    print(f"Peso máximo da mochila: {problema_mochila.peso_maximo:.2f} kg")
    print("\n========= Resultados =========")
    
    print(f"Peso total na mochila: {peso_total:.2f} kg")
    print(f"Valor total dos itens: R$ {valor_total:.2f}")
