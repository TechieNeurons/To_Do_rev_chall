1. On a un Fichier **.hs** qui est donc un code source haskell
2. On a une fonction **extractFlag** qui vérifie que le Flag est au format **HTB{}**
   - la fonction **chunks**, transforme un tableau en un tableau de petit tableau
   - **checkFlag**, vérification de l'entrée de l'utilisateur
   - Il vérifie que le flag est de **76 charactères**
   - Analyse des conditions **where** qui sont les conditions qui doivent être vrai pour valider le flag
     - La variable **content** contient la partie entre **{}** c'est à dire le flag
     - **one** va prendre le flag, le découper en chunk de 2 et soustraire, le résultat des soustraction est stockés dans one et comparé au tableau "a"
     - **two** va prendre le flag, le découper en chunk de 3 et xor les trois ensemble, stock dans la variable two et compare à "b"
     - **three** va prendre le flag, le découper en chunk de 4 et additionne les 4 éléments, résultat stocké dans three et comparé à "c"
     - **four** va prendre le flag, le découper en chunk de 5 et ne garde que le premier charactère, stocké dans four et comparé à "d"
3. Création d'un script python 3 utilisant z3 pour résoudre le chall :)
4. Quand on print model la liste est désordonnée, on peut faire un script pour la remettre dans l'odre, mais attention l'ordre risque d'être flag_1, flag_10, etc. donc encore de l'ordre à mettre ensuite. Moi j'ai remis dans l'odre à la main
5. Une fois qu'on a les nombres dans l'ordre on peut les transformer en ASCII (décimal vers ascii)