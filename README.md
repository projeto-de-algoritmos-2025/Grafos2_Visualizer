# 🧩 Labirinto Dijkstra — Grafos2_Visualizer

*Projeto da disciplina de Grafos 2 — Aplicação prática com visualização interativa em Pygame*

## 👥 Alunos
| Matrícula | Nome |
|----------|------|
| 22/2006641 | Davi de Aguiar Vieira |
| 22/2006801 | Henrique Carvalho Neves |

## 📝 Entregas
| Grafos 2 |
|----------|
| [Apresentação]() 
---


# Visualizador do Algoritmo de Dijkstra

Este é um visualizador interativo do algoritmo de Dijkstra implementado em Python utilizando a biblioteca Pygame. Ele permite que o usuário desenhe obstáculos, defina um ponto de início e um ponto final, e visualize o caminho mais curto entre eles.

## Requisitos

* Python 3.7 ou superior
* Pygame

### Instalando o Pygame

Use o pip para instalar o Pygame:

```bash
pip install pygame
```

> Dica: Recomenda-se utilizar um ambiente virtual (como `venv`) para isolar as dependências.

## Como executar

Clone o repositório ou salve o arquivo `dijkstra.py`, depois execute:

```bash
python dijkstra.py
```

Certifique-se de estar na pasta onde o arquivo está localizado.

## Como jogar

A interface consiste em uma grade onde você pode interagir com o mouse e o teclado.

### Comandos do Mouse:

* **Clique esquerdo**:

  * Primeiro clique define o ponto de **início** (verde)
  * Segundo clique define o ponto **final** (vermelho)
  * Cliques subsequentes adicionam **paredes** (obstáculos pretos)

* **Clique direito**:

  * Remove o conteúdo da célula (ponto ou parede)

### Teclas do Teclado:

* **Espaço**: Inicia o algoritmo de Dijkstra para encontrar o caminho mais curto entre o ponto de início e o final.
* **C**: Limpa a grade inteira, permitindo começar do zero.

## Recursos

* Caminho calculado é exibido em **amarelo**
* Células exploradas pelo algoritmo são mostradas em **azul**
* Algoritmo considera apenas movimentação em quatro direções (cima, baixo, esquerda, direita)