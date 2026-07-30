# Mapas

Este documento descreve os mapas oficiais do jogo, sua disposição de obstáculos e observações de equilíbrio.

Todos os mapas utilizam um tabuleiro 8×8 e seguem as regras oficiais do jogo.

---

## Legenda

```text
. = Casa livre
X = Obstáculo
A = Zona Inicial do Jogador A
B = Zona Inicial do Jogador B
M = Zona Inicial Mista
P = Portal (quando existir)
```

---

## 01 – A Ponte Quebrada

### Descrição

Um corredor central liga os dois lados do campo de batalha.

```text
    A B C D E F G H

8 | X A A A A A A X
7 | X X A A A A X X
6 | . . X . . X . .
5 | . . X . . X . .
4 | . . X . . X . .
3 | . . X . . X . .
2 | X X B B B B X X
1 | X B B B B B B X
```

---

## 02 – Jardim dos Ecos

### Descrição

Obstáculos espalhados criam diversos caminhos.

```text
    A B C D E F G H

8 | . . . X A A A A
7 | . X . . . . X A
6 | . . . X X . . .
5 | X . . . . . . X
4 | X . . . . . . X
3 | . . . X X . . .
2 | B X . . . . X .
1 | B B B B X . . .
```

---

## 03 – Arena da Convergência

### Descrição

Mapa aberto com obstáculos concentrados no centro.

```text
    A B C D E F G H

8 | A A A A A A A A
7 | A X . X X X X A
6 | . X . . . . X .
5 | . X . . . . X .
4 | . X . . . . X .
3 | . X . . . . X .
2 | B X X X X . X B
1 | B B B B B B B B
```

---

## 04 – Ruínas do Tempo

### Descrição

As ruínas dividem o mapa em vários corredores.

```text
    A B C D E F G H

8 | A A A A A A A A
7 | X X X . . X X X
6 | X . . . . . . .
5 | . . . . X . X .
4 | . X . X . . . .
3 | X . . . . . . X
2 | X X X . . X X X
1 | B B B B B B B B
```

---

## 05 – Fortaleza Partida

### Descrição

Dois blocos de obstáculos simulam fortalezas separadas.

```text
    A B C D E F G H

8 | A A . . . . A A
7 | A A X . . X A A
6 | . X X . . X X .
5 | . . . . . . . .
4 | . . . . . . . . 
3 | . X X . . X X .
2 | A A X . . X A A
1 | A A . . . . A A
```

---

## 06 – Bosque Silencioso (Em teste)

### Descrição

Obstáculos distribuídos de forma irregular simulam uma floresta. Mara gerado aleatoriamente, cada jogador coloca 03 peças de obstáculos (árvores), simulando uma parte qualquer da floresta.
Pode colocar na zona inicial.

```text
    A B C D E F G H

8 | A A X A X A A A
7 | A X A A A X A A
6 | . . . X . . X .
5 | X . . . . . . X
4 | X . . . . . . X
3 | . . X . X . . .
2 | B X B B B X B B
1 | B B X B X B B B
```
