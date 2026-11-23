from . import L

LEVELS = [

L(16, "Functions: Your Own Mini Machines",
  "Write a block of code once and use it many times.",
  "Apprentice", 120,
r"""
### What is a function?
A **function** is a small machine that does one job. You build it once and use it as many times as you want. `printf` is a function somebody else wrote. Now you will write your own.

### Parts of a function
```
void say_hi() {
    printf("Hi!\n");
}
```
- `void` means "gives nothing back".
- `say_hi` is the name.
- `( )` can hold **parameters**, which are the inputs.
- The `{ }` hold the work.

### Calling a function
Write its name with brackets: `say_hi();`. Functions are written **above** `main`, or you add a short **prototype** (a promise) at the top.

### Why use functions?
They stop you from copying code again and again, and they make big programs easy to read.
""",
r"""
#include <stdio.h>

void print_line(int n) {
    for (int i = 0; i < n; i++) {
        printf("-");
    }
    printf("\n");
}

int main() {
    print_line(5);
    print_line(10);
    return 0;
}
""",
  "Star line machine",
  "Write a function print_stars(int n) that prints n stars. Call it with 3 and then with 5.",
r"""
#include <stdio.h>

// Write your function here

int main() {
    print_stars(3);
    print_stars(5);
    return 0;
}
""",
  "***\n*****", ["voidprint_stars", "for"],
  "The function prints n stars with a loop and then prints a newline.",
r"""
#include <stdio.h>

void print_stars(int n) {
    for (int i = 0; i < n; i++) {
        printf("*");
    }
    printf("\n");
}

int main() {
    print_stars(3);
    print_stars(5);
    return 0;
}
""",
  "What does the word void mean before a function name?",
  ["The function returns nothing", "The function is broken", "The function returns a number", "The function is private"], 0,
  "void means the function does its job but does not send any value back."),

L(17, "Functions That Give Answers (return) and Scope",
  "Send a value back from a function and learn where variables live.",
  "Apprentice", 120,
r"""
### Returning a value
Some machines hand you a result. A calculator function can give back the answer. We use `return` for that.

```
int add(int a, int b) {
    return a + b;
}
```
- `int` before the name says the answer is an int.
- `return` sends the answer back and ends the function.
- You can store the answer: `int total = add(3, 4);`

### Scope: where does a variable live?
A variable made inside a function is **local**. It only exists inside that function, like a toy kept in your own room. Other functions cannot see it.

### Tip
Give each function one clear job. `add`, `square` and `bigger` are good names because they say what they do.
""",
r"""
#include <stdio.h>

int square(int x) {
    return x * x;
}

int main() {
    int answer = square(6);
    printf("6 squared is %d\n", answer);
    return 0;
}
""",
  "Find the bigger number",
  "Write a function bigger(int a, int b) that returns the larger number. Print the bigger of 4 and 9.",
r"""
#include <stdio.h>

// Write int bigger(int a, int b) here

int main() {
    printf("Bigger: %d\n", bigger(4, 9));
    return 0;
}
""",
  "Bigger: 9", ["intbigger", "return"],
  "if (a > b) return a; else return b;",
r"""
#include <stdio.h>

int bigger(int a, int b) {
    if (a > b) {
        return a;
    }
    return b;
}

int main() {
    printf("Bigger: %d\n", bigger(4, 9));
    return 0;
}
""",
  "What does return do?",
  ["Repeats the function", "Sends a value back and ends the function", "Prints the value", "Deletes the function"], 1,
  "return hands the result back to the caller and finishes the function."),

L(18, "Arrays: A Row of Boxes",
  "Store many values in one variable.",
  "Apprentice", 120,
r"""
### Too many variables!
Imagine storing the marks of 30 students. Making 30 variables is silly. An **array** is a row of boxes, all of the same type, under one name.

### Making an array
`int marks[5] = {70, 80, 90, 60, 50};`

- The number 5 is the size.
- Boxes are numbered from **0**. So `marks[0]` is 70 and `marks[4]` is 50.
- `marks[5]` does not exist! Going outside the array is a dangerous bug.

### Looping through an array
A `for` loop is the perfect partner:
```
for (int i = 0; i < 5; i++) { ... marks[i] ... }
```

### Remember
The first box is number **0**, not 1. This surprises everybody at the start.
""",
r"""
#include <stdio.h>

int main() {
    int marks[5] = {70, 80, 90, 60, 50};
    for (int i = 0; i < 5; i++) {
        printf("Student %d: %d\n", i + 1, marks[i]);
    }
    return 0;
}
""",
  "Add up the scores",
  "Print all the scores on one line, then print their sum.",
r"""
#include <stdio.h>

int main() {
    int scores[5] = {10, 20, 30, 40, 50};
    int sum = 0;
    // Loop through the array, print each score and add it to sum

    printf("\nSum: %d\n", sum);
    return 0;
}
""",
  "10 20 30 40 50\nSum: 150", ["for", "scores[i]", "sum+="],
  "Use scores[i] inside the loop and sum += scores[i];",
r"""
#include <stdio.h>

int main() {
    int scores[5] = {10, 20, 30, 40, 50};
    int sum = 0;
    for (int i = 0; i < 5; i++) {
        printf("%d ", scores[i]);
        sum += scores[i];
    }
    printf("\nSum: %d\n", sum);
    return 0;
}
""",
  "In int a[5], what is the number of the FIRST box?",
  ["1", "0", "5", "-1"], 1,
  "Arrays in C start counting at 0, so the first box is a[0] and the last is a[4]."),

L(19, "Strings: Words in C",
  "Work with names and sentences using character arrays.",
  "Apprentice", 120,
r"""
### A string is a row of letters
C has no special word type. A **string** is just an array of `char` that ends with a hidden zero character `'\0'`. That hidden mark tells C "the word stops here".

### Making a string
`char name[20] = "Quest";`
Use `%s` to print it: `printf("%s", name);`

### Useful helpers (add `#include <string.h>`)
- `strlen(s)` gives the length.
- `strcpy(a, b)` copies b into a.
- `strcat(a, b)` sticks b at the end of a.
- `strcmp(a, b)` compares. It gives 0 when they are the same.

### Be careful
The array must be big enough for all the letters **plus** the hidden `'\0'`. A small box with a long word causes a crash.
""",
r"""
#include <stdio.h>
#include <string.h>

int main() {
    char name[30] = "Quest";
    printf("Name: %s\n", name);
    printf("Length: %d\n", (int)strlen(name));
    strcat(name, " AI");
    printf("Now: %s\n", name);
    return 0;
}
""",
  "Join words",
  "Make the text 'Hello C' by joining 'Hello', a space and 'C'. Print it and its length.",
r"""
#include <stdio.h>
#include <string.h>

int main() {
    char text[30] = "Hello";
    // Add " C" to the end using strcat, then print the text and its length

    return 0;
}
""",
  "Hello C\nLength: 7", ["strcat", "strlen"],
  "Print the length with (int)strlen(text) and %d.",
r"""
#include <stdio.h>
#include <string.h>

int main() {
    char text[30] = "Hello";
    strcat(text, " C");
    printf("%s\n", text);
    printf("Length: %d\n", (int)strlen(text));
    return 0;
}
""",
  "Which special character marks the end of a C string?",
  ["'\\n'", "'\\0'", "';'", "'.'"], 1,
  "The null character '\\0' tells C where the string ends."),

L(20, "Mini Project 4: Marks Report Card",
  "Build a report card that finds the total, average, highest mark and grade.",
  "Apprentice", 180,
r"""
### Our report card project
Teachers do this every day, and now your program can do it too. We store five subject marks in an array and then work out:
1. The **total** of all marks.
2. The **average** (total divided by 5).
3. The **highest** mark.
4. A **grade** from the average.

### Plan
- Loop through the array once.
- Keep a running `total` and a `highest` value.
- After the loop: `average = total / 5.0`. Use `5.0` to keep decimals.
- Use `if / else if` to pick a grade:
  - 90 or more: A
  - 75 or more: B
  - 60 or more: C
  - otherwise: D

### Finding the highest
Start with `highest = marks[0]`. In each round, if `marks[i]` is bigger, replace `highest`.
""",
r"""
#include <stdio.h>

int main() {
    int marks[5] = {60, 70, 80, 90, 100};
    int total = 0, highest = marks[0];

    for (int i = 0; i < 5; i++) {
        total += marks[i];
        if (marks[i] > highest) highest = marks[i];
    }
    float average = total / 5.0;

    printf("Total: %d\n", total);
    printf("Average: %.1f\n", average);
    printf("Highest: %d\n", highest);
    if (average >= 90) printf("Grade: A\n");
    else if (average >= 75) printf("Grade: B\n");
    else printf("Grade: C or below\n");
    return 0;
}
""",
  "Complete the report card",
  "Marks are 78, 85, 62, 90, 70. Print the total, average, highest and grade.",
r"""
#include <stdio.h>

int main() {
    int marks[5] = {78, 85, 62, 90, 70};
    int total = 0;
    int highest = marks[0];
    // 1. Loop: add to total and find highest
    // 2. average = total / 5.0
    // 3. Print Total, Average (1 decimal), Highest, Grade
    //    Grade: 90+ A, 75+ B, 60+ C, else D

    return 0;
}
""",
  "Total: 385\nAverage: 77.0\nHighest: 90\nGrade: B", ["for", "highest", "5.0", "elseif"],
  "Remember the grade check order: 90 first, then 75, then 60.",
r"""
#include <stdio.h>

int main() {
    int marks[5] = {78, 85, 62, 90, 70};
    int total = 0;
    int highest = marks[0];
    for (int i = 0; i < 5; i++) {
        total += marks[i];
        if (marks[i] > highest) {
            highest = marks[i];
        }
    }
    float average = total / 5.0;
    printf("Total: %d\n", total);
    printf("Average: %.1f\n", average);
    printf("Highest: %d\n", highest);
    if (average >= 90) {
        printf("Grade: A\n");
    } else if (average >= 75) {
        printf("Grade: B\n");
    } else if (average >= 60) {
        printf("Grade: C\n");
    } else {
        printf("Grade: D\n");
    }
    return 0;
}
""",
  "To find the highest mark, what should 'highest' start as?",
  ["0 always", "The first element of the array", "-1", "The total"], 1,
  "Starting with the first element is safe. Then you only replace it when you meet a bigger value.",
  project=True),

L(21, "Pointers: Addresses in Memory",
  "Learn what a pointer is, the most famous idea in C.",
  "Adept", 150,
r"""
### Memory is like a street
Your computer memory is like a long street of houses. Every house has an **address**. A variable lives in one of those houses.

### What is a pointer?
A **pointer** is a variable that stores an **address** instead of a normal value. It is like a note that says "the treasure is at house number 1024".

### Two special symbols
- `&x` means "the address of x".
- `*p` means "go to the address stored in p and use what is there".

```
int age = 15;
int *p = &age;   // p remembers where age lives
*p = 16;         // changes age through the pointer
```

### Why do we care?
Pointers let functions change the original variables, and they are the key to using memory in smart ways.
""",
r"""
#include <stdio.h>

int main() {
    int coins = 10;
    int *p = &coins;

    printf("Coins: %d\n", coins);
    printf("Through pointer: %d\n", *p);

    *p = 25;
    printf("After change: %d\n", coins);
    return 0;
}
""",
  "Change a value by pointer",
  "Make a pointer to age and use it to change age to 16. Then print age.",
r"""
#include <stdio.h>

int main() {
    int age = 15;
    // 1. Make an int pointer p that points to age
    // 2. Use *p to set the value to 16

    printf("age = %d\n", age);
    return 0;
}
""",
  "age = 16", ["int*p", "&age", "*p=16"],
  "int *p = &age; then *p = 16;",
r"""
#include <stdio.h>

int main() {
    int age = 15;
    int *p = &age;
    *p = 16;
    printf("age = %d\n", age);
    return 0;
}
""",
  "What does the & symbol give you in front of a variable (like &age)?",
  ["Its value", "Its address in memory", "Its size", "Its name"], 1,
  "& is the address-of operator. It gives the memory address where the variable lives."),

L(22, "Pointers and Functions: Changing Original Values",
  "Use pointers to let a function change variables from outside.",
  "Adept", 150,
r"""
### A problem
When you give a number to a function, C hands over a **copy**. If the function changes the copy, your original does not change. It is like giving someone a photocopy of your homework. Scribbles on the copy do not change the original.

### The fix: send the address
If you give the function the **address**, it can go to the real variable and change it. This is called **call by reference**.

```
void add_one(int *n) {
    *n = *n + 1;
}
// call it like this:
add_one(&score);
```

### Famous example: swap
Swapping two values needs a helper box (temp) and pointers. You will build it now.

### Arrays are special
When you pass an array to a function, C already passes its address. That is why functions can change array values.
""",
r"""
#include <stdio.h>

void add_ten(int *n) {
    *n = *n + 10;
}

int main() {
    int score = 5;
    add_ten(&score);
    printf("Score: %d\n", score);
    return 0;
}
""",
  "Swap two numbers",
  "Finish the swap function so that a = 3 and b = 8 become a = 8 and b = 3.",
r"""
#include <stdio.h>

void swap(int *x, int *y) {
    // Use a helper variable called temp
}

int main() {
    int a = 3, b = 8;
    swap(&a, &b);
    printf("a=%d b=%d\n", a, b);
    return 0;
}
""",
  "a=8 b=3", ["temp", "*x", "*y"],
  "temp = *x; then *x = *y; then *y = temp;",
r"""
#include <stdio.h>

void swap(int *x, int *y) {
    int temp = *x;
    *x = *y;
    *y = temp;
}

int main() {
    int a = 3, b = 8;
    swap(&a, &b);
    printf("a=%d b=%d\n", a, b);
    return 0;
}
""",
  "Why do we pass &a instead of a when we want a function to change a?",
  ["It is shorter", "The function needs the address to change the real variable", "C requires it for numbers", "To print faster"], 1,
  "Without the address the function only changes a copy. With the address it can reach the original."),

L(23, "Structures: Make Your Own Data Type",
  "Group different pieces of information into one package.",
  "Adept", 150,
r"""
### One package, many facts
A game player has a name, health and speed. Using three separate variables is messy. A **struct** bundles them into one package.

### Making a struct
```
struct Player {
    char name[20];
    int health;
    float speed;
};
```
This is the **blueprint**, like the plan of a house. It does not use memory yet.

### Using it
```
struct Player p1 = {"Zara", 100, 2.5};
printf("%s", p1.name);
```
Use the **dot** `.` to reach each part.

### With pointers
If you have a pointer to a struct, use the arrow `->` instead of the dot: `ptr->health`.

### Real life
Almost every app stores data in this way: users, products, songs, players.
""",
r"""
#include <stdio.h>

struct Book {
    char title[30];
    int pages;
};

int main() {
    struct Book b = {"C is Fun", 120};
    printf("Title: %s\n", b.title);
    printf("Pages: %d\n", b.pages);
    return 0;
}
""",
  "Player profile",
  "Create a Player named Zara with health 100 and speed 2.5, then print all three values.",
r"""
#include <stdio.h>

struct Player {
    char name[20];
    int health;
    float speed;
};

int main() {
    // Make a Player variable p1 and print its fields

    return 0;
}
""",
  "Name: Zara\nHealth: 100\nSpeed: 2.5", ["structPlayer", "p1."],
  "struct Player p1 = {\"Zara\", 100, 2.5}; Print with p1.name, p1.health, p1.speed.",
r"""
#include <stdio.h>

struct Player {
    char name[20];
    int health;
    float speed;
};

int main() {
    struct Player p1 = {"Zara", 100, 2.5};
    printf("Name: %s\n", p1.name);
    printf("Health: %d\n", p1.health);
    printf("Speed: %.1f\n", p1.speed);
    return 0;
}
""",
  "How do you read the health field of a struct variable named p1?",
  ["p1->health", "p1.health", "p1[health]", "health(p1)"], 1,
  "Use the dot operator with a normal struct variable. The arrow is only for pointers."),

L(24, "Mini Project 5: Student Record Keeper",
  "Store many students using an array of structs and find the topper.",
  "Adept", 180,
r"""
### Our project
A school keeps records: a name and a score for each student. Let's make a program that stores 3 students and finds the **topper** (the one with the highest score).

### Plan
1. Create a `struct Student` with `name` and `score`.
2. Make an **array of structs**: `struct Student list[3]`.
3. Loop to print every student.
4. Loop again (or the same loop) to find the highest score.

### Array of structs
Each box in the array holds one whole student. `list[0].name` is the name of the first student and `list[1].score` is the score of the second.

### Level-up ideas
Add a menu so the user can add new students, search by name or sort them by score. These are the building blocks of real school software.
""",
r"""
#include <stdio.h>

struct Student {
    char name[20];
    int score;
};

int main() {
    struct Student list[2] = {{"Mina", 88}, {"Kabir", 95}};
    for (int i = 0; i < 2; i++) {
        printf("%s - %d\n", list[i].name, list[i].score);
    }
    return 0;
}
""",
  "Find the topper",
  "Print every student as 'Name - Score'. Then print the name of the topper.",
r"""
#include <stdio.h>

struct Student {
    char name[20];
    int score;
};

int main() {
    struct Student list[3] = {{"Asha", 85}, {"Ravi", 92}, {"Meena", 78}};
    int best = 0;  // index of the best student so far
    // Loop 0..2: print the student and update best if the score is higher

    printf("Topper: %s\n", list[best].name);
    return 0;
}
""",
  "Asha - 85\nRavi - 92\nMeena - 78\nTopper: Ravi", ["for", "list[i].score", "best"],
  "If list[i].score > list[best].score then best = i;",
r"""
#include <stdio.h>

struct Student {
    char name[20];
    int score;
};

int main() {
    struct Student list[3] = {{"Asha", 85}, {"Ravi", 92}, {"Meena", 78}};
    int best = 0;
    for (int i = 0; i < 3; i++) {
        printf("%s - %d\n", list[i].name, list[i].score);
        if (list[i].score > list[best].score) {
            best = i;
        }
    }
    printf("Topper: %s\n", list[best].name);
    return 0;
}
""",
  "What is an array of structs useful for?",
  ["Storing one number", "Storing many records like many students", "Drawing pictures", "Making sounds"], 1,
  "An array of structs keeps many records of the same shape, like a list of students.",
  project=True),

L(25, "Dynamic Memory: malloc and free",
  "Ask the computer for memory while the program is running.",
  "Adept", 150,
r"""
### Fixed size is not always enough
With a normal array you must choose the size before the program runs. But what if you do not know how many items you need? **Dynamic memory** lets you ask for space **while the program is running**.

### Four important helpers (`#include <stdlib.h>`)
- `malloc(bytes)` asks for memory and gives back a pointer.
- `calloc(count, size)` is like malloc but fills it with zeros.
- `free(p)` gives the memory back when you are done.
- Always check that the pointer is not `NULL`. `NULL` means "no memory was available".

### Example
`int *a = malloc(5 * sizeof(int));` asks for room for 5 ints.

### Golden rule
Every `malloc` needs one `free`. If you forget, you create a **memory leak**, like borrowing library books and never returning them.
""",
r"""
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *a = malloc(3 * sizeof(int));
    if (a == NULL) return 1;

    for (int i = 0; i < 3; i++) a[i] = i * 10;
    for (int i = 0; i < 3; i++) printf("%d ", a[i]);
    printf("\n");

    free(a);
    return 0;
}
""",
  "Squares on the heap",
  "Use malloc to make room for 5 ints. Store the squares 1, 4, 9, 16, 25, print them and their sum, then free the memory.",
r"""
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *a = malloc(5 * sizeof(int));
    int sum = 0;
    // Fill a[i] with (i+1)*(i+1), print each value, add to sum

    printf("\nSum: %d\n", sum);
    // Do not forget free(a);
    return 0;
}
""",
  "1 4 9 16 25\nSum: 55", ["malloc", "free(a)"],
  "Inside the loop: a[i] = (i + 1) * (i + 1);",
r"""
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *a = malloc(5 * sizeof(int));
    int sum = 0;
    for (int i = 0; i < 5; i++) {
        a[i] = (i + 1) * (i + 1);
        printf("%d ", a[i]);
        sum += a[i];
    }
    printf("\nSum: %d\n", sum);
    free(a);
    return 0;
}
""",
  "What happens if you forget to call free()?",
  ["The computer explodes", "A memory leak happens", "Nothing ever", "The code will not compile"], 1,
  "The memory stays reserved and cannot be used again. That is called a memory leak."),

L(26, "File Handling: Saving Data Forever",
  "Write to a file and read it back.",
  "Adept", 150,
r"""
### Memory forgets, files remember
When your program ends, all variables disappear. A **file** keeps data on the disk, even after the computer is switched off.

### Steps to use a file
1. **Open** it with `fopen("name.txt", "w")`.
   - `"w"` write (creates or erases the file)
   - `"r"` read
   - `"a"` append (add to the end)
2. **Use** it with `fprintf` (write) or `fgets` (read a line).
3. **Close** it with `fclose`.

### Always check
`fopen` returns `NULL` if the file could not be opened. Always check this before using it.

### Real life
Games save your progress. Notes apps save your notes. Both use files.
""",
r"""
#include <stdio.h>

int main() {
    FILE *f = fopen("diary.txt", "w");
    if (f == NULL) return 1;
    fprintf(f, "Dear diary, I learned C today.\n");
    fclose(f);
    return 0;
}
""",
  "Save and load",
  "Write the line 'Hello file!' into notes.txt, close it, then open it again and print what is inside.",
r"""
#include <stdio.h>

int main() {
    char line[50];
    // 1. Open notes.txt for writing, write "Hello file!" and close
    // 2. Open notes.txt for reading, read a line with fgets, print it, close

    return 0;
}
""",
  "Hello file!", ["fopen", "fclose", "fgets"],
  "Use \"w\" to write first and then \"r\" to read.",
r"""
#include <stdio.h>

int main() {
    char line[50];
    FILE *f = fopen("notes.txt", "w");
    if (f == NULL) return 1;
    fprintf(f, "Hello file!\n");
    fclose(f);

    f = fopen("notes.txt", "r");
    if (f == NULL) return 1;
    fgets(line, 50, f);
    printf("%s", line);
    fclose(f);
    return 0;
}
""",
  "Which mode of fopen creates a file for writing?",
  ["\"r\"", "\"w\"", "\"x\"", "\"z\""], 1,
  "\"w\" opens for writing. It creates the file or erases it if it already exists."),

L(27, "Searching and Sorting",
  "Find a value in a list and put a list in order.",
  "Adept", 150,
r"""
### Two jobs computers do all the time
1. **Searching**: finding something in a list.
2. **Sorting**: putting a list in order, like marks from small to big.

### Linear search
Check each box one by one until you find the value. Simple, but slow for huge lists.

### Bubble sort
A simple way to sort. Walk through the list and compare neighbours. If two neighbours are in the wrong order, swap them. Repeat. The biggest numbers slowly "bubble" to the end like air bubbles in water.

### In code
Two loops: the outer loop repeats the passes, the inner loop compares neighbours.
```
if (a[j] > a[j+1]) { swap them }
```

### Real life
Sorting is used when your phone arranges contacts A to Z, and search is used when you look for a song.
""",
r"""
#include <stdio.h>

int main() {
    int a[4] = {4, 2, 9, 1};
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3 - i; j++) {
            if (a[j] > a[j + 1]) {
                int t = a[j]; a[j] = a[j + 1]; a[j + 1] = t;
            }
        }
    }
    for (int i = 0; i < 4; i++) printf("%d ", a[i]);
    printf("\n");
    return 0;
}
""",
  "Sort then search",
  "Sort the array with bubble sort, print it, then search for 7 and print its position (counting from 0).",
r"""
#include <stdio.h>

int main() {
    int a[5] = {5, 2, 9, 1, 7};
    // 1. Bubble sort the array
    // 2. Print the sorted array on one line
    // 3. Loop to find 7 and print: Found 7 at position X

    return 0;
}
""",
  "1 2 5 7 9\nFound 7 at position 3", ["for", "for", "a[j]>a[j+1]"],
  "Outer loop i < 4, inner loop j < 4 - i. Swap with a temp variable.",
r"""
#include <stdio.h>

int main() {
    int a[5] = {5, 2, 9, 1, 7};
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4 - i; j++) {
            if (a[j] > a[j + 1]) {
                int t = a[j];
                a[j] = a[j + 1];
                a[j + 1] = t;
            }
        }
    }
    for (int i = 0; i < 5; i++) {
        printf("%d ", a[i]);
    }
    printf("\n");
    for (int i = 0; i < 5; i++) {
        if (a[i] == 7) {
            printf("Found 7 at position %d\n", i);
        }
    }
    return 0;
}
""",
  "In bubble sort, what do we do when two neighbours are in the wrong order?",
  ["Delete one", "Swap them", "Print them", "Stop the program"], 1,
  "Bubble sort swaps neighbours that are in the wrong order again and again until the list is sorted."),

L(28, "Recursion: A Function That Calls Itself",
  "Solve big problems by solving smaller copies of the same problem.",
  "Master", 180,
r"""
### Mirrors facing each other
Stand between two mirrors and you see yourself again and again. **Recursion** is similar: a function that calls **itself**.

### Two rules
Every recursive function needs:
1. A **base case**: the simple case where it stops. Without it, the function never stops.
2. A **recursive case**: it calls itself with a smaller problem.

### Example: factorial
`5! = 5 x 4 x 3 x 2 x 1 = 120`. Notice that `5! = 5 x 4!`. So:
```
int fact(int n) {
    if (n <= 1) return 1;     // base case
    return n * fact(n - 1);   // recursive case
}
```

### Careful
If you forget the base case, the computer runs out of space and crashes. This is called a **stack overflow**.
""",
r"""
#include <stdio.h>

int sum_to(int n) {
    if (n == 0) return 0;
    return n + sum_to(n - 1);
}

int main() {
    printf("Sum 1 to 4 = %d\n", sum_to(4));
    return 0;
}
""",
  "Factorial machine",
  "Write a recursive function factorial(int n). Print 5! = 120.",
r"""
#include <stdio.h>

// Write int factorial(int n) using recursion

int main() {
    printf("5! = %d\n", factorial(5));
    return 0;
}
""",
  "5! = 120", ["intfactorial", "factorial(n-1)"],
  "Base case: if n <= 1 return 1. Otherwise return n * factorial(n - 1).",
r"""
#include <stdio.h>

int factorial(int n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

int main() {
    printf("5! = %d\n", factorial(5));
    return 0;
}
""",
  "What is a base case in recursion?",
  ["The first line of the program", "The simple case where the function stops calling itself", "A type of loop", "A variable"], 1,
  "The base case stops the recursion. Without it the function would call itself forever."),

L(29, "Mini Project 6: ATM Machine",
  "Build a bank machine with deposit, withdraw and balance checks.",
  "Master", 200,
r"""
### Let's build an ATM!
An ATM lets you deposit money, withdraw money and see your balance. The most important rule: **you cannot take out more money than you have**.

### Plan
- A variable `balance` stores the money.
- A function `deposit(amount)` adds money.
- A function `withdraw(amount)` checks first. If there is enough money, it subtracts. Otherwise it prints "Insufficient balance!".

### Using pointers
The functions need to change the real `balance`. So we pass its address: `deposit(&balance, 500)`.

### Testing your program
Good programmers test the strange cases too: withdrawing too much, or withdrawing zero. A program must behave well even when users make mistakes.

### Next step
Wrap it in a `while` loop with a menu (1. Deposit, 2. Withdraw, 3. Exit) and you have a full ATM!
""",
r"""
#include <stdio.h>

void deposit(int *balance, int amount) {
    *balance += amount;
    printf("Deposited %d. Balance: %d\n", amount, *balance);
}

int main() {
    int balance = 100;
    deposit(&balance, 50);
    return 0;
}
""",
  "Safe withdraw",
  "Write withdraw so it refuses when the amount is more than the balance. Run the tests in main.",
r"""
#include <stdio.h>

void deposit(int *balance, int amount) {
    *balance += amount;
    printf("Deposited %d. Balance: %d\n", amount, *balance);
}

void withdraw(int *balance, int amount) {
    // If amount > *balance print "Insufficient balance!"
    // Otherwise subtract and print "Withdrew X. Balance: Y"
}

int main() {
    int balance = 1000;
    deposit(&balance, 500);
    withdraw(&balance, 200);
    withdraw(&balance, 2000);
    printf("Final balance: %d\n", balance);
    return 0;
}
""",
  "Deposited 500. Balance: 1500\nWithdrew 200. Balance: 1300\nInsufficient balance!\nFinal balance: 1300",
  ["voidwithdraw", "Insufficientbalance!", "*balance-="],
  "Use if (amount > *balance) { ... } else { *balance -= amount; ... }",
r"""
#include <stdio.h>

void deposit(int *balance, int amount) {
    *balance += amount;
    printf("Deposited %d. Balance: %d\n", amount, *balance);
}

void withdraw(int *balance, int amount) {
    if (amount > *balance) {
        printf("Insufficient balance!\n");
    } else {
        *balance -= amount;
        printf("Withdrew %d. Balance: %d\n", amount, *balance);
    }
}

int main() {
    int balance = 1000;
    deposit(&balance, 500);
    withdraw(&balance, 200);
    withdraw(&balance, 2000);
    printf("Final balance: %d\n", balance);
    return 0;
}
""",
  "Why must withdraw check the balance first?",
  ["To print faster", "To stop the balance from going below what the user really has", "Because C needs it", "To use less memory"], 1,
  "Checking first prevents taking out money that does not exist. This is called input validation.",
  project=True),

L(30, "Final Capstone: To-Do List Manager",
  "Combine structs, arrays, loops and functions into your biggest project yet.",
  "Master", 300,
r"""
### You made it to the final level!
Time for your **capstone project**. A capstone uses everything you learned. You will build a **To-Do List Manager**, just like the apps people use every day.

### What it uses
- `struct` to describe a task (a title and whether it is done).
- An **array** to hold many tasks.
- **Loops** to print them.
- **Functions** to keep the code tidy.
- (Bonus) **files** to save the list, **malloc** to grow it.

### Plan
1. `struct Task` with `title` and `done` (0 = not done, 1 = done).
2. A function `mark_done(task)` that sets `done = 1`.
3. A function `print_tasks` that shows `[ ]` for pending and `[x]` for done.
4. Count how many are still pending.

### What next?
Build a menu so the user can add, delete and save tasks. Then learn **Java** on this website and make the same project again. You are now a real programmer. Well done!
""",
r"""
#include <stdio.h>

struct Task {
    char title[30];
    int done;
};

int main() {
    struct Task t = {"Learn C", 0};
    t.done = 1;
    printf("[%c] %s\n", t.done ? 'x' : ' ', t.title);
    return 0;
}
""",
  "To-Do list",
  "Mark task 2 as done, print all tasks with numbers, then print how many tasks are still pending.",
r"""
#include <stdio.h>

struct Task {
    char title[30];
    int done;
};

int main() {
    struct Task tasks[3] = {
        {"Do homework", 0},
        {"Practice C", 0},
        {"Play chess", 0}
    };
    // 1. Mark the second task (index 1) as done
    // 2. Loop: print like "1. [ ] Do homework" ([x] if done)
    // 3. Count and print pending tasks

    return 0;
}
""",
  "1. [ ] Do homework\n2. [x] Practice C\n3. [ ] Play chess\nPending tasks: 2",
  ["tasks[1].done=1", "for", "pending"],
  "Use tasks[i].done ? 'x' : ' ' to pick the symbol, and count the ones with done == 0.",
r"""
#include <stdio.h>

struct Task {
    char title[30];
    int done;
};

int main() {
    struct Task tasks[3] = {
        {"Do homework", 0},
        {"Practice C", 0},
        {"Play chess", 0}
    };
    tasks[1].done = 1;
    int pending = 0;
    for (int i = 0; i < 3; i++) {
        printf("%d. [%c] %s\n", i + 1, tasks[i].done ? 'x' : ' ', tasks[i].title);
        if (tasks[i].done == 0) {
            pending++;
        }
    }
    printf("Pending tasks: %d\n", pending);
    return 0;
}
""",
  "Which C feature lets you group a task title and a done flag into one item?",
  ["A loop", "A struct", "A comment", "A prototype"], 1,
  "A struct groups different pieces of data (like title and done) into one custom type.",
  project=True),
]
