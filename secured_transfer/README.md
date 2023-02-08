1 - Fonction main -> crée un socket et envoie un fichier via ce socket (le fichier est chiffré)
	dans fonction de chiffrement on troue la clef :
		supersecretkeyusedforencryption!
	Fonction intéresante, la clef (local_38) clic droit pour transformer en uchar[32]
2 - On remarque que c'est un chiffrement AES_256_CBC
	probablement l'IV : local_48 = "someinitialvalue";
	
3 - extraire la partie data des paquets, seulement du premier (copy as a hex stream)

4 - tous mettre dans icyberchef.com