import random
import math
import sympy # For algebraic equations


# Function to generate math problems and its solutions
def generate_math_problems():
    topic = random.choice(['arithmetics', 'algebra', 'geometry'])

    # Arithmetic operation logic
    if topic == 'arithmetic':
        num1 = random.randint(1,28)
        num2 = random.randint(1,28)
        operator = random.choice(['+', '-', '*', '//'])

        # Ensure division generates integer results
        if operator == '//' and num1 % num2 != 0:
            num1, num2 = num2, num1 # Swap if division does not result in an integer result

            problem = f"What is {num1} {operator} {num2} ?"
            solution = eval(str(num1) + operator + str(num2)) # Evaluate the expression to get the answer

    # Algebraic operation logic
    elif topic == "algebra":
        a, b, x = sympy.symbols('a b c')
        a_val = random.randint(1, 10)
        b_val = random.randint(1, 10)
        equation = sympy.Eq(a * x + b, random.randint(1, 20))
        problem = f"Solve for x: {a_val}x + {b_val} = {equation.rhs}"
        solution = sympy.solve(equation, x)

    else:  # Geometric operation logic
        shapes = ['circle', 'triangle', 'rectangle', 'square']
        shape = random.choice(shapes)

        if shape == 'circle':
            radius = random.randint(1, 10)
            problem = f"What is the area of a circle with radius {radius}?"
            solution = round(math.pi * radius**2, 2)

        elif shape == 'triangle':
            base = random.randint(1, 10)
            height = random.randint(1, 10)
            problem = f"What is the area of a triangle with the base {base} and height {height} ?"
            solution = 0.5 * base * height

        elif shape == 'rectangle':
            length = random.randint(1, 10)
            width = random.randint(1, 10)
            problem = f"What is the area of a rectangle with length {length} and width {width}?"
            solution = length * width

        else:
            side = random.randint(1, 10)
            problem = f"What is the area of a square with side length {side}?"
            solution = side**2

    return problem, solution


# Start the math teacher AI by generating a problem and asking the student to solve it
# Main loop to run the math teacher AI
while True:
    problem, solution = generate_math_problems()
    print(f"Teacher: {problem}")
    student_answer = float(input("Student: "))

    if abs(student_answer - solution) <= 0.01:
        print("Teacher: Correct! The solution is:", solution)
    else:
        print("Teacher: Incorrect! The correct solution is:", solution)

    play_again = input("Teacher: Would you like to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break
