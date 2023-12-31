import random 

#juego de las cuevas y el dragón
def cueva(opcion):
    
    dragon = random.randint(1,2)
    
    if opcion == dragon:
        return False #ha muerto
    else:
       
        return True #cuerva con tesoro



premio = 0
print("Hay dos cuevas y tienes que escoger una de ellas para entrar. Sin embargo, puede que haya un dragón 🐉 dentro, y morirás. De lo contrario hay un tesoro. Si acumulas más de 500 en tesoros, acaba el juego.")
while True:
    
    opcion = int(input("Cueva 1 o 2?: "))
    if opcion == 0:
        break
    elif premio >= 500:
        print("Has salido vivo de las cuevas con", premio, "💰 tesoros. Enhorabuena 🥳!")
        break
    else:
        cueva(opcion)
        if cueva(opcion):
            print("Sigues vivo!🤫")
            premio+= random.randint(45,130)
        else:
            print("Has muerto!😫 Has acumulado", premio,"💰 de tesoro.")
            exit()
