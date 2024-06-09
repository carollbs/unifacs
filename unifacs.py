class Lista:
    def __init__(self):
        self.items = []

    def inserir(self, item):
        self.items.append(item)

    def remover(self):
        if self.items:
            return self.items.pop(0)
        else:
            return None

    def __str__(self):
        return str(self.items)


class Pilha:
    def __init__(self):
        self.items = []

    def inserir(self, item):
        self.items.append(item)

    def remover(self):
        if self.items:
            return self.items.pop()
        else:
            return None

    def __str__(self):
        return str(self.items)


class Fila:
    def __init__(self):
        self.items = []

    def inserir(self, item):
        self.items.append(item)

    def remover(self):
        if self.items:
            return self.items.pop(0)
        else:
            return None

    def __str__(self):
        return str(self.items)


def main():
    # Passo 1
    lista = Lista()
    for i in range(1, 6):
        lista.inserir(i)
    print("Lista inicial:", lista)

    # Passo 2
    pilha = Pilha()
    for _ in range(5):
        pilha.inserir(lista.remover())
    print("Pilha após remover da lista:", pilha)

    # Passo 3
    fila = Fila()
    for _ in range(5):
        fila.inserir(pilha.remover())
    print("Fila após remover da pilha:", fila)

    # Passo 4
    for i in range(6, 11):
        lista.inserir(i)
    print("Lista após inserir [6, 7, 8, 9, 10]:", lista)

    # Passo 5
    for _ in range(5):
        pilha.inserir(lista.remover())
    print("Pilha após remover da lista novamente:", pilha)

    for _ in range(5):
        fila.inserir(pilha.remover())
    print("Fila após remover da pilha novamente:", fila)

    # Passo 6
    print("Números na fila:", fila)


if __name__ == "__main__":
    main()
