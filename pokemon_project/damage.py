def ClaculateDamage(AtkType, DefType, Atk, Def):
    effect = 0
    

    AtkType = input("Attacker is Fire, Grass, Water or Electric? : ")
    DefType = input("Reciever is Fire, Grass, Water or Electric? : ")

    if AtkType == "fire":

        if DefType == "grass":
            effect = 2

        if DefType == "water":
            effect = 0.5
        
        if DefType == "electric":
            effect = 1

    if AtkType == "water":

        if DefType == "grass":
            effect = 1.5

        if DefType == "fire":
            effect = 2
        
        if DefType == "electric":
            effect = 0.5

    if AtkType == "grass":

        if DefType == "fire":
            effect = 0.5

        if DefType == "water":
            effect = 2
        
        if DefType == "electric":
            effect = 1

    if AtkType == "electric":

        if DefType == "grass":
            effect = 1

        if DefType == "water":
            effect = 2
        
        if DefType == "fire":
            effect = 1


    return 50 * (Atk/Def) * effect