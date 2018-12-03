# -*- coding: utf-8 -*-

#%% Excerises 1

    
prices = {"Guitar":1000,"Pick Box":5, "Guitar Strings":10, "Insurance":5, "Priority mail":10}

prices_cart = []
service_prices =[]

def checkout_blue(mycart):

        
    if "Insurance" in mycart:
            service_prices.append(prices["Insurance"])
    if "Priority mail" in mycart:
        service_prices.append(prices["Priority mail"])
    
    if "Insurance" in mycart:
        mycart.remove("Insurance")
    if "Priority mail" in mycart:
        mycart.remove("Priority mail")
    if "Insurance" in mycart:
        raise Exception ("You already have insurance")
    if "Priority mail" in mycart:
        raise Exception ("You already have priority mail")
    
    if mycart == []:
        return None
    
    else:
        for i in mycart: 

            prices_cart.append(prices[i])          
                
    return sum(prices_cart) + sum (service_prices)
    
checkout_blue([ "Insurance", "Guitar", "Priority mail", "Priority mail"])
#%% Excerise 2

try:
    file= open("data.txt")
    
    for line in file:
        print (line.upper())
except Exception:
    print ("the file doesn´t exist")


#%%
#Excerise 3

def copy_file(origin, destination):

        origin_file = open(origin)
        destination_file = open(destination, "w")
        
    
        for line in origin_file:
            destination_file.write(line)
            return destination_file

