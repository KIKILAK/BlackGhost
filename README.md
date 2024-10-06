# BlackGhost 🌐👻🕵️‍♂️
# Introduction: 1.- What is BlackGhost / 2.- Installation / 3.- How to use / 4.- Updates

# What is it
Blackghost is a script made in python with the purpose of facilitating, teaching and raising awareness about doxing and OSINT investigations, providing various tools, techniques, and codes that will help you in your mission, BlackGhost is not designed to harm other people, it can be illegal and punishable by jail time doxing so keep it in mind and use it in controlled environments or to learn, Blackghost has 20+ varied options for every need, some commands and a suggestion system that are sent through a Discord webhook, the script will be updated if we consider adding any recommendations and ideas, bugs will be quickly fixed

# Installation 

Now let's see how to download this script from 3 operating systems

## Windows Installation
first, download Python and Visual Studio Code, you can do it here 👇

https://www.python.org/downloads/ https://code.visualstudio.com/

Now, setup both apps and download this repo in Desktop, then open visual studio and move BlackGhost into the app, install python extension on visual studio and run the setup.py script to install necesary requirements, you can do it with the play button that is Up to the right, Finally, you must get the API Key of the option to collect information from phone numbers here: https://opencagedata.com/api
![image](https://github.com/user-attachments/assets/538c1e67-a4dc-4ae4-8371-69fabae6ce54)
You need to sign up, it not takes a lot.

When you sign up you should be redirected to this site: https://opencagedata.com/dashboard, 
![image](https://github.com/user-attachments/assets/189a331d-3aae-47b9-8df4-6947e8c74132)

Go to the Geogcoding API button and there will be your key, copy it and go to visual studio to edit the BlackGhost.py file and go to line 165, there you must put your key and it should look like this: ![image](https://github.com/user-attachments/assets/65c49cde-4fc5-451c-82fe-1fcd18d95710)
Save the edited script with ctrl + s and is ready to run.
run it using visual studio terminal, you can do it with the play button that is Up to the right

## Linux Installation (tested on parrot)

    git clone https://github.com/KIKILAK/BlackGhost
    cd BlackGhost
    python3 setup.py

### set opencage api key for phonenumbers
here: https://opencagedata.com/api
sign up and copy the api key that is on https://opencagedata.com/dashboard
now, use nano and add your api key on line 165, save the file and run it with this command

    python3 BlackGhost.py
well done!

Extra:

    # Resolve the error EXTERNALLY-MANAGED
      sudo rm /usr/lib/python3.11/EXTERNALLY-MANAGED

## Termux Installation
