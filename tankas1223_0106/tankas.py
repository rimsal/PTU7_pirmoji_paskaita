import random

class Tank:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = 'pirmyn'
        self.shot_directions = {'pirmyn': 0, 'atgal': 0, 'kairen': 0, 'desinen': 0}
        self.targets_hit = 0

    def move(self, direction_to_move):
        self.direction = direction_to_move
        if direction_to_move == 'pirmyn':
            self.y += 1  # Tankas pavažiavo į priekį
        elif direction_to_move == 'atgal':
            self.y -= 1  # Tankas pavažiavo į atgal
        elif direction_to_move == 'kairen':
            self.x -= 1  # Tankas pavažiavo į kairę
        elif direction_to_move == 'desinen':
            self.x += 1  # Tankas pavažiavo į dešinę

    def shoot(self, targetx, targety):

        print('Šūvis!')
        self.shot_directions[self.direction] += 1
        if self.x == targetx:
            if self.y < targety:
                if self.direction == 'pirmyn':
                    self.targets_hit += 1
                    return True
            else:
                if self.direction == 'atgal':
                    self.targets_hit += 1
                    return True
        if self.y == targety:
            if self.x < targetx:
                if self.direction == 'desinen':
                    self.targets_hit += 1
                    return True
            else:
                if self.direction == 'kairen':
                    self.targets_hit += 1
                    return True

        return False

    def info(self):
        print(f"Kryptis: {self.direction}")
        print(f"Koordinatės: {self.x}:{self.y}")
        print(f"Šūvių iš viso: {sum(self.shot_directions.values())}")
        print(f"{self.shot_directions}")
        print((f"Targets Hit: {self.targets_hit}"))


class Target:
    def __init__(self):
        self.x = random.randint(-5, 5)
        self.y = random.randint(-5, 5)

    def reset(self):
        self.x = random.randint(-5, 5)
        self.y = random.randint(-5, 5)


tankas = Tank()
taikinys = Target()
POINTS = 100

print("Sveiki, žaidžiam!")
while POINTS != 0:  # Programa veiks kol taškai nesibaigs.
    print("Judesiai:")
    print("w: aukštyn, s: žemyn, a: kairėn, d: dešinėn")
    print("b: Šūvis, i: informacija, q: išeiti")
    print(f"x: {tankas.x}, y: {tankas.y}")
    x = str(input("Tavo pasirinkimas: "))
    POINTS -= 10  # už kiekvieną ėjimą nuskaitomi 10 taškų

    if x == 'w':
        tankas.move('pirmyn')
    elif x == 's':
        tankas.move('atgal')
    elif x == 'a':
        tankas.move('kairen')
    elif x == 'd':
        tankas.move('desinen')
    elif x == 'b':
        if tankas.shoot(taikinys.x, taikinys.y):
            print('Pataikei')
            POINTS += 50  # Pataikius pridedami 50 taškų
            taikinys.reset()  # Per naują nustatomas taikinys
    elif x == 'i':
        tankas.info()
    elif x == "q":
        print(f"Targets Hit: {tankas.targets_hit}")
        break
    elif x == "c":
        print(f"{taikinys.x}: {taikinys.y}")

print("Taškai baigėsi.\nGalite pradėti iš naujo.")
