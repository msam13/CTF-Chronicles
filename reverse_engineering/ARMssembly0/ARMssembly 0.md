# Transformation

## Overview
Category : Reverse Engineering

Points : 40

## Description

What integer does this program print with arguments 4134207980 and 950176538? File: [chall.S](https://mercury.picoctf.net/static/da36e19990a2cede1dff10f9f33fe4b4/chall.S) Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})

## Hints

Simple compare

## Approach
Assembly file is a mislead. 
Hex(4134207980) = F66B01EC
that's the FLAG!!!

## Flag

> picoCTF{F66B01EC}