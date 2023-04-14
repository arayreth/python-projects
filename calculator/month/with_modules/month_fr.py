## importation du module calendrier
import calendar

print("Bonjour ! \nCe programme permet de savoir le nombre de jours d'un mois en fonction de son année !")
## demander l'année
input_years = int(input("Quel est l'année ? "))
## demander le mois
month = input("Quel est le mois ? ")
## liste des mois
month_list = ["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Décembre",]
## si le mois est un nombre et que ce nombre est compris entre 1 et 12 (parceque il n'existe que 12 mois) transformer la variable month en integer
if month.isdigit() and 0<int(month)<13:
    month = int(month)
## sinon si le mois est dans la liste des mois transformer le mois qui est en lettre (récuper sa position dans la liste) en nombre pour pouvoir utiliser la focntion monthrange    
elif month in month_list:
    month = month_list.index(month)+1
## sinon indiquer à l'utilisateur que le mois n'est pas valide et quitter le programme    
else:
    print("Vous devez entrer un mois valide !")
    quit()
## calculer le nombre de jours dans le mois avec la fonction monthrange du module calendar    	
nb_day = calendar.monthrange(input_years,month)
## indiquer à l'utilisateur le résultat du calcul (nb_day[1] car il nous faut le deuxiéme résultat de la fonction monthrange, le premier étant le premier jour du mois et le second étant le nombre de jours dans le mois)
print("Il y'as ",nb_day[1]," jours dans ce mois !")
