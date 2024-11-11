void main() {
  int myNumber = 42;
  String myString = "Hello, world!";
  bool myBool = true;

  print(myNumber); // Output: 42
  print(myString); // Output: Hello, world!
  print(myBool); // Output: true

  if (myNumber > 0) {
    print("myNumber is positive");
  } else {
    print("myNumber is negative or zero");
  }

  for (int i = 0; i < 5; i++) {
    print("Iteration $i");
  }

  List<int> myList = [1, 2, 3, 4, 5];
  for (int item in myList) {
    print(item);
  }

  Map<String, int> myMap = {
    "apple": 1,
    "banana": 2,
    "cherry": 3
  };

  myMap["orange"] = 4;
  print(myMap);  
}