# Transformation

## Overview
Category : Reverse Engineering

Points : 50

## Description

Your mission is to enter Dr. Evil's laboratory and retrieve the blueprints for his Doomsday Project. The laboratory is protected by a series of locked vault doors. Each door is controlled by a computer and requires a password to open. Unfortunately, our undercover agents have not been able to obtain the secret passwords for the vault doors, but one of our junior agents obtained the source code for each vault's computer! You will need to read the source code for each level to figure out what the password is for that vault door. As a warmup, we have created a replica vault in our training facility. The source code for the training vault is here: [VaultDoorTraining.java](https://jupiter.challenges.picoctf.org/static/1afdf83322ee9c0040f8e3a3c047e18b/VaultDoorTraining.java)

## Hints

1.The password is revealed in the program's source code.

## Approach
User input is compared with "w4rm1ng_Up_w1tH_jAv4_eec0716b713" in the checkPassword function. So this is most likely the flag. 
Oh yeah it work !!

## Flag

> picoCTF{w4rm1ng_Up_w1tH_jAv4_eec0716b713}