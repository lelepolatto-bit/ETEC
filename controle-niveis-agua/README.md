# Controle de Níveis de Água

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Reposit%C3%B3rio-black?logo=github&logoColor=white)
![Água](https://img.shields.io/badge/Água-Monitoramento-0891b2)

Atividade acadêmica da ETEC desenvolvida em **Python** para representar o monitoramento do nível de água de um reservatório. O programa informa a situação atual usando uma mensagem e uma cor correspondente.

## Objetivo

Praticar o uso de listas, funções, estruturas condicionais e bibliotecas externas em Python por meio de um sistema simples de controle de níveis de água.

## Funcionamento

1. A lista `mensagens` armazena as descrições dos cinco níveis de água.
2. A lista `cores` armazena as cores correspondentes da biblioteca `colorama`.
3. A função `exibir_nivel` verifica se o nível informado está entre 1 e 5.
4. Quando o nível é válido, o programa calcula o índice da lista e exibe a mensagem com sua cor.
5. Quando o nível está fora do intervalo permitido, o programa informa que ele é inválido.

O valor usado na execução é definido na variável `nivel_atual`. No código da atividade, essa variável possui o valor `3`, correspondente ao nível **Médio**.

## Classificação dos níveis

| Nível | Mensagem | Cor |
| --- | --- | --- |
| 1 | Muito baixo (crítico) | Vermelho |
| 2 | Baixo | Amarelo |
| 3 | Médio | Verde |
| 4 | Alto | Ciano |
| 5 | Muito alto (alerta) | Azul |

## Conceitos utilizados

- **Listas**: armazenam as mensagens e as cores dos níveis.
- **Função**: organiza a verificação e a exibição do nível.
- **`if` e `else`**: validam se o valor informado está dentro do intervalo permitido.
- **Índices**: permitem acessar os itens correspondentes nas duas listas.
- **`len()`**: identifica a quantidade de níveis cadastrados.
- **Colorama**: adiciona cores ao texto exibido no terminal.

## Requisito

É necessário ter o Python 3 instalado e adicionar a biblioteca `colorama` ao ambiente:

```bash
python3 -m pip install colorama
```

## Como executar

Com o terminal aberto na raiz do repositório, execute:

```bash
cd controle-niveis-agua
python3 controle_niveis_agua.py
```

## Exemplo de execução

Para `nivel_atual = 3`, o programa apresenta:

```text
=== Monitoramento do Reservatório ===
Médio
```

A palavra `Médio` é exibida em verde quando o terminal oferece suporte a cores.

Para testar outra situação, altere o valor da variável `nivel_atual` para um número de 1 a 5.

## Estrutura

```text
controle-niveis-agua/
├── controle_niveis_agua.py
└── README.md
```

- **`controle_niveis_agua.py`**: código do monitoramento do reservatório.
- **`README.md`**: documentação e instruções da atividade.

## Autora

**Letícia Polatto**<br>
Desenvolvimento de Sistemas — ETEC
