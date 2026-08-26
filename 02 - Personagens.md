# Personagens

Cada Condutor controla uma equipe composta por cinco personagens, um de cada classe: Tanque, DPS, Atirador, Mago e Suporte. Cada personagem possui atributos próprios e habilidades que definem seu papel em combate.

---

# Tanques
Personagens que devem ser capazes de suportar muito dano.

## Atributos

| Atributo  | Valor |
|-----------|------:|
| Vida      | 7 |
| Movimento | 4 |
| Ataque    | 3 |
| Alcance   | 1 |

## Cavaleiro
### Habilidades

#### Investida *(Ação Especial)* 
- Se você ainda não moveu uma peça neste turno, pode mover o Cavaleiro até **4 casas em linha reta** (não diagonalmente). Durante essa investida, ele pode atravessar outras peças.
Cada peça atravessada sofre **2 de dano**.

## Hoplita Grego
### Habilidades

#### Muralha de Escudos *(Passiva)*
- Enquanto o Hoplita Grego estiver adjacente a pelo menos um aliado, ele e todos os aliados ortogonalmente adjacentes a ele recebem -1 de dano.

---

# DPS
Personagens focados em dano.

## Atributos

| Atributo  | Valor |
|-----------|------:|
| Vida      | 6 |
| Movimento | 3 |
| Ataque    | 4 |
| Alcance   | 1 |

## Bárbaro
### Habilidades

#### Medo do Sobrenatural *(Passiva)* 
- O Bárbaro sofre **+1 de dano** sempre que recebe dano de um **Mago**.

## Samurai
### Habilidades

#### Corte Preciso *(Passiva)*
- Ataques realizados na diagonal causam o dano normal do Samurai. Ataques realizados ortogonalmente causam apenas 2 de dano.

---

# Atiradores
Personagens focados em dano a longo alcance.

## Atributos

| Atributo  | Valor |
|-----------|------:|
| Vida      | 5 |
| Movimento | 2 |
| Ataque    | 2 |
| Alcance   | 3 |

## Besteiro
### Habilidades

#### Olho Longo *(Ação Especial)* 
- Realiza um ataque com **alcance ilimitado**, em linha reta (inclusive diagonalmente).
Esse ataque causa **1 de dano** e **não pode atravessar outras peças**.

#### Travessia *(Passiva)* 
- Pode mover-se e atacar na diagonal.

#### Mira Cuidadosa *(Passiva)* 
- Se não se moveu desde o turno anterior, seu ataque normal causa **+1 de dano**.

## - Guerreiro Tupi
### Habilidades

#### Fumaça Venenosa *(Ação Especial)* 
- Alcance 3, pode atacar na diagonal. Cause 1 de dano ao alvo. Um inimigo adjacente ao alvo, à sua escolha, também sofre 1 de dano.

#### Caçador da Mata *(Passiva)* 
- Após realizar um ataque normal, o Guerreiro Tupi pode mover 1 casa, inclusive na diagonal.

#### Caçador Nato *(Passiva)* 
- O Guerreiro Tupi pode realizar ataques normais na diagonal.

---

# Mago
Personagens focados em uso de habilidades.

## Atributos

| Atributo  | Valor |
|-----------|------:|
| Vida      | 4 |
| Movimento | 2 |
| Ataque    | 1 |
| Alcance   | 2 |

## Mago Negro
### Habilidades

#### Bomba Mágica *(1 vez por partida)* 
- Escolha uma casa dentro do alcance. Todas as peças nessa casa e nas casas ortogonalmente adjacentes sofrem **2 de dano**.

#### Maldição *(Ação Especial)* 
- O Mago Negro sofre **X de dano**. Escolha um inimigo dentro do alcance. Esse inimigo sofre **X + 1 de dano**.

#### Animar Morto *(Ação Especial)* 
- O Mago Negro sofre **1 de dano**. Ressuscite uma peça aliada destruída em uma casa livre da Zona Inicial. Ela retorna com **2 pontos de vida**.

## Druida
### Habilidades

#### Ira da Natureza *(1 vez por partida)*
- Escolha uma linha do tabuleiro. Vinhas percorrem toda a linha causando 1 de dano em todas as peças atingidas. No próximo turno, as peças atingidas não podem se mover. O Druida não sofre dano desta habilidade.

#### Cipós  *(Ação Especial)* 
- Escolha uma peça inimiga dentro do alcance. Mova-a até duas casas adjacentes livres, em linhas retas ou na diagonal.

#### Espírito do Lobo *(Ação Especial)* 
- Escolha um aliado dentro do alcance. Até o fim do turno, ele recebe +2 de Movimento.

---

# Suporte

## Atributos

| Atributo  | Valor |
|-----------|------:|
| Vida      | 4 |
| Movimento | 2 |
| Ataque    | 1 |
| Alcance   | 2 |

## Clérigo
### Habilidades

#### Conversão *(Ação Especial)* 
- Assuma permanentemente o controle de uma peça inimiga com **2 ou menos pontos de vida** dentro do alcance.

#### Cura *(Ação Especial)* 
- Uma peça aliada dentro do alcance recupera **3 pontos de vida**, até seu valor inicial. O Clérigo **não pode curar a si mesmo**.

#### Confinamento Místico *(1 vez por partida)*
- Uma peça inimiga dentro do alcance fica presa no tempo. Ela não pode mover-se, atacar, usar habilidade nem ser atacada. Duração de 2 turnos.

## Mártir
### Habilidades

#### Sacrifício *(1 vez por partida)* 
- Quando um aliado em qualquer lugar do mapa estiver com 1 de vida, você pode eliminar este personagem para recuperar toda a vida do aliado ferido.

#### Transferência Vital
- Sofra 1 de dano. Escolha um aliado dentro do alcance para recuperar 4 de Vida.

#### Regeneração 
- Recupere 1 de Vida.

---

# Habilidades em Desenvolvimento e Sem Classe Definida
- Habilidade que troca de lugar com outro.
- Habilidade de teletransporte.
- Raiz Faminta - Escolha uma peça. Ela sofre 1 de dano.Cure 1 de Vida do Druida.
- Bosque Vivo - Alcance: 3 - Escolha uma casa vazia. Até o início do seu próximo turno, essa casa não pode ser atravessada nem ocupada.
- Reincarnação (druida) - Escolha um aliado derrotado. Ele retorna para o jogo como um esquilo (colocar mais opções de animais). Ele aparece na zona inicial. Somente um esquilo ativo por jogo. (2 vida, 3 mov, 1 atq, 1 alc)
- Vampiric Strike - Cada vez que der ataque com o ataque básico, cura 1 vida.
- Stick Charge - Move in a straight line, pushing an enemy unit and dealing 2 dmg. The mov ends if the pushed unit collides with another unit or if the rider runs out of movement.
- Healing Sprouts - Place 2 berries in free spaces within range. Each berry heals 1 hp when an ally unit enters its space.
- Oven guard - Prepare a 1 tile Parry Zone around the squire until your next turn. While its active: reduce the firts melee attack received in this zone by 2, or negate the first projectile that crosses this zone.





