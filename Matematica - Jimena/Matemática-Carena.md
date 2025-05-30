# Guía Completa de Sistemas Numéricos y Conversiones

Esta guía cubre exhaustivamente todos los aspectos de los sistemas numéricos y sus conversiones, con múltiples ejemplos y ejercicios prácticos.

---

## Tabla de Contenidos

1. [Introducción a los Sistemas Numéricos](#introducción-a-los-sistemas-numéricos)
2. [Sistema Decimal (Base 10)](#1-sistema-decimal-base-10)
3. [Sistema Binario (Base 2)](#2-sistema-binario-base-2)
4. [Sistema Octal (Base 8)](#3-sistema-octal-base-8)
5. [Sistema Hexadecimal (Base 16)](#4-sistema-hexadecimal-base-16)
6. [Conversiones Directas entre Bases](#5-conversiones-directas-entre-bases)
7. [Números Fraccionarios](#6-números-fraccionarios)
8. [Aplicaciones en Computación](#7-aplicaciones-en-computación)
9. [Ejercicios Resueltos Adicionales](#ejercicios-resueltos-adicionales)
10. [Consejos para las Conversiones](#consejos-para-las-conversiones)

---

## Introducción a los Sistemas Numéricos

Los sistemas numéricos son conjuntos de símbolos y reglas que nos permiten representar cantidades. Existen diferentes tipos según la base que utilicen (cuántos símbolos distintos usan).

### ¿Por qué son importantes en informática?

- **Binario (base 2)**: Lenguaje nativo de las computadoras (0 y 1 = apagado/encendido).
- **Octal (base 8) y Hexadecimal (base 16)**: Formas compactas de representar números binarios.
- **Decimal (base 10)**: Sistema que usamos cotidianamente.

---

## 1. Sistema Decimal (Base 10)

**Concepto**:  
Usa 10 dígitos (0-9). Cada posición representa una potencia de 10.

**Ejemplos**:

1. **327**:
   - 3 × 100 (10²) = 300
   - 2 × 10 (10¹) = 20
   - 7 × 1 (10⁰) = 7
   - **Total**: 300 + 20 + 7 = 327

2. **25**:  
   2 × 10¹ + 5 × 10⁰ = 20 + 5

3. **10906**:  
   1×10⁴ + 0×10³ + 9×10² + 0×10¹ + 6×10⁰

4. **0.5**:  
   5 × 10⁻¹

5. **123.45**:  
   1×10² + 2×10¹ + 3×10⁰ + 4×10⁻¹ + 5×10⁻²

**Propiedades clave**:
- Es posicional: el valor del dígito depende de su posición.
- Usa potencias de 10 (10⁰ = 1, 10¹ = 10, 10² = 100, etc.).

---

## 2. Sistema Binario (Base 2)

**Concepto**:  
Usa solo 2 dígitos (0 y 1). Cada posición es una potencia de 2.

**Ejemplos de conteo**:

1. 0₂ = 0₁₀  
2. 1₂ = 1₁₀  
3. 10₂ = 2₁₀ (1×2¹ + 0×2⁰)  
4. 11₂ = 3₁₀ (1×2¹ + 1×2⁰)  
5. 100₂ = 4₁₀ (1×2² + 0×2¹ + 0×2⁰)

**Conversión Binario → Decimal**:

1. **1011₂**:
   - 1 × 2³ = 8  
   - 0 × 2² = 0  
   - 1 × 2¹ = 2  
   - 1 × 2⁰ = 1  
   - **Total**: 8 + 0 + 2 + 1 = 11₁₀

2. **1100₂**:  
   8 + 4 + 0 + 0 = 12₁₀

3. **101010₂**:  
   32 + 0 + 8 + 0 + 2 + 0 = 42₁₀

4. **1111₂**:  
   8 + 4 + 2 + 1 = 15₁₀

5. **10001₂**:  
   16 + 0 + 0 + 0 + 1 = 17₁₀

**Conversión Decimal → Binario (División por 2)**:

1. **5₁₀**:
   - 5 ÷ 2 = 2, resto 1  
   - 2 ÷ 2 = 1, resto 0  
   - 1 ÷ 2 = 0, resto 1  
   - **Lee los restos al revés**: 101₂

2. **10₁₀** → 1010₂  
3. **25₁₀** → 11001₂  
4. **42₁₀** → 101010₂  
5. **100₁₀** → 1100100₂

---

## 3. Sistema Octal (Base 8)

**Concepto**:  
Usa 8 dígitos (0-7). Cada posición es una potencia de 8.

**Ejemplos de conteo**:

1. 7₈ = 7₁₀  
2. 10₈ = 8₁₀ (1×8¹ + 0×8⁰)  
3. 77₈ = 63₁₀ (7×8¹ + 7×8⁰)  
4. 100₈ = 64₁₀ (1×8²)  
5. 123₈ = 1×64 + 2×8 + 3×1 = 83₁₀

**Conversión Octal → Decimal**:

1. **75₈**:
   - 7 × 8¹ = 56  
   - 5 × 8⁰ = 5  
   - **Total**: 56 + 5 = 61₁₀

2. **245₈**:  
   2×64 + 4×8 + 5×1 = 165₁₀

3. **126₈**:  
   1×64 + 2×8 + 6×1 = 86₁₀

4. **15₈**:  
   1×8 + 5×1 = 13₁₀

5. **1473₈**:  
   1×512 + 4×64 + 7×8 + 3×1 = 827₁₀

**Conversión Decimal → Octal (División por 8)**:

1. **941₁₀**:
   - 941 ÷ 8 = 117, resto 5  
   - 117 ÷ 8 = 14, resto 5  
   - 14 ÷ 8 = 1, resto 6  
   - 1 ÷ 8 = 0, resto 1  
   - **Lee los restos al revés**: 1655₈

2. **1006₁₀** → 1756₈  
3. **8₁₀** → 10₈  
4. **25₁₀** → 31₈  
5. **143₁₀** → 217₈

---

## 4. Sistema Hexadecimal (Base 16)

**Concepto**:  
Usa 16 símbolos (0-9, A=10, B=11, C=12, D=13, E=14, F=15). Cada posición es una potencia de 16.

**Tabla de equivalencias**:
- A = 10, B = 11, C = 12, D = 13, E = 14, F = 15

**Ejemplos de conteo**:

1. F₁₆ = 15₁₀  
2. 10₁₆ = 16₁₀ (1×16¹ + 0×16⁰)  
3. FF₁₆ = 255₁₀ (15×16 + 15)  
4. 100₁₆ = 256₁₀ (1×16²)  
5. ABC₁₆ = 10×256 + 11×16 + 12×1 = 2748₁₀

**Conversión Hexadecimal → Decimal**:

1. **AB₁₆**:
   - A (10) × 16¹ = 160  
   - B (11) × 16⁰ = 11  
   - **Total**: 160 + 11 = 171₁₀

2. **C10₁₆**:  
   12×256 + 1×16 + 0 = 3088₁₀

3. **DE9A₁₆**:  
   13×4096 + 14×256 + 9×16 + 10×1 = 56986₁₀

4. **F₁₆** → 15₁₀

5. **ADE5₁₆**:  
   10×4096 + 13×256 + 14×16 + 5×1 = 44517₁₀

**Conversión Decimal → Hexadecimal (División por 16)**:

1. **125₁₀**:
   - 125 ÷ 16 = 7, resto 13 (D)  
   - 7 ÷ 16 = 0, resto 7  
   - **Lee los restos al revés**: 7D₁₆

2. **1250₁₀** → 4E2₁₆  
3. **8₁₀** → 8₁₆  
4. **25₁₀** → 19₁₆  
5. **143₁₀** → 8F₁₆

---

## 5. Conversiones Directas entre Bases

### Binario ↔ Octal

**Regla**:  
Agrupar de 3 en 3 bits (de derecha a izquierda).

**Ejemplos Binario → Octal**:

1. **101101011₂**:
   - Separa: 101 | 101 | 011  
   - Convierte: 5 | 5 | 3  
   - **Resultado**: 553₈

2. **1101001₂**:
   - Agrupa: 001 | 101 | 001  
   - **Resultado**: 151₈

3. **0.110101₂**:
   - Agrupa la parte fraccionaria: 0. | 110 | 101  
   - **Resultado**: 0.65₈

4. **10011011.1₂**:
   - Agrupa: 010 | 011 | 011 . 100  
   - **Resultado**: 233.4₈

5. **1110101011₂**:
   - Agrupa: 001 | 110 | 101 | 011  
   - **Resultado**: 1653₈

**Ejemplos Octal → Binario**:

1. **217₈**:
   - Convierte cada dígito: 2 = 010, 1 = 001, 7 = 111  
   - Junta: 010001111₂ (se puede omitir el 0 inicial → 10001111₂)

2. **10.14₈**:
   - Conversión: 001 | 000 . 001 | 100 = 1000.0011₂

3. **0.65₈**:
   - Conversión: 0. | 110 | 101 = 0.110101₂

4. **5.5₈**:
   - Conversión: 101.101₂

5. **233.4₈**:
   - Conversión: 010 | 011 | 011 . 100 = 10011011.1₂

---

### Binario ↔ Hexadecimal

**Regla**:  
Agrupar de 4 en 4 bits (de derecha a izquierda).

**Ejemplos Binario → Hexadecimal**:

1. **101011011110₂**:
   - Separa: 1010 | 1101 | 1110  
   - Convierte: A | D | E  
   - **Resultado**: ADE₁₆

2. **1101001₂**:
   - Agrupa: 0110 | 1001  
   - **Resultado**: 69₁₆

3. **0.110101₂**:
   - Agrupa: 0. | 1101 | 0100 (añadiendo ceros si es necesario)  
   - **Resultado**: 0.D4₁₆

4. **10011011.1₂**:
   - Agrupa: 1001 | 1011 . 1000  
   - **Resultado**: 9B.8₁₆

5. **1110101011₂**:
   - Agrupa: 0011 | 1010 | 1011  
   - **Resultado**: 3AB₁₆

**Ejemplos Hexadecimal → Binario**:

1. **8F₁₆**:
   - Convierte cada dígito: 8 = 1000, F = 1111  
   - **Resultado**: 10001111₂

2. **5.A₁₆**:
   - Conversión: 0101 . 1010 = 101.1010₂

3. **9B.8₁₆**:
   - Conversión: 1001 | 1011 . 1000 = 10011011.1₂

4. **C10₁₆**:
   - Conversión: 1100 | 0001 | 0000 = 110000010000₂

5. **F940₁₆**:
   - Conversión: 1111 | 1001 | 0100 | 0000 = 1111100101000000₂

---

## 6. Números Fraccionarios

### Conversión Decimal → Otra Base (parte fraccionaria)

**Método**:  
Multiplicación sucesiva por la base, tomando la parte entera de cada producto.

**Ejemplo Decimal → Binario (5.8125)**:

1. **Parte entera (5)**:  
   → 101₂

2. **Parte fraccionaria (0.8125)**:
   - 0.8125 × 2 = 1.625 → toma 1  
   - 0.625 × 2 = 1.25   → toma 1  
   - 0.25 × 2 = 0.5    → toma 0  
   - 0.5 × 2 = 1.0     → toma 1  
   - **Resultado**: 0.1101₂

3. **Junta**:  
   101.1101₂

**Más ejemplos**:

1. **10.7₁₀ → Binario**:
   - **Parte entera**: 1010₂  
   - **Parte fraccionaria**:
     - 0.7 × 2 = 1.4 → 1  
     - 0.4 × 2 = 0.8 → 0  
     - 0.8 × 2 = 1.6 → 1  
     - 0.6 × 2 = 1.2 → 1  
     - 0.2 × 2 = 0.4 → 0 (se vuelve periódico)  
   - **Resultado**: 1010.10110...₂

2. **5.625₁₀ → Binario** → 101.101₂  
3. **0.828125₁₀ → Binario** → 0.110101₂  
4. **5.375₁₀ → Hexadecimal** → 5.6₁₆  
5. **165.859375₁₀ → Hexadecimal** → A5.DC₁₆  

### Números Periódicos

**Ejemplo**: Convertir 1.55₁₀ → Octal

1. **Parte entera**: 1  
2. **Parte fraccionaria**:
   - 0.55 × 8 = 4.4 → 4  
   - 0.4 × 8 = 3.2  → 3  
   - 0.2 × 8 = 1.6  → 1  
   - 0.6 × 8 = 4.8  → 4  
   - 0.8 × 8 = 6.4  → 6  
   - 0.4 × 8 = 3.2  → 3 (comienza a repetirse)
   - **Resultado**: 1.431463146...₈, que se puede representar como 1.43146₈ (con período 3146)

---

## 7. Aplicaciones en Computación

**Unidades de información**:

- **Bit**: 1 dígito binario (0 o 1)
- **Nibble**: 4 bits (equivalente a 1 dígito hexadecimal)
- **Byte**: 8 bits (2 dígitos hexadecimales)
- **Palabra**: 16 bits (4 dígitos hexadecimales)

**Notación en programación**:

- **Binario**: `0b1010` (por ejemplo, `0b1010` = 10₁₀)
- **Octal**: `0123` (por ejemplo, `0123` = 83₁₀)
- **Hexadecimal**: `0x1A3` (por ejemplo, `0x1A3` = 419₁₀)

**Ejemplos prácticos**:

1. **Color RGB (24 bits)**:
   - `0xFF0000` = Rojo puro  
   - `0x00FF00` = Verde puro  
   - `0x0000FF` = Azul puro

2. **Permisos en Unix**:
   - `755₈` = 111 101 101₂ (rwxr-xr-x)

3. **Máscara de red**:
   - `255.255.255.0` = 0xFFFFFF00

4. **Dirección MAC**:
   - Ejemplo: `00:1A:2B:3C:4D:5E` (6 bytes en hexadecimal)

5. **Codificación ASCII**:
   - `'A'` = 65₁₀ = 0x41 = 01000001₂

---

## Ejercicios Resueltos Adicionales

1. **Convertir 11011011₂ a decimal**:

   Cálculo:  
   1×2⁷ + 1×2⁶ + 0×2⁵ + 1×2⁴ + 1×2³ + 0×2² + 1×2¹ + 1×2⁰  
   = 128 + 64 + 0 + 16 + 8 + 0 + 2 + 1  
   = 219₁₀

2. **Convertir 255₁₀ a hexadecimal**:

   Cálculo:  
   255 ÷ 16 = 15, resto 15 (F)  
   15 ÷ 16 = 0, resto 15 (F)  
   **Resultado**: FF₁₆

3. **Convertir 3AB₁₆ a binario**:

   - Conversión: 3 = 0011, A = 1010, B = 1011  
   - Resultado: 001110101011₂ (se puede representar sin ceros iniciales como 1110101011₂)

4. **Convertir 47.375₁₀ a binario**:

   - **Parte entera (47)**: 101111₂  
   - **Parte fraccionaria (0.375)**:
     - 0.375 × 2 = 0.75 → 0  
     - 0.75 × 2 = 1.5 → 1  
     - 0.5 × 2 = 1.0 → 1  
     - **Resultado (parte fraccionaria)**: 0.011₂  
   - **Total**: 101111.011₂

5. **Convertir 101111.011₂ a octal**:

   - Agrupar: 101 | 111 . 011  
   - Conversión: 5 | 7 . 3  
   - **Resultado**: 57.3₈

---

## Consejos para las Conversiones

1. **Binario-Hexadecimal**:  
   Memoriza la tabla de 4 bits (0000 a 1111 = 0 a F).

2. **Decimal a otra base**:  
   Para la parte entera, divide; para la parte fraccionaria, multiplica.

3. **Verificación**:  
   Siempre convierte de vuelta a decimal para comprobar.

4. **Práctica**:  
   Realiza muchos ejercicios hasta que el proceso te resulte natural.

5. **Herramientas**:  
   Usa una calculadora científica para verificar tus resultados.

---

Esta guía abarca todos los aspectos fundamentales de los sistemas numéricos y sus conversiones, apoyándose en ejemplos y ejercicios prácticos. La práctica constante es la clave para dominar estos conceptos, esenciales en informática.