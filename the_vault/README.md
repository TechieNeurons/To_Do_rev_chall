1. On lance le logiciel on a un message disant qu'il trouve pas le mot de passe
2. Ouvrir le binaire dans Ghidra, on remarque des chaines de charactères et notamment une chaine **"flag.txt"**
3. On va créer un fichier **flag.txt** avec n'importe quoi dedans car je pense que le logiciel ouvre ce fichier pour tester son contenu contre le vrai flag (on entre le flag dans un fichier plutôt qu'en argument)
4. Ensuite on va suivre la **XREF** de la chaine **flag.txt** pour lire la fonction qui fait appel à cette chaine (c'est également dans cette fonction qu'il y a la phrase de réussite ou d'échec)
5. Malheureusement la lecture de la fonction nous aide pas trop...

Ici on a l'ouverture du fichier flag.txt :
```
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  std::basic_ifstream<char,std::char_traits<char>>::basic_ifstream((char *)user_flag,0x10e004);
                    /* try { // try from 0010c25e to 0010c400 has its CatchHandler @ 0010c2a5 */
  bVar2 = std::basic_ifstream<char,std::char_traits<char>>::is_open();
  if ((bVar2 & 1) == 0) {
    std::operator<<((basic_ostream *)&std::cout,"Could not find credentials\n");
                    /* WARNING: Subroutine does not return */
    exit(-1);
  }
```

Et la comparaison pour savoir si on a le bon flag :
```
  bVar1 = true;
  i = 0;
  while( true ) {
    local_241 = 0;
    if (i < 0x19) {
      local_241 = std::basic_ios<char,std::char_traits<char>>::good();
    }
    if ((local_241 & 1) == 0) break;
    std::basic_istream<char,std::char_traits<char>>::get((char *)user_flag);
    bVar2 = (***(code ***)(&PTR_PTR_00117880)[(byte)(&DAT_0010e090)[(int)i]])();
    if ((int)local_219 != (uint)bVar2) {
      bVar1 = false;
    }
    i = i + 1;
  }
```
Cette comparaison nous apprend que le flag fait 25 char (**i < 0x19**)
Le reste je sais pas trop \o/

6. J'ai décidé de faire un bon de dynamique parce que le statique ne m'aidait pas... J'ai donc ouvert le fichier avec IDA et j'ai écris 25 'A' dans le fichier flag (c'est important d'avoir le même nombre de char que dans le flag, **car le programme n'a pas l'air de se terminer avant d'avoir tout comparé**)
7. Dans la fonction main on voit qu'il y a un appel à une autre fonction (**call    sub_5620B8D2E220**), on va se déplacer dans cette fonction et placer un breakpoint sur la ligne **lea     rsi, aFlagTxt**, juste avant l'ouverture en mémoire du fichier.
8. A ce moment là je vais appuyer sur f5 pour obtenir le code décompilé plus simple à lire (l'assembleur c'est chiant...), ensuite on va avancer (f8) et quand IDA repasse sur l'assembleur je reappuye sur f5
9. J'ai remarqué que ces deux lignes **v0 = off_55BCAC870880[byte_55BCAC867090[i]];** et **v6 = ((__int64 (__fastcall *)(__int64 (__fastcall \*\*\*)()))\*\*v0)(v0);** avait l'air d'accèder au vrai flag ( et de faire des actions dessus), après cette deuxième ligne quand on avance (f8) on sort du décompilé (changement de fonction il me semble)
10. la ligne sur laquelle on arrive est : **mov     al, [rbp+var_23B]** et on remarque que à l'adresse **[rbp+var_23B]** il y a un 'H', j'ai donc placé un breakpoint sur cette ligne et j'ai cliqué sur run pour aller au prochain breakpoint (c'est-à-dire cette ligne mais à la prochaine itération de la boucle) et on a un 'T', puis un 'B', puis '{', ça ne fait plus aucun doute notre flag apparait ici, on a plus qu'à répété l'action jusqu'au '}' et on est bon !
