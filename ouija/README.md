1 - ltrace : on voit flag chiffré :
	ZLT{Kdwhafy_ak_fgl_gtxmkuslagf}
	
2 - Ghidra !!! Pow!Pow!Pow!

main(void)
{
  complex32 crypted_flag;
  int local_3c;
  int local_38;
  int local_34;
  int local_30;
  int local_2c;
  int local_28;
  int local_24;
  char *crypted_flag_in_memory;
  int local_14;
  int local_10;
  int i;
  
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

-->        
puts("This one\'s an uppercase letter!");

        if (*crypted_flag_in_memory + -0x12 < 'A') {
          *crypted_flag_in_memory = *crypted_flag_in_memory + '\x1a';
        }
        *crypted_flag_in_memory = *crypted_flag_in_memory + -0x12;

--> 
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
