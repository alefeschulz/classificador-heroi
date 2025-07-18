# 🦸‍♂️ Classificador de Nível de Herói

[![GitHub Pages](https://img.shields.io/badge/GitHub-Pages-blue?logo=github)](https://alefeschulz.github.io/classificador-heroi)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Este projeto classifica o nível de um herói com base na quantidade de experiência (XP). Faz parte do desafio da **DIO - Classificador de Nível de Herói**.

🌐 **Demo online:** [alefeschulz.github.io/classificador-heroi](https://alefeschulz.github.io/classificador-heroi)

## 🚀 Tecnologias usadas
- JavaScript (Node.js)
- Python
- HTML + CSS + JavaScript (Interativo)

## 📂 Estrutura
- `js/classificador.js`: versão para Node.js
- `python/classificador.py`: versão para rodar com Python
- `web/index.html`: versão interativa para navegador

## 🏃‍♂️ Como rodar

### ✅ JavaScript
```bash
cd js
node classificador.js
```

### ✅ Python
```bash
cd python
python classificador.py
```

### ✅ Web (Interativo)
Abra o arquivo `web/index.html` no navegador.

## 💡 Sobre o desafio
O programa pede o nome e XP de um herói e retorna o nível correspondente:

| XP                | Nível       |
|--------------------|-------------|
| < 1000             | Ferro       |
| 1001 - 2000        | Bronze      |
| 2001 - 5000        | Prata       |
| 5001 - 7000        | Ouro        |
| 7001 - 8000        | Platina     |
| 8001 - 9000        | Ascendente  |
| 9001 - 10000       | Imortal     |
| >= 10001           | Radiante    |

Exemplo de saída:
```
O Herói de nome Artemis está no nível de Ascendente
```

## 📝 Licença
MIT License
