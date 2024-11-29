// Clase para representar un libro
class Libro {
  String titulo;
  String autor;
  int anioPublicacion;
  bool disponible;

  // Constructor
  Libro(this.titulo, this.autor, this.anioPublicacion, this.disponible);

  // Método para mostrar información del libro
  void mostrarInfo() {
    print(
        'Título: $titulo | Autor: $autor | Año: $anioPublicacion | Disponible: ${disponible ? "Sí" : "No"}');
  }
}

// Clase para manejar la biblioteca
class Biblioteca {
  // Lista de libros
  List<Libro> _libros = [];

  // Agregar un libro a la biblioteca
  void agregarLibro(Libro libro) {
    _libros.add(libro);
    print('Libro "${libro.titulo}" agregado a la biblioteca.');
  }

  // Buscar libros por autor
  List<Libro> buscarPorAutor(String autor) {
      List<Libro> librosPorAutor = [];
      for (var libro in _libros) {
        if (libro.autor == autor) {
          librosPorAutor.add(libro);
        }
      }
    return librosPorAutor;
  }

  // Prestar un libro
  void prestarLibro(String titulo) {
    for (var libro in _libros) {
      if (libro.titulo == titulo && libro.disponible) {
        libro.disponible = false;
        print('Has prestado el libro: $titulo');
        return;
      }
    }
    print('El libro "$titulo" no está disponible.');
  }

  // Mostrar todos los libros
  void mostrarTodosLosLibros() {
    print('\n--- Catálogo de la Biblioteca ---');
    for (var libro in _libros) {
      libro.mostrarInfo();
    }
  }
}

void main() {
  // Crear la biblioteca
  var biblioteca = Biblioteca();

  // Variables de diferentes tipos
  String nombreBiblioteca = "Biblioteca Central";
  int anioFundacion = 1990;
  double presupuestoAnual = 15000.75;
  Set<String> categorias = {'Novela', 'Ciencia', 'Fantasía'};
  Map<String, int> estadisticas = {'Libros': 1200, 'Usuarios': 300};

  // Mostrar información inicial
  print('Bienvenido a $nombreBiblioteca, fundada en $anioFundacion.');
  print('Presupuesto anual: \$${presupuestoAnual.toStringAsFixed(2)}');
  print('Categorías disponibles: $categorias');
  print('Estadísticas iniciales: $estadisticas');

  // Agregar libros
  Libro libro1=Libro( '1984', 'George Orwell',1949, true);
  Libro libro2=Libro( 'Fundación', 'Isaac Asimov', 1951, true);
  Libro libro3=Libro('El Hobbit', 'J.R.R. Tolkien', 1937, true);
  biblioteca.agregarLibro(libro1);
  biblioteca.agregarLibro(libro2);
  biblioteca.agregarLibro(libro3);

  // Mostrar libros disponibles
  biblioteca.mostrarTodosLosLibros();

}