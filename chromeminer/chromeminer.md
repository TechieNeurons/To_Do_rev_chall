1. On lance l'instance
2. On télécharge DiscurdNitru.exe
3. Ouvrir dans Ghidra, dans les chaînes de charactère on a une URL : ".htb/c2VjcmV0/archive.zip?k=ZGlzY3VyZG5pdHJ1"
4. Coller l'URL à la fin de l'instance HTB pour télécharger le fichier archive.zip
5. Dans archive.zip, un manifest et des images inutiles, intéressant : le fichier js
6. Il est obfuscé, commencer par une désobfucation via un site, on remarque qu'il y a deux tableaux de char qui servent à former les fonctions, variables, etc.
7. Modifier le fichier pour print la totalité des chaînes de charactère du fichier
8. Quand on affiche les chaines de charactères on remarque les éléments suivants : AES-CBC, _NOT_THE_SECRET_, iv, key
9. Utiliser la chaine _NOT_THE_SECRET_ en tant qu'iv et que clef dans icyberchef.com pour décoder la grande chaine hex et on obtient le flag.
