# #Simple Function
# # def greet():
# # print ("Hello Nyk")
# # greet()
# #Function that allows for input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}")
# greet_with_name("Nyk")     

#Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"what is it like in {location}")
    

#greet_with("Nyk", "Nowhere")
#Vs.
#greet_with(name="Nyk", location="Nowhere")
#Functions with keyword arguments

greet_with(location="Brazil", name="Nyk")