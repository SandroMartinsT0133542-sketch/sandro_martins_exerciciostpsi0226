# Exercícios de Python

Este repositório reúne um conjunto de exercícios de iniciação a Python, com foco em estruturas condicionais, ciclos, `match/case` e funções auxiliares. O projeto foi organizado para permitir uma exploração simples, com scripts interativos que podem ser executados diretamente na consola.

## Atualizações Recentes

- 13/03/2026: adicionado `run_tests.py` na raiz para executar os testes sem dependência de manipulação manual de `sys.path` nos ficheiros de teste.
- 13/03/2026: ajustados imports de testes e de `Exercicios/exec_loop.py` para funcionamento correto em modo package (`Exercicios`).
- 13/03/2026: corrigido `Exercicios/test_loop.py` para validar output de `exec1()` e permitir import correto ao correr testes desde a raiz do projeto.
- 13/03/2026: refatorado `Exercicios/exec_loop.py` para estrutura 100% baseada em funções (`exec1` a `exec22`) chamadas automaticamente em `main()`.
- 13/03/2026: corrigido o teste em `Exercicios/test_utils.py` para usar `mock.patch` com `from unittest import mock`, garantindo compatibilidade na execução dos testes.
- Testes unitários de `Exercicios/utils.py` validados com sucesso (`3 tests OK`).

## Regra de Manutenção

- A cada alteração de código relevante, este `README.md` deve ser atualizado para refletir as mudanças.

## Objetivo

Este projeto foi pensado para praticar:

- Leitura e validação de dados introduzidos pelo utilizador.
- Estruturas de decisão com `if/elif/else`.
- Repetições com ciclos.
- Padrões com `match/case`.
- Criação e teste de funções auxiliares.

## Estrutura do Projeto

- `Exercicios/exec_if.py` contém exercícios centrados em estruturas condicionais.
- `Exercicios/exec_loop.py` contém exercícios com ciclos e interação contínua com o utilizador.
- `Exercicios/exec_match.py` contém exercícios baseados em `match/case`.
- `Exercicios/utils.py` reúne funções auxiliares reutilizáveis.
- `Exercicios/test_utils.py` contém testes unitários para as funções auxiliares.

## Requisitos

- Python 3.10 ou superior.
- PowerShell no Windows, caso pretenda usar exatamente os comandos apresentados abaixo.

## Como Executar

A partir da raiz do projeto, pode executar os scripts de duas formas.

### Opção recomendada (venv do projeto no Windows)

```powershell
& .\.venv\Scripts\python.exe .\Exercicios\exec_if.py
& .\.venv\Scripts\python.exe .\Exercicios\exec_loop.py
& .\.venv\Scripts\python.exe .\Exercicios\exec_match.py
```

### Opção alternativa (entrar na pasta Exercicios)

```powershell
Set-Location Exercicios
```

Depois execute o ficheiro pretendido:

```powershell
python exec_if.py
python exec_loop.py
python exec_match.py
```

Se o comando `python` não estiver associado à versão correta do Python no seu sistema, pode usar:

```powershell
py exec_if.py
py exec_loop.py
py exec_match.py
```

Em alternativa, pode indicar explicitamente o caminho do interpretador:

```powershell
& C:/Python313/python.exe exec_loop.py
```

## O Que Esperar dos Scripts

- Os ficheiros principais são interativos e pedem dados ao utilizador ao longo da execução.
- Cada script pode executar vários exercícios de seguida.
- A maior parte dos resultados é apresentada diretamente no terminal.

## Testes

Os testes automáticos disponíveis incidem sobre as funções definidas em `Exercicios/utils.py`.

Para executar todos os testes a partir da raiz do projeto:

```powershell
& .\.venv\Scripts\python.exe .\run_tests.py
```

Forma alternativa:

```powershell
Set-Location Exercicios
& ..\.venv\Scripts\python.exe -m unittest discover -p "test*.py"
```

Em alternativa, para um ficheiro especifico:

```powershell
& .\.venv\Scripts\python.exe .\Exercicios\test_utils.py
```

## Validação Técnica

- Compilação de verificação efetuada com `python -m compileall .` sem erros de sintaxe.
- Estado atual dos testes: `OK` (5 testes).

## Funções Auxiliares

O ficheiro `Exercicios/utils.py` inclui atualmente:

- `print_client`, para apresentar os dados de um cliente num formato estruturado.
- `print_tabuada`, para mostrar a tabuada de um número.

## Notas

- O projeto não depende de bibliotecas externas.
- Basta ter Python instalado para executar os scripts e os testes.
- O conteúdo do projeto está orientado para prática e aprendizagem, não para utilização em produção.

## Assinatura

Documento mantido e atualizado com apoio do GitHub Copilot.
