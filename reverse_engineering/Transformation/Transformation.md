# Transformation

## Overview
Category : Reverse Engineering

Points : 20

## Description

I wonder what this really is... enc ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

## Hints

You may find some decoders online

## Approach
Encrypted Text : 灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥ㄴㅡて㝽

Hexdump of the Text : 

└─$ hexdump enc   
0000000 81e7 e6a9 af8d 8de4 e494 bb99 84e3 e5b6
0000010 a2bd a5e6 e7b4 9f8d a5e6 e7ae b48d 8ce3
0000020 e6b4 9f91 bde6 e5a6 b8bc bde5 e3a5 b484
0000030 85e3 e3a1 a681 9de3 00bd               
0000039

I usually use Cyberchef for decoding unknown encryption, it has many different filters. Best suited filter in this case is "Decode text", it outputs the text decrypted for common encoding. UTF-16BE decrypt starts with picoCTO{.

## Flag

> picoCTF{16_bits_inst34d_of_8_e141a0f7}