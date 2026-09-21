# Sistema de Classificação de Consumo de Água

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Reposit%C3%B3rio-black?logo=github&logoColor=white)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen)
![Sustentabilidade](https://img.shields.io/badge/Sustentabilidade-Uso%20consciente%20da%20%C3%A1gua-0891b2)

Atividade acadêmica da ETEC desenvolvida em **Python** para classificar o consumo mensal de água conforme o tipo de imóvel e o volume informado, em metros cúbicos (m³).

## Objetivo

Praticar estruturas de decisão em Python e incentivar a reflexão sobre o uso consciente da água, apresentando uma mensagem de acordo com as regras da atividade.

## Funcionamento

1. O programa solicita o tipo de imóvel: `comercial`, `casa` ou `apartamento`.
2. Converte o texto informado para letras minúsculas com `.lower()`.
3. Solicita o consumo mensal em m³ e converte a entrada para `float`.
4. Avalia os casos com `match/case` e exibe a mensagem correspondente à primeira regra atendida.

### Classificações de consumo

| Tipo de imóvel | Consumo mensal | Resultado |
| --- | --- | --- |
| Comercial | Qualquer valor numérico | Tarifa comercial aplicada; consultar o plano corporativo. |
| Apartamento | Menor que 10 m³ | Consumo econômico. |
| Apartamento | De 10 até 25 m³, inclusive | Consumo moderado. |
| Casa | Até 25 m³, inclusive | Consumo moderado. |
| Casa ou apartamento | Acima de 25 m³ | Consumo excessivo; economizar e verificar vazamentos. |
| Outros tipos informados | Qualquer valor numérico | Regra padrão: mensagem de consumo excessivo. |

As classificações seguem as regras didáticas do programa. O sistema não calcula o valor da conta de água.

### Conceitos utilizados

- **`input()`**: recebe os dados digitados no terminal.
- **`float`**: converte o consumo para um número que pode ter casas decimais.
- **`match/case`**: seleciona a regra de acordo com o tipo de imóvel.
- **Condições com `if`**: acrescentam verificações de consumo aos casos.
- **Operadores de comparação `<` e `<=`**: verificam os limites de consumo.
- **Operador `|` no `match`**: permite alternativas, como `"apartamento" | "casa"`.
- **`case _`**: trata os casos que não correspondem às regras anteriores.

## Tecnologias

| Tecnologia | Utilização |
| --- | --- |
| **Python 3.10 ou superior** | Linguagem utilizada; suporte à estrutura `match/case`. |
| **Terminal** | Entrada dos dados e exibição do resultado. |
| **Git e GitHub** | Versionamento e hospedagem do projeto. |
| **Markdown** | Documentação do projeto. |

O programa utiliza apenas recursos nativos do Python e não exige instalação de bibliotecas externas.

## Como executar

Com **Python 3.10 ou superior** instalado, baixe ou clone este repositório e abra o terminal na raiz dele. Execute:

```bash
cd consumo-agua
python3 app.py
```

Informe o tipo de imóvel e o consumo quando solicitado. Para valores decimais, use ponto, por exemplo: `12.5`.

Digite o tipo de imóvel sem espaços antes ou depois do nome. A entrada de consumo deve ser numérica; o programa não implementa tratamento para texto inválido nem validação de valores negativos.

### Exemplo de execução

```text
Seu imóvel é comercial, casa ou apartamento? apartamento
Qual o seu consumo mensal, em m³, de água? 8
Consumo econômico - excelente controle de água!
```

## Estrutura

```text
consumo-agua/
├── app.py
└── README.md
```

- **`app.py`**: programa de classificação de consumo de água.
- **`README.md`**: documentação e instruções de execução.

## 👩‍💻 Autora

**Letícia Polatto**  
Atividade acadêmica — ETEC.
