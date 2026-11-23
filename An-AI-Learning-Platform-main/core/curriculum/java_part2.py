from . import L

LEVELS = [

L(16, "Strings: Working with Words",
  "Use the many helpful tools that come with String.",
  "Apprentice", 120,
r"""
### Strings are objects with superpowers
A `String` holds text, and it comes with many helpful methods. You call them with a dot.

### Useful String methods
- `s.length()` gives the number of characters.
- `s.toUpperCase()` and `s.toLowerCase()` change the letters.
- `s.charAt(0)` gives the first letter.
- `s.substring(0, 3)` cuts out a piece.
- `s.contains("ava")` checks if a piece is inside.
- `s.equals("Java")` checks if two strings have the same text.

### Important: use equals, not ==
Compare strings with `equals`. The `==` sign checks something different (whether it is the very same object), and it can give wrong answers.

### Strings never change
A String is **immutable**. Methods like `toUpperCase()` give you a **new** string. You must save it: `s = s.toUpperCase();`.
""",
r"""
public class Main {
    public static void main(String[] args) {
        String name = "quest";
        System.out.println(name.toUpperCase());
        System.out.println("Length: " + name.length());
        System.out.println("First letter: " + name.charAt(0));
    }
}
""",
  "Shout it",
  "Turn 'hello java' into capital letters and print it. Then print its length.",
r"""
public class Main {
    public static void main(String[] args) {
        String text = "hello java";
        // Print the text in capital letters
        // Print: Length: 10

    }
}
""",
  "HELLO JAVA\nLength: 10", ["toUpperCase()", "length()"],
  "text.toUpperCase() and text.length()",
r"""
public class Main {
    public static void main(String[] args) {
        String text = "hello java";
        System.out.println(text.toUpperCase());
        System.out.println("Length: " + text.length());
    }
}
""",
  "Which is the right way to compare the text of two Strings?",
  ["a == b", "a.equals(b)", "a = b", "a.same(b)"], 1,
  "equals checks whether the text is the same. == does not do that reliably for Strings."),

L(17, "Mini Project 4: Marks Report Card",
  "Build a report card that finds the total, average, highest mark and grade.",
  "Apprentice", 180,
r"""
### Our report card project
Teachers do this daily. Your program will do it in a blink. With five subject marks in an array, we work out:
1. The **total**.
2. The **average**.
3. The **highest** mark.
4. A **grade**.

### Plan
- Loop through the array once with for-each.
- Keep a running `total` and a `highest`.
- After the loop: `double average = total / 5.0;`
- Grades from the average:
  - 90 or more: A
  - 75 or more: B
  - 60 or more: C
  - otherwise: D

### Finding the highest
Begin with `highest = marks[0]`. If another mark is bigger, replace `highest`.

### Level-up idea
Ask the user to type the five marks with `Scanner` inside a loop.
""",
r"""
public class Main {
    public static void main(String[] args) {
        int[] marks = {60, 70, 80, 90, 100};
        int total = 0, highest = marks[0];
        for (int m : marks) {
            total += m;
            if (m > highest) highest = m;
        }
        double average = total / 5.0;
        System.out.println("Total: " + total);
        System.out.println("Average: " + average);
        System.out.println("Highest: " + highest);
    }
}
""",
  "Complete the report card",
  "Marks are 78, 85, 62, 90, 70. Print the total, average, highest and grade.",
r"""
public class Main {
    public static void main(String[] args) {
        int[] marks = {78, 85, 62, 90, 70};
        int total = 0;
        int highest = marks[0];
        // 1. Loop: add to total and find the highest
        // 2. average = total / 5.0
        // 3. Print Total, Average, Highest and Grade
        //    Grade: 90+ A, 75+ B, 60+ C, else D

    }
}
""",
  "Total: 385\nAverage: 77.0\nHighest: 90\nGrade: B", ["for", "highest", "5.0", "elseif"],
  "Check the grade from the biggest limit (90) down to the smallest (60).",
r"""
public class Main {
    public static void main(String[] args) {
        int[] marks = {78, 85, 62, 90, 70};
        int total = 0;
        int highest = marks[0];
        for (int m : marks) {
            total += m;
            if (m > highest) {
                highest = m;
            }
        }
        double average = total / 5.0;
        System.out.println("Total: " + total);
        System.out.println("Average: " + average);
        System.out.println("Highest: " + highest);
        if (average >= 90) {
            System.out.println("Grade: A");
        } else if (average >= 75) {
            System.out.println("Grade: B");
        } else if (average >= 60) {
            System.out.println("Grade: C");
        } else {
            System.out.println("Grade: D");
        }
    }
}
""",
  "To find the highest mark, what should 'highest' start as?",
  ["Zero always", "The first element of the array", "The total", "-1"], 1,
  "Starting with the first element is safe. You only replace it when you meet a bigger value.",
  project=True),

L(18, "Classes and Objects",
  "Make blueprints and build things from them.",
  "Adept", 150,
r"""
### Real-world things in code
Think of a **blueprint** for a house. It is not a house, but you can build many houses from it. In Java:
- A **class** is the blueprint.
- An **object** is a real thing built from the blueprint.

### Parts of a class
- **Fields** (variables) store facts, like `name` and `health`.
- **Methods** are actions, like `attack()`.

### Making an object
```
Player p = new Player();
p.name = "Zara";
p.health = 100;
```
`new` builds the object. The dot `.` reaches inside it.

### Why this matters
Java is an **object-oriented** language. Almost everything you will build is made of objects: players, books, bank accounts, songs.

### Tip
Class names start with a capital letter (`Player`). Variable names start with a small letter (`p`).
""",
r"""
public class Main {
    public static void main(String[] args) {
        Dog d = new Dog();
        d.name = "Rocky";
        d.bark();
    }
}

class Dog {
    String name;

    void bark() {
        System.out.println(name + " says Woof!");
    }
}
""",
  "Build a player",
  "Create a Player object, set its name to Zara and health to 100, then call show() to print it.",
r"""
public class Main {
    public static void main(String[] args) {
        // Make a Player object called p, set name and health, then call p.show()

    }
}

class Player {
    String name;
    int health;

    void show() {
        System.out.println(name + " has " + health + " health");
    }
}
""",
  "Zara has 100 health", ["newPlayer()", "p.name", "p.show()"],
  "Player p = new Player(); p.name = \"Zara\"; ...",
r"""
public class Main {
    public static void main(String[] args) {
        Player p = new Player();
        p.name = "Zara";
        p.health = 100;
        p.show();
    }
}

class Player {
    String name;
    int health;

    void show() {
        System.out.println(name + " has " + health + " health");
    }
}
""",
  "What is the difference between a class and an object?",
  ["They are the same", "A class is a blueprint and an object is a real thing built from it", "An object is a blueprint", "A class is a loop"], 1,
  "A class describes what something is like. An object is an actual thing created from that description."),

L(19, "Constructors and the this Keyword",
  "Set up an object the moment it is born.",
  "Adept", 150,
r"""
### Setting values one by one is slow
Writing `p.name = ...` and `p.health = ...` after every `new` is tiring and easy to forget. A **constructor** sets up an object **as it is created**.

### Making a constructor
```
class Pet {
    String name;
    int age;

    Pet(String name, int age) {
        this.name = name;
        this.age = age;
    }
}
```
- A constructor has the **same name as the class** and **no return type**.
- It runs automatically when you write `new Pet("Rocky", 3)`.

### What is this?
Inside the class, `this` means "this very object". `this.name = name;` means "my field called name gets the value from the parameter called name".

### Tip
If you write no constructor, Java quietly gives you an empty one for free.
""",
r"""
public class Main {
    public static void main(String[] args) {
        Book b = new Book("Java is Fun", 120);
        b.show();
    }
}

class Book {
    String title;
    int pages;

    Book(String title, int pages) {
        this.title = title;
        this.pages = pages;
    }

    void show() {
        System.out.println(title + " has " + pages + " pages");
    }
}
""",
  "Meet the pet",
  "Write the constructor for Pet so that Rocky, age 3 prints 'Rocky is 3 years old'.",
r"""
public class Main {
    public static void main(String[] args) {
        Pet p = new Pet("Rocky", 3);
        p.show();
    }
}

class Pet {
    String name;
    int age;

    // Write the constructor here using this.name and this.age

    void show() {
        System.out.println(name + " is " + age + " years old");
    }
}
""",
  "Rocky is 3 years old", ["Pet(Stringname,intage)", "this.name=name", "this.age=age"],
  "Pet(String name, int age) { this.name = name; this.age = age; }",
r"""
public class Main {
    public static void main(String[] args) {
        Pet p = new Pet("Rocky", 3);
        p.show();
    }
}

class Pet {
    String name;
    int age;

    Pet(String name, int age) {
        this.name = name;
        this.age = age;
    }

    void show() {
        System.out.println(name + " is " + age + " years old");
    }
}
""",
  "What is special about a constructor's name?",
  ["It is always 'start'", "It is the same as the class name", "It must be a number", "It has no name"], 1,
  "A constructor must have exactly the same name as its class."),

L(20, "Encapsulation: Protect Your Data",
  "Hide fields with private and control them with getters and setters.",
  "Adept", 150,
r"""
### Why protect data?
Imagine anyone could write `account.balance = 1000000`. Chaos! **Encapsulation** means hiding the data and only allowing safe ways to change it. Think of a vending machine: you cannot reach inside, you press buttons.

### How to do it
- Mark fields `private`. Only the class itself can touch them.
- Add public **getter** methods to read the value: `getAge()`.
- Add public **setter** methods to change it safely: `setAge(int age)`.

### Rules in the setter
Inside the setter you can check the value first. For example, an age cannot be negative.

```
void setAge(int age) {
    if (age > 0) { this.age = age; }
    else { System.out.println("Invalid age!"); }
}
```

### Tip
Fields private, methods public. This is the normal pattern in Java.
""",
r"""
public class Main {
    public static void main(String[] args) {
        Wallet w = new Wallet();
        w.setMoney(50);
        System.out.println("Money: " + w.getMoney());
    }
}

class Wallet {
    private int money;

    int getMoney() { return money; }

    void setMoney(int m) {
        if (m >= 0) money = m;
    }
}
""",
  "Safe age",
  "Finish setAge so that 15 is accepted but -5 prints 'Invalid age!'.",
r"""
public class Main {
    public static void main(String[] args) {
        Kid k = new Kid();
        k.setAge(15);
        System.out.println("Age: " + k.getAge());
        k.setAge(-5);
        System.out.println("Age: " + k.getAge());
    }
}

class Kid {
    private int age;

    int getAge() { return age; }

    void setAge(int age) {
        // Only accept the age if it is more than 0
        // Otherwise print: Invalid age!
    }
}
""",
  "Age: 15\nInvalid age!\nAge: 15", ["if", "this.age=age", "Invalidage!"],
  "if (age > 0) { this.age = age; } else { println(...) }",
r"""
public class Main {
    public static void main(String[] args) {
        Kid k = new Kid();
        k.setAge(15);
        System.out.println("Age: " + k.getAge());
        k.setAge(-5);
        System.out.println("Age: " + k.getAge());
    }
}

class Kid {
    private int age;

    int getAge() { return age; }

    void setAge(int age) {
        if (age > 0) {
            this.age = age;
        } else {
            System.out.println("Invalid age!");
        }
    }
}
""",
  "What does the private keyword do to a field?",
  ["Makes it faster", "Only the same class can access it directly", "Deletes it", "Makes it a number"], 1,
  "private hides the field from other classes. They must use the public getters and setters."),

L(21, "Mini Project 5: Student Record Keeper",
  "Store many students as objects and find the topper.",
  "Adept", 180,
r"""
### Our project
A school stores a name and a score for every student. We will build a program that keeps three students as **objects** and finds the **topper** (highest score).

### Plan
1. Make a class `Student` with a `name` and a `score`, a constructor and getters.
2. Make an **array of Student objects**: `Student[] list = new Student[3];` or fill it directly.
3. Loop to print each student.
4. While looping, keep track of the best student.

### Why objects are great here
One object keeps a student's name and score together. You cannot mix them up, which could happen with two separate arrays.

### Level-up ideas
Use an `ArrayList` (you will learn it soon) so the list can grow, and add a menu to add, search and delete students.
""",
r"""
public class Main {
    public static void main(String[] args) {
        Student[] list = { new Student("Mina", 88), new Student("Kabir", 95) };
        for (Student s : list) {
            System.out.println(s.getName() + " - " + s.getScore());
        }
    }
}

class Student {
    private String name;
    private int score;

    Student(String name, int score) {
        this.name = name;
        this.score = score;
    }

    String getName() { return name; }
    int getScore() { return score; }
}
""",
  "Find the topper",
  "Print every student as 'Name - Score'. Then print the topper's name.",
r"""
public class Main {
    public static void main(String[] args) {
        Student[] list = {
            new Student("Asha", 85),
            new Student("Ravi", 92),
            new Student("Meena", 78)
        };
        Student best = list[0];
        // Loop through the list: print each student and update best if the score is higher

        System.out.println("Topper: " + best.getName());
    }
}

class Student {
    private String name;
    private int score;

    Student(String name, int score) {
        this.name = name;
        this.score = score;
    }

    String getName() { return name; }
    int getScore() { return score; }
}
""",
  "Asha - 85\nRavi - 92\nMeena - 78\nTopper: Ravi", ["for", "getScore()", "best="],
  "If s.getScore() > best.getScore() then best = s;",
r"""
public class Main {
    public static void main(String[] args) {
        Student[] list = {
            new Student("Asha", 85),
            new Student("Ravi", 92),
            new Student("Meena", 78)
        };
        Student best = list[0];
        for (Student s : list) {
            System.out.println(s.getName() + " - " + s.getScore());
            if (s.getScore() > best.getScore()) {
                best = s;
            }
        }
        System.out.println("Topper: " + best.getName());
    }
}

class Student {
    private String name;
    private int score;

    Student(String name, int score) {
        this.name = name;
        this.score = score;
    }

    String getName() { return name; }
    int getScore() { return score; }
}
""",
  "Why is an array of Student objects better than two separate arrays (names and scores)?",
  ["It is shorter", "Each student's name and score stay together", "Java requires it", "It uses no memory"], 1,
  "Objects keep related data together, so a name can never get mixed up with someone else's score.",
  project=True),

L(22, "Inheritance: Reuse with extends",
  "Let one class receive the abilities of another.",
  "Adept", 150,
r"""
### Family traits
Children inherit things from their parents, like eye colour. In Java a class can **inherit** fields and methods from another class. This avoids copying the same code again and again.

### How to do it
```
class Animal { void eat() {...} }
class Dog extends Animal { void bark() {...} }
```
- `Animal` is the **parent** (superclass).
- `Dog` is the **child** (subclass).
- A `Dog` can use `eat()` from `Animal` and also has its own `bark()`.

### The super keyword
`super` means "my parent". Use `super(...)` to call the parent's constructor.

### The "is-a" test
Use inheritance only if the sentence "A Dog **is an** Animal" sounds right. "A Car is an Engine" sounds wrong. A car **has** an engine.

### Rule
A Java class can extend only **one** parent.
""",
r"""
public class Main {
    public static void main(String[] args) {
        Cat c = new Cat();
        c.sleep();
        c.meow();
    }
}

class Animal {
    void sleep() { System.out.println("Zzz..."); }
}

class Cat extends Animal {
    void meow() { System.out.println("Meow!"); }
}
""",
  "Dog extends Animal",
  "Write class Dog that extends Animal and has a bark() method printing 'Woof! Woof!'. Then call eat() and bark().",
r"""
public class Main {
    public static void main(String[] args) {
        Dog d = new Dog();
        d.eat();
        d.bark();
    }
}

class Animal {
    void eat() {
        System.out.println("This animal eats");
    }
}

// Write class Dog here

""",
  "This animal eats\nWoof! Woof!", ["classDogextendsAnimal", "bark()"],
  "class Dog extends Animal { void bark() { ... } }",
r"""
public class Main {
    public static void main(String[] args) {
        Dog d = new Dog();
        d.eat();
        d.bark();
    }
}

class Animal {
    void eat() {
        System.out.println("This animal eats");
    }
}

class Dog extends Animal {
    void bark() {
        System.out.println("Woof! Woof!");
    }
}
""",
  "Which keyword makes a class inherit from another?",
  ["inherits", "extends", "implements", "super"], 1,
  "extends is used when a class inherits from another class."),

L(23, "Polymorphism and Method Overriding",
  "One command, many different behaviours.",
  "Adept", 150,
r"""
### Same button, different result
Press "play" on a music player, a video player or a game console. It is the same word, but each machine does something different. This idea is **polymorphism** ("many forms").

### Overriding
A child class can **override** a parent method, which means giving it its own version:
```
class Animal { void sound() { println("..."); } }
class Dog extends Animal {
    @Override
    void sound() { println("Woof"); }
}
```
`@Override` asks Java to double-check that you really are replacing a parent method.

### The magic
A parent variable can hold a child object:
```
Animal a = new Dog();
a.sound();   // prints Woof
```
Java looks at the **real** object at run time and picks the right version.

### Why useful?
You can keep a list of different animals and just call `sound()` on each one without caring which kind it is.
""",
r"""
public class Main {
    public static void main(String[] args) {
        Shape s = new Square();
        s.draw();
    }
}

class Shape {
    void draw() { System.out.println("Drawing a shape"); }
}

class Square extends Shape {
    @Override
    void draw() { System.out.println("Drawing a square"); }
}
""",
  "Talking animals",
  "Override sound() in Cat to print 'Meow'. Then loop through the array and call sound() on each animal.",
r"""
public class Main {
    public static void main(String[] args) {
        Animal[] zoo = { new Dog(), new Cat() };
        // Loop through zoo and call sound() on each animal

    }
}

class Animal {
    void sound() { System.out.println("..."); }
}

class Dog extends Animal {
    @Override
    void sound() { System.out.println("Woof"); }
}

class Cat extends Animal {
    // Override sound() here
}
""",
  "Woof\nMeow", ["@Override", "sound()", "for"],
  "In Cat: @Override void sound() { System.out.println(\"Meow\"); }",
r"""
public class Main {
    public static void main(String[] args) {
        Animal[] zoo = { new Dog(), new Cat() };
        for (Animal a : zoo) {
            a.sound();
        }
    }
}

class Animal {
    void sound() { System.out.println("..."); }
}

class Dog extends Animal {
    @Override
    void sound() { System.out.println("Woof"); }
}

class Cat extends Animal {
    @Override
    void sound() { System.out.println("Meow"); }
}
""",
  "What does method overriding mean?",
  ["Deleting a method", "A child class gives its own version of a parent method", "Calling a method twice", "Making a method private"], 1,
  "Overriding lets a child class replace the parent's method with its own behaviour."),

L(24, "Abstract Classes and Interfaces",
  "Make rules that other classes must follow.",
  "Adept", 150,
r"""
### Promises and contracts
Sometimes you want to say: "Anything that can fly **must** have a `fly()` method", without saying how. This is a **contract**.

### Interface
An `interface` lists methods with no body. A class that `implements` it **must** write all of them.
```
interface Flyable { void fly(); }
class Bird implements Flyable {
    public void fly() { println("Bird flaps wings"); }
}
```
Methods from an interface must be marked `public` in the class.

### Abstract class
An `abstract class` is a half-finished class. It can have some real methods and some `abstract` ones that children must complete. You cannot make an object directly from it.

### Which one?
- Interface: "can do" ability (Flyable, Swimmable). A class can have many.
- Abstract class: a shared base with some code, like `Shape`.
""",
r"""
public class Main {
    public static void main(String[] args) {
        Swimmable f = new Fish();
        f.swim();
    }
}

interface Swimmable {
    void swim();
}

class Fish implements Swimmable {
    public void swim() { System.out.println("Fish swims with fins"); }
}
""",
  "Fly!",
  "Make class Plane implement Flyable and print 'Plane uses its engines' in fly(). Then call fly() on both.",
r"""
public class Main {
    public static void main(String[] args) {
        Flyable[] things = { new Bird(), new Plane() };
        for (Flyable f : things) {
            f.fly();
        }
    }
}

interface Flyable {
    void fly();
}

class Bird implements Flyable {
    public void fly() { System.out.println("Bird flaps its wings"); }
}

// Write class Plane here

""",
  "Bird flaps its wings\nPlane uses its engines", ["classPlaneimplementsFlyable", "publicvoidfly()"],
  "class Plane implements Flyable { public void fly() { ... } }",
r"""
public class Main {
    public static void main(String[] args) {
        Flyable[] things = { new Bird(), new Plane() };
        for (Flyable f : things) {
            f.fly();
        }
    }
}

interface Flyable {
    void fly();
}

class Bird implements Flyable {
    public void fly() { System.out.println("Bird flaps its wings"); }
}

class Plane implements Flyable {
    public void fly() { System.out.println("Plane uses its engines"); }
}
""",
  "What must a class do when it implements an interface?",
  ["Nothing", "Write all the methods of the interface", "Delete the interface", "Become abstract only"], 1,
  "A class that implements an interface promises to provide a body for every method in it."),

L(25, "Exceptions: Handling Errors Safely",
  "Stop your program from crashing when something goes wrong.",
  "Adept", 150,
r"""
### When things go wrong
What if the user types letters instead of a number? Or you divide by zero? Java throws an **exception**, which is like a fire alarm. If nobody handles it, the program stops.

### try and catch
```
try {
    // risky code
} catch (ArithmeticException e) {
    // what to do if it goes wrong
} finally {
    // always runs at the end
}
```
- `try` holds the risky code.
- `catch` rescues the program and shows a friendly message.
- `finally` always runs. It is good for cleaning up.

### Common exceptions
- `ArithmeticException`: like dividing by zero.
- `ArrayIndexOutOfBoundsException`: using a bad array index.
- `NumberFormatException`: turning bad text into a number.

### You can throw too
`throw new IllegalArgumentException("Bad value");` creates your own alarm.
""",
r"""
public class Main {
    public static void main(String[] args) {
        try {
            int[] a = new int[2];
            a[5] = 1;
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Oops! That box does not exist.");
        }
        System.out.println("Program is still running");
    }
}
""",
  "Safe division",
  "Divide 10 by 0 inside try. Catch the error and print 'Cannot divide by zero!'. Use finally to print 'Done'.",
r"""
public class Main {
    public static void main(String[] args) {
        int a = 10, b = 0;
        // Put the division in try { } and handle ArithmeticException
        // Use finally to print Done

    }
}
""",
  "Cannot divide by zero!\nDone", ["try", "catch(ArithmeticException", "finally"],
  "try { int c = a / b; ... } catch (ArithmeticException e) { ... } finally { ... }",
r"""
public class Main {
    public static void main(String[] args) {
        int a = 10, b = 0;
        try {
            int c = a / b;
            System.out.println(c);
        } catch (ArithmeticException e) {
            System.out.println("Cannot divide by zero!");
        } finally {
            System.out.println("Done");
        }
    }
}
""",
  "When does the finally block run?",
  ["Only when there is an error", "Only when there is no error", "Always", "Never"], 2,
  "finally runs whether or not an exception happened. It is good for cleanup work."),

L(26, "ArrayList: A List That Grows",
  "Use a flexible list instead of a fixed-size array.",
  "Adept", 150,
r"""
### Arrays cannot grow
A normal array has a fixed size. An **ArrayList** is a list that can grow and shrink while the program runs, like a notebook where you can always add or tear out pages.

### Using it
First bring it in: `import java.util.ArrayList;`
```
ArrayList<String> fruits = new ArrayList<>();
fruits.add("Apple");
fruits.add("Banana");
fruits.get(0);        // Apple
fruits.remove("Banana");
fruits.size();        // how many items
```
- The `<String>` part says what type the list holds.
- `get(i)` reads an item. The first one is at 0.
- `size()` gives the count (not `length`).

### Looping
```
for (String f : fruits) { ... }
```

### Tip
For lists of numbers use `ArrayList<Integer>`. Java needs the capital-letter version for lists.
""",
r"""
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<String> names = new ArrayList<>();
        names.add("Mina");
        names.add("Kabir");
        for (String n : names) {
            System.out.println(n);
        }
        System.out.println("Count: " + names.size());
    }
}
""",
  "Fruit basket",
  "Add Apple, Banana and Cherry. Remove Banana. Print each fruit and the size.",
r"""
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<String> fruits = new ArrayList<>();
        // add Apple, Banana, Cherry
        // remove Banana
        // print each fruit, then: Size: 2

    }
}
""",
  "Apple\nCherry\nSize: 2", ["add(", "remove(", "size()"],
  "fruits.add(\"Apple\"); ... fruits.remove(\"Banana\");",
r"""
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<String> fruits = new ArrayList<>();
        fruits.add("Apple");
        fruits.add("Banana");
        fruits.add("Cherry");
        fruits.remove("Banana");
        for (String f : fruits) {
            System.out.println(f);
        }
        System.out.println("Size: " + fruits.size());
    }
}
""",
  "How do you find how many items are in an ArrayList?",
  ["list.length", "list.size()", "list.count", "list.length()"], 1,
  "ArrayList uses size(). Arrays use .length, and Strings use length()."),

L(27, "HashMap: Look Things Up by Name",
  "Store key and value pairs, like a dictionary.",
  "Adept", 150,
r"""
### A real dictionary
In a dictionary you look up a **word** (key) and find its **meaning** (value). A `HashMap` works in exactly the same way. You find the value super fast using its key.

### Using it
`import java.util.HashMap;`
```
HashMap<String, Integer> scores = new HashMap<>();
scores.put("Asha", 85);          // add or update
int s = scores.get("Asha");      // read
scores.containsKey("Ravi");      // true or false
scores.remove("Asha");
```
- `<String, Integer>` means keys are Strings and values are Integers.
- Every key is unique. Putting the same key again replaces its value.
- Asking for a key that is not there gives `null`.

### Real life
Phone contacts (name to number), game scoreboards (player to points), and word counters all use maps.
""",
r"""
import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        HashMap<String, String> capital = new HashMap<>();
        capital.put("India", "New Delhi");
        capital.put("Japan", "Tokyo");
        System.out.println(capital.get("Japan"));
    }
}
""",
  "Score board",
  "Store Asha = 85 and Ravi = 92 in a map. Print 'Ravi scored 92'. Then print whether Meena is in the map.",
r"""
import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        HashMap<String, Integer> scores = new HashMap<>();
        // put Asha 85 and Ravi 92
        // print: Ravi scored 92
        // print: Is Meena here? false  (use containsKey)

    }
}
""",
  "Ravi scored 92\nIs Meena here? false", ["put(", "get(", "containsKey("],
  "scores.get(\"Ravi\") and scores.containsKey(\"Meena\")",
r"""
import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        HashMap<String, Integer> scores = new HashMap<>();
        scores.put("Asha", 85);
        scores.put("Ravi", 92);
        System.out.println("Ravi scored " + scores.get("Ravi"));
        System.out.println("Is Meena here? " + scores.containsKey("Meena"));
    }
}
""",
  "What is a HashMap used for?",
  ["Storing key and value pairs", "Drawing maps", "Repeating code", "Reading files only"], 0,
  "A HashMap stores pairs. You use the key to quickly find its value."),

L(28, "Mini Project 6: Bank Account",
  "Build a bank account class that protects the money with exceptions.",
  "Master", 200,
r"""
### Let's build a bank!
A bank account lets you deposit and withdraw money. The golden rule: **you cannot take out more than you have**.

### Plan
- Class `BankAccount` with a **private** `balance`.
- Method `deposit(int amount)` adds money.
- Method `withdraw(int amount)` checks first. If the balance is too low, it **throws an exception**.
- `main` uses `try / catch` to show a friendly message.

### Skills used
Classes and objects, encapsulation, exceptions and methods. This is how real banking software is organised.

### Why throw an exception?
The account class does not know how the program wants to talk to the user. So it raises an alarm (`throw`), and the code that uses the account decides what message to show (`catch`).

### Level-up idea
Add a list of transactions and a menu using `Scanner`.
""",
r"""
public class Main {
    public static void main(String[] args) {
        BankAccount acc = new BankAccount(100);
        acc.deposit(50);
        System.out.println("Balance: " + acc.getBalance());
    }
}

class BankAccount {
    private int balance;

    BankAccount(int start) { balance = start; }

    void deposit(int amount) { balance += amount; }

    int getBalance() { return balance; }
}
""",
  "Safe withdraw",
  "Finish withdraw: if the amount is more than the balance, throw an IllegalArgumentException with the message 'Insufficient balance!'.",
r"""
public class Main {
    public static void main(String[] args) {
        BankAccount acc = new BankAccount(1000);
        acc.deposit(500);
        System.out.println("Deposited 500. Balance: " + acc.getBalance());
        try {
            acc.withdraw(200);
            System.out.println("Withdrew 200. Balance: " + acc.getBalance());
            acc.withdraw(2000);
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }
        System.out.println("Final balance: " + acc.getBalance());
    }
}

class BankAccount {
    private int balance;

    BankAccount(int start) { balance = start; }

    void deposit(int amount) { balance += amount; }

    void withdraw(int amount) {
        // If amount > balance: throw new IllegalArgumentException("Insufficient balance!");
        // Otherwise subtract the amount
    }

    int getBalance() { return balance; }
}
""",
  "Deposited 500. Balance: 1500\nWithdrew 200. Balance: 1300\nInsufficient balance!\nFinal balance: 1300",
  ["thrownewIllegalArgumentException", "balance-="],
  "if (amount > balance) { throw new IllegalArgumentException(\"Insufficient balance!\"); } balance -= amount;",
r"""
public class Main {
    public static void main(String[] args) {
        BankAccount acc = new BankAccount(1000);
        acc.deposit(500);
        System.out.println("Deposited 500. Balance: " + acc.getBalance());
        try {
            acc.withdraw(200);
            System.out.println("Withdrew 200. Balance: " + acc.getBalance());
            acc.withdraw(2000);
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }
        System.out.println("Final balance: " + acc.getBalance());
    }
}

class BankAccount {
    private int balance;

    BankAccount(int start) { balance = start; }

    void deposit(int amount) { balance += amount; }

    void withdraw(int amount) {
        if (amount > balance) {
            throw new IllegalArgumentException("Insufficient balance!");
        }
        balance -= amount;
    }

    int getBalance() { return balance; }
}
""",
  "Why is the balance field marked private?",
  ["To make it faster", "So other code can only change it through safe methods", "Java needs it", "So it cannot be printed"], 1,
  "Keeping balance private forces everyone to use deposit and withdraw, which keep the rules safe.",
  project=True),

L(29, "Searching and Sorting",
  "Find a value in a list and put a list in order.",
  "Master", 180,
r"""
### Two jobs computers do all the time
1. **Searching** means finding something in a list.
2. **Sorting** means putting a list in order.

### Linear search
Look at each item one by one until you find the one you want. Easy, but slow for very big lists.

### Bubble sort
Compare neighbours. If a pair is in the wrong order, swap them. Repeat until nothing needs swapping. Big values "bubble" up to the end.

### Java's built-in helper
You do not always have to write sorting yourself. `Arrays.sort(a)` sorts an array for you. Use `Arrays.toString(a)` to print an array nicely. Bring them in with `import java.util.Arrays;`.

### Why learn bubble sort then?
Writing it yourself teaches you how loops and swaps work together. Real programmers use the built-in sort, but they understand what it does.
""",
r"""
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] a = {4, 2, 9, 1};
        Arrays.sort(a);
        System.out.println(Arrays.toString(a));
    }
}
""",
  "Sort then search",
  "Sort the array with Arrays.sort, print it with Arrays.toString, then use a loop to find 7 and print its position.",
r"""
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] a = {5, 2, 9, 1, 7};
        // 1. Sort the array
        // 2. Print it using Arrays.toString
        // 3. Loop to find 7 and print: Found 7 at position X

    }
}
""",
  "[1, 2, 5, 7, 9]\nFound 7 at position 3", ["Arrays.sort", "Arrays.toString", "for"],
  "Arrays.sort(a); then a for loop with if (a[i] == 7).",
r"""
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] a = {5, 2, 9, 1, 7};
        Arrays.sort(a);
        System.out.println(Arrays.toString(a));
        for (int i = 0; i < a.length; i++) {
            if (a[i] == 7) {
                System.out.println("Found 7 at position " + i);
            }
        }
    }
}
""",
  "What does Arrays.sort(a) do?",
  ["Deletes the array", "Puts the array in order", "Prints the array", "Copies the array"], 1,
  "Arrays.sort rearranges the array so that the values are in increasing order."),

L(30, "Final Capstone: To-Do List Manager",
  "Combine classes, lists and loops into your biggest project yet.",
  "Master", 300,
r"""
### You reached the final level!
A **capstone project** uses everything you have learned. You will build a **To-Do List Manager**, just like the apps people use every day.

### What it uses
- A **class** `Task` with a `title` and a `done` flag.
- Encapsulation (private fields, getters).
- An **ArrayList** to hold many tasks.
- **Loops** to print them.
- **Methods** to keep things tidy.

### Plan
1. `class Task` with `title`, `done`, a constructor, `markDone()` and getters.
2. `ArrayList<Task>` to store the tasks.
3. Mark one task as done.
4. Print every task with a number and `[ ]` or `[x]`.
5. Count how many are still pending.

### What next?
Use `Scanner` to build a menu to add, remove and mark tasks. Then try saving tasks to a file, or build a small game. You are now a real Java programmer. Congratulations!
""",
r"""
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<Task> list = new ArrayList<>();
        list.add(new Task("Learn Java"));
        list.get(0).markDone();
        System.out.println(list.get(0).getTitle() + " done? " + list.get(0).isDone());
    }
}

class Task {
    private String title;
    private boolean done;

    Task(String title) { this.title = title; }

    void markDone() { done = true; }
    String getTitle() { return title; }
    boolean isDone() { return done; }
}
""",
  "To-Do list",
  "Mark the second task as done, print all tasks with numbers, then print how many are still pending.",
r"""
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<Task> list = new ArrayList<>();
        list.add(new Task("Do homework"));
        list.add(new Task("Practice Java"));
        list.add(new Task("Play chess"));
        // 1. Mark the second task (index 1) as done
        // 2. Loop: print like "1. [ ] Do homework"  ([x] when done)
        // 3. Count and print: Pending tasks: 2

    }
}

class Task {
    private String title;
    private boolean done;

    Task(String title) { this.title = title; }

    void markDone() { done = true; }
    String getTitle() { return title; }
    boolean isDone() { return done; }
}
""",
  "1. [ ] Do homework\n2. [x] Practice Java\n3. [ ] Play chess\nPending tasks: 2",
  ["markDone()", "for", "pending"],
  "Use list.get(1).markDone(); and count tasks where !isDone().",
r"""
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<Task> list = new ArrayList<>();
        list.add(new Task("Do homework"));
        list.add(new Task("Practice Java"));
        list.add(new Task("Play chess"));
        list.get(1).markDone();
        int pending = 0;
        for (int i = 0; i < list.size(); i++) {
            Task t = list.get(i);
            String box = t.isDone() ? "[x]" : "[ ]";
            System.out.println((i + 1) + ". " + box + " " + t.getTitle());
            if (!t.isDone()) {
                pending++;
            }
        }
        System.out.println("Pending tasks: " + pending);
    }
}

class Task {
    private String title;
    private boolean done;

    Task(String title) { this.title = title; }

    void markDone() { done = true; }
    String getTitle() { return title; }
    boolean isDone() { return done; }
}
""",
  "Which Java collection is best for a to-do list that grows as you add tasks?",
  ["A fixed int array", "ArrayList", "A single String", "A char"], 1,
  "An ArrayList grows and shrinks as needed, which suits a list of tasks.",
  project=True),
]
