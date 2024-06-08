import pandas as pd
import matplotlib.pyplot as tp
import numpy as np
for i in range (100):
    print("Welcome to PARKING PARTNER".center(120))
    c1=int(input("\n 1) Create a new account (REGISTER) \n 2) Already a user (LOGIN) \n SELECT AN OPTION:"))
    if c1==1:
        DF1=pd.read_csv("LoginData.csv")
        UNameL=input("Enter User Name(minimum length:5 character):")
        EmailL=input("Enter Email:")
        PWordL=input("Create Password(minimum length:8 character):")
        CNoL=int(input("Enter a Contact Number: +91"))
        DF1=pd.read_csv("LoginData.csv")
        DF1.loc[0]=[UNameL,EmailL,PWordL,CNoL]
        DF1.to_csv("LoginData.csv",index=None)
    elif c1==2:
        DF1=pd.read_csv("LoginData.csv")
        UName=input("Enter User Name:")
        PWord=input("Enter Password:")
        DF2=DF1["User_Name"][DF1["User_Name"]==UName]
        DF3=DF1["Password"][DF1["Password"]==PWord]
        DF2=np.array([DF2])
        DF3=np.array([DF3])              
        if np.array([UName])==DF2  and np.array([PWord])==DF3:
                            print("Login Successful".center(130))
                            c2=0
                            while c2!=5:
                                    print("="*90)
                                    print("1)Profile".center(55),"2) Book a spot".center(95))
                                    print("3) Vehicle Details \n\n\n".center(215))
                                    print("4) Get Premium".center(55),"5) Logout".center(95))
                                    print("="*90)
                                    c2=int(input("Enter Choice:"))                                
                                    if c2==1:
                                        print("="*90)
                                        print("Profile".center(130))
                                        DF1=pd.read_csv("LoginData.csv")
                                        for i in range (len(DF1["User_Name"])):
                                            if DF1["User_Name"][i]==UName:
                                                    print("Personal Details")
                                                    print(DF1.loc[i:i,:])
                                                    
                                    elif c2==2:
                                        print("="*90)
                                        print("Book a Spot".center(130))
                                        for i in  range (3):
                                            c3=int(input("1) View History \n 2) Add New Booking \n 3) Back \n SELECT AN OPTION:"))
                                            if c3==1:
                                                UName=input("Enter User Name:")
                                                DF2=pd.read_csv("UserDetails.csv")
                                                for i in range (len(DF2["User_Name"])):
                                                    if DF2.User_Name[i]==UName:
                                                        print("Your Booking Details")
                                                        print(DF2.loc[i:i,:])
                                            elif c3==2:
                                                UName=input("Enter User Name:")
                                                L=input("Enter Location:")
                                                T=input("Enter Vechile Type:")
                                                D=input("Enter Date(DD/MM/YY):")
                                                En=input("Entry Time:")
                                                Ex=input("Exit Time:")
                                                H=int(input("Number of Hours:"))
                                                DF1=pd.read_csv("UserDetails.csv")
                                                DF1.at["a",:]=[UName,L,T,D,En,Ex,H]
                                                DF1.to_csv("UserDetails.csv",index=None)
                                                DF2=pd.read_csv("UserDetails.csv")
                                                for i in range (len(DF2["User_Name"])):
                                                    if DF2.User_Name[i]==UName:
                                                        if DF2.Date[i]==D:
                                                            print("Your Booking Details")
                                                            print(DF2.loc[i:i,:])
                                                            print("Payment Portal")
                                                            co=350
                                                            print("User Name \t Location \t\t Date \t\t Cost")
                                                            print(DF2.User_Name[i],"\t",DF2.Location[i],"\t",DF2.Date[i],"\t",co)

                                            elif c3==3:
                                                exit
                                                
                                    elif c2==3:
                                        print("="*90)
                                        print("Vechile Details".center(130))
                                        c3=int(input("1) View Details \n 2) Add Details \n 3) Back \n SELECT AN OPTION:"))
                                        if c3==1:
                                            UName=input("Enter User Name:")
                                            DF2=pd.read_csv("CarDetails.csv")
                                            for i in range (len(DF2["User_Name"])):
                                                    if DF2.User_Name[i]==UName:
                                                        print("Your Vechile Details")
                                                        print(DF2.loc[i:i,:])
                                        elif c3==2:
                                            UName=input("Enter User Name:")
                                            T=input("Enter Vechile Type:")
                                            NP=input("Enter Plate Number:")
                                            C=input("Car Company:")
                                            M=input("Car Model:")
                                            DF1=pd.read_csv("CarDetails.csv")
                                            DF1.at["a",:]=[UName,T,NP,C,M]
                                            DF1.to_csv("CarDetails.csv",index=None)
                                            DF2=pd.read_csv("CarDetails.csv")
                                            for i in range (len(DF2["User_Name"])):
                                                        if DF2.User_Name[i]==UName:
                                                            if DF2.Number_Plate[i]==NP:
                                                                print("Your Vechile Details")
                                                                print(DF2.loc[i:i,:])
                                        elif c3==3:
                                                exit

                                    elif c2==4:
                                        print("="*90)
                                        print("Premium".center(130))
                                        print("-> 25% discount on every booking")
                                        print("-> Reserved parking spot")
                                        print("-> Spot for a week + Maintainance")
                                        print("-> For INR 199/month")
                                        c3=int(input("1) Buy Premium \n 2) Back \n SELECT AN OPTION:"))
                                        if c3==1:
                                            no=int(input("Enter Card Number:"))
                                            cv=int(input("Enter CV Number:"))
                                            print("Transaction Complete")
                                        elif c3==2:
                                            exit
                                        
                                    elif c2==5:
                                        print("Logged Out")
                                        exit
        else:
            print("Incorrect Details")
