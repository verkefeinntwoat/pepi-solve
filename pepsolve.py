# AI math assitant made by pepi
 
import numpy as np
 
print("(made my pepi)")
 
def ai_math_assistant():
    print("Welcome to the AI Math Assistant!")
    while True:
        user_input = input("Please enter a math question (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Thank you for using the AI Math Assistant. Goodbye!")
            break
        try:
            result = eval(user_input)
            print(f"The result is: {result}")
        except Exception as e:
            print(f"An error occurred: {e}")
 
if __name__ == "__main__":
    ai_math_assistant()
 
    #i <3 pepsi