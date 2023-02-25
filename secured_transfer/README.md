1. Ouvrir le binaire avec Ghidra
2. Dans la fonction **main**, on remarque la création d'un socket et l'envoie d'un fichier via, le fichier est chiffré avant d'être envoyé
3. Dans fonction de chiffrement on troue la clef de chiffrement : **supersecretkeyusedforencryption!**
   - Pour récupérer la clef : faire un clic droit sur **local_38** puis transformer en **uchar[32]**
4. On remarque également que c'est un chiffrement **AES_256_CBC** et on a l'IV : **local_48 = "someinitialvalue";**
5. Ouvrir le fichier pcap et extraire la partie data du paquet contenant des datas (copy as a hex stream)
6. Tous mettre dans **icyberchef.com**