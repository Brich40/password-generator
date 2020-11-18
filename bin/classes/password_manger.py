#!/usr/bin/env python3
import re


class PasswordManger:
    def __init__(self, passwords):
        self.passwords = passwords

    def get_pwd_symbol_stats(self):
        stats = {}
        for password in sorted(self.passwords, key=len):
            key = str(len(password)) + "_symbol"
            if key in stats:
                stats[key] += 1
            else:
                stats[key] = 0
        return stats

    def get_pwd_type_stats(self):
        alpha_pwd = 0
        numeric_pwd = 0
        special_char_pwd = 0
        mixed_pwd_count = 0

        for password in self.passwords:
            if password.isalpha():
                alpha_pwd += 1
            elif password.isnumeric():
                numeric_pwd += 1
            elif re.match("[^A-Za-z0-9]", password):
                special_char_pwd += 1
            else:
                mixed_pwd_count += 1

        return {
            "alpha_pwd": alpha_pwd,
            "numeric_pwd": numeric_pwd,
            "special_char_pwd": special_char_pwd,
            "mixed_pwd_count": mixed_pwd_count,
        }
