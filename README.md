# Scientific Calculator 
## Using **Python**
---
> Student Info 👨‍🎓

**NAME :**  Dhanvinesh K

**APPLICATION NUMBER :** 33296

**BRANCH :** CSE-CCY

**UNIVERSITY :** Amrita Vishwa Vidhyapeetham

**Campus :** Chennai campus

---

> Project Info 💻

This project is a simple scientific calculator written in Python that performs operations like.... *addition, subtraction, multiplication, and many more*.

This project is done for Cognizance 2020 as Task-4.
 
 ---
 ---
 *You can find this project in this link below...* 👇

 [Task-4](https://github.com/Dhan2623/Cognizance2020/tree/task4)

---
---
### Python

Python is an interpreted, high-level and general-purpose programming language.

![Python logo](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)

 Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach to help programmers write clear, logical code for small and large-scale projects. 
 
 It was created and released by Guido Van Rossum. And he's here 👇

![Guido Van Rossum](https://www.tutorjoes.in/img/python.png)


*To know more about python.. Try this website...*
[Python](https://en.wikipedia.org/wiki/Python_(programming_language))

*To download this programming language, use this link...*
[Download](https://www.python.org/downloads/)

---
## Project- Scientific calculator
---
**What is a calculator?**
---
A calculator is a device that performs arithmetic operations on numbers. The simplest calculators can do only addition, subtraction, multiplication, and division. More sophisticated calculators like scientific calculators can handle exponential operations, roots, logarithms, trigonometric functions, and hyperbolic functions.

*I have created a calculator that performs all the arithmetic operations and some of the operations that can be performed in scientific calculator.*

![Calculator Animation](https://www.clker.com/cliparts/2/6/8/3/15168308841567480746graphing-calculator-clipart.med.png)

---
> Operations that you can perform using my scientific calculator 👇

| Operations that can be done |Operators used   |
| ---------------- | ---------|
| Addition         |    +     |
| Subtraction      |    -     |
| Multiplication   |    *     |
| Division         |     /    |
| Power            |    **    |
| Remainder        |    %     |
| Square           |    **2   |


![Arithmetic operations](https://is3-ssl.mzstatic.com/image/thumb/Purple128/v4/79/1f/d1/791fd19d-6ce0-8728-ab31-d2723d660484/source/512x512bb.jpg)

---
---
| Operations that can be done       | In-built Functions used |
| ---------------- | ---------- |
|Square Root       |math.sqrt() |
|Absolute          |math.fabs() |
|Sine Function     |math.sin()  |
|Cosine Function   |math.cosin()|
|Tangent Function  |math.tan()  | 
|Ceil              |math.ceil() |
|Floor             |math.floor()|

![Trignometric funcions](https://satprepget800.com/wp-content/uploads/2014/06/TrigFunctions.png)
---

>**NOTE --** *All these in-built functions are available in the python library "math"*.
---


## Explanation of the Source code:
---
1. To use these mathematical functions we have to type the following code....

``` Python
import math
```
2. Then, we have to create functions to perform each and every operation. These functions are called as **user-defined** functions.

*For example....*
``` Python
def add(a,b):
    return a+b
```
``` Python
def sin(x):
    # Here math.sin(x) is an in-built function
    result=math.sin(x)
    return result
```
3. After creating the user-defined functions for all the operations, Let's create a list showing specific numbers to specific operations so that we can choose any specific operation to perform using a number. Here, print() function should be used so that the user of the calculator can see the list during execution.

**(1-Add, 2-Subtract, 3-Product, 4-Division, 5-SquareRoot, 6-Power, 7-Remainder, 8-Square, 9-Absolute, 10-sin(x), 11-cos(x), 12-tan(x), 13-ceil, 14-floor)**

4. Now, let's get the choice from the user which he/she wanted to do.

5. Now, let's create a while loop with a condition, choice <== 14: i.e., If the choice chosen by the user is less than or equal to 14, then the loop gets executed. Or else the control comes out.
``` Python
while choice <= 14:
```

6. By using if...elif...else statements, we should create a set of code for getting the inputs (parameters) required for the operation, and call the function that we should use for that operation.

*Syntax is...*
``` Python
if <condition_1>:
     <Statements to get the parameters to perform the respective operation>
elif <condition_2>:
     <Statements to get the parameters to perform the respective operation>
.
.
.
else:
     <Statements to get the parameters to perform the respective operation>
```

7. To continue performing operations, we can get an input by asking a question from the user. If yes-1 and if no-0.

8. Then we have to create another if loop to continue performing the operation. If the user press '1' then the whole while loop repeats whereas when the user press '0' or any other number, the loop will break.

---
## Raw output :

> Let's take this as an example of the output in the scientific calculator

> Press F5 to execute the command and display the output

Choose a number for the following operations.....

 1 - Addition(a,b)

 2 - Subtraction(a,b)

 3 - Multiplication(a,b)

 4 - Division(a,b)

 5 - Square_Root(a)

 6 - Power(a,b) -- Power of 'a' times 'b'
 
 7 - Remainder(a,b)
 
 8 - Square(a)
 
 9 - Absolute(a)

10 - sin(x)

11 - cos(x)

12 - tan(x)

13 - ceil(x)

14 - floor(x)

Enter the number to choose the operation you wanter to perform: **4**

Enter two numbers....

Enter a: **5**

Enter b: **3**

The division of 5 by 3 is: 2

Do you like to continue to perform other operation? (YES-1)/(NO-0) **1**

What operation do you like to do next? Please select the number:**13**

Enter a: **4.74**

The ceil of 4.74 is: 5

Do you like to continue to perform other operation? (YES-1)/(NO-0) **0**

Thanks for using our scientific calculator!!

> That's how the output screen of our calculator looks like!! ☝
---

## References for Beginners to learn Python programming:
[Getting Started](https://www.python.org/about/gettingstarted/)

[Basics and Tutorials](https://www.learnpython.org/)

[Python Tutorial Video](https://www.youtube.com/watch?v=_uQrJ0TkZlc&vl=en)

[Python Crash course](https://www.youtube.com/watch?v=rfscVS0vtbw)

> Or you can buy or learn some courses in the following platforms...

* [Udemy](https://www.udemy.com/topic/python/) -- Paid course 🤑

* [Coursera](https://www.coursera.org/learn/python) -- Free course 🤩

* [Udacity](https://www.udacity.com/course/introduction-to-python--ud1110) -- Free course 😍

---
**MORE INFO :**

*I  uploaded the source code file  in Github repository **'Cognizance2020'***

 This is a README (Markdown) file that displays the information about Python, and the process taken place in this project.

---
### To view my other projects in Cognizance2020...
[Cognizance2020](https://github.com/Dhan2623/Cognizance2020)

---

### Contact 🤝:
**GitHub Email ID** : dhanvineshk2003@gmail.com

**GitHub Username** : Dhan2623

---
---















































