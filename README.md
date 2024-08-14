# Projeto Fractal de Mandelbrot

Este projeto implementa um gerador do fractal de Mandelbrot usando Python e C em conjunto. O código C é responsável pelos cálculos, enquanto o Python gerencia a interface do usuário e a exibição do fractal.
Este é um trabalho da disciplina de Conceitos de Linguagens de Programação, que tem o objetivo de explorar o uso de 2 linguagens de programação em conjunto.

## Requisitos

- GCC 11.4.0
- Python 3.9.0
- NumPy 1.21.0
- Matplotlib 3.4.2

## Estrutura do Repositório

- `include/mandelbrot.h`: Arquivo de cabeçalho C para a função de cálculo do Mandelbrot.
- `src/mandelbrot.c`: Implementação em C da função de cálculo do Mandelbrot.
- `src/main.py`: Script Python para interface com o usuário e visualização.
- `Makefile`: Arquivo para compilação e execução do projeto.

## Instalação de bibliotecas necessárias

Para instalar as bibliotecas python necessárias, execute o comando:

```
pip install -r requirements.txt
```

## Compilação

Para compilar o projeto, execute:

```
make
```

Isso irá gerar a biblioteca compartilhada `libmandelbrot.so`.

## Execução

Para executar o programa, use:

```
make run
```

Isso irá rodar o script Python, que por sua vez carregará a biblioteca C e exibirá o fractal de Mandelbrot.

## Limpeza

Para limpar os arquivos gerados:

```
make clean
```