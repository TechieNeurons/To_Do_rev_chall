1. En utilisant **ltrace** on obtiens le flag chiffré :	**ZLT{Kdwhafy_ak_fgl_gtxmkuslagf}**
2. Dans Ghidra, on a pas mal de for dans des for et on a des for qui se répétent (les for qui nous font attendre), après analyse du code source j'ai trouvé le fonctionnement suivant :

   - Définition du flag chiffré et un for qui va le déchiffrer :

```
main(void)
{ 
  crypted_flag._0_8_ = 0x6877644b7b544c5a;
  crypted_flag._8_8_ = 0x665f6b615f796661;
  crypted_flag._16_8_ = 0x6b6d7874675f6c67;
  crypted_flag._24_4_ = 0x616c7375;
  crypted_flag._28_2_ = 0x6667;
  crypted_flag._30_1_ = 0x7d;
  setvbuf(stdout,(char *)0x0,2,0);
  crypted_flag_in_memory = strdup((char *)&crypted_flag);
  puts("Retrieving key.");
  
  for (; *crypted_flag_in_memory != '\0'; crypted_flag_in_memory = crypted_flag_in_memory + 1) {
```

   - Ensuite plus bas on a un for qui va appliquer une règle si la lettre est en majuscule :


```        
puts("This one\'s an uppercase letter!");

        if (*crypted_flag_in_memory + -0x12 < 'A') {
          *crypted_flag_in_memory = *crypted_flag_in_memory + '\x1a';
        }
        *crypted_flag_in_memory = *crypted_flag_in_memory + -0x12;
``` 

   - Une règle pour si la lettre est en minuscule :

```
puts("This one\'s a lowercase letter");
      if (*crypted_flag_in_memory + -0x12 < 'a') {
        *crypted_flag_in_memory = *crypted_flag_in_memory + '\x1a';
      }
      *crypted_flag_in_memory = *crypted_flag_in_memory + -0x12;

    printf("%c\n",(ulong)(uint)(int)*crypted_flag_in_memory);
  }
  puts("You\'re still here?");
  return 0;
}
```

3. Plus qu'a écrire un script qui va déchihffrer notre flag :)