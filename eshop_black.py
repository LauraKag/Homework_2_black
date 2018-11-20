# -*- coding: utf-8 -*-

#%%

products={"Guitar":"1000",
          "Pick box":"5",
          "Guitar Strings":"10"}

services={"Insurance":"5",
          "Priority mail":"10"}

def checkout(list,tier):
    costproducts=0
    costservices=0
    if list==[] or list==["Insurance","Priority mail"] or list==["Priority mail","Insurance"]:
        return "Please add something to your shopping cart before checkout"
    
    else:
        for product in list:
            if list.count("Insurance") > 1 or list.count("Priority mail")>1:
                return "You cant add more the one Insurance and Priority mail"
            elif product in products:   
                costproducts+=int(products[product])
            elif product in services:
                costservices+=int(services[product])
        
        finalcost=costproducts+costservices
        
        if tier=="silver":
            finalcost=finalcost-0.02*costproducts
        elif tier=="golden":
            finalcost=finalcost-0.05*finalcost
        else:
            return "Your cost is: " +"$" + str(finalcost)
                    
                    
        return "Your cost is: " + "$" + str(finalcost)
    

