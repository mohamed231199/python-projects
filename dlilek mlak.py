print "bienvenue dans un jeu de dlilek mlak"
raw_input ('entrez votre nom...: ')
print "si vous ecrivez un lieu vous ne pouvez plus le retapez ,il ya 2 lieux qui peuvent vous enlever tous l'argent que vous possedez"
print "choisis un lieu....:   tunis ,la marsa ,jerba ,jandouba ,mannouba ,sfax ,gabes ,gammarth ,paris ,new york city ,tokyo ,istambul ,madrid ,alger ,hawaii"
prix =[1000, 500, 2000, 20, 6000, 10, 200, 900000, 300, 400, 600 ,3000 ,4000 ,7000 ,800000]
lieu =['tunis' ,'la marsa' ,'jerba' ,'jandouba','mannouba' ,'sfax' ,'gabes' ,'gammarth' ,'paris' ,'new york city' ,'tokyo' ,'istambul' ,'madrid' ,'alger' ,'hawaii']
x =['****' ,'****' ,'****' ,'****','****' ,'****' ,'****' ,'****' ,'****' ,'****' ,'****' ,'****' ,'****' ,'****' ,'****']
y =['****', '****', '****', '****', '****', '****', '****', 'gammarth', '****', '****', '****', '****', '****', '****', 'hawaii']
z =['****', '****', '****', '****', '****', '****', '****', 900000, '****', '****', '****', '****', '****', '****', 800000]
lien =[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13 ,14]
while x != lieu:    
    destinaton = raw_input("lieu.....: ")
    while destinaton not in lieu:
        destinaton = raw_input("erreur Entrez un autre Lieu...:  ")
    if destinaton not in lieu :
        print("ERROR!")
    if destinaton == 'tunis':
        print "1000M perdus! bien"
        pos = lieu.index('tunis')
        pos_prix = lien[pos]
        prix[pos] = "****"
        lieu[pos] = "****"
    if destinaton == 'la marsa':
        print "500M perdus! c'est tres bien"
        pos = lieu.index('la marsa')                        
        pos_prix = lien[pos]
        prix[pos] = "****"
        lieu[pos] = "****"
    if destinaton == 'jerba':   
        print "2000M perdus!attention"
        pos = lieu.index('jerba')
        pos_prix = lien[pos]
        prix[pos] = "****"
        lieu[pos] = "****"
    if destinaton == 'jandouba':
        print "20M perdus! ouf t'as eu de la chance"
        pos = lieu.index('jandouba')
        pos_prix = lien[pos]
        prix[pos] = "****"
        lieu[pos] = "****"
    if destinaton == 'mannouba':
        print "6000M perdus!tu vas peux etre perdre"
        pos = lieu.index('mannouba')                        
        pos_prix = lien[pos]
        prix[pos] = "****"
        lieu[pos] = "****"
    if destinaton == 'gabes':
        print "200M perdus!t'as eu de la chance"
        pos = lieu.index('gabes')                        
        pos_prix = lien[pos]
        prix[pos] = "****"
        lieu[pos] = "****"
    if destinaton == 'sfax':
        print "10M perdus!super"
        pos = lieu.index('sfax')                        
        pos_prix = lien[pos]
        prix[pos] = "****"
        lieu[pos] = "****"
    if destinaton == 'gammarth':
        print "900000M perdus! muahahahahahahahahahahahahahahahahahahahaha tas perdu"
        pos = lieu.index('gammarth')                        
        pos_prix = lien[pos]
        prix[pos] = "****"
        lieu[pos] = "****"
        print "fini"
    if destinaton == 'paris':
        print "300M perdus!c'est bien"
        pos = lieu.index('paris')
        pos_prix = lien[pos]
        prix[pos] = "****"
        lieu[pos] = "****"
    if destinaton == 'new york city':
        print "400M perdus!c'est bien"
        pos = lieu.index('new york city')
        pos_prix = lien[pos]
        prix[pos] = "****"
        lieu[pos] = "****"
    if destinaton == 'tokyo':
        print "600M perdus! bien"
        pos = lieu.index('tokyo')
        pos_prix = lien[pos]
        prix[pos] = "****"
        lieu[pos] = "****"
    if destinaton == 'istambul':
        print "3000M perdus!attention"
        pos = lieu.index('istambul')
        pos_prix = lien[pos]
        prix[pos] = "****"
        lieu[pos] = "****"
    if destinaton == 'madrid':
        print "4000M perdus!"
        pos = lieu.index('madrid')
        pos_prix = lien[pos]
        prix[pos] = "****"
        lieu[pos] = "****"
    if destinaton == 'alger':
        print "7000M perdus!oh nnon"
        pos = lieu.index('alger')
        pos_prix = lien[pos]
        prix[pos] = "****"
        lieu[pos] = "****"
    if destinaton == 'hawaii':
        print "900000M perdus! muahahahahahahahahahahahahahahahahahahahaha tas perdu"
        print "fini"
        pos = lieu.index('hawaii')
        pos_prix = lien[pos]
        prix[pos] = "****"
        lieu[pos] = "****"
    if lieu == y and prix == z:
        print "victoire"
        break
    print lieu
    print prix
        


    

    



    

    
    








