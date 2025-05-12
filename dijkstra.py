import pygame
import sys
import heapq
import itertools

# Configurações da grade
LARGURA = 600
ALTURA = 600
LINHAS = 30
COLUNAS = 30
TAMANHO_CELULA = LARGURA // COLUNAS

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
CINZA = (200, 200, 200)
AMARELO = (255, 255, 0)

# Inicialização do Pygame
pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA + 40))
pygame.display.set_caption("Visualizador do Algoritmo de Dijkstra")
fonte = pygame.font.SysFont("Arial", 20)

# Classe para representar cada célula da grade
class Celula:
    def __init__(self, linha, coluna):
        self.linha = linha
        self.coluna = coluna
        self.x = coluna * TAMANHO_CELULA
        self.y = linha * TAMANHO_CELULA
        self.cor = BRANCO
        self.vizinhos = []
        self.distancia = float('inf')
        self.anterior = None
        self.parede = False
        self.peso = 1  # Peso padrão para cada célula

    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, (self.x, self.y, TAMANHO_CELULA, TAMANHO_CELULA))
        pygame.draw.rect(tela, CINZA, (self.x, self.y, TAMANHO_CELULA, TAMANHO_CELULA), 1)

    def atualizar_vizinhos(self, grade):
        self.vizinhos = []
        if self.linha < LINHAS - 1 and not grade[self.linha + 1][self.coluna].parede:
            self.vizinhos.append(grade[self.linha + 1][self.coluna])
        if self.linha > 0 and not grade[self.linha - 1][self.coluna].parede:
            self.vizinhos.append(grade[self.linha - 1][self.coluna])
        if self.coluna < COLUNAS - 1 and not grade[self.linha][self.coluna + 1].parede:
            self.vizinhos.append(grade[self.linha][self.coluna + 1])
        if self.coluna > 0 and not grade[self.linha][self.coluna - 1].parede:
            self.vizinhos.append(grade[self.linha][self.coluna - 1])

def criar_grade():
    return [[Celula(i, j) for j in range(COLUNAS)] for i in range(LINHAS)]

def desenhar_grade(tela, grade, custo=None):
    tela.fill(BRANCO)
    for linha in grade:
        for celula in linha:
            celula.desenhar(tela)

    # Legenda
    pygame.draw.rect(tela, VERDE, (10, ALTURA + 5, 20, 20))
    tela.blit(fonte.render("Início", True, PRETO), (35, ALTURA + 5))

    pygame.draw.rect(tela, VERMELHO, (100, ALTURA + 5, 20, 20))
    tela.blit(fonte.render("Fim", True, PRETO), (125, ALTURA + 5))

    pygame.draw.rect(tela, PRETO, (170, ALTURA + 5, 20, 20))
    tela.blit(fonte.render("Parede", True, PRETO), (195, ALTURA + 5))

    pygame.draw.rect(tela, AZUL, (270, ALTURA + 5, 20, 20))
    tela.blit(fonte.render("Visitado", True, PRETO), (295, ALTURA + 5))

    pygame.draw.rect(tela, AMARELO, (390, ALTURA + 5, 20, 20))
    tela.blit(fonte.render("Caminho", True, PRETO), (415, ALTURA + 5))

    if custo is not None:
        tela.blit(fonte.render(f"Custo: {custo}", True, (0, 0, 0)), (520, ALTURA + 5))

    pygame.display.update()

def obter_posicao_mouse(pos):
    x, y = pos
    linha = y // TAMANHO_CELULA
    coluna = x // TAMANHO_CELULA
    return linha, coluna

def definir_peso(grade, pos):
    linha, coluna = obter_posicao_mouse(pos)
    celula = grade[linha][coluna]
    if not celula.parede and celula.cor not in [VERDE, VERMELHO]:
        novo_peso = input("Digite o peso para esta célula (número inteiro): ")
        if novo_peso.isdigit():
            celula.peso = int(novo_peso)
            intensidade = max(0, 255 - celula.peso * 20)  # Ajusta a cor com base no peso
            celula.cor = (intensidade, intensidade, 255)  # Tons de azul para representar o peso

def dijkstra(grade, inicio, fim):
    contador = itertools.count()
    fila = []
    heapq.heappush(fila, (0, next(contador), inicio))
    inicio.distancia = 0

    while fila:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        distancia_atual, _, celula_atual = heapq.heappop(fila)

        if celula_atual == fim:
            while celula_atual.anterior:
                celula_atual = celula_atual.anterior
                if celula_atual != inicio:
                    celula_atual.cor = AMARELO
                    desenhar_grade(tela, grade, fim.distancia)
                    pygame.time.delay(20)
            desenhar_grade(tela, grade, fim.distancia)
            return

        for vizinho in celula_atual.vizinhos:
            temp_distancia = celula_atual.distancia + vizinho.peso  # Usa o peso da célula
            if temp_distancia < vizinho.distancia:
                vizinho.distancia = temp_distancia
                vizinho.anterior = celula_atual
                heapq.heappush(fila, (vizinho.distancia, next(contador), vizinho))
                if vizinho != fim:
                    vizinho.cor = AZUL

        desenhar_grade(tela, grade)
        pygame.time.delay(1)

def main():
    grade = criar_grade()
    inicio = None
    fim = None
    executando = True

    while executando:
        desenhar_grade(tela, grade)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False

            if pygame.mouse.get_pressed()[0]:  # Botão esquerdo do mouse
                pos = pygame.mouse.get_pos()
                if pos[1] >= ALTURA:
                    continue
                linha, coluna = obter_posicao_mouse(pos)
                celula = grade[linha][coluna]
                if not inicio and celula != fim:
                    inicio = celula
                    inicio.cor = VERDE
                elif not fim and celula != inicio:
                    fim = celula
                    fim.cor = VERMELHO
                elif celula != inicio and celula != fim:
                    celula.parede = True
                    celula.cor = PRETO

            elif pygame.mouse.get_pressed()[2]:  # Botão direito do mouse
                pos = pygame.mouse.get_pos()
                if pos[1] >= ALTURA:
                    continue
                linha, coluna = obter_posicao_mouse(pos)
                celula = grade[linha][coluna]
                if celula == inicio:
                    inicio = None
                elif celula == fim:
                    fim = None
                celula.parede = False
                celula.cor = BRANCO

            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 2:  # Botão do meio do mouse
                pos = pygame.mouse.get_pos()
                if pos[1] < ALTURA:
                    definir_peso(grade, pos)

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE and inicio and fim:
                    for linha in grade:
                        for celula in linha:
                            celula.atualizar_vizinhos(grade)
                    dijkstra(grade, inicio, fim)

                if evento.key == pygame.K_c:
                    inicio = None
                    fim = None
                    grade = criar_grade()

    pygame.quit()

if __name__ == "__main__":
    main()