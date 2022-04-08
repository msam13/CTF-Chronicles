# Transformation

## Overview
Category : Reverse Engineering

Points : 50

## Description

There is something on my shop network running at nc mercury.picoctf.net 16524, but I can't tell what it is. Can you?

## Hints

1.What language does a CNC machine use?

## Approach
CNC uses G-code. There are many G-code viewers. I used [cnc- NCviewer](https://ncviewer.com/). 
 
 >nc mercury.picoctf.net 16524 | cat > cnc

upload cnc file to the website.

## Flag

> picoCTF{num3r1cal_c0ntr0l_1395ffad}
