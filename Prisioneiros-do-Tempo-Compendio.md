# Prisioneiros do Tempo

## Compêndio Oficial

Este documento é gerado automaticamente pelo GitHub Actions.

---

# Contexto Oficial para IA

Este documento representa a documentação oficial do projeto **Prisioneiros do Tempo**.

Sempre que houver conflito entre este documento e qualquer conversa anterior, este documento prevalece.

Novas ideias discutidas em conversa somente passam a fazer parte do projeto após aprovação do autor e atualização da documentação oficial.

---

**Gerado em:** 01/08/2026 16:23 UTC

**Commit:** `9599a5f`

**Quantidade de documentos:** 6

---

# Índice

- [01 - Regras e Mecânicas.md](#01---regras-e-mecânicasmd)
- [02 - Personagens.md](#02---personagensmd)
- [03 - Mapas.md](#03---mapasmd)
- [04 - Lore.md](#04---loremd)
- [05 - Backlog.md](#05---backlogmd)
- [README.md](#readmemd)


---


================================================================================

<a id="01---regras-e-mecânicasmd"></a>

# 01 - Regras e Mecânicas.md

*Arquivo original:* `01 - Regras e Mecânicas.md`

---

# Regras e Mecânicas

## Objetivo

O objetivo da partida é:

- Eliminar todas as peças do adversário; ou
- Alcançar **4 pontos**, obtidos ao eliminar peças inimigas.

---

## Componentes

Para o protótipo são utilizados:

- 1 tabuleiro de xadrez (8×8);
- Peças de xadrez representando os personagens;
- Peças de dama representando obstáculos.

---

## Preparação

1. Escolha um mapa ou jogue o dado para um mapa aleatório (um número para cada mapa).
2. Posicione os obstáculos conforme o mapa escolhido.
3. Decida aleatoriamente quem inicia a partida.
4. Os jogadores alternam posicionando suas peças na Zona Inicial.
5. O jogador que posicionou a primeira peça realiza o primeiro turno.

---

## Turno

Em seu turno, cada jogador pode:

1. Mover uma peça;
2. Realizar uma ação.

A ação pode ser:

- Ataque;
- Habilidade Especial.

Após realizar uma ação, a peça não pode mais se mover naquele turno.

---

## Movimento

- As peças movem-se apenas na horizontal e vertical.
- Cada personagem possui um valor de Movimento.
- Movimentos diagonais somente quando uma habilidade permitir.
- Não é permitido atravessar peças.
- Não é permitido terminar o movimento sobre outra peça.

---

## Ataques

- Os ataques são realizados em linha reta.
- Cada personagem possui um valor de Alcance.
- Ataques diagonais somente quando uma habilidade permitir.
- Ataques não atravessam peças nem obstáculos.

Quando uma peça recebe dano, perde Vida igual ao Ataque do agressor.

Ao chegar a 0 de Vida, ela é removida do tabuleiro.

---

## Obstáculos

Os obstáculos:

- bloqueiam movimento;
- bloqueiam ataques;
- não podem ser ocupados;
- não podem ser destruídos.

---

## Ressurreição

Algumas habilidades permitem ressuscitar personagens.

Sempre que uma peça inimiga é eliminada, seu controlador recebe **1 ponto**.

Caso essa peça seja posteriormente ressuscitada, esse ponto é perdido.

---

## Efeitos

### Confinamento Místico

Uma peça sob Confinamento Místico:

- não pode mover-se;
- não pode atacar;
- não pode utilizar habilidades;
- não pode ser alvo de ataques.

---

## Vitória

A partida termina imediatamente quando:

- um jogador elimina todas as peças adversárias; ou
- um jogador alcança **4 pontos**.




================================================================================

<a id="02---personagensmd"></a>

# 02 - Personagens.md

*Arquivo original:* `02 - Personagens.md`

---

# Personagens

Cada Condutor controla uma equipe composta por cinco personagens, um de cada classe. Cada personagem possui atributos próprios e habilidades que definem seu papel em combate.

---

# Tanques

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
- Escolha uma linha do tabuleiro. Vinhas percorrem toda a linha. Todas as peças atingidas sofrem 1 de dano. No próximo turno, as peças atingidas não podem se mover. O Druida não sofre dano desta habilidade.

#### Cipós  *(Ação Especial)* 
- Escolha uma peça inimiga dentro do alcance. Mova-a até duas casas adjacentes livres, na ortogonal, não pode mover na diagonal.

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
- Uma peça inimiga dentro do alcance fica presa no tempo. Ela não pode mover-se, atacar, usar habilidade nem ser atacada. Pode ser movida por habilidades de deslocamento, porém não toma dano. Duração de 2 turnos.

## Mártir

### Habilidades

#### Sacrifício *(1 vez por partida)* 
- Quando um aliado em qualquer lugar do mapa estiver com 1 de vida, você pode eliminar este personagem para recuperar toda a vida do aliado ferido.

#### Transferência Vital
- Sofra 1 de dano. Um aliado recupera 2 de Vida.

#### Regeneração 
- Recupere 1 de Vida.

---

# Habilidades em Desenvolvimento e Sem Classe Definida
- Habilidade que empurra aliado.
- Habilidade que troca de lugar com outro.
- Habilidade de teletransporte.
- Escudo de Bronze: Na primeira vez que sofrer dano em cada rodada, reduza esse dano em 1.
- Raiz Faminta - Escolha uma peça. Ela sofre 1 de dano.Cure 1 de Vida do Druida.
- Linha Inquebrável: Aliados adjacentes ao Hoplita não podem ser empurrados ou deslocados por habilidades.
- Habilidade Normal - Bosque Vivo - Alcance: 3 - Escolha uma casa vazia. Até o início do seu próximo turno, essa casa não pode ser atravessada nem ocupada.









================================================================================

<a id="03---mapasmd"></a>

# 03 - Mapas.md

*Arquivo original:* `03 - Mapas.md`

---

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




================================================================================

<a id="04---loremd"></a>

# 04 - Lore.md

*Arquivo original:* `04 - Lore.md`

---

# Lore

Este documento reúne a história do universo, suas leis, facções, personagens e eventos relevantes.

## Ideias Gerais

- Personagens presos dentro de um loop temporal (justifica várias partidas).
- **Convergência:** o loop gera um desgaste na linha temporal; algo força o loop para tentar romper.
- Qual o objetivo/razão das guerras?
  - Por que são jogados dentro do loop?
  - Quem ou o que os lançou ali?
  - Por qual razão?
  - **Desenvolver.**
- Como foram parar dentro do loop? (justifica a entrada de novos personagens.)
  - **Desenvolver.**
- Personagens de várias épocas (boa justificativa para classes misturadas).
  - **Convergência.**
- Criar um lore para diferentes cenários e modos de jogo:
  - Defender uma zona.
  - Recuperar um item.
  - Tabuleiros maiores.
  - Partidas com mais de dois jogadores.

---

## Perguntas Fundamentais

- O que é a Convergência?
- Quem criou o loop?
- Por que os guerreiros foram escolhidos?
- Quem são realmente os Condutores?
- É possível quebrar o ciclo?

---

## Observação

> Colocar como **Leis do Destempo**.

---

# Rascunho

Ninguém sabe quando a primeira batalha começou.

Cavaleiros, mercenários e guerreiros de eras distantes acordam no mesmo mundo. Em um piscar de olhos, são arrancados de seu tempo e lançados em um conflito que não tem fim.

Quando caem em combate, não encontram a morte. Despertam novamente, lembrando apenas fragmentos das incontáveis batalhas que já travaram.

Os sábios chamam esse lugar de **Convergência**. Um domínio onde o tempo se rompeu, fazendo épocas e mundos colidirem. Ali, nenhuma vitória é definitiva e nenhuma derrota é o fim.

Mas há algo ainda mais estranho.

Sempre que uma batalha começa, cada guerreiro sente uma presença invadir sua mente. Uma vontade invisível conduz seus passos, escolhe seus caminhos e decide seus ataques.

Essas entidades jamais foram vistas, mas todos conhecem seu nome: **Condutores**.

Alguns acreditam que sejam deuses. Outros, espíritos ancestrais. Há quem diga que são ecos de um mundo além da própria Convergência.

Os guerreiros aprenderam a conviver com essa influência. Alguns resistem. Outros entregam sua confiança aos Condutores, esperando que, entre as infinitas batalhas repetidas pelo tempo, um deles encontre finalmente o caminho capaz de romper o ciclo.

Até lá…

**A guerra continua.**




================================================================================

<a id="05---backlogmd"></a>

# 05 - Backlog.md

*Arquivo original:* `05 - Backlog.md`

---

# Backlog

## Ideias Não Testadas

Este documento reúne ideias, mecânicas experimentais e sugestões ainda não incorporadas oficialmente ao jogo. Ainda, registra testes e ideias aprovadas ou não.

### Classes
- Verificar forma prática de fazer o balanceamento de classes usando agentes AI.

### Modo de Jogo 
- Modo de defender zona; - Somar com a introdução de personagem que empurre.
- Modo de recuperar item; -  Moeda para baú a ser capturado (ganha um ponto?)
- Modo Cooperativo;
- Modo de partida com mais de 2 jogadores;
- Modo de Ondas - Um mestre de jogo, roda o dado para saber qual classe vai controlar, começa com um e cada rodada tem uma peça a mais. O jogador pode fazer qualquer combinação de figuras. Os ataques de 1 por partida resetam a cada duas partidas (uma com, uma sem); O mestre de jogo não tem os ataques de 1 por partida.

### Mapas
- Usei dama para obstáculos.
- Usar portais, entra em um sai no outro;
- Zona Inicial dividida em vários locais do mapa/compartilhada.
- Mecânicas de portais, moedas, etc não devem ser fixas dos mapas, devem ser modulares. Descobrir uma forma de balancear a implementação; Qual jogador decide onde vai ser?

### Componentes
- Peças impressas em 3D;
- Tabuleiro Modular;

## Em teste
- Habilidade que empurra aliado.
- Habilidade que troca de lugar com outro.
- Habilidade de teletransporte.
- Habilidade de cura através de doação de hp.

## OBSERVAÇÕES DE PLAYTEST

### BALANCEAMENTO
- Primeira peça eliminada:
- Última peça viva:
- Habilidade mais decisiva:
- Peça menos utilizada:
- Problemas encontrados:
- Ideias surgidas:

---

# Roadmap - Versão 1.0

## 0. Identidade do Jogo
- Manter regras simples.
- Garantir que o jogo seja divertido.
- Garantir alta replayabilidade.

## 1. Personagens
- [x] Criar 10 personagens jogáveis.
- [x] 2º Tanque
- [x] 2º DPS
- [x] 2º Atirador
- [x] 2º Mago
- [x] 2º Suporte
- [ ] Balancear todos os personagens.

## 2. Mapas
- [X] Criar 6 mapas oficiais - *Falta testar cada modelo*
- [ ] Balancear todos os mapas.
- [X] Implementar seleção aleatória por dado.

## 3. Mecânicas Variáveis
### Definição
- [ ] Definir as mecânicas especiais da partida.
- [ ] Definir quais elementos pertencem aos mapas.
- [ ] Definir quais elementos serão sorteados antes da partida.

### Mecânicas em estudo
- [ ] Portais.
- [ ] Zona de Captura.
- [ ] Zona Inicial Mista.

### Implementação
- [ ] Balancear todas as mecânicas.
- [ ] Implementar seleção aleatória por dado.

## 4. Componentes
- [ ] Finalizar cartas de personagens.
- [ ] Finalizar cartas de regras.
- [ ] Finalizar cartas das mecânicas especiais.
- [ ] Finalizar tabuleiro.
- [ ] Finalizar peças.
- [ ] Finalizar marcadores.
- [ ] Preparar arquivos para impressão.

## 5. Validação
- [ ] Realizar partidas de teste.
- [ ] Corrigir problemas encontrados.
- [ ] Validar o balanceamento geral.
- [ ] Validar a diversão.
- [ ] Validar a replayabilidade.

## Critérios para conclusão da Versão 1.0
- [ ] O jogo pode ser jogado do início ao fim sem regras provisórias.
- [ ] Todos os personagens estão finalizados.
- [ ] Todos os mapas estão finalizados.
- [ ] Todas as mecânicas especiais estão finalizadas.
- [ ] Todos os componentes estão prontos para impressão.
- [ ] O jogo foi validado por partidas de teste.




================================================================================

<a id="readmemd"></a>

# README.md

*Arquivo original:* `README.md`

---

# Prisioneiros do Tempo

Projeto do jogo de tabuleiro.


