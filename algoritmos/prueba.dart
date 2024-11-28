import 'dart:math'; // Importar librería matemática

// Clase para representar un Rectángulo
class Rectangulo {
  // Atributos para almacenar las dimensiones
  final double base;
  final double altura;

  // Constructor
  Rectangulo(this.base, this.altura);

  // Método para calcular el área
  double calcularArea() {
    return base * altura;
  }

  // Método para calcular el perímetro
  double calcularPerimetro() {
    var baseAltura = base + altura;
    return 2 * baseAltura;
  }
}

// Clase para realizar operaciones básicas con números
class Operaciones {
  // Método estático para encontrar el mayor de dos números
  static int encontrarMayor(int a, int b) {
    return max(a,b);
  }

  // Método estático para sumar los elementos de una lista
  static int sumarLista(List<int> lista) {
    int suma = 0;
    for (int numero in lista) {
      suma += numero;
    }
    return suma;
  }
}

// Función principal
void main() {
  // Instanciar un objeto de la clase Rectangulo
  Rectangulo miRectangulo = Rectangulo(10.0, 5.0);
  print("Base del rectángulo: ${miRectangulo.base}");
  print("Altura del rectángulo: ${miRectangulo.altura}");
  print("Área del rectángulo: ${miRectangulo.calcularArea()}");
  print("Perímetro del rectángulo: ${miRectangulo.calcularPerimetro()}");

  // Operaciones matemáticas básicas
  int a = 15;
  int b = 20;
  print("Mayor entre $a y $b: ${Operaciones.encontrarMayor(a, b)}");

  // Trabajar con listas
  List<int> numeros = [10, 20, 30, 40, 50];
  print("Lista original: $numeros");
  numeros[3] = 100; // Modificar un elemento
  print("Lista después de modificar un elemento: $numeros");
  print("Suma de los elementos de la lista: ${Operaciones.sumarLista(numeros)}");

  // Trabajar con conjuntos
  Set<String> ciudades = {'Lima', 'Bogotá', 'Santiago'};
  print("Conjunto original: $ciudades");
  ciudades.add('Buenos Aires'); // Agregar un elemento
  print("Conjunto después de agregar un elemento: $ciudades");
  ciudades.remove('Bogotá'); // Eliminar un elemento
  print("Conjunto después de eliminar un elemento: $ciudades");

  // Trabajar con diccionarios
  Map<String, int> inventario = {
    'Manzanas': 50,
    'Naranjas': 30,
    'Plátanos': 20
  };
  print("Inventario original: $inventario");
  inventario['Manzanas'] = 60; // Modificar un valor
  print("Inventario después de modificar un valor: $inventario");
  inventario['Uvas'] = 25; // Agregar un nuevo par clave-valor
  print("Inventario después de agregar un nuevo producto: $inventario");

  // Bucle while
  int contador = 0;
  print("Contador usando while:");
  while (contador < 3) {
    print("Contador: $contador");
    contador++;
  }

  // Bucle do-while
  print("Contador usando do-while:");
  do {
    contador--;
    print("Contador: $contador");
  } while (contador > 0);

  // Bucle for clásico
  print("Iterando sobre la lista con un bucle for:");
  for (int i = 0; i < numeros.length; i++) {
    print("Elemento en índice $i: ${numeros[i]}");
  }

  // Iterar sobre un diccionario
  print("Iterando sobre el diccionario:");
  for (var entrada in inventario.entries) {
    print("Producto: ${entrada.key}, Cantidad: ${entrada.value}");
  }

  // Iterar sobre un conjunto
  print("Iterando sobre el conjunto de ciudades:");
  for (String ciudad in ciudades) {
    print("Ciudad: $ciudad");
  }

  // Función externa
  print("Resultado de la función externa: ${calcularPromedio([5, 10, 15])}");
}
// Función externa para calcular el promedio
double calcularPromedio(List<int> numeros) {
  if (numeros.isEmpty){ return 0.0; }
  int suma = 0;
  for (int numero in numeros) {
    suma += numero;
  }
  return suma / numeros.length;

}
//$hola
