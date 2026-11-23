from . import L

LEVELS = [

L(1, "Hello, Java! Your First Program",
  "Learn what Java is and print your first message.",
  "Novice", 100,
r"""
### What is Java?
Java is a popular programming language. It runs Android apps, banking systems, games like Minecraft and much more. It is loved because it is clear, safe and works on almost every computer.

### How does Java run?
You write code in a file. A tool called the **compiler** turns it into a special code called **bytecode**. Then the **JVM** (Java Virtual Machine) runs it. Think of the JVM as a translator that lets the same program work on Windows, Mac and Linux. That is why people say "Write once, run anywhere".

### Your first program
- `public class Main` is the box that holds our code. The name must match the file name.
- `public static void main(String[] args)` is the **front door**. Java starts here.
- `System.out.println("...")` prints words on the screen and moves to a new line.
- Every instruction ends with a semicolon `;`.
- Curly brackets `{ }` mark where things start and end.
""",
r"""
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, Java!");
    }
}
""",
  "Say hello",
  "Make the program print: Quest Java Activated",
r"""
public class Main {
    public static void main(String[] args) {
        // Write your println line below

    }
}
""",
  "Quest Java Activated", ["System.out.println", "QuestJavaActivated"],
  "Write System.out.println(\"your words\"); and do not forget the semicolon.",
r"""
public class Main {
    public static void main(String[] args) {
        System.out.println("Quest Java Activated");
    }
}
""",
  "What does the JVM do?",
  ["Runs Java bytecode on any computer", "Draws pictures", "Writes code for you", "Connects to the internet"], 0,
  "The JVM runs the bytecode. Because each computer has its own JVM, the same Java program works everywhere."),

L(2, "Variables and Data Types",
  "Store numbers, decimals, letters, words and true/false values.",
  "Novice", 100,
r"""
### Variables are named boxes
A **variable** is a box with a name. You put a value inside and use it later. Java needs to know what **type** of value goes in the box.

### Main types
- `int` for whole numbers: `int age = 15;`
- `double` for decimal numbers: `double height = 5.5;`
- `char` for one letter in single quotes: `char grade = 'A';`
- `boolean` for true or false: `boolean isFun = true;`
- `String` for words in double quotes: `String name = "Zara";`

### Joining text with +
Use `+` to join words and values: `System.out.println("Age: " + age);`

### Comments
`// like this` is a note for humans. Java ignores it.

### Naming tip
Use clear names like `score`, not `x`. Start with a small letter and use capital letters for new words: `highScore`.
""",
r"""
public class Main {
    public static void main(String[] args) {
        String name = "Zara";
        int score = 90;
        double price = 12.5;
        System.out.println(name + " scored " + score);
        System.out.println("Price: " + price);
    }
}
""",
  "Student card",
  "Print the four lines using the variables: Name, Age, Height and Grade.",
r"""
public class Main {
    public static void main(String[] args) {
        String name = "Zara";
        int age = 15;
        double height = 5.5;
        char grade = 'A';

        // Print: Name: Zara   Age: 15   Height: 5.5   Grade: A

    }
}
""",
  "Name: Zara\nAge: 15\nHeight: 5.5\nGrade: A", ["+name", "+age", "+height", "+grade"],
  "System.out.println(\"Name: \" + name);",
r"""
public class Main {
    public static void main(String[] args) {
        String name = "Zara";
        int age = 15;
        double height = 5.5;
        char grade = 'A';

        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Height: " + height);
        System.out.println("Grade: " + grade);
    }
}
""",
  "Which type should you use for the word \"Hello\"?",
  ["int", "char", "String", "boolean"], 2,
  "String holds words and sentences. char only holds one single letter."),

L(3, "Talking to the Computer with Scanner",
  "Ask the user to type something and read it.",
  "Novice", 100,
r"""
### Getting input
With `Scanner` your program can **listen** to the user. First we must bring in the tool:

`import java.util.Scanner;` (at the very top of the file)

### Using it
```
Scanner sc = new Scanner(System.in);
int age = sc.nextInt();
```
- `System.in` means "the keyboard".
- `sc.nextInt()` reads a whole number.
- `sc.nextDouble()` reads a decimal number.
- `sc.nextLine()` reads a whole line of text.
- `sc.next()` reads one word.

### Tip
Always print a message first like `Enter your age:` so the user knows what to do.

**Note:** The practice box here cannot type input, so we pretend the user typed 15. Try real Scanner programs on your own computer too!
""",
r"""
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter your age:");
        int age = sc.nextInt();
        System.out.println("You are " + age + " years old.");
    }
}
""",
  "Next year",
  "Read the age with Scanner and print how old the user will be next year. (Pretend the user types 15.)",
r"""
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter your age:");
        // 1. Read the age with nextInt()
        // 2. Print: Next year you will be 16

    }
}
""",
  "Enter your age:\nNext year you will be 16", ["Scanner", "nextInt()", "age+1"],
  "int age = sc.nextInt(); then print with age + 1 (use brackets: (age + 1)).",
r"""
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter your age:");
        int age = sc.nextInt();
        System.out.println("Next year you will be " + (age + 1));
    }
}
""",
  "Which Scanner method reads a whole number?",
  ["nextInt()", "nextWord()", "readNumber()", "getInt()"], 0,
  "nextInt() reads the next whole number the user types."),

L(4, "Operators: Maths and Comparisons",
  "Do maths and ask yes/no questions.",
  "Novice", 100,
r"""
### Maths operators
- `+` add, `-` subtract, `*` multiply, `/` divide
- `%` remainder (what is left after dividing)

### Whole number division
If you divide two `int` numbers, Java drops the decimals: `17 / 5` is `3`. Make one of them a `double` to keep decimals: `17 / 5.0` is `3.4`.

### Shortcuts
`x++` adds 1. `x--` subtracts 1. `x += 5` adds 5.

### Comparison operators
They give back `true` or `false`.
- `==` equal, `!=` not equal
- `>` `<` `>=` `<=`

**Common mistake:** `=` stores a value but `==` compares two values.

### Real-life use
`n % 2 == 0` checks if a number is even.
""",
r"""
public class Main {
    public static void main(String[] args) {
        int a = 10, b = 3;
        System.out.println(a + " + " + b + " = " + (a + b));
        System.out.println(a + " / " + b + " = " + (a / b));
        System.out.println("Is a bigger? " + (a > b));
    }
}
""",
  "Maths machine",
  "With a = 17 and b = 5 print the sum, the whole-number division, the remainder and the decimal division.",
r"""
public class Main {
    public static void main(String[] args) {
        int a = 17, b = 5;
        // Print:
        // 17 + 5 = 22
        // 17 / 5 = 3
        // 17 % 5 = 2
        // 17 / 5.0 = 3.4

    }
}
""",
  "17 + 5 = 22\n17 / 5 = 3\n17 % 5 = 2\n17 / 5.0 = 3.4", ["a+b", "a/b", "a%b", "5.0"],
  "Put the maths inside brackets so Java adds the numbers instead of joining text.",
r"""
public class Main {
    public static void main(String[] args) {
        int a = 17, b = 5;
        System.out.println(a + " + " + b + " = " + (a + b));
        System.out.println(a + " / " + b + " = " + (a / b));
        System.out.println(a + " % " + b + " = " + (a % b));
        System.out.println(a + " / 5.0 = " + (a / 5.0));
    }
}
""",
  "What is 17 / 5 when both are int?",
  ["3.4", "3", "4", "2"], 1,
  "Integer division throws away the decimal part, so 17 / 5 is 3."),

L(5, "Mini Project 1: Pocket Money Tracker",
  "Build your first real program that tracks how much pocket money is left.",
  "Novice", 150,
r"""
### Let's build something real!
You know variables, printing and maths. Time for your first **mini project**: a Pocket Money Tracker.

### What the program does
1. Stores the money you started with.
2. Stores the money you spent.
3. Works out how much is left.
4. Works out the percent you still have.

### Plan before you code
Smart programmers think first:
- Step 1: make `int money` and `int spent`.
- Step 2: `int left = money - spent;`
- Step 3: `double percent = left * 100.0 / money;`. We use `100.0` so Java keeps the decimals.
- Step 4: print everything neatly.

### Try later
Use `Scanner` to let the user type their own money and spending. Change the numbers and watch the answers change!
""",
r"""
public class Main {
    public static void main(String[] args) {
        int money = 500;
        int spent = 120;
        int left = money - spent;
        double percent = left * 100.0 / money;

        System.out.println("Pocket money: " + money);
        System.out.println("Spent: " + spent);
        System.out.println("Left: " + left);
        System.out.println("You still have " + percent + "% of your money");
    }
}
""",
  "Finish the tracker",
  "Work out how much is left and the percent left, then print the 4 lines shown.",
r"""
public class Main {
    public static void main(String[] args) {
        int money = 500;
        int spent = 120;
        // 1. int left = money - spent
        // 2. double percent = left * 100.0 / money
        // 3. Print the four lines

    }
}
""",
  "Pocket money: 500\nSpent: 120\nLeft: 380\nYou still have 76.0% of your money",
  ["money-spent", "100.0", "double"],
  "Use 100.0 so the answer keeps its decimals.",
r"""
public class Main {
    public static void main(String[] args) {
        int money = 500;
        int spent = 120;
        int left = money - spent;
        double percent = left * 100.0 / money;
        System.out.println("Pocket money: " + money);
        System.out.println("Spent: " + spent);
        System.out.println("Left: " + left);
        System.out.println("You still have " + percent + "% of your money");
    }
}
""",
  "Why do we use 100.0 instead of 100 in the percent formula?",
  ["It looks nicer", "So Java keeps the decimal part", "Java needs it", "It is faster"], 1,
  "With 100.0 the maths uses decimals, so the answer is not rounded down.",
  project=True),

L(6, "Making Decisions with if and else",
  "Teach your program to choose between two paths.",
  "Novice", 100,
r"""
### A program that decides
"If it rains, take an umbrella. Otherwise, wear sunglasses." Your programs can make choices like this using `if` and `else`.

### How it looks
```
if (condition) {
    // runs when true
} else {
    // runs when false
}
```
- The condition goes in round brackets `( )` and must be `true` or `false`.
- The `else` part is optional.

### else if
When there are more than two choices, add `else if`:
```
if (marks >= 90) { ... }
else if (marks >= 75) { ... }
else { ... }
```
Java checks from top to bottom and stops at the first true one.

### Tip
Indent the code inside `{ }` so it is easy to read.
""",
r"""
public class Main {
    public static void main(String[] args) {
        int marks = 82;
        if (marks >= 90) {
            System.out.println("Grade A");
        } else if (marks >= 75) {
            System.out.println("Grade B");
        } else {
            System.out.println("Keep trying!");
        }
    }
}
""",
  "Odd or even",
  "The number is 7. Print '7 is odd' or '7 is even' using if / else.",
r"""
public class Main {
    public static void main(String[] args) {
        int n = 7;
        // Use if / else with n % 2

    }
}
""",
  "7 is odd", ["if", "else", "%2"],
  "If n % 2 == 0 the number is even.",
r"""
public class Main {
    public static void main(String[] args) {
        int n = 7;
        if (n % 2 == 0) {
            System.out.println(n + " is even");
        } else {
            System.out.println(n + " is odd");
        }
    }
}
""",
  "When does the else part run?",
  ["Always", "When the if condition is false", "When the if condition is true", "Never"], 1,
  "else is the 'otherwise' path. It runs only when the if condition is false."),

L(7, "The switch Statement",
  "Pick one path from many exact choices.",
  "Novice", 100,
r"""
### When to use switch
If you compare **one variable** with many exact values (like day 1, 2, 3), `switch` is neater than many `else if` lines.

### How it works
```
switch (day) {
    case 1: ... break;
    case 2: ... break;
    default: ...
}
```
- Each `case` is one possible value.
- `break;` stops Java from running the next case too. Forgetting it is a famous bug.
- `default:` runs when nothing matches.

### Works with
`int`, `char` and `String` values.

### Modern Java
Newer Java also has arrow style: `case 1 -> System.out.println("Monday");`. It does not need `break`. You can try it later!
""",
r"""
public class Main {
    public static void main(String[] args) {
        String color = "green";
        switch (color) {
            case "red": System.out.println("Stop"); break;
            case "green": System.out.println("Go"); break;
            default: System.out.println("Wait");
        }
    }
}
""",
  "Day namer",
  "Use switch to print the name of day number 3 (1 = Monday, 2 = Tuesday, 3 = Wednesday).",
r"""
public class Main {
    public static void main(String[] args) {
        int day = 3;
        // Write a switch with cases 1, 2 and 3

    }
}
""",
  "Wednesday", ["switch", "case", "break"],
  "Remember break; after each case.",
r"""
public class Main {
    public static void main(String[] args) {
        int day = 3;
        switch (day) {
            case 1: System.out.println("Monday"); break;
            case 2: System.out.println("Tuesday"); break;
            case 3: System.out.println("Wednesday"); break;
            default: System.out.println("Unknown day");
        }
    }
}
""",
  "What does break do inside a switch case?",
  ["Closes the program", "Stops Java from running the next case", "Prints a message", "Starts a loop"], 1,
  "break leaves the switch so the following cases do not run too."),

L(8, "Combining Conditions: &&, || and !",
  "Join several yes/no questions together.",
  "Novice", 100,
r"""
### Joining questions
Real questions often have more than one part: "Are you 13 or older **and** younger than 20?"

### Logical operators
- `&&` means AND. Both sides must be true.
- `||` means OR. At least one side must be true.
- `!` means NOT. It flips true to false.

### Examples
```
boolean isTeen = age >= 13 && age <= 19;
boolean weekend = day == 6 || day == 7;
boolean notEmpty = !isEmpty;
```

### Short-circuit
Java is lazy in a smart way. In `a && b`, if `a` is false, Java does not even check `b`, because the answer is already false.

### Tip
Use brackets when mixing `&&` and `||` so your meaning is clear.
""",
r"""
public class Main {
    public static void main(String[] args) {
        int height = 130;
        int age = 9;
        boolean canRide = height >= 120 && age >= 8;
        System.out.println("Can ride: " + canRide);
    }
}
""",
  "Teenager check",
  "Age is 15. Print whether the person is a teenager (13 to 19) and whether they can vote (18 or more).",
r"""
public class Main {
    public static void main(String[] args) {
        int age = 15;
        boolean isTeen = false;   // fix this using >= , <= and &&
        boolean canVote = false;  // fix this using >=

        System.out.println("Is teenager: " + isTeen);
        System.out.println("Can vote: " + canVote);
    }
}
""",
  "Is teenager: true\nCan vote: false", ["&&", ">="],
  "isTeen = age >= 13 && age <= 19;",
r"""
public class Main {
    public static void main(String[] args) {
        int age = 15;
        boolean isTeen = age >= 13 && age <= 19;
        boolean canVote = age >= 18;

        System.out.println("Is teenager: " + isTeen);
        System.out.println("Can vote: " + canVote);
    }
}
""",
  "When is (a && b) true?",
  ["When a is true", "When b is true", "When both a and b are true", "Always"], 2,
  "&& means AND. Both sides have to be true."),

L(9, "Mini Project 2: Simple Calculator",
  "Build a calculator that can add, subtract, multiply and divide.",
  "Novice", 150,
r"""
### Our second project
Let's build a **calculator**. The user gives two numbers and an operation (+, -, *, /). The program prints the answer.

### Plan
1. Store the numbers `a` and `b`.
2. Store the operation in a `char` called `op`.
3. Use `switch (op)` to pick the correct maths.
4. Print the result.

### Important: dividing by zero
Dividing by 0 is not allowed. A careful program checks first and shows a friendly message. Checking user input like this is called **validation**.

### Skills used
Variables, `Scanner`, operators and `switch`.

### Full version idea
Read the symbol using `char op = sc.next().charAt(0);`. Then put everything in a loop so the user can keep calculating.
""",
r"""
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter: number operator number");
        double a = sc.nextDouble();
        char op = sc.next().charAt(0);
        double b = sc.nextDouble();

        switch (op) {
            case '+': System.out.println(a + b); break;
            case '-': System.out.println(a - b); break;
            case '*': System.out.println(a * b); break;
            case '/':
                if (b == 0) System.out.println("Cannot divide by zero!");
                else System.out.println(a / b);
                break;
            default: System.out.println("Unknown operator");
        }
    }
}
""",
  "Add the divide button",
  "The calculator has no division yet. Add the '/' case so that 20 / 5 prints '20 / 5 = 4'.",
r"""
public class Main {
    public static void main(String[] args) {
        int a = 20, b = 5;
        char op = '/';

        switch (op) {
            case '+': System.out.println(a + " + " + b + " = " + (a + b)); break;
            case '-': System.out.println(a + " - " + b + " = " + (a - b)); break;
            case '*': System.out.println(a + " * " + b + " = " + (a * b)); break;
            // TODO: add case '/' here. Check that b is not 0 first!
        }
    }
}
""",
  "20 / 5 = 4", ["case'/'", "b==0", "a/b"],
  "In case '/': if (b == 0) print a warning, else print the division.",
r"""
public class Main {
    public static void main(String[] args) {
        int a = 20, b = 5;
        char op = '/';

        switch (op) {
            case '+': System.out.println(a + " + " + b + " = " + (a + b)); break;
            case '-': System.out.println(a + " - " + b + " = " + (a - b)); break;
            case '*': System.out.println(a + " * " + b + " = " + (a * b)); break;
            case '/':
                if (b == 0) {
                    System.out.println("Cannot divide by zero!");
                } else {
                    System.out.println(a + " / " + b + " = " + (a / b));
                }
                break;
        }
    }
}
""",
  "Why check if b == 0 before dividing?",
  ["Division is slow", "Dividing integers by zero crashes the program", "Java hates zero", "To get a bigger answer"], 1,
  "Dividing an int by zero throws an error and stops the program. Checking first keeps it safe.",
  project=True),

L(10, "The for Loop",
  "Repeat work without typing it again and again.",
  "Apprentice", 120,
r"""
### Why loops?
Imagine writing "I will do my homework" 100 times. A **loop** tells the computer to repeat work for you.

### The for loop
```
for (start; condition; step) {
    // repeated work
}
```
- **start**: where to begin, like `int i = 1`.
- **condition**: keep going while it is true, like `i <= 5`.
- **step**: what happens after each round, like `i++`.

It is like climbing stairs: start at step 1, keep going while you are at or below step 5, and move up one step each time.

### Printing on one line
`System.out.print(...)` prints **without** a new line. `System.out.println(...)` adds the new line.
""",
r"""
public class Main {
    public static void main(String[] args) {
        for (int i = 1; i <= 5; i++) {
            System.out.println("Round " + i);
        }
    }
}
""",
  "Even numbers",
  "Use a for loop to print the even numbers from 2 to 10 on one line.",
r"""
public class Main {
    public static void main(String[] args) {
        // Print: 2 4 6 8 10
        // Hint: start at 2 and go up by 2

        System.out.println();
    }
}
""",
  "2 4 6 8 10", ["for", "i+=2"],
  "Use i += 2 as the step.",
r"""
public class Main {
    public static void main(String[] args) {
        for (int i = 2; i <= 10; i += 2) {
            System.out.print(i + " ");
        }
        System.out.println();
    }
}
""",
  "In for (int i = 1; i <= 5; i++), how many times does the loop run?",
  ["4", "5", "6", "Forever"], 1,
  "i takes the values 1, 2, 3, 4 and 5. That is 5 rounds."),

L(11, "while and do-while Loops",
  "Repeat until something changes.",
  "Apprentice", 120,
r"""
### When you do not know how many times
A `for` loop is great when you know the count. A `while` loop is better for "keep going **until** something happens", like "play until the game is over".

### while
```
while (condition) {
    // work
}
```
Java checks the condition first. If it is false at the start, the loop never runs.

### do-while
`do { ... } while (condition);` runs the work **once first** and then checks. Perfect for menus that must show at least once.

### Danger: infinite loop
If the condition never becomes false, the loop never ends. Always change something inside the loop, like `n--`.
""",
r"""
public class Main {
    public static void main(String[] args) {
        int coins = 3;
        while (coins > 0) {
            System.out.println("Coins left: " + coins);
            coins--;
        }
        System.out.println("Out of coins!");
    }
}
""",
  "Rocket countdown",
  "Use a while loop to count down from 5 to 1, then print 'Blast off!'.",
r"""
public class Main {
    public static void main(String[] args) {
        int n = 5;
        // while n is more than 0, print n and then lower it by 1

        System.out.println("Blast off!");
    }
}
""",
  "5\n4\n3\n2\n1\nBlast off!", ["while", "n--"],
  "Inside the loop: print n, then n--.",
r"""
public class Main {
    public static void main(String[] args) {
        int n = 5;
        while (n > 0) {
            System.out.println(n);
            n--;
        }
        System.out.println("Blast off!");
    }
}
""",
  "What is special about do-while?",
  ["It never runs", "It always runs the body at least once", "It is only for numbers", "It cannot stop"], 1,
  "do-while checks the condition after the body, so the body always runs at least one time."),

L(12, "Nested Loops, break and continue",
  "Draw patterns and control your loops.",
  "Apprentice", 120,
r"""
### A loop inside a loop
Put one loop inside another and you get a **nested loop**. Think of a clock: for every hour (outer loop), the minute hand goes around many times (inner loop).

### Drawing patterns
- The **outer loop** handles the rows.
- The **inner loop** handles what is printed in each row.
- After each row, call `System.out.println()` to go to the next line.

### break and continue
- `break;` stops the loop completely.
- `continue;` skips to the next round.

Example: print 1 to 10 but skip 5 (`continue`) and stop at 8 (`break`).

### Tip
For a triangle, the inner loop runs as many times as the row number: row 1 has 1 star, row 2 has 2 stars, and so on.
""",
r"""
public class Main {
    public static void main(String[] args) {
        for (int row = 1; row <= 3; row++) {
            for (int col = 1; col <= row; col++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
""",
  "Star triangle",
  "Print a triangle with 4 rows of stars (1, 2, 3 and 4 stars).",
r"""
public class Main {
    public static void main(String[] args) {
        // Outer loop for rows 1 to 4
        // Inner loop prints stars

    }
}
""",
  "*\n**\n***\n****", ["for", "for", "*"],
  "The inner loop should run from 1 up to the row number.",
r"""
public class Main {
    public static void main(String[] args) {
        for (int row = 1; row <= 4; row++) {
            for (int col = 1; col <= row; col++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
""",
  "What does continue do in a loop?",
  ["Stops the loop", "Skips the rest of this round and goes to the next", "Restarts the program", "Prints a message"], 1,
  "continue jumps straight to the next round of the loop."),

L(13, "Mini Project 3: Times Table and Guessing Game",
  "Use loops to build a times table and a number guessing game.",
  "Apprentice", 150,
r"""
### Two projects in one
Loops make real programs possible. Let's build two things.

### Project A: Times Table
A `for` loop runs from 1 to 10 and prints `number x i = answer`. We also keep a running **total** of all the answers.

### Project B: Guessing Game
The program hides a secret number. The player guesses again and again until correct:
1. `int secret = 7;`
2. A `while` loop asks for a guess with `Scanner`.
3. Too low? Print "Too low!". Too high? Print "Too high!".
4. When right, print how many tries it took.

### Skills used
`for`, `while`, `if / else`, `Scanner`, variables and maths.

### Level-up idea
Use `new Random().nextInt(10) + 1` to make the computer pick a different secret every time!
""",
r"""
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int secret = 7, guess = 0, tries = 0;
        while (guess != secret) {
            System.out.println("Guess the number (1-10):");
            guess = sc.nextInt();
            tries++;
            if (guess < secret) System.out.println("Too low!");
            else if (guess > secret) System.out.println("Too high!");
        }
        System.out.println("You got it in " + tries + " tries!");
    }
}
""",
  "Times table builder",
  "Print the table of 4 from 1 to 5, then print the total of all the answers.",
r"""
public class Main {
    public static void main(String[] args) {
        int num = 4;
        int total = 0;
        // Loop i from 1 to 5
        // Print: 4 x 1 = 4 ... and add each answer to total

        System.out.println("Total: " + total);
    }
}
""",
  "4 x 1 = 4\n4 x 2 = 8\n4 x 3 = 12\n4 x 4 = 16\n4 x 5 = 20\nTotal: 60", ["for", "total+="],
  "Inside the loop print the line and then total += num * i;",
r"""
public class Main {
    public static void main(String[] args) {
        int num = 4;
        int total = 0;
        for (int i = 1; i <= 5; i++) {
            System.out.println(num + " x " + i + " = " + (num * i));
            total += num * i;
        }
        System.out.println("Total: " + total);
    }
}
""",
  "Which loop fits best when you do not know how many guesses the player needs?",
  ["for with a fixed count", "while", "switch", "No loop"], 1,
  "A while loop repeats until the condition changes, which suits an unknown number of tries.",
  project=True),

L(14, "Methods: Your Own Mini Machines",
  "Write code once and use it many times.",
  "Apprentice", 120,
r"""
### What is a method?
A **method** is a small machine that does one job. You build it once and use it whenever you like. `println` is a method somebody else wrote. Now you write your own.

### Parts of a method
```
static int add(int a, int b) {
    return a + b;
}
```
- `static` lets us call it from `main` without making an object (you will learn objects soon).
- `int` is the type of the answer. Use `void` if nothing comes back.
- `add` is the name.
- `(int a, int b)` are the **parameters**, the inputs.
- `return` sends the answer back.

### Calling a method
`int total = add(3, 4);`

### Why use methods?
They save typing, avoid mistakes and make big programs easy to read. Give each method one clear job.
""",
r"""
public class Main {
    static int square(int x) {
        return x * x;
    }

    static void greet(String name) {
        System.out.println("Hello, " + name + "!");
    }

    public static void main(String[] args) {
        greet("Quest");
        System.out.println("6 squared is " + square(6));
    }
}
""",
  "Find the bigger number",
  "Write a method bigger(int a, int b) that returns the larger number. Print the bigger of 4 and 9.",
r"""
public class Main {
    // Write static int bigger(int a, int b) here

    public static void main(String[] args) {
        System.out.println("Bigger: " + bigger(4, 9));
    }
}
""",
  "Bigger: 9", ["staticintbigger", "return"],
  "if (a > b) return a; otherwise return b;",
r"""
public class Main {
    static int bigger(int a, int b) {
        if (a > b) {
            return a;
        }
        return b;
    }

    public static void main(String[] args) {
        System.out.println("Bigger: " + bigger(4, 9));
    }
}
""",
  "What does the word void mean in front of a method?",
  ["It returns a number", "It returns nothing", "It is broken", "It is private"], 1,
  "void means the method does its work but does not send any value back."),

L(15, "Arrays: A Row of Boxes",
  "Store many values of the same type under one name.",
  "Apprentice", 120,
r"""
### Too many variables!
To store the marks of 30 students you would not create 30 variables. An **array** is a row of boxes under one name, all holding the same type.

### Making an array
`int[] marks = {70, 80, 90, 60, 50};`

- Boxes are numbered from **0**. `marks[0]` is 70 and `marks[4]` is 50.
- `marks.length` tells you how many boxes there are (no brackets after `length` for arrays).
- Going outside the array, like `marks[5]`, causes an `ArrayIndexOutOfBoundsException` error.

### Looping through an array
```
for (int i = 0; i < marks.length; i++) { ... }
```
or the friendly **for-each** loop:
```
for (int m : marks) { ... }
```
Read it as "for each m in marks".
""",
r"""
public class Main {
    public static void main(String[] args) {
        int[] marks = {70, 80, 90};
        for (int m : marks) {
            System.out.println("Mark: " + m);
        }
        System.out.println("Boxes: " + marks.length);
    }
}
""",
  "Add up the scores",
  "Print all scores on one line, then print their sum.",
r"""
public class Main {
    public static void main(String[] args) {
        int[] scores = {10, 20, 30, 40, 50};
        int sum = 0;
        // Loop through the array, print each score and add it to sum

        System.out.println();
        System.out.println("Sum: " + sum);
    }
}
""",
  "10 20 30 40 50\nSum: 150", ["for", "sum+="],
  "for (int s : scores) { print s and add to sum }",
r"""
public class Main {
    public static void main(String[] args) {
        int[] scores = {10, 20, 30, 40, 50};
        int sum = 0;
        for (int s : scores) {
            System.out.print(s + " ");
            sum += s;
        }
        System.out.println();
        System.out.println("Sum: " + sum);
    }
}
""",
  "What is the index of the FIRST box in an array?",
  ["1", "0", "-1", "length"], 1,
  "Arrays start counting at 0. The first box is a[0]."),
]
