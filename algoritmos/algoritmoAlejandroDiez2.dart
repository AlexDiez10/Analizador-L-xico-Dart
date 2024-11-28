void main(){

  Set<int> numeros = {1, 2, 3, 4};

  for (int i = 0; i < 3 ; i++){
    print('El número es: $i');
  }

  for (int numero in numeros){
    print('El número es: $numero');
  }

  final candidatos = [
    Candidato('Alice', 5),
    Candidato('Bob', 3),
    Candidato('Charlie', 7)
  ];

  for (final Candidato(:name, :yearsExp) in candidatos) {
    print('$name tiene $yearsExp años de experiencia.');
  }



}

String hola() {
  return "hola";
}

String mensaje(String mensaje) {
  return 'Este es el mensaje: $mensaje';
}

class Candidato {
  final String name;
  final int yearsExp;

  Candidato(this.name, this.yearsExp);
}
