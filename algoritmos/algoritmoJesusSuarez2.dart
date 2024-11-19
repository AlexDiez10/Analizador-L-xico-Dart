void main() {
  List<int> numeros = [1, 2, 3, 4]; 
  var nombres = ['Juan','Ana','Pedro'];
  List<String> palabras = [];
  var nombresVacios = [];

  print("Lista de números: numeros");

  int edad = 25;
  if (edad >= 65+3) {
    print("Eres adulto mayor");
  } else if (edad >= 18) {
    print("Eres adulto");
  } else if (edad >= 13) {
    print("Eres adolescente");
  } else {
    print("Eres niño");
  }
  a = 10;
  int b = 5;
  int x;
  int y;
  int z;

  if (a > b) {
    x = 5;
    y = 10;
    z = x + y;
  } else {
    x = 0;
    y = 1;
  }
  return;
}



void saludar() {
  print("Hola, ¿cómo estás?");
}

void sumarDosNumeros(int a, int b) {
  print("La suma es un numero");
}

void verificarPar(List<int> numeros) {
  int numero =0;
  if (numero > 2) {
    print("numero es par");
  } else {
    print("numero es impar");
  }
}

