#!/usr/bin/env python3
from bin.classes.password_manger import PasswordManger
from bin.classes.string_manager import StringManager
from bin.classes.graph import Graph

PASSWORD_FILE_PATH = "../../passwords/Ashley-Madison.txt"


if __name__ == '__main__':
    passwords = StringManager.file_to_string_list(PASSWORD_FILE_PATH)
    print("Nombre de mot de passe dans le corpus : ", len(passwords))

    average = StringManager.get_average_len(passwords)
    print("Longueur moyenne des mots contenus dans le corpus : ", "%.2f" % average)

    duplicate = StringManager.getDuplicatesWithCount(passwords)
    print("Nombre de  mots redondants : " + str(len(duplicate)))

    password_manager = PasswordManger(passwords)
    stats = password_manager.get_pwd_symbol_stats()
    Graph.draw_pwd_symbol_stats(stats)

    contains_stats = password_manager.get_pwd_type_stats()

    print("\n")
    for key, value in contains_stats.items():
        print(key + " : " + str(value))

    Graph.draw_bar_graph(contains_stats)
