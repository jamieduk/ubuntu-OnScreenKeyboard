#!/bin/bash
# (c) J~Net 2026
#
# ./compile.sh
#
#
gcc `pkg-config --cflags gtk+-3.0` -o onscreen_keyboard onscreen_keyboard.c `pkg-config --libs gtk+-3.0` -lX11 -lXtst
