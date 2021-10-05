import datetime
order=0
x=0
pizzatopping=0
top=[0,0,0,0,0,0]
topname=['chicken','extra cheese','pepperoni','mushrooms','spinach','olives']  
totaltop=0
y=1
least=0
most=0
least=0
while x==0:
    size=input("enter the size? s, m, l:")
    if size!="s" and size!="m" and size!="l":
        print("enter valid data")
    else:
        base=input("enter base. thick or thin?:")

        if base!="thin" and base!="thick":
            print("enter valid data")
        else:
            topping=int(input("enter no. of topping(max is 3):"))
            if topping>3:
                print("enter valid data")
            else:
                counter=0
                while counter<topping:
                    pizzatopping= int(input("enter your topping. either 0 for chicken or 1 for extra cheese or 2 for pepperoni or 3 for mushrooms or 4 for spinach or 5 for olives:"))
                    top[pizzatopping]=top[pizzatopping]+ 1
                    totaltop=totaltop+1
                    counter=counter+1
                            
            
                dec=input("do u want to edit or confirm or delete:")
                if dec=="edit":
                    x=0
                elif dec=="confirm":
                       order= order+1 
                       print(order,",",datetime.datetime.now()) #unique order
                       add=input("do u want more? yes or no:")
                       if add=="no":
                           x=1
                           while y<6:
                               if top[most]<top[y]:
                                   most=y
                               else:
                                   if top[y]<top[least]:
                                       least=y
                               y=y+1
                           print("most:",topname[most],"=", (top[most]/totaltop)*100,"%")
                           
                           print("least:",topname[least],"=", (top[least]/totaltop)*100,"%")
                          
                                
                              
                                   
                                         
                            

                        








                        
                        
                            

                            
                                   
                                   
                        
                               
                           
                           
                           
                       
                       
                        


                    
                    
                    
                             
                             
                     
            
        
               
    
 
                     
                     
            
        


