/*
  Este es un comentario multilinea.
  Define una función de cálculo.
*/

/// Comentario de documentación
/// para la función principal
void main() {
    // Variables constantes y finales
    final int maxLimit = 100;
    const double pi = 3.1415;
    String greeting = "Hola, mundo!";

    // Comentario de una sola línea
    print(greeting);

    // Declaración de variables de diferentes tipos
    int counter = 0;
    double result = 0.0;
    bool isActive = true;
    var dynamicVar = "Soy una variable dinámica";

    // Operadores aritméticos
    counter++;
    counter += 5;
    counter = counter - 2;
    result = pi * counter / 2;
    
    // Condicionales y operadores de comparación
    if (isActive && counter < maxLimit) {
        print("El contador es menor que el límite y está activo");
    } else if (counter >= maxLimit || !isActive) {
        print("El contador ha alcanzado o superado el límite o está inactivo");
    } else {
        print("Estado desconocido");
    }

    // Bucle 'for' y operadores de incremento y decremento
    for (int i = 0; i < 5; i++) {
        print("Iteración número: ${i + 1}");
        dynamicVar = "Valor actualizado en la iteración ${i + 1}";
    }

    // Switch-case
    switch (counter) {
        case 10:
            print("El contador es exactamente 10");
            break;
        case 20:
            print("El contador es exactamente 20");
            break;
        default:
            print("El contador tiene un valor distinto a 10 o 20");
    }

    // Llamada a una función asíncrona
    fetchData();
}

// Función asíncrona de ejemplo
Future<void> fetchData() async {
    await Future.delayed(Duration(seconds: 1));
    print("Datos obtenidos de forma asíncrona.");
}
