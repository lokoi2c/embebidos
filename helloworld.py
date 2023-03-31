def func():
    print("me quieres? (Y/N):")
    answer = input()
    if answer == 'Y' :
        print("YO TAMBIEN :)")
    else:
        print("me importa 1e32 hectareas")
    print()
    
class estudiante:
    def aprueba(self, nota, dinero):
        if nota > 3 & dinero > 3500:
            print("Apreuba")
        else:
            print("no aprueba, pobreton")
        return 0
            
    def estudiante(self, nombre, apellido):
        print("Apreuba")
        print("no aprueba")
        return 0

estud = estudiante()


    #func()
estud.estudiante('carlos','lopez')
estud.aprueba(2, 200)