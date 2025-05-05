# 🧠 Analizador Léxico y Sintáctico con PLY

Este proyecto es un software básico de análisis léxico y sintáctico, desarrollado en Python utilizando la biblioteca **PLY (Python Lex-Yacc)**. Su propósito es **reconocer, validar y evaluar expresiones aritméticas**, con soporte parcial para palabras clave como `if`, `else`, y `while`.

---

## 🎯 Objetivo

Implementar un analizador que procese expresiones con operaciones básicas (+, -, *, /), números enteros y decimales, paréntesis para agrupación, y reconocimiento de palabras clave.

---

## 📋 Características del lenguaje

- **Operadores**: `+`, `-`, `*`, `/`
- **Agrupación**: Paréntesis `( )`
- **Soporte léxico**: Palabras clave `if`, `else`, `while`
- **Tipos numéricos**: Enteros y decimales

---

---

## 🚀 Instrucciones de Ejecución

1. **Requisitos previos:**
   - Python 3.8 o superior
   - Biblioteca PLY

2. **Instalación de dependencias:**

   ```bash
   pip install ply

## 🚀 Cómo ejecutar

1. Instala Python (3.8+ recomendado)
2. Instala PLY:
   ```bash
   pip install ply

## 🧪 Ejemplos de Entrada y Salida

### ✅ Ejemplo 1: Expresión Aritmética

**Entrada:**

```text
3 + 4 * (2 - 1)
Salida:
Tokens:
LexToken(NUMBER,3,1,0)
LexToken(PLUS,'+',1,2)
LexToken(NUMBER,4,1,4)
LexToken(TIMES,'*',1,6)
LexToken(LPAREN,'(',1,8)
LexToken(NUMBER,2,1,9)
LexToken(MINUS,'-',1,11)
LexToken(NUMBER,1,1,13)
LexToken(RPAREN,')',1,14)

Resultado del parser:
Resultado: 7

✅ Ejemplo 2: Uso de palabra clave if
Entrada:

text
Copiar
Editar
if 10 / 2
Salida:

text
Copiar
Editar
Tokens:
LexToken(IF,'if',1,0)
LexToken(NUMBER,10,1,3)
LexToken(DIVIDE,'/',1,6)
LexToken(NUMBER,2,1,8)

Resultado del parser:
Encontrado IF con expresión: 5.0
Resultado: 5.0
✅ Ejemplo 3: Error de Sintaxis
Entrada:

text
Copiar
Editar
3 + * 4
Salida:

text
Copiar
Editar
Tokens:
LexToken(NUMBER,3,1,0)
LexToken(PLUS,'+',1,2)
LexToken(TIMES,'*',1,4)
LexToken(NUMBER,4,1,6)

Resultado del parser:
Error de sintaxis en '*'

