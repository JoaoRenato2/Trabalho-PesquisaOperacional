# Script de Minimização de Custo de Atribuição

## Introdução
Este script em Python é projetado para resolver um problema de atribuição com o objetivo de minimizar o custo total da atribuição de `N` agentes a `M` tarefas. O problema é modelado e resolvido utilizando técnicas de programação linear fornecidas pela biblioteca PuLP.

## Características
- Geração de uma matriz de custos com valores aleatórios.
- Utilização de programação linear para minimização de custos.
- Saída clara da atribuição ótima e do custo total minimizado.

## Pré-requisitos
- Python 3.x
- NumPy
- PuLP

## Instalação

Para configurar o ambiente necessário:

- git clone https://github.com/JoaoRenato2/Trabalho-PesquisaOperacional.git
- cd Trabalho-PesquisaOperacional
- pip install numpy pulp


## Saída
O script fornece as seguintes informações:

- O status da solução (Ótimo, Inviável, etc.).
- A atribuição ótima de agentes para tarefas.
- O custo total minimizado da atribuição.

