print("Bonjour ! \nCe programme permet de savoir le nombre de jours d'un mois en fonction de son année !")
input_years = input("Quel est l'année ? ")
## Si l'années est un string reposer la question sinon continuer
if input_years.isdigit():
    ## continuer 
    ## verifier si l'anne est bisextille (divisible par 4)
    int_years = int(input_years)
    ## ajouter les mois en numéro
    ## essayer de le faire avec des modules aprés
    month_list = ["Janvier","01","1","Février","02","2","Mars","03","3","Avril","04","4","Mai","05","5","Juin","06","6","Juillet","07","7","Aout","08","8","Septembre","09","9","Octobre","10","Novembre","11","Décembre","12"]
    if int_years%4 == 0:
        month_bis = input("Quel est le mois ? ")
        ##si le mois n'est pas dans la liste, reposer la question sinon dire la réponse
        if month_bis in month_list:
            list_31_day = ["Janvier","Mars","Mai","Juillet","Aout","Octobre","Décembre","01","1","03","3","04","4","07","7","08","8","12"]
            ## si c'est février c'est 29 jours
            if month_bis=="Février" or month_bis=="2" or month_bis=="02":
                print("Ce mois comportme 29 jours !")
            elif month_bis in list_31_day:
                print("Ce mois comporte 31 jours !")   
            else:
                print("Ce mois comporte 30 jours !")    
        else:
            print("Vous devez entrer un mois valide !")
            quit()
    else:
        month = input("Quel est le mois ? ")
        if month in month_list:
            list_31_day = ["Janvier","Mars","Mai","Juillet","Aout","Octobre","Décembre","01","1","03","3","04","4","07","7","08","8","12"]
            ## si c'est février c'est 29 jours
            if month=="Février" or month=="2" or month=="02":
                print("Ce mois comporte 28 jours !")
            elif month in list_31_day:
                print("Ce mois comporte 31 jours !")   
            else:
                print("Ce mois comporte 30 jours !")
        else:
            print("Vous devez entrer un mois valide !")
            quit()                
else:
    print("Vous devez entrer un nombre !")
    quit()
