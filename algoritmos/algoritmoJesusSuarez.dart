/*
  Este es un comentario multilinea.
  Este algoritmo es una variante del algoritmo de ordenamiento bogosort.
*/

void stoogesort(List<int> arr, int l, int h) {
  if (arr[l] > arr[h]) {
    // Intercambia si el elemento inicial es mayor que el final
    int temp = arr[l];
    arr[l] = arr[h];
    arr[h] = temp;
  }

  if (h - l + 1 > 2) {
    int t = (h - l + 1) ~/ 3;

    // Llamadas recursivas
    stoogesort(arr, l, h - t);      // Ordena los primeros 2/3
    stoogesort(arr, l + t, h);      // Ordena los últimos 2/3
    stoogesort(arr, l, h - t);      // Ordena los primeros 2/3 de nuevo
  }
}

void main() {
  List<int> arr = [5, 3, 8, 6, 2];
  stoogesort(arr, 0, arr.length - 1);
  print('Arreglo ordenado: $arr');
}