# Usando as abas no IDE do Processing
# TL:DR; As abas se comportam como *módulos* de Python

from nome_aba import *
import random as rnd
from random import choice`
from nome_aba import uma_funcao, outra_funcao, uma_classe, outra_classe
Múltiplas abas são utilizadas para organizar melhor um * sketch * mais longo. é comum separar as definições de classes e outras funções em abas "secundárias".

**as funções `setup()`,  `draw()` assim como as que são acionadas por eventos, por exemplo, `mouse_dragged()` ou `key_pressed()`, precisam ficar na primeira aba.**

# Abas secundárias no modo Python

diferente das abas do modo java tradicional, que são tratadas como uma continuidade do código na primeira aba, as abas no modo python são arquivos `.py` e se comportam como "módulos" python,  por isso precisam ser "importadas", sendo referenciadas com a instrução `import`.

ao criar uma nova aba, por exemplo, com o nome `segunda_aba`, ela se torna o arquivo `segunda_aba.py`. note que a primeira aba do * sketch * é um arquivo com a extensão `.pyde`, extensão que fica oculta.

na primeira aba, ou em qualquer aba que precise do código de outro módulo/aba, é preciso usar algo como:
```python
```
ou ainda, considerado preferível e mais elegante em projetos grandes na comunidade python:
```python
```
note que o nome do módulo é escrito ** sem a extensão `.py`.**

# Atenção 1: Não esqueça de salvar sempre quando usar abas!

*sketches * com mais de uma aba, quando modificados não executam corretamente a menos que sejam salvos!

# Atenção 2: Se as abas secundárias tiverem caracteres não-ASCII

acrescente `  # -*- coding: utf-8 -*-` na primeira linha do arquivo.

veja também:  [`from __future__ import unicode_literals`](futuro.md)

# Exemplo de importação da biblioteca padrão do Python

A instrução `import` e suas variantes são usadas para importar ferramentas da biblioteca padrão do python, módulos que vem junto com o interpretador python contendo diversas funções e classes, mas que só ficam disponíveis quando requisitados.

vamos usar como exemplo aqui o módulo `random` de python que tem uma função chamada `choice()`, que 'sorteia um item' (leia mais sobre[pseudo-aleatoriedade](aleatoriedade_1.md) e o[módulo `random`](aleatoriedade_2.md)) de uma coleção, que pode ser uma tupla, lista, conjunto..., e isso pode ser bastante útil na programação criativa.

se fizermos `import random`, temos dois problemas, matamos a função `random()` do processing e temos que usar a forma `sorteio = random.choice(colecao)` que é muito longa. A forma `from random import *` também mata o `random()` do processing. uma opção melhor pode ser fazer assim:

```python

colecao = ("A", "B", "C", "D")
sorteio = choice(colecao)
```

um estilo muito comum, se você precisa de todos os métodos de `random`, mas não quer 'poluir' os nomes globais do processing, é fazer assim:

```python

colecao = ("A", "B", "C", "D")
sorteio = rnd.choice(colecao)
```

# Glossário

[módulo](https: // penseallen.github.io/pense_python2e/03-funcoes.html  # termo:m%C3%B3dulo)

um arquivo que contém uma coleção de funções relacionadas e outras definições.

[instrução de importação](https: // penseallen.github.io/pense_python2e/03-funcoes.html  # termo:instrução%20de%20importação)

uma instrução que lê um arquivo de módulo e cria um objeto de módulo.

---
texto e imagens / text and images: CC BY-NC-SA 4.0; Código / code: GNU GPL v3.0 exceto onde explicitamente indicado por questões de compatibilidade.
