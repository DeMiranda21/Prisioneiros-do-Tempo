# Personagens

Cada Condutor controla uma equipe composta por cinco personagens, um de cada classe. Cada personagem possui atributos próprios e habilidades que definem seu papel em combate.

---

# Tanques

## Cavaleiro

### Atributos

| Atributo  | Valor |
|-----------|------:|
| Vida      | 7 |
| Movimento | 4 |
| Ataque    | 3 |
| Alcance   | 1 |

### Habilidades

#### Investida *(Ação Especial)*

Se você ainda não moveu uma peça neste turno, pode mover o Cavaleiro até **4 casas em linha reta** (não diagonalmente).

Durante essa investida, ele pode atravessar outras peças.

Cada peça atravessada sofre **2 de dano**.

### Função

- Alta resistência.
- Excelente para iniciar confrontos.
- Ideal para bloquear corredores e proteger aliados.

---

# DPS

## Bárbaro

### Atributos

| Atributo  | Valor |
|-----------|------:|
| Vida      | 6 |
| Movimento | 3 |
| Ataque    | 4 |
| Alcance   | 1 |

### Habilidades

### Passivo

#### Medo do Sobrenatural *(Passiva)*

O Bárbaro sofre **+1 de dano** sempre que recebe dano de um **Mago Negro**.

### Função

- Alto dano corpo a corpo.
- Grande capacidade ofensiva.
- Vulnerável contra magia.

---

# Atiradores

## Besteiro

### Atributos

| Atributo  | Valor |
|-----------|------:|
| Vida      | 5 |
| Movimento | 2 |
| Ataque    | 2 |
| Alcance   | 3 |

## Habilidades

### Olho Longo *(Ação Especial)*

Realiza um ataque com **alcance ilimitado**, em linha reta (inclusive diagonalmente).

Esse ataque causa **1 de dano** e **não pode atravessar outras peças**.

## Passivos

### Travessia *(Passiva)*

Pode mover-se e atacar na diagonal.

### Mira Cuidadosa *(Passiva)*

Se não se moveu desde o turno anterior, seu ataque normal causa **+1 de dano**.

### Função

- Especialista em combate à distância.
- Excelente para controlar corredores.
- Recompensa posicionamento estratégico.

---

# Mago

## Mago Negro

## Atributos

| Atributo  | Valor |
|-----------|------:|
| Vida      | 4 |
| Movimento | 2 |
| Ataque    | 1 |
| Alcance   | 2 |

### Habilidades

#### Bomba Mágica *(1 vez por partida)*

Escolha uma casa dentro do alcance.

Todas as peças nessa casa e nas casas ortogonalmente adjacentes sofrem **2 de dano**.

#### Maldição

O Mago Negro sofre **X de dano**.

Escolha um inimigo dentro do alcance.

Esse inimigo sofre **X + 1 de dano**.

#### Animar Morto

O Mago Negro sofre **1 de dano**.

Ressuscite uma peça aliada destruída em uma casa livre da Zona Inicial.

Ela retorna com **2 pontos de vida**.

### Função

- Controle de área.
- Alto potencial tático.
- Sacrifica a própria vida para utilizar habilidades poderosas.

---

# Suporte

## Clérigo

### Atributos

| Atributo  | Valor |
|-----------|------:|
| Vida      | 4 |
| Movimento | 2 |
| Ataque    | 1 |
| Alcance   | 2 |

### Habilidades

#### Conversão

Assuma permanentemente o controle de uma peça inimiga com **2 ou menos pontos de vida** dentro do alcance.

#### Cura

Uma peça aliada dentro do alcance recupera **3 pontos de vida**, até seu valor inicial.

O Clérigo **não pode curar a si mesmo**.

#### Confinamento Místico *(1 vez por partida)*

Uma peça inimiga dentro do alcance fica presa no tempo. Ela não pode mover-se, atacar, usar habilidade nem ser atacada. Pode ser movida por habilidades de deslocamento, porém não toma dano. Duração de 2 turnos.


### Função

- Suporte da equipe.
- Cura aliados.
- Pode converter inimigos enfraquecidos.
- Controla o campo de batalha através do Confinamento Místico.

# Personagens em Criação

## Habilidades em Desenvolvimento e Sem Classe Definida
- Habilidade que empurra aliado.
- Habilidade que troca de lugar com outro.
- Habilidade de teletransporte.
- Habilidade de cura através de doação de hp.
- Escudo de Bronze: Na primeira vez que sofrer dano em cada rodada, reduza esse dano em 1.
- Escudos Unidos: Sempre que um aliado adjacente sofrer um ataque, o Hoplita pode sofrer 1 ponto desse dano em seu lugar.

## Hoplita Grego - 2º Tanque
- Habilidade — Muralha de Escudos 
Enquanto o Hoplita Grego estiver adjacente a pelo menos um aliado, ele e todos os aliados ortogonalmente adjacentes a ele recebem -1 de dano.

- (Não implementada) Passiva (Em teste, implementar quando tiver deslocamento no jogo, vai ter que colocar passivo para o cavaleiro) - Linha Inquebrável: Aliados adjacentes ao Hoplita não podem ser empurrados ou deslocados por habilidades.

## - Samurai - 2º DPS
- Corte Preciso (Passiva)
Ataques realizados na diagonal causam o dano normal do Samurai. Ataques realizados ortogonalmente causam apenas 2 de dano.

## - Guerreiro Tupi - 2º Atirador
Usa a zarabatana
- Habilidade — Flecha Envenenada - Alcance 3. Causa 1 de dano. No início do próximo turno do alvo, ele sofre mais 1 de dano.
- Caçador da Mata (Passiva) - Após realizar um ataque, o Guerreiro Tupi pode mover 1 casa, inclusive na diagonal.
- (Não implementada) Caçador Nato (Passiva) - O Guerreiro Tupi pode realizar ataques normais na diagonal.

