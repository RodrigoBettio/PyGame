# Projeto PyGame: Primeiras Experiências

Este projeto foi desenvolvido como uma introdução ao **Pygame**, uma biblioteca popular de Python para o desenvolvimento de jogos. Durante este projeto, foi possível aprender conceitos fundamentais do Pygame, como a criação de janelas, manipulação de eventos e controle de gráficos.

## Instalação

Para rodar este projeto, siga os passos abaixo:

1. Clone o repositório:

    ```bash
    git clone https://github.com/RodrigoBettio/PyGame.git
    ```

2. Instale as dependências:

    ```bash
    pip install pygame
    ```

3. Execute o jogo:

    ```bash
    python main.py
    ```

## Como Jogar

- Utilize as **setas direcionais** (esquerda, direita, cima e baixo) para mover o personagem.
- O objetivo é alcançar o quadrado verde no canto inferior direito do labirinto.
- Evite colidir com as paredes representadas pela cor cinza.

## Detalhes do Código

O jogo foi desenvolvido utilizando o Pygame e consiste em:

- **Configuração da Tela**: A tela do jogo é inicializada com dimensões de 800x600 pixels.
- **Personagem e Objetivo**: O personagem é representado por uma imagem (`mario.png`) e o objetivo é um quadrado verde.
- **Labirinto**: O labirinto é composto por retângulos (paredes) que o personagem deve evitar.
- **Movimentação e Colisão**: O personagem pode se mover pelas setas do teclado, e a colisão com as paredes é verificada antes de permitir o movimento.
