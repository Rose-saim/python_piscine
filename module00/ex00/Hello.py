ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}
# Modify ft_list
ft_list[1] = "World!"
# Modify my tuple
ft_tuple = ("Hello", "France!")
# Modify my set
ft_set.clear()
ft_set = { "Paris!", "Hello"}
# Modify my dictionary
ft_dict["Hello"] = '42Paris!'

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

# $>python Hello.py | cat -e
# ['Hello', 'World!']$
# ('Hello', 'France!')$
# {'Hello', 'Paris!'}$
# {'Hello': '42Paris!'}$
# $>