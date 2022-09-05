#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 16:45:19 2022

@author: juan
"""

"""
Enunciado: Crea un programa que calcule el daño de un ataque durante una batalla Pokémon.
- La fórmula será la siguiente: daño = 50 * (ataque/defensa) * efectividad
- Efectividad x2, x1, x0.5
- Tipos: Agua, Fuego, Planta, Eléctrico
- El programa recibe los siguientes parámetros
    - Tipo del pokemon atacante
    - Tipo del pokemon defensor
    - Ataque: 1-100
    - Defensa: 1-100
"""

types = ("water", "fire", "grass", "electric")
type_chart = { 
    types[0] : { types[0]: 1,   types[1]: 2,   types[2]: 0.5, types[3]: 1   },
    types[1] : { types[0]: 0.5, types[1]: 0.5, types[2]: 2,   types[3]: 1   },
    types[2] : { types[0]: 2,   types[1]: 0.5, types[2]: 0.5, types[3]: 1   },
    types[3] : { types[0]: 2,   types[1]: 1,   types[2]: 0.5, types[3]: 0.5 }
    }


def CalculateDamage(a_type, d_type, attack, defense):
    return 50 * (attack / defense) * type_chart[a_type][d_type]


a_type = input("Attacker type: ").lower()
d_type = input("Defender type: ").lower()
attack = int(input("Attack power: "))
defense = int(input("Defense power: "))


print(CalculateDamage(a_type, d_type, attack, defense))
    
    