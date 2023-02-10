1. Fichier .hs --> haskell language
2. Fonction extractFlag = vérifie que le Flag est au format HTB{}
  fonction chunks --> transforme un tableau en un tableau de petit tableau
  checkFlag --> vérification de l'entrée
    Le flag doit faire 76 charactères
    Ensuite on va regarder les where (conditions)
    content contient la partie entre {}
    one va prendre le flag, le découper en chunk de 2 et soustraire, le résultat des soustraction est stockés dans one et comparé au tableau "a"
    two va prendre le flag, le découper en chunk de 3 et xor les trois ensemble, stock dans la variable two et compare à "b"
    three va prendre le flag, le découper en chunk de 4 et additionne les 4 éléments, résultat stocké dans three et comparé à "c"
    four va prendre le flag, le découper en chunk de 5 et ne garde que le premier charactère, stocké dans four et comparé à "d"
3. Création d'un script python 3 utilisant z3 pour résoudre le chall