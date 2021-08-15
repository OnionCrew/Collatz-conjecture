
i = int(input("Input some number: "))     

def FirstNumber():
         global i
         first_result = i // 2
         print(first_result)
         i = first_result
         Checking()

       
def SecondNumber():
         global i
         second_result = 3 * i + 1
         print(second_result)
         i = second_result
         Checking()
   
         
def Checking():        
    if i % 2 == 0:
            FirstNumber()
    elif i % 2 == 1:
            SecondNumber()
         
if i % 2 == 0:
            FirstNumber()
elif i % 2 == 1:
            SecondNumber()


