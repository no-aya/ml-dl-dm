print("hello")
#%%
#Boites et contenu
boites ={
    1:9,
    2:8,
    3:5,
    4:2,
    5:11,
    6:3,
    7:5,
    8:12,
    9:5,
    10:-2,
    11:4,
    12:-6,
    13:6
}



#%%
# 1 : soustraire nombre boite boite 7 - boite 6 et mettre dans boite 12
boites[12] = boites[7] - boites[6]
#%%
# 2 : ajouter nombre boite 12 à boite 13 et mettre dans boite 12
boites[12] = boites[12] + boites[13]
#%%
# A-ton dan 12 un nombre divisible par 5?
boites[12] % 5 == 0
#%%
# 4. Changer instruction 2 : décrémenter le numéro de la seconde boite mentionnéee par (nombre dans la boite dont le numéro est dans la boite 11)
boites[2] = boites[2] - 1
#%%
# 5. A ton nombre dn boite 2 inférieur au numéro de la seconde boite mentionnee dan l'instruction 2?
boites[2] < boites[boites[11]][0]
#%%
# Afficher boite 12
print(boites[11])
#%%
# Oncherche a doubler le contenu de 1,4,7,10
# a. Ajouter nombre dans boite 1 + nombre boite 1 mettre le résultat dans boite 1
boites[0][1] = boites[0][1] + boites[0][1]
#%%
# b. modifier l'intruction a : augmenter de 3 chaqune numéro de boite mentionnée
boites[0][0] = boites[0][0] + 3

#%%
# c. Aton nombre boite 2 inférieur au numéro de la seconde boite mentionnée par l'instruction a?
boites[1][1] < boites[boites[0][0]-1][0]
#%%
# refaire a b et c
boites[3][1] = boites[3][1] + boites[3][1]
boites[3][0] = boites[3][0] + 3
boites[3][1] < boites[boites[3][0]-1][0]

#%%
print(boites[1])
#%%

