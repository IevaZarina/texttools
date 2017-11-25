# -*- coding: utf-8 -*-

from symbols import symbol_dict


def transliterate(line):
    return "".join([symbol_dict[letter] if letter in symbol_dict else letter for letter in line])


if __name__ == '__main__':
    print transliterate(u"Šaursliežu dzelzceļš, Chemin de fer à voie étroite, Узкоколейная железная дорога")
