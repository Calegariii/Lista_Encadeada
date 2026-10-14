# Estruturas de Dados - Lista Simplesmente Encadeada
# Exercicios 1 a 5 reunidos em um unico arquivo
# Aluno: Gabriel Calegari Rodrigues
#
# Cada exercicio foi mantido intacto e pode ser executado pelo menu principal.


# ============================================================
# Exercicio 1 - Fila de chamados de suporte tecnico
# ============================================================
class Chamado:
    def __init__(self, codigo, solicitante, descricao, prioridade):
        self.codigo = codigo
        self.solicitante = solicitante
        self.descricao = descricao
        self.prioridade = prioridade
        self.proximo = None  # referencia para o proximo no (equivale ao ponteiro)


class ListaChamados:
    def __init__(self):
        self.inicio = None  # primeiro no da lista (None = lista vazia)
        self.fim = None     # ultimo no (permite inserir no final sem percorrer)

    def registrar(self):
        codigo = int(input("Codigo: "))
        solicitante = input("Solicitante: ")
        descricao = input("Descricao: ")
        prioridade = int(input("Prioridade (1-5): "))

        novo = Chamado(codigo, solicitante, descricao, prioridade)

        if self.inicio is None:      # lista vazia: novo e inicio e fim
            self.inicio = novo
            self.fim = novo
        else:                        # encadeia no fim
            self.fim.proximo = novo  # antigo ultimo aponta para o novo
            self.fim = novo          # fim passa a ser o novo
        print("Chamado registrado.")

    def listar(self):
        atual = self.inicio          # percorre com um auxiliar
        if atual is None:
            print("Nenhum chamado registrado.")
            return
        print("\n--- Chamados ---")
        while atual is not None:     # vai ate encontrar None
            print(f"Codigo: {atual.codigo} | Solicitante: {atual.solicitante} "
                  f"| Prioridade: {atual.prioridade}")
            print(f"  Descricao: {atual.descricao}")
            atual = atual.proximo

    def buscar(self):
        codigo = int(input("Codigo a buscar: "))
        atual = self.inicio
        while atual is not None:
            if atual.codigo == codigo:
                print(f"Encontrado: {atual.solicitante} | Prioridade: {atual.prioridade}")
                return
            atual = atual.proximo
        print("Chamado nao encontrado.")

    def contar(self):
        total = 0
        atual = self.inicio
        while atual is not None:
            total += 1
            atual = atual.proximo
        print(f"Total de chamados: {total}")

    def remover_primeiro(self):
        if self.inicio is None:      # teste: lista vazia
            print("Lista vazia. Nada a remover.")
            return
        removido = self.inicio       # guarda a referencia antes de remover
        self.inicio = self.inicio.proximo
        if self.inicio is None:      # teste: era o unico elemento
            self.fim = None          # inicio e fim viram None (lista vazia)
        # em Python nao ha free: o objeto e coletado automaticamente
        print("Primeiro chamado removido.")


def exercicio1():
    lista = ListaChamados()
    while True:
        print("\n=== CHAMADOS DE SUPORTE ===")
        print("1 - Registrar chamado")
        print("2 - Listar chamados")
        print("3 - Buscar por codigo")
        print("4 - Quantidade de chamados")
        print("5 - Remover primeiro chamado")
        print("0 - Encerrar")
        opcao = input("Opcao: ")

        if opcao == "1":
            lista.registrar()
        elif opcao == "2":
            lista.listar()
        elif opcao == "3":
            lista.buscar()
        elif opcao == "4":
            lista.contar()
        elif opcao == "5":
            lista.remover_primeiro()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opcao invalida.")


# ============================================================
# Exercicio 2 - Cadastro de imoveis de uma imobiliaria
# ============================================================
class Imovel:
    def __init__(self, codigo, bairro, tipo, dormitorios, valor):
        self.codigo = codigo
        self.bairro = bairro
        self.tipo = tipo
        self.dormitorios = dormitorios
        self.valor = valor
        self.proximo = None


class ListaImoveis:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def inserir(self):
        codigo = int(input("Codigo: "))
        bairro = input("Bairro: ")
        tipo = input("Tipo: ")
        dormitorios = int(input("Dormitorios: "))
        valor = float(input("Valor: "))

        novo = Imovel(codigo, bairro, tipo, dormitorios, valor)
        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.proximo = novo
            self.fim = novo
        print("Imovel inserido.")

    def listar(self):
        atual = self.inicio
        if atual is None:
            print("Catalogo vazio.")
            return
        print("\n--- Imoveis ---")
        while atual is not None:
            print(f"Codigo: {atual.codigo} | {atual.bairro} | {atual.tipo} "
                  f"| {atual.dormitorios} dorm | R$ {atual.valor:.2f}")
            atual = atual.proximo

    def buscar(self):
        codigo = int(input("Codigo a buscar: "))
        atual = self.inicio
        while atual is not None and atual.codigo != codigo:
            atual = atual.proximo
        if atual is None:
            print("Imovel nao encontrado.")
        else:
            print(f"Encontrado: {atual.bairro} | {atual.tipo} | R$ {atual.valor:.2f}")

    def listar_por_bairro(self):
        bairro = input("Bairro: ")
        atual = self.inicio
        achou = False
        while atual is not None:
            if atual.bairro == bairro:
                print(f"Codigo: {atual.codigo} | {atual.tipo} | R$ {atual.valor:.2f}")
                achou = True
            atual = atual.proximo
        if not achou:
            print("Nenhum imovel nesse bairro.")

    def alterar_valor(self):
        codigo = int(input("Codigo do imovel: "))
        atual = self.inicio
        while atual is not None and atual.codigo != codigo:
            atual = atual.proximo
        if atual is None:
            print("Imovel nao encontrado.")
            return
        atual.valor = float(input("Novo valor: "))
        print("Valor atualizado.")

    def remover(self):
        if self.inicio is None:
            print("Catalogo vazio.")
            return
        codigo = int(input("Codigo a remover: "))
        atual = self.inicio
        anterior = None  # permanece None enquanto nao ha elemento anterior

        while atual is not None and atual.codigo != codigo:
            anterior = atual          # anterior acompanha o percurso
            atual = atual.proximo

        if atual is None:
            print("Imovel nao encontrado.")
            return

        if anterior is None:
            # removendo o PRIMEIRO
            self.inicio = atual.proximo
        else:
            # removendo do MEIO ou do FIM
            anterior.proximo = atual.proximo

        if atual is self.fim:
            # removeu o ULTIMO: atualiza a referencia fim
            self.fim = anterior

        print("Imovel removido.")

    def maior_valor(self):
        if self.inicio is None:
            print("Catalogo vazio.")
            return
        atual = self.inicio
        maior = self.inicio
        while atual is not None:
            if atual.valor > maior.valor:
                maior = atual
            atual = atual.proximo
        print(f"Maior valor: codigo {maior.codigo} | {maior.bairro} | R$ {maior.valor:.2f}")


def exercicio2():
    lista = ListaImoveis()
    while True:
        print("\n=== IMOBILIARIA ===")
        print("1 - Inserir imovel")
        print("2 - Listar imoveis")
        print("3 - Buscar por codigo")
        print("4 - Listar por bairro")
        print("5 - Alterar valor")
        print("6 - Remover por codigo")
        print("7 - Imovel de maior valor")
        print("0 - Encerrar")
        opcao = input("Opcao: ")

        if opcao == "1":
            lista.inserir()
        elif opcao == "2":
            lista.listar()
        elif opcao == "3":
            lista.buscar()
        elif opcao == "4":
            lista.listar_por_bairro()
        elif opcao == "5":
            lista.alterar_valor()
        elif opcao == "6":
            lista.remover()
        elif opcao == "7":
            lista.maior_valor()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opcao invalida.")


# ============================================================
# Exercicio 3 - Controle de estoque de produtos
# ============================================================
class Produto:
    def __init__(self, codigo, descricao, quantidade, preco):
        self.codigo = codigo
        self.descricao = descricao
        self.quantidade = quantidade
        self.preco = preco
        self.proximo = None


class ListaEstoque:
    def __init__(self):
        self.inicio = None

    def _buscar(self, codigo):
        # Retorna (atual, anterior) para o ponto de insercao/consulta
        atual = self.inicio
        anterior = None
        while atual is not None and atual.codigo < codigo:
            anterior = atual
            atual = atual.proximo
        return atual, anterior

    def inserir(self):
        codigo = int(input("Codigo: "))
        descricao = input("Descricao: ")
        quantidade = int(input("Quantidade: "))
        preco = float(input("Preco: "))

        atual, anterior = self._buscar(codigo)
        if atual is not None and atual.codigo == codigo:
            print("Erro: codigo duplicado.")
            return

        novo = Produto(codigo, descricao, quantidade, preco)

        # Ligacoes do desafio de raciocinio do Exercicio 3
        novo.proximo = atual          # novo aponta para quem vem depois
        if anterior is None:
            # inserindo no INICIO (codigo menor que todos)
            self.inicio = novo
        else:
            anterior.proximo = novo   # anterior aponta para o novo
        print("Produto inserido.")

    def entrada(self):
        codigo = int(input("Codigo: "))
        atual, _ = self._buscar(codigo)
        if atual is None or atual.codigo != codigo:
            print("Produto nao encontrado.")
            return
        qtd = int(input("Unidades de entrada: "))
        atual.quantidade += qtd
        print(f"Entrada registrada. Novo estoque: {atual.quantidade}")

    def saida(self):
        codigo = int(input("Codigo: "))
        atual, _ = self._buscar(codigo)
        if atual is None or atual.codigo != codigo:
            print("Produto nao encontrado.")
            return
        qtd = int(input("Unidades de saida: "))
        if qtd > atual.quantidade:
            print(f"Erro: saida maior que o estoque ({atual.quantidade}).")
            return
        atual.quantidade -= qtd
        print(f"Saida registrada. Novo estoque: {atual.quantidade}")

    def buscar(self):
        codigo = int(input("Codigo a buscar: "))
        atual, _ = self._buscar(codigo)
        if atual is None or atual.codigo != codigo:
            print("Produto nao encontrado.")
        else:
            print(f"{atual.codigo} | {atual.descricao} | {atual.quantidade} un | R$ {atual.preco:.2f}")

    def listar(self):
        atual = self.inicio
        if atual is None:
            print("Estoque vazio.")
            return
        print("\n--- Produtos (ordem crescente de codigo) ---")
        while atual is not None:
            print(f"{atual.codigo} | {atual.descricao} | {atual.quantidade} un | R$ {atual.preco:.2f}")
            atual = atual.proximo

    def listar_estoque_baixo(self):
        atual = self.inicio
        achou = False
        while atual is not None:
            if atual.quantidade < 5:
                print(f"{atual.codigo} | {atual.descricao} | {atual.quantidade} un")
                achou = True
            atual = atual.proximo
        if not achou:
            print("Nenhum produto com menos de 5 unidades.")

    def remover_zerados(self):
        atual = self.inicio
        anterior = None
        removidos = 0
        while atual is not None:
            if atual.quantidade == 0:
                if anterior is None:
                    self.inicio = atual.proximo
                    atual = self.inicio
                else:
                    anterior.proximo = atual.proximo
                    atual = atual.proximo
                removidos += 1
            else:
                anterior = atual
                atual = atual.proximo
        print(f"Produtos removidos: {removidos}")


def exercicio3():
    lista = ListaEstoque()
    while True:
        print("\n=== ESTOQUE ===")
        print("1 - Inserir produto")
        print("2 - Registrar entrada")
        print("3 - Registrar saida")
        print("4 - Buscar produto")
        print("5 - Listar produtos")
        print("6 - Produtos com menos de 5 unidades")
        print("7 - Remover produtos zerados")
        print("0 - Encerrar")
        opcao = input("Opcao: ")

        if opcao == "1":
            lista.inserir()
        elif opcao == "2":
            lista.entrada()
        elif opcao == "3":
            lista.saida()
        elif opcao == "4":
            lista.buscar()
        elif opcao == "5":
            lista.listar()
        elif opcao == "6":
            lista.listar_estoque_baixo()
        elif opcao == "7":
            lista.remover_zerados()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opcao invalida.")


# ============================================================
# Exercicio 4 - Playlist de musicas
# ============================================================
class Musica:
    def __init__(self, codigo, titulo, artista, duracao_segundos):
        self.codigo = codigo
        self.titulo = titulo
        self.artista = artista
        self.duracao_segundos = duracao_segundos
        self.proximo = None


class Playlist:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def _buscar(self, codigo):
        atual = self.inicio
        anterior = None
        while atual is not None and atual.codigo != codigo:
            anterior = atual
            atual = atual.proximo
        return atual, anterior

    def adicionar(self):
        novo = Musica(
            int(input("Codigo: ")),
            input("Titulo: "),
            input("Artista: "),
            int(input("Duracao (segundos): ")),
        )
        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.proximo = novo
            self.fim = novo
        print("Musica adicionada.")

    def inserir_depois(self):
        codigo_ref = int(input("Codigo da musica de referencia: "))
        atual, _ = self._buscar(codigo_ref)
        if atual is None:
            print("Musica de referencia nao encontrada.")
            return

        novo = Musica(
            int(input("Codigo: ")),
            input("Titulo: "),
            input("Artista: "),
            int(input("Duracao (segundos): ")),
        )

        # A ordem das duas instrucoes e importante
        novo.proximo = atual.proximo  # 1) novo aponta para o sucessor
        atual.proximo = novo          # 2) atual aponta para o novo

        if novo.proximo is None:      # inserido apos o ultimo
            self.fim = novo
        print(f"Musica inserida apos o codigo {codigo_ref}.")

    def listar(self):
        atual = self.inicio
        if atual is None:
            print("Playlist vazia.")
            return
        print("\n--- Playlist ---")
        while atual is not None:
            print(f"{atual.codigo} | {atual.titulo} - {atual.artista} "
                  f"({atual.duracao_segundos} s)")
            atual = atual.proximo

    def buscar_por_artista(self):
        artista = input("Artista: ")
        atual = self.inicio
        achou = False
        while atual is not None:
            if atual.artista == artista:
                print(f"{atual.codigo} | {atual.titulo} ({atual.duracao_segundos} s)")
                achou = True
            atual = atual.proximo
        if not achou:
            print("Nenhuma musica desse artista.")

    def remover(self):
        codigo = int(input("Codigo a remover: "))
        atual, anterior = self._buscar(codigo)
        if atual is None:
            print("Musica nao encontrada.")
            return
        if anterior is None:
            self.inicio = atual.proximo
        else:
            anterior.proximo = atual.proximo
        if atual is self.fim:
            self.fim = anterior
        print("Musica removida.")

    def duracao_total(self):
        atual = self.inicio
        total = 0
        while atual is not None:
            total += atual.duracao_segundos
            atual = atual.proximo
        print(f"Duracao total: {total} s ({total // 60} min {total % 60} s)")

    def mover_para_inicio(self):
        codigo = int(input("Codigo da musica a mover: "))
        atual, anterior = self._buscar(codigo)
        if atual is None:
            print("Musica nao encontrada.")
            return
        if anterior is None:
            print("A musica ja esta no inicio.")
            return

        # Desencadeia o no da posicao atual
        anterior.proximo = atual.proximo
        if atual is self.fim:
            self.fim = anterior          # era o ultimo: fim volta para anterior

        # Reencadeia no inicio
        atual.proximo = self.inicio
        self.inicio = atual              # inicio passa a apontar para a musica
        print("Musica movida para o inicio.")


def exercicio4():
    lista = Playlist()
    while True:
        print("\n=== PLAYLIST ===")
        print("1 - Adicionar musica")
        print("2 - Inserir depois de uma musica")
        print("3 - Listar playlist")
        print("4 - Buscar por artista")
        print("5 - Remover musica")
        print("6 - Duracao total")
        print("7 - Mover musica para o inicio")
        print("0 - Encerrar")
        opcao = input("Opcao: ")

        if opcao == "1":
            lista.adicionar()
        elif opcao == "2":
            lista.inserir_depois()
        elif opcao == "3":
            lista.listar()
        elif opcao == "4":
            lista.buscar_por_artista()
        elif opcao == "5":
            lista.remover()
        elif opcao == "6":
            lista.duracao_total()
        elif opcao == "7":
            lista.mover_para_inicio()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opcao invalida.")


# ============================================================
# Exercicio 5 - Sistema de entregas de uma transportadora
# ============================================================
class Entrega:
    def __init__(self, codigo, cliente, endereco, status, distancia_km):
        self.codigo = codigo
        self.cliente = cliente
        self.endereco = endereco
        self.status = status
        self.distancia_km = distancia_km
        self.proximo = None


class ListaEntregas:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def cadastrar(self):
        novo = Entrega(
            int(input("Codigo: ")),
            input("Cliente: "),
            input("Endereco: "),
            input("Status (Pendente/Em rota/Entregue): "),
            float(input("Distancia (km): ")),
        )
        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.proximo = novo
            self.fim = novo
        print("Entrega cadastrada.")

    def listar(self):
        atual = self.inicio
        if atual is None:
            print("Nenhuma entrega cadastrada.")
            return
        print("\n--- Entregas ---")
        while atual is not None:
            print(f"{atual.codigo} | {atual.cliente} | {atual.endereco} "
                  f"| {atual.status} | {atual.distancia_km:.1f} km")
            atual = atual.proximo

    def buscar(self):
        codigo = int(input("Codigo a buscar: "))
        atual = self.inicio
        while atual is not None and atual.codigo != codigo:
            atual = atual.proximo
        if atual is None:
            print("Entrega nao encontrada.")
        else:
            print(f"{atual.cliente} | {atual.endereco} | {atual.status} "
                  f"| {atual.distancia_km:.1f} km")

    def alterar_estado(self):
        codigo = int(input("Codigo: "))
        atual = self.inicio
        while atual is not None and atual.codigo != codigo:
            atual = atual.proximo
        if atual is None:
            print("Entrega nao encontrada.")
            return
        atual.status = input("Novo status: ")
        print("Estado alterado.")

    def contar_pendentes(self):
        atual = self.inicio
        total = 0
        while atual is not None:
            if atual.status == "Pendente":
                total += 1
            atual = atual.proximo
        print(f"Entregas pendentes: {total}")

    def distancia_total(self):
        atual = self.inicio
        total = 0.0
        while atual is not None:
            total += atual.distancia_km
            atual = atual.proximo
        print(f"Distancia total: {total:.1f} km")

    def remover_entregues(self):
        atual = self.inicio
        anterior = None
        removidos = 0
        while atual is not None:
            if atual.status == "Entregue":
                if anterior is None:
                    # removendo o inicio
                    self.inicio = atual.proximo
                    atual = self.inicio
                else:
                    # salta o no; anterior NAO avanca (pode haver outro
                    # "Entregue" logo em seguida)
                    anterior.proximo = atual.proximo
                    atual = atual.proximo
                removidos += 1
            else:
                anterior = atual          # so avanca anterior se nao removeu
                atual = atual.proximo
        # Ajusta fim caso o ultimo tenha sido removido
        if self.inicio is None:
            self.fim = None
        else:
            no = self.inicio
            while no.proximo is not None:
                no = no.proximo
            self.fim = no
        print(f"Entregas removidas: {removidos}")

    def liberar_lista(self):
        # Esvazia completamente a lista (desafio de raciocinio do Exercicio 5)
        self.inicio = None
        self.fim = None
        print("Lista esvaziada.")


def exercicio5():
    lista = ListaEntregas()
    while True:
        print("\n=== ENTREGAS ===")
        print("1 - Cadastrar entrega")
        print("2 - Listar entregas")
        print("3 - Buscar por codigo")
        print("4 - Alterar estado")
        print("5 - Contar pendentes")
        print("6 - Distancia total")
        print("7 - Remover entregas concluidas")
        print("8 - Esvaziar a lista")
        print("0 - Encerrar")
        opcao = input("Opcao: ")

        if opcao == "1":
            lista.cadastrar()
        elif opcao == "2":
            lista.listar()
        elif opcao == "3":
            lista.buscar()
        elif opcao == "4":
            lista.alterar_estado()
        elif opcao == "5":
            lista.contar_pendentes()
        elif opcao == "6":
            lista.distancia_total()
        elif opcao == "7":
            lista.remover_entregues()
        elif opcao == "8":
            lista.liberar_lista()
        elif opcao == "0":
            lista.liberar_lista()
            print("Encerrando...")
            break
        else:
            print("Opcao invalida.")


# ============================================================
# Menu principal - escolhe qual exercicio executar
# ============================================================
def main():
    while True:
        print("\n=== LISTA DE EXERCICIOS (PYTHON) ===")
        print("1 - Exercicio 1: Chamados de suporte")
        print("2 - Exercicio 2: Imobiliaria")
        print("3 - Exercicio 3: Estoque")
        print("4 - Exercicio 4: Playlist")
        print("5 - Exercicio 5: Entregas")
        print("0 - Sair")
        opcao = input("Opcao: ")

        if opcao == "1":
            exercicio1()
        elif opcao == "2":
            exercicio2()
        elif opcao == "3":
            exercicio3()
        elif opcao == "4":
            exercicio4()
        elif opcao == "5":
            exercicio5()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opcao invalida.")


if __name__ == "__main__":
    main()
