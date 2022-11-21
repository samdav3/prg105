from creature_class import Creature
from creature_class import Orc
from creature_class import OrcBoss


def main():
    creature = Creature('raccoon', 'true', (2, 50, 33), 'raccoon.gif')
    orc = Orc('kangaroo', 'false', (-150, 300, 25), 'kangaroo.gif', 'boomerang', '200', '125')
    orc_boss = OrcBoss('lion', 'true', (200, -150, 45), 'lion.gif', 'claws of steel', '400', '350', 'Sebastian', 'deafening roar')
    print(creature.__str__())
    print('\n')
    print(orc.__str__())
    print('\n')
    print(orc_boss.__str__())


main()
