import re
from text import input1, input2,input3



        



def tax_calc(import_tax_t, tax_t, price):

    taxes = 0.1
    import_taxes = 0.05
    import_tax=0
    tax=0

    if(import_tax_t):
        import_tax = price*import_taxes   #Price = 
        price+=import_tax
        price=round(price,2)

        #print("Import: "+str(price))
    

    if(tax_t):
        tax = price* taxes  # Choclate -> 10€ * 0.5% -> 0,5€
        price += tax
        price=round(price,2)

        #print("Tax: "+str(price))

    return round(price,2),(round(tax+import_tax,2))



def Output(amount,type,pricetax,import_t):
    
    text=amount+" "
    if(import_t==True):
        text=text+"imported "
    if(type == 'perfume'):
        text= text+"bottle of "+type
    if(type == 'chocolates'):
        text=text+"box of "+type
    if(type == 'pills'):
        text = text + "packet of headache pills" 
    else:
        text = text + type

    text = text +": "+str(pricetax)

    return text

    
        
   




    



def splitting(input):

    tax=True
    import_tax=False
    warenkorbpreis=0
    warenkorbtax=0


    input = re.split('>',input) #or re.split('\n,input..')
    #print(input)

    for j in range(1,len(input)):

        textline = str(re.split(',',input[j]))#[' 1 book at 12.49']
        
        words = re.split(' bottle | at |of | box | ',textline)#[' 1 , book , at , 12.49']
        
        for i in range(len(words)):
            
            if(words[i]=='imported'):
                import_tax = True 

            if(words[i] == 'perfume'or words[i] =='music'):
                tax = True
                type = words[i]
            elif('chocolat'in words[i] or words[i] =='book' or words[i] =='pills'):
                tax= False
                type = words[i]

        quantity = re.sub("[^0-9.]", "",words[1])        
        price = words[len(words)-1]
        price = re.sub("[^0-9.]", "",price)
        price = float(price)

        #print(f"Produkt: {type}, Preis: {price}, Import: {import_tax}, Tax: {tax}, Anzahl: {quantity}")
        

        price_tax, fulltax=tax_calc(import_tax, tax, price)
        text=Output(quantity,type, price_tax,import_tax)
        print(text)
        #print(f'Gesammtpreis: {price_tax} davon Steuer: {fulltax}')
        warenkorbtax+=fulltax
        warenkorbpreis+=price_tax

        import_tax=False
        tax=True
    print(f'Sales Taxes: {round(warenkorbtax,2)} \nTotal: {round(warenkorbpreis,2)} ')
    pass



if __name__ == '__main__':


    splitting(input1)
    splitting(input2)
    splitting(input3)
    


