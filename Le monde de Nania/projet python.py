def Menu):
    print(" ---------------------------")
    print("                            ")
    print("BIENVENUE DANS LE MONDE DE NANIA!")
    print("                            ")
    print(" ---------------------------")
    print("                            ")
    print("1: Créer une nouvelle partie")
    print("2: Charger une partie")
    print("3: A propos")
    print("4: Quitter")
    print("                            ")
    print(" ---------------------------")
    Choix = int(input())
    if Choix == 1:
        AskName()
        print("N'oubliez pas, pour avancer, appuyez sur la touche 'X' de votre clavier")
        PlayGame()
    elif Choix == 2:
        LoadGame()
    elif Choix == 3:
        About()
    else:
        Exit()



def About():
    print("LE JEU 'LE MONDE DE NANIA' EST UN JEU PRODUIT DANS LE CADRE")
    print("DU COURS DE PYTHON PAR NATHAN, ALEXANDRE ET MAEDEH")
    print("© Janvier 2021")
    print("Appuyez sur 'X' pour revenir au menu")
    choice = input()
    if choice == 'X':
        Menu()

#FONCTIONS PRINCIPALES DU JEU
def PlayGame():
    Armes()
    Entree()
    Niveau1()
    Niveau2()
    Niveau3()
    Niveau4()
    FinDuJeu()

#FONCTION EXIT (JOUEUR PERD SON COMBAT OU ABANDON DU JOUEUR)
def Exit():
    print("GAME OVER...")
    print("Merci d'avoir joué! A bientôt!")
    Menu()

#FONCTION NAME
def AskName():
    print('Pseudo:')
    Name = input()
    print('Bienvenue ' + Name + "!")
    return (Name)

#FONCTION SAC D'ARMES
def Armes():
    print("Dans votre sac se trouve les armes suivantes:")
    ListeArmes = []
    print(ListeArmes)

#FONCTION COMBAT
def Combat():
    print("Déclinez votre identité devant le monstre: ")

    Name = input()


    # Stats personnage
    Lvl: 1
    player_health = 100
    player_move = ["Coup de couteau"]
    Atk: 20
    Def: 20
    Xp: 0
    Inventaire: []
    Gold: 500

    # Stats du Bot1
    bot_health = 30
    AtkBot1: 25
    DefBot1: 5
    XP_gagne: 20

    # Stats du Bot2
    HpBot2: 50
    AtkBot2: 25
    DefBot2: 15
    XP_gagne: 50

    # Stats du Bot3
    HpBot3: 75
    AtkBot3: 35
    DefBot3: 20
    XP_gagne: 100

    # Stats du Bot4
    HpBot4: 125
    AtkBot4: 50
    DefBot4: 25
    XP_gagne: 200

    # Stats du Bot5
    HpBot4: 175
    AtkBot4: 75
    DefBot4: 30
    XP_gagne: 350

    # Stats du Boss
    HpBoss: 500
    AtkBoss: 150
    DefBoss: 100

    # Augmentation Stats Niveaux
    Hpup: 100
    Atkup: 20
    Defup: 20
    XP_gagne: 20
    XP_requis: 20

    # Fonction du combat

    import random
    import sys

    # pour savoir qui du bot ou du joueur commence en premier
    turn = random.randint(1, 2)
    if turn == 1:
        player_turn = True
        bot_turn = False
        print(Name + " ouvre les hostilités.")
    else:
        player_turn = False
        bot_turn = True
        print("Le monstre ouvre les hostilités.")
        print("Que souhaitez-vous faire ? :")
        print("1. Coup de couteau")
        print("2. Potion (Recupère de la vie 25 hp)")

    print("\nVos vies: ", player_health, "\n Vie du monstre: ", bot_health)

    # Loop du combat
    while (player_health != 0 or bot_health != 0):
        heal_up = False  # determine if heal has been used by the player. Resets false each loop.
        miss = False  # determine if the chosen move will miss.

        # create a dictionary of the possible moves and randomly select the damage it does when selected  ### Faire un input sur les listes
        moves = {"Coup de couteau": random.randint(18, 25)};
        if player_turn:
            print("Que souhaitez-vous faire ? :")
            print("1. Coup de couteau")
            print("2. Potion (Recupère de la vie 25 hp)")

        player_move = input("> ").lower()

        # Fonction qui donne une precision des attaques
        move_miss = random.randint(1, 5)

        if move_miss == 1:
            miss = True
        else:
            miss = False
        # Si = 0, l'attaque échoue
        if miss:
            player_move = 0
            print(Name + " a raté son attaque !")
            Exit()
        else:
            if player_move in ("1", "Coup de couteau", "couteau"):
                player_move = moves["Coup de couteau"]
                print(Name + " assène le monstre avec son couteau. " + Name + " inflige ", player_move, " dégats.");
            elif player_move in ("2", "heal"):
                heal_up = True
                player_move = moves['heal']
                print( Name + "utilise sa potion. Il soigne " + player_move + "de sa vie.")
            else:
                print("\nCeci n'est pas un coup valide, Essayez autre chose.")
        # Tour du BOT
    else:
        move_miss = random.randint(1, 5)
        if move_miss == 1:
            Exit()
        else:
            miss = False
            # Si = 0, Le bot inflige 0 dégat
            if miss:
                computer_move: 0
                print("Le monstre a raté son attaque !")
                sys.exit()
            else:
                if bot_health > 30:
                    if player_health > 75:
                        bot_move = moves[0]
                        print("\n Le monstre utilise Frappe violente. Il inflige ", bot_move, " de dégats.")
                    elif player_health > 35 and player_health <= 75:
                        randmoves = ["Coup de poing", "Frappe violente"]
                        randmoves = random.choice(randmoves)
                        bot_move = moves[randmoves]
                        print("\nLe monstre utilise ", randmoves, ". Il inflige ", bot_move, " de dégats.")
                    elif player_health <= 30:
                        bot_move = moves["Frappe violente"]  # Coup fatale
                        print("\nLe (bot) utilise Frappe violente. il inflige ", bot_move, " de dégats.")
                    else:  # Si le bot a moins de 30hp, il a 50% de chance de se soigner
                        heal_or_fight = random.randint(1, 2)
                        if heal_or_fight == 1:
                            heal_up = True
                            bot_move = moves["Heal"]
                            print("\nLe (bot) se soigne. Il récupère ", bot_move, " de point de vie.")
                        else:
                            if player_health > 75:
                                bot_move = moves[""]
                                print("\nLe (bot) utilise Coup de poing. Il inflige ", bot_move, " de dégats.")
                            elif player_health > 35 and player_health <= 75:
                                randmoves = ["Coup de poing", "Frappe violente"]
                                randmoves = random.choice(randmoves)
                                bot_move = moves[randmoves]
                                print("\nThe computer used ", randmoves, ". Il inflige ", bot_move, " de dégats.")
                            elif player_health <= 35:
                                bot_move = moves["Frappe violente"]  # FINISH HIM!
                                print("\nLe (bot) utilise Frappe violente. Il inflige ", bot_move, " de dégats.")

                    if heal_up:
                        if player_turn:
                            player_health += player_move
                            if player_health > 100:
                                player_health = 100
                        else:
                            bot_health += bot_move
                            if bot_health > 100:
                                bot_health = 100
                    else:
                        if player_turn:
                            bot_health -= player_move
                            if bot_health < 0:
                                bot_health = 0  # cap minimum health at 0
                                winner = "Player"

                        else:
                            player_health -= bot_move
                            if player_health < 0:
                                player_health = 0
                                winner = "bot"

#FONCTION ENTREE DANS LE JEU + ENTREE DANS LA GROTTE
def Entree():
    print("Vous atterissez devant un chemin sombre...")
    choice = input()
    if choice == 'X':
        print("Aucune information n'est disponible sur la localisation de ce lieu")
    choice = input()
    if choice == 'X':
        print("Continuez à avancer, vous en saurez peut-être un peu plus...")
    choice = input()
    if choice == 'X':
        print("Attention!!!")
    choice = input()
    if choice == 'X':
        print("....")
    choice = input()
    if choice == 'X':
        print("UN PISTOLET!")
    print("Appuyez sur la touche 'Y' pour l'ajouter dans votre sac")
    choice = input()
    if choice == 'Y':
        print("Vous avez une arme supplémentaire ajoutée dans votre sac")
        ListeArmes.append("Pistolet")
    print(ListeArmes)
    print("Au loin devant vous se trouve un passage mais impossible de savoir ce que c'est...")
    print("Voulez-vous continuer à avancer? Oui ou Non?")
    choice = input()
    if choice == "non" or choice == "Non" or choice == "NON":
        Exit()
    if choice == "oui" or choice == "Oui" or choice == "OUI":
        print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\    BIENVENUE DANS LA GROTTE!    ////////////////////")
    choice = input()
    if choice == "X":
        print("UNE GRILLE S'EST REFERMEE DERRIERE VOUS...")
    choice = input()
    if choice == "X":
        print("IL NE VOUS RESTE PLUS QU'A TRAVERSER LA GROTTE POUR Y SORTIR...")
    choice = input()
    if choice == "X":
        print("AVANCEZ! N'AYEZ PAS PEUR...")


ListeArmes = []


#FONCTION PREMIER NIVEAU: LES 3 CHEMINS
def Niveau1():
    print("3 chemins se trouvent face à vous, lequel prenez-vous? 1,2 OU 3? ")
    choice = int(input())
    if choice == 1 or choice == 2:
        print("Oh non! Vous rencontrez un monstre sur votre chemin! :(")
        print("Vous ne pourrez continuer votre chemin uniquement en le défiant...")
        choice = input()
        if choice == 'X':
            print("Appuyez sur 'Z' pour commencer le combat")
        choice = input()
        if choice == 'Z':
            Combat()
            print('WOW! Quel combat! Votre chemin est libre à présent...')
    if choice == 3:
        print("Regardez juste là... ")
        choice = input()
        if choice == 'X':
            print("UN SABRE!")
        choice = input()
        if choice == 'X':
            print("Appuyez sur la touche 'Y' pour l'ajouter dans votre sac")
        choice = input()
        if choice == 'Y':
            ListeArmes.append("Sabre")
            print("Vous avez une arme supplémentaire ajoutée dans votre sac")
            print(ListeArmes)


#FONCTION DEUXIEME NIVEAU: LE LABYRINTHE
def Niveau2():
    choice = input()
    if choice == 'X':
        print("Faites attention en marchant...")
    choice = input()
    if choice == 'X':
        print("La visibilité se réduit de plus en plus...")
    choice = input()
    if choice == 'X':
        print("Vous voulez vraiment continuer?")
    choice = input()
    if choice == "non" or choice == "Non" or choice == "NON":
        Exit()
    if choice == "Oui" or choice == "OUI" or choice == "Oui":
        print("≈≈≈≈≈≈≈≈≈≈≈≈≈≈    BIENVENUE DANS LE LABYRINTHE DE LA GROTTE    ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈")
    choice = input()
    if choice == 'X':
        print("Voici le plan de ce labyrinthe, pour vous déplacer: ")
    choice = input()
    if choice == 'X':
        print("H => Vers le haut")
        print("B => Vers le bas")
        print("D => Vers le droite")
        print("G => Vers le gauche")

    def CreateMap():
        Map = [[8, 8, 8, 8], [8, 8, 8, 8], [8, 8, 8, 8], [8, 8, 8, 8]]
        for l in Map:
            print(l)
        return Map

    def Movement(Map, Pos):
        dir = input()
        if dir == "D":
            Pos[1] = Pos[1] + 1
        if dir == "B":
            Pos[0] = Pos[0] + 1
        if dir == "H":
            Pos[0] = Pos[0] - 1
        if dir == "G":
            Pos[1] = Pos[1] - 1

        Map[Pos[0]][Pos[1]] = "P"
        return Pos

    M = CreateMap()
    P = [0, 0]
    #    0 1
    P = Movement(M, P)

    print("---")
    for l in M:
        print(l)

    P = Movement(M, P)

    print("---")
    for l in M:
        print(l)

    P = Movement(M, P)

    print("---")
    for l in M:
        print(l)

    print("ATTENTION VOUS FAITES A NOUVEAU DEVANT UN MONSTRE!!")
    print("Appuyez sur 'Z' pour lancer le combat")
    choice = input()
    if choice == 'Z':
        Combat()
        print("Pour continuer le jeu, appuyez sur la touche X")


#FONCTION TROISIEME NIVEAU: DILEMME
def Niveau3():
    choice = input()
    if choice == 'X':
        print("Quel dur combat...")
    choice = input()
    if choice == 'X':
        print("Tiens tiens...")
    choice = input()
    if choice == 'X':
        print("UN BAZOUKA!")
    choice = input()
    if choice == 'X':
        print("Appuyez sur Y pour l'ajouter dans votre sac d'armes")
    choice = input()
    if choice == 'Y':
        print("Vous avez une arme supplémentaire ajoutée dans votre sac")
        ListeArmes.append("Bazouka")
    print(ListeArmes)
    choice = input()
    if choice == 'X':
        print("Aïe aïe aïe...")
    choice = input()
    if choice == 'X':
        print("Vous vous retrouvez devant un dilemme")
    choice = input()
    if choice == 'X':
        print("Vous êtes devant une impasse")
        print("Un chemin se présente à votre droite...")
    choice = input()
    if choice == 'X':
        print("... Mais aussi à votre gauche!")
    choice = input()
    if choice == 'X':
        print("Quel chemin voulez-vous prendre ?")
    choice = input()
    if choice == 'Droite' or 'DROITE' or 'droite' or 'Gauche' or 'GAUCHE' or 'gauche':
        print("Aïe...")
    choice = input()
    if choice == 'X':
        print("Il semble qu'un autre monstre vous attende de nouveau au loin pour un combat...")
    choice = input()
    if choice == 'X':
        print("Appuyez sur 'Z' pour lancer le combat")
    choice = input()
    if choice == "Z":
        Combat()
    else:
        Exit()



def Niveau4():
    choice = input()
    if choice == 'X':
        print('WOW! 3 monstres éliminés, bravo!...')
    choice = input()
    if choice == 'X':
        print('Votre chemin est de nouveau libre à présent...')
    choice = input()
    if choice == 'X':
        print('Mon dieu...')
    choice = input()
    if choice == 'X':
        print('Regardez! Au loin!...')
    choice = input()
    if choice == 'X':
        print('LA SORTIE DE LA GROTTE!')
    choice = input()
    if choice == 'X':
        print('Allez-y vous êtes presque...')
    choice = input()
    if choice == 'X':
        print("!!!!!!!!")
    choice = input()
    if choice == 'X':
        print("!!!!!!!!")
    choice = input()
    if choice == 'X':
        print("OUPS")
    choice = input()
    if choice == 'X':
        print("Avant de sortir de la grotte, vous devez affronter un dernier obstacle...")
    choice = input()
    if choice == 'X':
        print("Un ultime combat vous attend pour sortir de la grotte...")
    choice = input()
    if choice == 'X':
        print("Appuyez sur 'Z' pour lancer l'ultime combat")
    choice = input()
    if choice == 'Z':
        Combat()

#FONCTION FIN DU JEU QUI RETOURNE AU MENU PRINCIPAL
def FinDuJeu():
    print("Bravo! Vous êtes sorti de la grotte et avait vaincu 4 monstres!")
    Menu()

Menu()
