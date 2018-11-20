# -*- coding: utf-8 -*-

#%%

import eshop_black

def test_eshop_black_normalorder():
    
    
    assert eshop_black.checkout(["Pick box","Guitar","Guitar Strings"],"normal")=="Your cost is: $1015"
    assert eshop_black.checkout(["Pick box","Guitar","Guitar Strings"],"silver")=="Your cost is: $994.7"
    assert eshop_black.checkout(["Pick box","Guitar","Guitar Strings"],"golden")=="Your cost is: $964.25"
    assert eshop_black.checkout(["Pick box","Guitar","Guitar Strings","Insurance","Priority mail"],"normal")=="Your cost is: $1030"
    assert eshop_black.checkout(["Pick box","Guitar","Guitar Strings","Insurance","Priority mail"],"silver")=="Your cost is: $1009.7"
    assert eshop_black.checkout(["Pick box","Guitar","Guitar Strings","Insurance","Priority mail"],"golden")=="Your cost is: $978.5"
    
    
def test_eshop_black_emptycart():
    assert eshop_black.checkout([],"normal")=="Please add something to your shopping cart before checkout"

def test_eshop_black_only_Insurance_or_Prioritymail():
    order1=["Insurance","Priority mail"]
    order2=["Priority mail","Insurance"]
    
    assert eshop_black.checkout(order1,"normal")=="Please add something to your shopping cart before checkout"
    assert eshop_black.checkout(order2,"normal")=="Please add something to your shopping cart before checkout"

def test_eshop_black_morethanonce_Insurance_or_Prioritymail():
    order1=["Pick box","Guitar","Guitar Strings","Insurance","Priority mail","Priority mail"]
    order2=["Pick box","Guitar","Guitar Strings","Insurance","Insurance","Priority mail","Priority mail"]
    
    assert eshop_black.checkout(order1,"normal")=="You cant add more the one Insurance and Priority mail"
    assert eshop_black.checkout(order2,"normal")=="You cant add more the one Insurance and Priority mail"
    
