#!/bin/bash

pkg update && pkg upgrade -y
pkg install cmake -y
pkg install make clang -y
pkg install git -y
pkg install python -y
pkg install python-pip -y
pip install --upgrade pip setuptools
pip install numpy
pip install patchelf
pip install ninja

# Instalación de las librerías adicionales
pip install os
pip install phonenumbers
pip install opencage
pip install folium
pip install webbrowser
pip install requests
pip install json
pip install python-whois
pip install socket
pip install discordwebhook
pip install public-ip