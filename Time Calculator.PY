print("@#$%*WAKE UP TIME CALCULATOR@#$%*")
def sleep():#WE ARE GIVING THE FUNCTION SLEEP

    cycles = int(input("Enter how many cycles do you want to sleep:"))#AS PER THE CYCLES PER 90 MINS SO IT IS ACCUSTUMED TO 4 OR MORE CYCLES 

    print("Enter the time when you want to wake up in 12 hour format:")#USE THE 12 HOURS FORMAT TO WAKE UP AND MENTION THE TIME

    hh = int(input("Enter the time in hours:"))#USE THE INTEGERS, MENTION THE TIME IN HOURS

    if(hh>12):#USES THE CONDITION if TO PROMOTE THE POSSIBILITY OF SLEEPING HOURS

        hh = int(input("Enter the value again"))#PLEASE ENTER TIME IN SLEEPING HOURS

    mm = int(input("Enter the time in minutes:"))#ENTER YOUR TIME IN SLEEPING MINUTES

    ss = int(input("Enter the time in seconds:"))#ENTER YOUR TIME IN SLEEPING MINUTE

    t = ((hh*60) + mm) - (cycles*105)#CALCUALTION OF TIME IN HOURS TO MINUTES AND THEN NEGLECTING WITH THE 4 CYLCES I.E 105
        
    hh = t//60#GIVING THE FLOOR DIVISION PROCESS CONVERTING TO HOURS 

    mm = t%60#USING THE MODULO IS CONVERTING THE TIME INTO MINUTES

    if(mm<10):#USING THE if CONDITION GIVING THE IDEA OF THE MINUTES CASES

        mm = '0' + str(mm)#ASSINGNING THE VALUE OF 0 WITH THE REMAINING THE UNIT DIGIT

    else:#CONDITION else TO DETERMINE THE FINITE SERIES

        mm = str(mm)#CONVERSION OF THE MINUTES WITH THE HELP OF STRINGS

    hh = hh%24#USING THE MODULO HELPS US TO CONVERT HOURS WITH IN 24 HOURS 

   

   

    if(hh>12):#USING if CONDITION FOR MORE THAN 12 HOURS FORMAT

        hh-=12#USING THIS TO DECREMENT UPTO THE HOURS TO 12 HOURS FORMAT

        s2  = str(hh) + ":" + mm#USING THE s2 ADDING THE STRING WITH THE MINUTES FORMAT

    elif(hh==12):#USING THE CONDITITON HOURS I,E COMPARING AND MAKING EQUAL TO 12 HOURS ONLY

        s2 = str(hh) + ":" + mm#USING THE s2 AGAIN GIVES THE IDEA OF THE HOURS AND MINUTES SHOULD BE IN THE CONDITION 

    elif(hh==0):#USING THE CONDITION OF THE HOURS TO COMPARING TO HOURS TO 0 

        hh=12#GIVING HOURS TO 12

        s2 = str(hh) +  ":" + mm#USING THE CONDITION AGAIN WITH s2 GIVING THE STRING TO HOURS TO MINUTES

    else:#GIVING THE FINAL CONDITION TO HOURS 

        s2 = str(hh) + ":" + mm#FINAL CONCLUSION MUST BE IN THE FORMAT OF IN THE FORM OF HOURS WITH IN THE MINUTES 

   

    

 

    c = input("AM or PM?")#ASKING THE USER FOR THE VALUE OF THE TIME IN AM OR PM 
    
    print("\nThe best time to sleep is:", end=" ")#ASKING TO PRINT THE STATEMENT IN THE NEW LINE
    while(c!="AM" or c!="PM"):#WHEN IT COMES TO c IS NOT EQUAL AM OR PM 
        if(c=="PM"):#COMPARING WITH THE VALUE PM TO VARIABLE c

            print(s2, "AM")#ASKING TO PRINT STATEMENT s2 and with the AM
            break#AS WE KNOW WE USING THE WHILE LOOP IT IS AN INFINTE LOOP SO MUST BRAKE IT TO FINITE

        elif(c=="AM"):#USING THE CONDTION elif COMPARING THE VARIABLE c to AM
    
            print(s2, "PM")#ASKING TO PRINT STATEMENT s2 AND WITH PM
            break#USING THE CONDTION elif COMPARING THE VARIABLE c to PM

        else:#FINAL CONDITION TO THE STATEMENT 

            print("Invalid Entry!")#ASKING TO PRINT IT WHEN IT IS NOT IN PROPER 
            c= input("Give a proper value")#IF THE CONDITION IS NOT GIVING A PROPER VALUE
        
   
    if(cycles<4):#USING if STATEMENT FOR THE LESSER THE 4 CYCLES

        print("\n Note: Since you have chosen", cycles, "Make sure you complete the rest of the cycles in the next session")#IN THE NEXT LINE IT PRINTS THE CONDITION LESSER THAN THAN 4 CYCLES USAGE

   

 

def wake():#WE ARE GIVING THE FUNCTION WAKE

    cycles = int(input("Enter how many cycles do you want to sleep:"))#AS PER THE CYCLES PER 90 MINS SO IT IS ACCUSTUMED TO 4 OR MORE CYCLES

    print("Enter your sleeping time in 12 hours format:")#USE THE 12 HOURS FORMAT TO WAKE UP AND MENTION THE TIME

    hh = int(input("Enter your sleeping time in hours:"))#USE THE INTEGERS, MENTION THE TIME IN HOURS

    if(hh>12):#USES THE CONDITION if TO PROMOTE THE POSSIBILITY OF SLEEPING HOURS

            hh = int(input("Enter the value again"))#PLEASE ENTER TIME IN FOR TO WAKE IN HOURS

    mm = int(input("Enter your sleeping time in minutes:"))#ENTER YOUR TIME IN SLEEPING MINUTES TO WAKE 

    ss = int(input("Enter your sleeping time in seconds:"))#ENTER YOUR TIME IN SLEEPING SECONDS TO WAKE

    t = (hh*60) + mm + (cycles*105)#CALCUALTION OF TIME IN HOURS TO MINUTES AND THEN NEGLECTING WITH THE 4 CYLCES I.E 105

    hh = t//60#GIVING THE FLOOR DIVISION PROCESS CONVERTING TO HOURS

    mm = t%60#USING THE MODULO IS CONVERTING THE TIME INTO MINUTES


    if(mm<10):#USING THE CONDITION if MINUTES LESS THAN 10

        mm = '0' + str(mm)#ASSINGNING THE VALUE OF 0 WITH THE REMAINING THE UNIT DIGIT

    else:#CONDITION else TO DETERMINE THE FINITE SERIES

        mm = str(mm)#CONVERSION OF THE MINUTES WITH THE HELP OF STRINGS

        hh = hh%24#USING THE MODULO HELPS US TO CONVERT HOURS WITH IN 24 HOURS

    if(hh>12):#USING if CONDITION FOR MORE THAN 12 HOURS FORMAT

        hh-=12#USING THIS TO DECREMENT UPTO THE HOURS TO 12 HOURS FORMAT

        s2  = str(hh) + ":" + mm#USING THE s2 ADDING THE STRING WITH THE MINUTES FORMAT

    elif(hh==12):#USING THE CONDITITON HOURS I,E COMPARING AND MAKING EQUAL TO 12 HOURS OF SLEEPING ONLY
        
        s2 = str(hh) + ":" + mm#USING THE s2 AGAIN GIVES THE IDEA OF THE HOURS AND MINUTES SHOULD BE IN THE CONDITION

    elif(hh==0):#USING THE CONDITION OF THE HOURS TO COMPARING TO HOURS TO 0

        hh=12#GIVING SLEEPING HOURS TO 12

        s2 = str(hh) +  ":" + mm#USING THE CONDITION AGAIN WITH s2 GIVING THE STRING TO HOURS TO MINUTES

    else:#GIVING THE FINAL CONDITION TO HOURS

        s2 = str(hh) + ":" + mm#FINAL CONCLUSION MUST BE IN THE FORMAT OF IN THE FORM OF HOURS WITH IN THE MINUTES 

    

    c = input("AM or PM?")#ASKING THE USER FOR THE VALUE OF THE TIME IN AM OR PM 
    
    print("\nThe best time to wake is:", end=" ")#ASKING TO PRINT THE STATEMENT IN THE NEW LINE
    while(c!="AM" or c!="PM"):#WHEN IT COMES TO c IS NOT EQUAL AM OR PM
        if(c=="PM"):#COMPARING WITH THE VALUE PM TO VARIABLE c

            print(s2, "AM")#ASKING TO PRINT STATEMENT s2 and with the AM
            break#AS WE KNOW WE USING THE WHILE LOOP IT IS AN INFINTE LOOP SO MUST BRAKE IT TO FINITE

        elif(c=="AM"):#USING THE CONDTION elif COMPARING THE VARIABLE c to AM
    
            print(s2, "PM")#ASKING TO PRINT STATEMENT s2 AND WITH PM
            break#USING THE CONDTION elif COMPARING THE VARIABLE c to PM

        else:#FINAL CONDITION TO THE STATEMENT 

            print("Invalid Entry!")#ASKING TO PRINT IT WHEN IT IS NOT IN PROPER 
            c= input("Give a proper value")#IF THE CONDITION IS NOT GIVING A PROPER VALUE
    if(cycles<4):#USING if STATEMENT FOR THE LESSER THE 4 CYCLES

        print("\n Note: Since you have chosen", cycles, "Make sure you complete the rest of the cycles in the next session")#IN THE NEXT LINE IT PRINTS THE CONDITION LESSER THAN THAN 4 CYCLES USAGE


print("MENU OF THE 12-HOUR ALARM CLOCK!!!")#MAKES TO PRINT THE STATEMENT    

print("1. Enter the sleeping time to know the wake up time")#PRINTS THIS STATEMENT TO KNOW THE SLEEPING TIME

print("2. Enter the wake up time to know the sleeping time")#PRINTS THIS STATEMENT TO KNOW THE WAKE UP TIME

print("3. Enter to exit")#PRINTS THIS TO EXITS FROM THE CALCULATOR

 

x = int(input("Enter your choice:"))#WE CAN ENTER THE CHOICE NUMBER FROM 1-3

 

if(x==1):#GIVING THE CONDITION if TO COMPARE THE EQUATION WITH THE x i.e to 1

    wake()#CALIING THE FUNCTION WAKE

elif(x==2):#GIVING THE FUNCTION TO COMPARE TO STATEMENT 2 WITH THE CHARACTER x

    sleep()#CALLING THE FUNCTION SLEEP

elif(x==3):#GIVING THE CONDITION elif TO BE COMPARING WITH STATEMENT 3

    pass#IT EXCUTES THE PROGRAMME

else:#IT IS THE FINAL CONDITION TO PROMOTE THE STATEMENT

    print("Invalid Entry!")#PRINTS THE GIVEN STATEMENT IF IT IS IN THE FORMAT OF IMPROPER
