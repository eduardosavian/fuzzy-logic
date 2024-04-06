# fuzzy-system

## Description

- Modelar e implementar uma solução de Sistema Fuzzy, para um problema escolhido pela equipe.

- A solução deverá ser apresentada, com o detalhamento do problema e as especificações de modelagem da solução (variáveis, funções, regras e demais escolhas feitas) e execução do sistema.

- A implementação deve ser feita no JFuzzyLogic, MatLab ou outra ferramenta para implementação de Sistemas Fuzzy.

- A apresentação devera ser feita por meio de um video gravado e o link postado junto com a implementação na atividade (até o horário especificado de entrega). As apresentações devem ter entre 5 e 10 minutos.

OBS.:

- Na aula anterior a data da entrega deverá ser apresentado para o professor o problema e a modelagem feita para aferição da pertinencia do proproblema e da modelagem.

- A trabalho em sala e a discussão da modelagem, antes da entrega final, fazem parte da avaliação do trabalho.

## Run

```bash
chmod +x jfuzzy.sh
```

```bash
./jfuzzy.sh work.fcl
```

## Theory

### Qualificadores

#### Desgaste do Pneu (0 - 1.0)

- 0, 0.05:  Nenhum
- 0.1, 0.5: Levemente desgastado
- 0.2, 0.7: Parcialmente desgastado
- 0.8, 1.0: Muito desgastado

#### Posicao na corrida (0 - 1.0)

-(C - p)/p
-C := numero de participantes
-p := posicao atual

- 0, 0.333: Pessimo
- 0.125, 0.5: Ruim
- 0.70, 0.8:  Mediano
- 0.85, 0.9:  Bem
- 0.9, 1.0:   Excelente

#### Progresso da corrida

- 0.0, 0.33:  Inicio
- 0.20, 0.60: Meio
- 0.60, 1:    Final
- 0.95, 1.0:  Reta Final

#### Nivel de combustivel

- 0.0,  0.33: Pouco
- 0.25, 0.5:  OkLeve
- 0.5,  0.75: OkPesado
- 0.7,  1.0:  Cheio

### Saida

- Urgencia de PitStop
- 0, 0.33:   TudoOk
- 0.2, 0.5:  PodeEsperar
- 0.4, 0.7:  RiscoElevado
- 0.66, 1.0: Urgente

## References

- [JFUzzy](https://jfuzzylogic.sourceforge.net/html/index.html)
