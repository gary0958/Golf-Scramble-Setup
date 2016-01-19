import smtplib
import time
import re
import urllib

lista = []
listb = []
listc = []



def scrambleSetup():
    i=0 
    level = raw_input("Enter Player Level (A,B,C) ")
    if level == "A" or level == "a":
        player1 = raw_input("Enter Player Name: ")
        lista.append(player1)
        lista.sort
        scrambleSetup()
        
    elif level == "B" or level == "b":
        player2 = raw_input("Enter Players Name ")
        listb.append(player2)
        listb.sort
        scrambleSetup()
        
    elif level == "C" or level == "c":
        player3 = raw_input("Enter Players Name ")
        listc.append(player3)
        listc.sort
        scrambleSetup()

    elif level == "0":
        print""
        option = raw_input("Do you wish to add players? Y or N ")
        print""
        if option == "N" or option =="n":
            print ""
            print "Have a Great Game Golfers"
            print""
            raw_input("Press any key to continue")
        
            
            while i <len(lista):
                print "Team ",i+1,'is ',lista[i],',',listb[i],',',listc[i],','
                print "Team Captain is :" ,lista[i]
                print ""
                """mailsendto = ['email@yahoo.com','email@gmail.com']
                mail = smtplib.SMTP('smtp.gmail.com',587)
                mail.ehlo()
                mail.starttls()
                mail.login('email@gmail.com','password')
                mail.sendmail('email@gmail.com',mailsendto[i],"Your team consists of " + lista[i] + "," + listb[i] + "," + listc[i] + '\n'"Your captain is " + lista[i])
                mail.close()
                textsendto = [mobile #,]"""
                message = "Your Team is " + lista[i] + ',' + listb[i] + ',' + listc[i] 
                server = smtplib.SMTP('smtp.gmail.com',587)
                server.starttls()
                server.login('username@gmail.com','Password')
                server.sendmail('From Name','Mobile Phone#@messaging.sprintpcs.com',message) 
                i=i+1

            if i<len(lista):
                pass
            else:
                raw_input("Press Enter/Return to Exit")
                    
            for a in lista:    
                myfile_lista = open("C:\Users\MyPath\Desktop\Golfstuff\ScrambleListA.txt","a")
                myfile_lista.write (str(a) + '\n')
                myfile_lista.close()
            for b in listb:    
                myfile_listb = open("C:\Users\MyPath\Desktop\Golfstuff\ScrambleListB.txt","a")
                myfile_listb.write (str(b) + '\n')
                myfile_listb.close()    
            for c in listc:    
                myfile_listc = open("C:\Users\MyPath\Desktop\Golfstuff\ScrambleListC.txt","a")
                myfile_listc.write (str(c) + '\n')
                myfile_listc.close()
                sendto = ['Email1@yahoo.com','Email2@gmail.com']
                
            
        elif option == "Y" or option == "y":
            print""
            scrambleSetup()
        
        else:
             print "Please Enter a valid Response"
             print ""
             scrambleSetup()
        
       
    else:
        print "Please Enter a valid Player Level"
        print""
        scrambleSetup()
        

    
              

scrambleSetup()
