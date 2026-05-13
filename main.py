import functions.functions as functions
import helpers.helpers2 as helpers2

print("starting app")

x = input("Enter your name: ")
print("Hello " + x)

result = functions.Add(5, 3)
print("Result:", result)

data = helpers2.getData()
print("Data:", data)
