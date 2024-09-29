# On-Screen Keyboard for Ubuntu ARM RPI 5 64 Bit

### Created By: J~Net 2024

## Overview

This project provides an on-screen keyboard specifically designed for Ubuntu ARM architecture on the Raspberry Pi 5. It features a user-friendly interface that allows for easy text input without the need for a physical keyboard. Additionally, it includes an upgraded version of `gnome-screenshot`, which removes the annoying flash that occurs during screenshots.

## Features

- **On-Screen Keyboard**: Easy-to-use interface for typing.
- **Caps Lock Toggle**: Toggle between uppercase and lowercase letters.
- **Copy to Clipboard**: Quickly copy text from the on-screen keyboard to the clipboard.
- **Emoji Support**: Easily insert emojis with dedicated buttons.
- **Number and Symbol Support**: Access numbers and various symbols with tabs.
- **Upgraded gnome-screenshot**: A screenshot tool without the annoying flash effect.

## Installation

1. **Copy Binaries**: 
   To install the on-screen keyboard and the upgraded `gnome-screenshot`, copy all files to the `/usr/bin/` directory.

   ```bash
   cp *.* /usr/bin/

gcc `pkg-config --cflags gtk+-3.0` -o onscreen_keyboard onscreen_keyboard.c `pkg-config --libs gtk+-3.0`

sudo chmod +x ./onscreen_keyboard

cp ./onscreen_keyboard ~/.local/bin/

cp ./onscreen_keyboard ~/.local/bin/osk
cp ./onscreen_keyboard ~/.local/bin/om-screen-keyboard

cp ./onscreen_keyboard /usr/bin/osk
cp ./onscreen_keyboard /usr/bin/on-screen-keyboard

x /usr/bin/osk
x /usr/bin/on-screen-keyboard


where x =

sudo chmod +x

