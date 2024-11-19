import 'dart:io';

void main() {
  // Imprimir un mensaje
  print("Hola mundo!"); // Comentario simple

  // Declaración de un diccionario (mapa)
  Map<String, int> edades = {"Juan": 25, "Ana": 30, "Pedro": 40};

  // Ciclo while
  int contador = 0;
  while (contador < 5) {
    print("Contador: $contador");
    contador++;
  }

  // Ciclo do-while
  int numero = 0;
  do {
    print("Número: $numero");
    numero++;
  } while (numero < 3);
}

// Función que devuelve un entero
int sumar(int a, int b) {
  int suma = a + b;
  return suma;
}

// Otra función que devuelve un entero
int multiplicar(int a, int b) {
  int producto = a * b;

  // Uso de un for simple
  for (int i = 0; i < producto; i++) {
    print("Iteración $i");
  }

  return producto;
}

int pedirNumero() {
  print("Ingrese un número entero:");

  // Leer entrada desde stdin
  int entrada = stdin.readLineSync();

  // Retornar el cuadrado del número
  return numero * numero;
}
