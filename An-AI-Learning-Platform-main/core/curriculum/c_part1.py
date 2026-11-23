from . import L

LEVELS = [

L(1, "Hello, World! Your First C Program",
  "Learn what programming is and write your very first C program.",
  "Novice", 100,
r"""
### What is programming?
A computer is super fast, but it cannot think. It only does what you tell it, one step at a time. **Programming** means writing those steps in a language the computer understands.

### Why learn C?
C is one of the oldest and most loved languages. Phones, games and even other programming languages are built with C. Once you know C, other languages feel easy.

### Your first program
Every C program starts at a place called `main`. Think of it as the front door of a house. The computer walks in through this door.

- `#include <stdio.h>` lets us use `printf`.
- `int main()` is the front door.
- `printf` means "print on the screen". The words go inside double quotes.
- `\n` means "go to a new line".
- Every instruction ends with a semicolon `;` like a full stop in English.
- `return 0;` means "everything went fine".
""",
r"""
#include <stdio.h>

int main() {
    printf("Hello, World!\n");
    return 0;
}
""",
  "Say hello",
  "Make the program print: Quest C Activated",
r"""
#include <stdio.h>

int main() {
    // Write your printf line below

    return 0;
}
""",
  "Quest C Activated", ["printf", "QuestCActivated"],
  "Write printf, then your words inside double quotes, then \\n and a semicolon.",
r"""
#include <stdio.h>

int main() {
    printf("Quest C Activated\n");
    return 0;
}
""",
  "What does printf do?",
  ["Prints words on the screen", "Saves a file", "Turns off the computer", "Draws a picture"], 0,
  "printf prints text on the screen. It is the way a C program talks to you."),

L(2, "Printing Many Lines and Writing Comments",
  "Print more than one line and leave notes inside your code.",
  "Novice", 100,
r"""
### Printing many lines
You can use `printf` as many times as you like. Each `printf` prints its words one after the other. If you want the next words on a new line, end the text with `\n`.

### Special characters
- `\n` goes to a new line.
- `\t` leaves a big space (like pressing the Tab key).
- `\"` prints a double quote.

### Comments
A **comment** is a note for humans. The computer ignores it. Good programmers write comments to explain their code.

- `// like this` is a one-line comment.
- `/* like this */` can cover many lines.

Comments are like sticky notes on your homework. They do not change the answer, but they help you remember.
""",
r"""
#include <stdio.h>

int main() {
    // This line prints a title
    printf("My Diary\n");
    printf("Day 1:\tI learned C!\n");
    /* This is a
       longer comment */
    printf("She said \"Hi\"\n");
    return 0;
}
""",
  "About me",
  "Print three lines: My name is Quest, I am learning C, It is fun!",
r"""
#include <stdio.h>

int main() {
    // Print 3 lines. Do not forget \n at the end of each one.

    return 0;
}
""",
  "My name is Quest\nI am learning C\nIt is fun!",
  ["printf", "MynameisQuest", "IamlearningC", "Itisfun!"],
  "Use three printf lines. Put \\n at the end of each text.",
r"""
#include <stdio.h>

int main() {
    printf("My name is Quest\n");
    printf("I am learning C\n");
    printf("It is fun!\n");
    return 0;
}
""",
  "Which symbol starts a one-line comment?",
  ["//", "##", "<>", "!!"], 0,
  "Two slashes // start a one-line comment. The computer ignores everything after them on that line."),

L(3, "Variables and Data Types",
  "Store numbers, decimals and letters in named boxes called variables.",
  "Novice", 100,
r"""
### What is a variable?
A **variable** is a box with a name on it. You can put a value inside and use it later. Before using a box, C wants to know what kind of thing goes inside. That is the **data type**.

### Main data types
- `int` is for whole numbers like 15 or -3.
- `float` is for decimal numbers like 5.5.
- `char` is for one single letter like 'A'. Use single quotes.

### Printing variables
Use a **format code** as a placeholder inside `printf`:
- `%d` for int
- `%f` for float (use `%.1f` to show one decimal place)
- `%c` for char

Example: `printf("Age: %d\n", age);` puts the value of `age` where `%d` is.

### Constants
If a value should never change, write `const` before it, like `const float PI = 3.14;`.
""",
r"""
#include <stdio.h>

int main() {
    int score = 90;
    float price = 12.5;
    char letter = 'Q';

    printf("Score: %d\n", score);
    printf("Price: %.1f\n", price);
    printf("Letter: %c\n", letter);
    return 0;
}
""",
  "Player card",
  "Print the age, height and grade using the three variables.",
r"""
#include <stdio.h>

int main() {
    int age = 15;
    float height = 5.5;
    char grade = 'A';

    // Print: Age: 15, Height: 5.5, Grade: A

    return 0;
}
""",
  "Age: 15\nHeight: 5.5\nGrade: A", ["%d", "%.1f", "%c"],
  "Use %d for age, %.1f for height and %c for grade.",
r"""
#include <stdio.h>

int main() {
    int age = 15;
    float height = 5.5;
    char grade = 'A';

    printf("Age: %d\n", age);
    printf("Height: %.1f\n", height);
    printf("Grade: %c\n", grade);
    return 0;
}
""",
  "Which data type should you use to store 5.5?",
  ["int", "float", "char", "const"], 1,
  "float stores numbers with a decimal point. int can only store whole numbers."),

L(4, "Talking to the Computer with scanf",
  "Ask the user to type something and store it in a variable.",
  "Novice", 100,
r"""
### Getting input
So far the program only talks. With `scanf` the program can **listen**. It waits for the user to type something and saves it in a variable.

### How scanf works
`scanf("%d", &age);`

- `"%d"` says "I expect a whole number".
- `&age` says "put it in the box named age". The `&` sign means "the address (home) of age". You will learn why later.

### Other codes
- `%d` for int
- `%f` for float
- `%c` for char

### Tip
Always print a message first, like `Enter your age:`, so the user knows what to type. A program that asks without saying anything is confusing.

**Note:** The practice box on this website cannot type input for you, so we pretend the user typed 15. Try real `scanf` programs on your own computer too!
""",
r"""
#include <stdio.h>

int main() {
    int age;
    printf("Enter your age: ");
    scanf("%d", &age);
    printf("You are %d years old.\n", age);
    return 0;
}
""",
  "Next year",
  "Ask for the age with scanf, then print how old the user will be next year. (Pretend the user types 15.)",
r"""
#include <stdio.h>

int main() {
    int age;
    printf("Enter your age:\n");
    // 1. Use scanf to read age
    // 2. Print: Next year you will be 16 (use age + 1)

    return 0;
}
""",
  "Enter your age:\nNext year you will be 16", ["scanf", "&age", "age+1"],
  "scanf(\"%d\", &age); then printf with %d and age + 1.",
r"""
#include <stdio.h>

int main() {
    int age;
    printf("Enter your age:\n");
    scanf("%d", &age);
    printf("Next year you will be %d\n", age + 1);
    return 0;
}
""",
  "What does the & sign do in scanf(\"%d\", &age)?",
  ["Adds two numbers", "Tells scanf where the variable lives so it can store the value", "Prints the value", "Closes the program"], 1,
  "The & gives scanf the address of the variable, so scanf knows exactly where to put the typed value."),

L(5, "Math Operators",
  "Add, subtract, multiply, divide and find remainders.",
  "Novice", 100,
r"""
### Doing maths in C
C can do maths for you. The symbols are called **operators**.

- `+` add
- `-` subtract
- `*` multiply
- `/` divide
- `%` remainder (what is left over after dividing)

### Watch out: whole number division
When you divide two `int` numbers, C throws away the decimal part. So `17 / 5` gives `3`, not 3.4. The `%` operator tells you what was left: `17 % 5` is `2`.

### Shortcuts
- `x++` means add 1 to x.
- `x--` means subtract 1 from x.
- `x += 5` means add 5 to x.

### Real-life use
The remainder `%` is great for checking even or odd. If `n % 2` is 0 the number is even.
""",
r"""
#include <stdio.h>

int main() {
    int a = 10, b = 3;
    printf("%d + %d = %d\n", a, b, a + b);
    printf("%d / %d = %d\n", a, b, a / b);
    printf("%d %% %d = %d\n", a, b, a % b);
    return 0;
}
""",
  "Maths machine",
  "With a = 17 and b = 5, print the sum, the division and the remainder.",
r"""
#include <stdio.h>

int main() {
    int a = 17, b = 5;
    // Print:
    // 17 + 5 = 22
    // 17 / 5 = 3
    // 17 % 5 = 2

    return 0;
}
""",
  "17 + 5 = 22\n17 / 5 = 3\n17 % 5 = 2", ["a+b", "a/b", "a%b"],
  "To print a percent sign in printf you must write %% (two of them).",
r"""
#include <stdio.h>

int main() {
    int a = 17, b = 5;
    printf("%d + %d = %d\n", a, b, a + b);
    printf("%d / %d = %d\n", a, b, a / b);
    printf("%d %% %d = %d\n", a, b, a % b);
    return 0;
}
""",
  "What is 17 % 5 in C?",
  ["3", "2", "3.4", "85"], 1,
  "17 divided by 5 is 3 with 2 left over. The % operator gives the leftover, which is 2."),

L(6, "Mini Project 1: Pocket Money Tracker",
  "Build your first real program that tracks how much pocket money is left.",
  "Novice", 150,
r"""
### Let's build something real!
You now know variables, printing, input and maths. Time to put them together in a **mini project**: a Pocket Money Tracker.

### What the program does
1. Keeps the money you had at the start.
2. Keeps the money you spent.
3. Works out how much is left.
4. Works out what percent you still have.

### Plan before you code
Good programmers think first:
- Step 1: make variables `money` and `spent`.
- Step 2: `left = money - spent`.
- Step 3: `percent = left * 100.0 / money`. We use `100.0` (with a decimal) so C does not throw away the decimal part.
- Step 4: print everything neatly.

### Idea to try later
Change the numbers and watch the answers change. You can also use `scanf` to let the user type their own numbers!
""",
r"""
#include <stdio.h>

int main() {
    int money = 500;
    int spent = 120;
    int left = money - spent;
    float percent = left * 100.0 / money;

    printf("Pocket money: %d\n", money);
    printf("Spent: %d\n", spent);
    printf("Left: %d\n", left);
    printf("You still have %.1f%% of your money\n", percent);
    return 0;
}
""",
  "Finish the tracker",
  "Calculate how much is left and the percent left, then print the 4 lines shown below.",
r"""
#include <stdio.h>

int main() {
    int money = 500;
    int spent = 120;
    // 1. Make an int called left (money - spent)
    // 2. Make a float called percent (left * 100.0 / money)
    // 3. Print the four lines

    return 0;
}
""",
  "Pocket money: 500\nSpent: 120\nLeft: 380\nYou still have 76.0% of your money",
  ["money-spent", "100.0", "%.1f"],
  "Use 100.0 not 100 so the answer keeps its decimals. Print % with %%.",
r"""
#include <stdio.h>

int main() {
    int money = 500;
    int spent = 120;
    int left = money - spent;
    float percent = left * 100.0 / money;
    printf("Pocket money: %d\n", money);
    printf("Spent: %d\n", spent);
    printf("Left: %d\n", left);
    printf("You still have %.1f%% of your money\n", percent);
    return 0;
}
""",
  "Why do we write 100.0 instead of 100 in the percent formula?",
  ["It looks nicer", "So C keeps the decimal part of the answer", "It makes the program faster", "C does not allow 100"], 1,
  "When all numbers are ints, C drops the decimals. Using 100.0 makes the whole calculation use decimals.",
  project=True),

L(7, "Comparing Things: Comparison and Logical Operators",
  "Ask yes/no questions in code using ==, <, >, && and ||.",
  "Novice", 100,
r"""
### Asking questions
Programs often need to ask a question: "Is the score bigger than 50?" The answer is always **yes** or **no**. In C, yes is `1` and no is `0`.

### Comparison operators
- `==` is equal to (two equal signs!)
- `!=` is not equal to
- `>` greater than, `<` less than
- `>=` greater than or equal, `<=` less than or equal

**Common mistake:** `=` stores a value. `==` compares values. They are different!

### Logical operators
They join questions together:
- `&&` means AND. Both must be true.
- `||` means OR. At least one must be true.
- `!` means NOT. It flips yes to no.

Example: you can ride a roller coaster if `height >= 120 && age >= 8`. You need both.
""",
r"""
#include <stdio.h>

int main() {
    int marks = 72;
    printf("Passed: %d\n", marks >= 40);
    printf("Topper: %d\n", marks > 90);
    printf("Good and passed: %d\n", marks >= 40 && marks < 90);
    return 0;
}
""",
  "Teenager check",
  "Age is 15. Print 1 or 0 for 'Is teenager' (13 to 19) and 'Can vote' (18 or more).",
r"""
#include <stdio.h>

int main() {
    int age = 15;
    int is_teen = 0;   // change this using >= , <= and &&
    int can_vote = 0;  // change this using >=

    printf("Is teenager: %d\n", is_teen);
    printf("Can vote: %d\n", can_vote);
    return 0;
}
""",
  "Is teenager: 1\nCan vote: 0", ["&&", ">="],
  "is_teen = (age >= 13 && age <= 19);",
r"""
#include <stdio.h>

int main() {
    int age = 15;
    int is_teen = (age >= 13 && age <= 19);
    int can_vote = (age >= 18);
    printf("Is teenager: %d\n", is_teen);
    printf("Can vote: %d\n", can_vote);
    return 0;
}
""",
  "Which one checks if two values are equal?",
  ["=", "==", "=>", "!"], 1,
  "== compares two values. A single = is used to store a value in a variable."),

L(8, "Making Decisions with if and else",
  "Teach your program to choose between two paths.",
  "Novice", 100,
r"""
### A program that decides
Real life is full of choices: "If it rains, take an umbrella. Otherwise, wear sunglasses." Programs can decide too using `if` and `else`.

### How it looks
```
if (condition) {
    // runs when the condition is true
} else {
    // runs when the condition is false
}
```

- The condition goes inside round brackets `( )`.
- The code to run goes inside curly brackets `{ }`.
- `else` is optional. It is the "otherwise" part.

### Even or odd trick
A number is even if the remainder after dividing by 2 is 0. So we write `if (n % 2 == 0)`.

### Tip
Use spaces inside the curly brackets (indent) so your code is easy to read.
""",
r"""
#include <stdio.h>

int main() {
    int temperature = 32;

    if (temperature > 30) {
        printf("It is hot! Drink water.\n");
    } else {
        printf("The weather is nice.\n");
    }
    return 0;
}
""",
  "Odd or even",
  "The number is 7. Print '7 is odd' if it is odd, or '7 is even' if it is even.",
r"""
#include <stdio.h>

int main() {
    int n = 7;
    // Use if / else with n % 2

    return 0;
}
""",
  "7 is odd", ["if", "else", "%2"],
  "If n % 2 == 0 it is even. Otherwise it is odd.",
r"""
#include <stdio.h>

int main() {
    int n = 7;
    if (n % 2 == 0) {
        printf("%d is even\n", n);
    } else {
        printf("%d is odd\n", n);
    }
    return 0;
}
""",
  "When does the else part run?",
  ["Always", "When the if condition is false", "When the if condition is true", "Never"], 1,
  "else is the 'otherwise' path. It runs only when the if condition is false."),

L(9, "else-if Ladder and switch",
  "Choose between many options, like grades or days of the week.",
  "Novice", 100,
r"""
### More than two choices
Sometimes two paths are not enough. A grade can be A, B, C or D. Use `else if` to add more questions. C checks them from top to bottom and stops at the first one that is true.

### switch
When you compare one variable with many fixed values, `switch` is neater.

- Each `case` is one possible value.
- `break;` stops C from running the next case too. If you forget it, C keeps going. This is a famous bug!
- `default:` runs when no case matches.

### Which one to use?
- Ranges like "marks above 80": use `else if`.
- Exact values like day 1, 2, 3: use `switch`.
""",
r"""
#include <stdio.h>

int main() {
    int marks = 82;
    if (marks >= 90) {
        printf("Grade A\n");
    } else if (marks >= 75) {
        printf("Grade B\n");
    } else {
        printf("Keep trying!\n");
    }

    int day = 2;
    switch (day) {
        case 1: printf("Monday\n"); break;
        case 2: printf("Tuesday\n"); break;
        default: printf("Another day\n");
    }
    return 0;
}
""",
  "Day namer",
  "Use switch to print the name of day number 3 (1 = Monday, 2 = Tuesday, 3 = Wednesday).",
r"""
#include <stdio.h>

int main() {
    int day = 3;
    // Write a switch with cases 1, 2 and 3

    return 0;
}
""",
  "Wednesday", ["switch", "case", "break"],
  "Do not forget break; after each case.",
r"""
#include <stdio.h>

int main() {
    int day = 3;
    switch (day) {
        case 1: printf("Monday\n"); break;
        case 2: printf("Tuesday\n"); break;
        case 3: printf("Wednesday\n"); break;
        default: printf("Unknown day\n");
    }
    return 0;
}
""",
  "What happens if you forget break in a switch case?",
  ["Nothing", "The program runs the next case too", "The program closes", "C gives an error"], 1,
  "Without break, C 'falls through' and also runs the code of the next case."),

L(10, "Mini Project 2: Simple Calculator",
  "Build a calculator that can add, subtract, multiply and divide.",
  "Novice", 150,
r"""
### Our second project
Let's build a **calculator**! The user picks two numbers and an operation (+, -, *, /). The program shows the answer.

### Plan
1. Store two numbers `a` and `b`.
2. Store the operation in a `char` called `op`.
3. Use `switch (op)` to pick the right maths.
4. Print the result.

### Important: dividing by zero
You cannot divide by 0 in maths. A good program checks this first and shows a friendly message instead of crashing. This is called **handling errors**.

### Using what you learned
- Variables (Level 3)
- Input with `scanf` (Level 4)
- Maths operators (Level 5)
- `switch` (Level 9)

In the full version, you use `scanf(" %c", &op);` (note the space before `%c`) to read the symbol.
""",
r"""
#include <stdio.h>

int main() {
    float a, b;
    char op;
    printf("Enter number, operator, number: ");
    scanf("%f %c %f", &a, &op, &b);

    switch (op) {
        case '+': printf("%.1f\n", a + b); break;
        case '-': printf("%.1f\n", a - b); break;
        case '*': printf("%.1f\n", a * b); break;
        case '/':
            if (b == 0) printf("Cannot divide by zero!\n");
            else printf("%.1f\n", a / b);
            break;
        default: printf("Unknown operator\n");
    }
    return 0;
}
""",
  "Add the divide button",
  "The calculator below has no division yet. Add the '/' case so that 20 / 5 prints '20 / 5 = 4'.",
r"""
#include <stdio.h>

int main() {
    int a = 20, b = 5;
    char op = '/';

    switch (op) {
        case '+': printf("%d + %d = %d\n", a, b, a + b); break;
        case '-': printf("%d - %d = %d\n", a, b, a - b); break;
        case '*': printf("%d * %d = %d\n", a, b, a * b); break;
        // TODO: add case '/' here. Check that b is not 0!
    }
    return 0;
}
""",
  "20 / 5 = 4", ["case'/'", "b==0", "a/b"],
  "Inside case '/': if (b == 0) print a warning, else print the division.",
r"""
#include <stdio.h>

int main() {
    int a = 20, b = 5;
    char op = '/';

    switch (op) {
        case '+': printf("%d + %d = %d\n", a, b, a + b); break;
        case '-': printf("%d - %d = %d\n", a, b, a - b); break;
        case '*': printf("%d * %d = %d\n", a, b, a * b); break;
        case '/':
            if (b == 0) {
                printf("Cannot divide by zero!\n");
            } else {
                printf("%d / %d = %d\n", a, b, a / b);
            }
            break;
    }
    return 0;
}
""",
  "Why should a calculator check if b == 0 before dividing?",
  ["Division is slow", "Dividing by zero is not allowed and can crash the program", "C hates zero", "To make the answer bigger"], 1,
  "Dividing by zero is undefined. A careful program checks first and shows a friendly message.",
  project=True),

L(11, "The for Loop: Repeat Without Typing Again",
  "Make the computer repeat work for you.",
  "Apprentice", 120,
r"""
### Why loops?
Imagine writing "I will do my homework" 100 times. Boring! A **loop** tells the computer: "Repeat this".

### The for loop
```
for (start; condition; step) {
    // repeated work
}
```
- **start**: where to begin, like `int i = 1`.
- **condition**: keep going while this is true, like `i <= 5`.
- **step**: what to do after each round, like `i++`.

Think of climbing stairs: start at step 1, keep going while you are below step 5, and go up one step each time.

### Tip
Programmers often name the counter `i`. It is short for "index" or "item".
""",
r"""
#include <stdio.h>

int main() {
    for (int i = 1; i <= 5; i++) {
        printf("Round %d\n", i);
    }
    return 0;
}
""",
  "Even numbers",
  "Use a for loop to print the even numbers from 2 to 10 on one line.",
r"""
#include <stdio.h>

int main() {
    // Print: 2 4 6 8 10
    // Hint: start at 2 and go up by 2

    printf("\n");
    return 0;
}
""",
  "2 4 6 8 10", ["for", "i+=2"],
  "Use i += 2 as the step so the counter jumps by 2.",
r"""
#include <stdio.h>

int main() {
    for (int i = 2; i <= 10; i += 2) {
        printf("%d ", i);
    }
    printf("\n");
    return 0;
}
""",
  "In for (int i = 1; i <= 5; i++), how many times does the loop run?",
  ["4", "5", "6", "Forever"], 1,
  "i takes the values 1, 2, 3, 4, 5. That is 5 rounds."),

L(12, "while and do-while Loops",
  "Repeat until something changes.",
  "Apprentice", 120,
r"""
### When you do not know how many times
A `for` loop is great when you know the count. A `while` loop is better when you repeat **until something happens**, like "keep playing until the game is over".

### while
```
while (condition) {
    // work
}
```
C checks the condition first. If it is false at the start, the loop never runs.

### do-while
`do { ... } while (condition);` runs the work **once first**, then checks. Use it for menus that must show at least one time.

### Danger: infinite loop
If the condition never becomes false, the loop runs forever. Always change something inside the loop (like `count--`) so it can end.
""",
r"""
#include <stdio.h>

int main() {
    int coins = 3;
    while (coins > 0) {
        printf("Coins left: %d\n", coins);
        coins--;
    }
    printf("Out of coins!\n");
    return 0;
}
""",
  "Rocket countdown",
  "Use a while loop to count down from 5 to 1, then print 'Blast off!'.",
r"""
#include <stdio.h>

int main() {
    int n = 5;
    // while n is more than 0: print n, then lower n by 1

    printf("Blast off!\n");
    return 0;
}
""",
  "5\n4\n3\n2\n1\nBlast off!", ["while", "n--"],
  "Inside the loop print n and then do n--.",
r"""
#include <stdio.h>

int main() {
    int n = 5;
    while (n > 0) {
        printf("%d\n", n);
        n--;
    }
    printf("Blast off!\n");
    return 0;
}
""",
  "What is the difference between while and do-while?",
  ["No difference", "do-while always runs at least once", "while is faster", "do-while cannot stop"], 1,
  "do-while checks the condition after running the body, so the body runs at least one time."),

L(13, "Loops Inside Loops: Patterns",
  "Draw shapes with stars using nested loops.",
  "Apprentice", 120,
r"""
### A loop inside a loop
You can put one loop inside another. This is called a **nested loop**. Think of a clock: for every 1 hour (outer loop), the minute hand goes around 60 times (inner loop).

### Drawing patterns
Nested loops are perfect for rows and columns:
- The **outer loop** handles the rows (lines).
- The **inner loop** handles what is printed in each row.

### Example: a triangle
Row 1 has 1 star, row 2 has 2 stars, row 3 has 3 stars. So the inner loop runs `row` times.

### Tip
After the inner loop finishes one row, print `\n` to move to the next line.
""",
r"""
#include <stdio.h>

int main() {
    for (int row = 1; row <= 3; row++) {
        for (int col = 1; col <= row; col++) {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}
""",
  "Star triangle",
  "Print a triangle with 4 rows of stars (1 star, 2 stars, 3 stars, 4 stars).",
r"""
#include <stdio.h>

int main() {
    // Outer loop for rows 1 to 4
    // Inner loop prints stars

    return 0;
}
""",
  "*\n**\n***\n****", ["for", "for", "*"],
  "The inner loop should run from 1 up to the row number.",
r"""
#include <stdio.h>

int main() {
    for (int row = 1; row <= 4; row++) {
        for (int col = 1; col <= row; col++) {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}
""",
  "In a pattern program, what does the outer loop usually control?",
  ["The columns", "The rows (lines)", "The colour", "The file name"], 1,
  "The outer loop picks the row. The inner loop prints the items inside that row."),

L(14, "break and continue",
  "Stop a loop early or skip one round.",
  "Apprentice", 120,
r"""
### Controlling a loop
Sometimes you want to change how a loop behaves while it is running.

### break
`break;` means "stop the loop right now and leave". Like quitting a game when you find the treasure.

### continue
`continue;` means "skip the rest of this round and start the next one". Like skipping a boring song but keeping the playlist going.

### Example
Print numbers 1 to 10, but skip 5 and stop at 8:
- when `i == 5` use `continue`
- when `i == 8` print and then `break`

### Careful
`continue` in a `while` loop must not skip the line that changes your counter, or you get an infinite loop.
""",
r"""
#include <stdio.h>

int main() {
    for (int i = 1; i <= 10; i++) {
        if (i == 3) continue;   // skip 3
        if (i == 6) break;      // stop at 6
        printf("%d ", i);
    }
    printf("\n");
    return 0;
}
""",
  "Skip and stop",
  "Print numbers from 1 to 10, but skip multiples of 3 and stop after printing 8.",
r"""
#include <stdio.h>

int main() {
    for (int i = 1; i <= 10; i++) {
        // skip multiples of 3 (use continue)
        // after printing 8, stop (use break)
    }
    printf("\n");
    return 0;
}
""",
  "1 2 4 5 7 8", ["continue", "break", "%3"],
  "Multiples of 3 have i % 3 == 0.",
r"""
#include <stdio.h>

int main() {
    for (int i = 1; i <= 10; i++) {
        if (i % 3 == 0) continue;
        printf("%d ", i);
        if (i == 8) break;
    }
    printf("\n");
    return 0;
}
""",
  "What does continue do?",
  ["Stops the whole program", "Skips to the next round of the loop", "Restarts the program", "Prints a message"], 1,
  "continue skips the rest of the current round and jumps to the next round."),

L(15, "Mini Project 3: Times Table and Guessing Game",
  "Use loops to build a times table and a number guessing game.",
  "Apprentice", 150,
r"""
### Two small projects in one
Loops make real programs possible. Let's build two things.

### Project A: Times Table
Print a multiplication table for any number. A `for` loop goes from 1 to 10 and prints `number x i = answer`. We also add up all the answers to show the **total**.

### Project B: Guessing Game
The computer hides a secret number. The player keeps guessing until correct:
1. Make `secret = 7`.
2. Use a `while` loop that asks for guesses with `scanf`.
3. If the guess is too low or too high, give a hint.
4. When correct, print a happy message and count the tries.

### Skills used
`for`, `while`, `if/else`, `scanf`, variables and maths. You have learned a lot already!
""",
r"""
#include <stdio.h>

int main() {
    int secret = 7, guess = 0, tries = 0;
    while (guess != secret) {
        printf("Guess the number (1-10): ");
        scanf("%d", &guess);
        tries++;
        if (guess < secret) printf("Too low!\n");
        else if (guess > secret) printf("Too high!\n");
    }
    printf("You got it in %d tries!\n", tries);
    return 0;
}
""",
  "Times table builder",
  "Print the table of 3 from 1 to 5, then print the total of all the answers.",
r"""
#include <stdio.h>

int main() {
    int num = 3;
    int total = 0;
    // Loop i from 1 to 5
    // Print: 3 x 1 = 3 ... and add each answer to total

    printf("Total: %d\n", total);
    return 0;
}
""",
  "3 x 1 = 3\n3 x 2 = 6\n3 x 3 = 9\n3 x 4 = 12\n3 x 5 = 15\nTotal: 45", ["for", "total+="],
  "Inside the loop: printf the line, then total += num * i;",
r"""
#include <stdio.h>

int main() {
    int num = 3;
    int total = 0;
    for (int i = 1; i <= 5; i++) {
        printf("%d x %d = %d\n", num, i, num * i);
        total += num * i;
    }
    printf("Total: %d\n", total);
    return 0;
}
""",
  "Which loop is best for a guessing game where you do not know how many guesses are needed?",
  ["for with a fixed count", "while", "No loop", "switch"], 1,
  "A while loop repeats until the condition changes, which is perfect when the number of tries is unknown.",
  project=True),
]
