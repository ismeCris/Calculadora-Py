# Calculadora Simples em Tkinter

Este mini projeto consiste na criação de uma **Calculadora funcional** utilizando a biblioteca gráfica nativa do Python, o **Tkinter**. O objetivo foi construir a interface (layout) e implementar a lógica básica de entrada de dados e cálculos matemáticos.

## Tecnologias Utilizadas
- **Python**: Linguagem de programação principal.
- **Tkinter**: Biblioteca padrão do Python para criação da interface gráfica (GUI).

## 🎨 Design e Estrutura
O design da calculadora foi baseado em um esquema de cores personalizado para separar visualmente as áreas e os tipos de botões:

| Cor Variável | Código Hexadecimal | Propósito Principal |
|--------------|------------------|------------------|
| cor1         | #127369           | Fundo principal   |
| cor4         | #4C5958           | Botões de operação |
| cor3         | #8AA6A3           | Botões numéricos  |

A interface é dividida em dois **Frames**:

- **frame_tela (Visor)**: Exibe a expressão atual e o resultado.  
- **frame_corpo (Corpo)**: Contém todos os botões da calculadora.

##  Funcionalidades Principais Implementadas

O projeto implementa quatro funções principais para gerenciar a lógica da calculadora:

| Função | Descrição | Mapeamento no Botão |
|--------|-----------|-------------------|
| `entrar_valore(valor)` | Acumula os números e operadores na variável `todos_valores` e os exibe no visor. | Números (0-9), Ponto (.), Operadores (+, -, *, /) |
| `limpar_tela()` | Reseta a variável `todos_valores` e limpa o visor. | DEL |
| `calcular()` | Utiliza a função `eval()` do Python para executar a expressão matemática contida em `todos_valores` e exibe o resultado. | = |
| `calcular_porcentagem()` | Implementa uma lógica específica para o botão `%`, dividindo o valor atual por 100, evitando erros de sintaxe com o `eval()`. | % |


##  Destaque: Lógica de Cálculo

A chave para o cálculo está no uso da função:

```python
eval(todos_valores)
```


Esta função interpreta a string acumulada (ex: "10+5*2") como uma expressão matemática válida e retorna o resultado, tornando o código de cálculo extremamente conciso.

Observação: A lógica do botão de porcentagem (%) precisou ser tratada separadamente, pois o eval() interpreta o % como o operador de módulo (resto da divisão), e não como uma porcentagem.


<img width="229" height="322" alt="{E653C32A-F7E2-496B-A371-E8EF63CDAF8F}" src="https://github.com/user-attachments/assets/6c9dd3cb-6fa9-4203-bd1a-a1210953aeff" />

