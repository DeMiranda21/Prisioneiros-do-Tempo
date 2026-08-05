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
- Mecânicas de portais, moedas, etc não devem ser fixas dos mapas, devem ser modulares. Descobrir uma forma de balancear a implementação; Qual jogador decide onde vai ser?

### Componentes
- Peças impressas em 3D;
- Tabuleiro Modular;

## Em teste
### Alterações No Modo de Jogo (Cartas de Objetivo) - Deixar para fazer somente após definir alterações de mapa e condições.
- Zona de Captura;
- Captura de Item;
### Alterações No Mapa (Cartas de Cenário)
- Relíquias/Altares - Terminar o turno na casa específica dá algum efeito. Vamos ter apenas altar de cura e de restauração de habilidade única. Vamos implementar futuramente.


### Condição da Convergência
- 01. Segunda Chance - A primeira peça eliminada na partida retorna imediatamente à Zona Inicial com 1 ponto de Vida. Essa eliminação não concede ponto. Habilidades de uso único já utilizadas não são restauradas.
- 02. Convergência - Antes do início da partida uma classe é selecionada aleatoriamente. Após a primeira eliminação da partida, as peças marcadas trocarão imediatamente de posição com a peça inimiga da mesma classe. Caso uma delas tenha sido eliminada, nada acontece com aquela classe.
- 03. Calmaria - Sem efeitos.
- 04. Pressão Constante - Nenhum jogador pode encerrar seu turno sem realizar uma ação, se houver uma ação legal disponível.
- 05. Caçada - O primeiro jogador a eliminar um personagem recebe 2 pontos em vez de 1.
- 06. Heróis da Convergência - No início da partida, sorteie uma peça de cada jogador. Enquanto permanecer viva, essa peça concede 2 pontos ao eliminar um inimigo. Quando for eliminada, concede 2 pontos ao adversário.
- 07. Última Esperança - Quando um jogador perder sua terceira peça, escolha um aliado sobrevivente. Ele recupera toda a Vida.
- 08. Exércitos Espalhados - Cada jogador deve posicionar pelo menos uma peça em cada metade da Zona Inicial.
- 09. O traidor - No início da partida, cada jogador escolhe secretamente uma peça inimiga. Após a primeira eliminação da partida, revelem as escolhas. As peças escolhidas passam imediatamente para o controle do adversário.
- 10. Forças Reservas - No início da partida, cada jogador posiciona apenas três peças. Sempre que uma peça aliada for eliminada, uma das peças restantes entra em jogo em qualquer casa livre da Zona Inicial.
- 11. Colapso Temporal - Após a primeira eliminação da partida, todas as peças retornam imediatamente às posições em que iniciaram a partida. Vida e habilidades utilizadas não são restauradas.

### Anomalias da Convergência (Alterações do Mapa)
- Portais da Convergência - Antes do início da partida, cada jogador escolhe secretamente uma casa livre do tabuleiro. Revelem simultaneamente. Essas casas tornam-se Portais da Convergência. Uma peça que terminar seu movimento sobre um Portal pode optar por ser transportada para o outro Portal. O transporte é opcional, se estiver ocupando o portal ele não pode ser usado.



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
