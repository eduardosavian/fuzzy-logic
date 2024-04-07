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
./jfuzzy.sh -e src/formula1.fcl 5.0 5.0 5.0 5.0
```

## Theory

### Qualificadores

#### Tyre Condition (1.0 - 0.0)

- Prime Performance : 1.0 - 0.8
- Optimal : 0.8 - 0.7
- Competitive 0.7 - 0.5
- Compromised : 0.5 - 0.05
- Degraded : 0.05 - 0.0

### Race Progress (1.0 - 0.0)

- Start: 1.0 - 0.33
- Middle: 0.20 - 0.60
- End: 0.60 - 0.0
- Final Straight: 0.95 - 1.0

### Fuel Level (1.0 - 0.0)

- Low: 1.0 - 0.33
- Ok (Light): 0.25 - 0.5
- Ok (Heavy): 0.5 - 0.75
- Full: 0.7 - 1.0

### Performance Rating

- Poor: 0 - 10
- Fair: 5 - 15
- Average: 10 - 20
- Good: 15 - 25
- Excellent: 20 - 30

### Race Position (1.0 - 0.0)

- Terrible: 1.0 - 0.333
- Bad: 0.125 - 0.5
- Average: 0.70 - 0.8
- Good: 0.85 - 0.9
- Excellent: 0.9 - 1.0

### Saida

- Urgencia de PitStop
- 0, 0.33:   TudoOk
- 0.2, 0.5:  PodeEsperar
- 0.4, 0.7:  RiscoElevado
- 0.66, 1.0: Urgente

## References

- [JFUzzy](https://jfuzzylogic.sourceforge.net/html/index.html)
