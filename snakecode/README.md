1. Décompiler .pyc avec uncompyle6
2. Le code est obfusqué mais on voit l'utilisation de **marshal.loads** à la première ligne ensuite les autres lignes se servent de cette ligne pour charger d'autres fonctions
3. Pour passer le marshal en pyc : https://gist.github.com/stecman/3751ac494795164efa82a683130cabe5#file-marshal-to-pyc-py
4. on récupère la première ligne :

```
python (print('base64 string').decode('base64')) >> ll.bin
```

5. Ensuite on utilise le script **marshal-to-pyc.py** pour transformer **ll.bin** en code python
6. Le code fait un **zlib.decompress** d'une chaine de charactère decodé de la base 64 et le load avec marshal
7. J'ai écris le script **prepare.py** pour décompiler toutes les fonctions marshall
8. Quand on lit les différentes fonction obtenu on trouve le flag dans la fonction a3