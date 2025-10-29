
# 📘 Assignment: Hangman Game (Forca)

## 🎯 Objetivo

Crie uma versão do clássico jogo da forca (Hangman) em Python que pratique manipulação de strings, estruturas de repetição e entrada do usuário.

O estudante deverá implementar a lógica principal do jogo: seleção aleatória de palavras, exibição do progresso com caracteres ocultos, processamento de palpites de letras e gestão de tentativas restantes.

**Skills practiced:** Manipulação de strings, loops, condicionais, seleção aleatória, interação via terminal

## 📝 Tarefas

### 🛠️ Hangman — Implementação principal

#### Description
Implemente o jogo da forca para executar no terminal. O programa deve selecionar uma palavra aleatoriamente de uma lista interna, pedir palpites de letra ao jogador e mostrar o estado atual da palavra (ex: _ a _ _ a) até o jogador vencer ou ficar sem tentativas.

#### Requirements
Completed program should:

- Selecionar uma palavra aleatoriamente de uma lista pré-definida (mínimo 10 palavras)
- Aceitar palpites de letra repetidamente e atualizar o estado visível da palavra (formato _ _ _ )
- Não penalizar por palpites corretos; descontar uma tentativa por palpite incorreto
- Mostrar letras já testadas e número de tentativas restantes
- Encerrar com mensagem de vitória se a palavra for descoberta, ou mensagem de derrota se as tentativas acabarem

#### Example
Exemplo de execução simplificada:

```
Palavra: _ a _ a _
Letras testadas: a, e, i
Tentativas restantes: 4
Digite uma letra: r

Boa! 'r' está na palavra.
Palavra: _ a r a _
```

### 🛠️ (Opcional) Melhorias e extensões

#### Description
Implemente uma ou mais melhorias opcionais se desejar desafios extras.

#### Requirements

- Permitir escolha de nível de dificuldade (mais ou menos tentativas)
- Carregar palavras de um arquivo externo (ex: `words.txt`)
- Adicionar desenho progressivo da forca (ASCII art)

