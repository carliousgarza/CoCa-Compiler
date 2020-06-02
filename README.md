# CoCa-Compiler

## Requerimientos

* Python 3.7+
  > Librería numpy
* Antlr4
  > antlr4-python3-runtime
  
## Desarrollo del proyecto

Para generar la gramática usando antlr 4:

```bash
$ java -Xmx500M -cp <path al ANTLR JAR> org.antlr.v4.Tool -Dlanguage=Python3 patito.g4
```

Para generar un alias, agrega esto a tu ~/.bash_profile:

```
export CLASSPATH=".:/usr/local/lib/antlr-4.8-complete.jar:$CLASSPATH"
alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.8-complete.jar:$CLASSPATH" org.antlr.v4.Tool'
alias grun='java -Xmx500M -cp "/usr/local/lib/antlr-4.8-complete.jar:$CLASSPATH" org.antlr.v4.gui.TestRig'
```

Corre:

```bash
$ source ~/.bash_profile
```
Cierra y vuelve a abrir tu terminal

Para generar la gramática usando antlr 4 y el alias:

```bash
$ antlr4 -Dlanguage=Python3 patito.g4
```
 
## ¡Corre tu programa!

```bash
$ python3 main.py Grammar/<nombre de tu archivo>.coca 
```

## Lenguaje Patito++

### Comentarios

Para poner comentarios en el código, se utilizan // para líneas y /* */ para bloques.
function void prueba (int n)

```
var int i;
{
 i = 20; // i es inicializada con 20
 while(i > 0) do {
   i = i-1;
   /* 
     Este es un largo comentario con varios
     espacios y líneas y no tiene influencia
     en la ejecución del programa
   */
 }
}
```

### Main

La función principal del programa que será ejecutada al inicio de la ejecución. No tiene valor de retorno ni variables locales.

```
program p;
var int: i, j;
bool: b;
float: f;

function void prueba (int n)
var int i;
{
 i = 20; // i es inicializada con 20
 while(i > 0) do {
   i = i-1;
 }
}

main()
{
 i = 20; // esta es la primera línea de código en ejecutarse
}
```

### Variables

Las variables solo pueden ser inicializadas al principio del programa (globales) o en la declaración de una función (locales).

#### Globales

```
program p;
var int: i, j;
bool: b;
float: f;
```
### Locales

```
function int factorial (int n)
var int i;
float f;
{
 ...
}
```

### Variables multidimensionales

Las variables multidimensionales deben ser inicializadas con índices enteros constantes mayores a 0.
Globales → Al inicio del programa

```
program p;
var int: i[10], j[20];
bool: b[2];
float: f[100];
Locales → En la declaración de una función
function int factorial (int n)
var int i[4];
float f[20][1];
{
 ...
}
```

### Escritura

Imprime valores en consola.

```
function int factorial (int n)
var int i;
float f[20][1];
{
  i = 20
  print(i);
  // imprime 20
  print(“i”);
  // imprime el string “i”
  print(“i+1= ”, i+1);
  // imprime el string “i+1= ” y 21
}
```

### Lectura

Permite al usuario agregar un valor a una variable previamente declarada.

```
function int factorial (int n)
var int i;
float f[20][1];
{
  input(i);
  print(i);
  // imprime el valor ingresado por el usuario
}
```

### Condicionales

Los estatutos condicionales son representados con un if then y opcionalmente un else. La condición siempre es determinada por un booleano.

```
if(i>0) then {
  i = i-1;
}
else {
  print(“i es igual a o menor a 0”);
} 
```

### Ciclos

#### Existen dos maneras de crear ciclos en el lenguaje.

#### From
Se utiliza una variable previamente declarada y se le asigna un valor. Mientras el valor sea menor a una expresión condicional, el ciclo seguirá vivo. La variable es automáticamente aumentada + 1 cada ciclo.

```
from i = 0 to 10/2 do {
 if(5>i) then {
   print(“estamos en la primera mitad del ciclo”);
 }
 else {
   print(“estamos en la segunda mitad del ciclo”);
 } 
}
```

#### While
Ciclo que se ejecuta mientras una expresión sea verdadera.

```
while(i > 0) do {
   i = i-1;
}
// i es 0
```

### Llamadas a funciones

Las funciones se diferencian por ser de tipo void o del resto. Las llamadas funciones void son ejecutados como estatutos. Eso significa que no esperan un valor regresado. En cambio, una función de cualquier otro tipo es ejecutada como expresión y regresa un valor. 
Las funciones pueden o no tener parámetros.

#### Void → sin parámetros

```
function void ejecuta_void ()
var int i;
{
  i = 20
  print(i);
  // imprime 20 y acaba el programa
}

main() {
  ejecuta_void();
}
```

#### Void → con parámetros

```
function void ejecuta_void(float f, string s)
{
  print(s, f);
  // imprime “el valor de pi es: ” y 30.4 y acaba el programa
}

main() {
  ejecuta_void(3.14, “el valor de pi es: ”);
}
```

#### Con retorno → sin parámetros
```
program p;
var int: i;

function int ejecuta_func ()
{
  return (20);
}

main() {
  i = ejecuta_func();
  print(i);
  // imprime 20 y acaba el programa
}
```

#### Con retorno→ con parámetros
```
program p;
var int: i;

function int ejecuta_func (bool b)
{
  if(b) then {
   return(20);
  }
  else {
   return(-10000);
  }
}

main() {
  i = ejecuta_func(5>0);
  print(i);
  // imprime 20 y acaba el programa
}
```

#### Operaciones especiales entre matrices
```
program p;
var int: mat[10][10];

// Asumiendo que las matrices ya tienen valores agregados
function void ejemplo ()
var float: f;
{
  f = mat$ // Determinante
  mat = mat? // Inversa
  mat = mat# // Transpuesta
}
```
