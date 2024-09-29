import os
import phonenumbers
import opencage
import folium
import webbrowser
from phonenumbers import geocoder
import requests
import json
import whois
import socket
from discordwebhook import Discord
import public_ip as ip



print("Select your OS (Windows - Linux/Termux)")
print("1.- Windows")
print("2.- Linux/Termux")
print("\n")
operating_system = input("$ ")
if operating_system == "2":
    print
elif operating_system == "1":
    print
else:
    print("Pick a number please..")
    quit()
    


print("do you wanna set a target before starting? if yes enter username here")
print("Enter the command !info to know more about targets.")
print("\n")
target = input("$ ")
if target == '!info':
    print("-" * 50)
    print("     " + "Info about targets")
    print("-" * 50)
    print("targets helps you to get info about more specific persons and complete the dox quickly")
    print("Typing a target will set all tools in target mode, making investigations faster.")
    print("you can also use !target.snipe to make a full search about your target and make the dox faster")
    print("some tools maybe will not set in target mode")
    quit()


if operating_system == '1':
    os.system("color 0a")
title2 = r"""
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                            ............                                            
            .-=:.                          :#%#++===+**##*+=-.                                      
           :*#-=#%*-.                     -*:..         ....-*#-.                                   
          .+*:. ..:+#%%#+.               :+:.                ..=#+:                                 
          :*+.      ...::+*.            .+-.                   ..=#-.                               
          .:+#*-.        .-#:          .=+:                      .=#=.                              
             ..-=++:.      :#=.        -*-.                 .::.  .=#-.                             
                 :#-.      .:#+.      .**:  .+=..           -%%*-. .+#:.                  -*#=.     
                 :*:.       ..++=-----+#=..=#:-+=:         .+*:-**-..*+.                 .+#*#=.    
                 -+:              ...:+%*:.++:. :++=-::. .-#*:  .+*: -#=++*****++==---==+##=.=%=.   
                 -=.                  :#+. .:+*=-::-*%#: .-#%#***#*:  +#-..::::......::-:..  .+%:.  
                 -=:                  :#+.     :+###*-.     ..:::..   .#=.                    :#+.  
                 .+=.                 :#+.        .......:::::::::----.+#..                   .##.  
                 .++.                 :#=.  ...:+#%%%%#**++=-----++====:%-.                    *%.  
                 =#:.                 -*= .=%%*+#+=%#.           .*-.=%:*+.             .::.  .##.  
                 .-+***#%:            -*- --.....:-:.             .+##-.+*.      .:*%*:.+*=+##*%-.  
                       .*%:           =*:                          .... -%.    .=+#+.:+##-...:-:.   
                        .=%*:.       .++.                               -%:   .=#::.  ....          
                          :+*###***=.:*+.                               :%-   .#-                   
                                 .-#*#%+.                               .%-  .:%-                   
                                  .:==*+.                               .%-  .-%-                   
                                     :*+.                               .%-  :%*.                   
                                     :*+:                                #:  *%.                    
                                     :*+:                               .*=+#%*                     
                                     :*+.                                -%*-:.                      
                                     :*+.                                *:                         
                                     -#=.                                *-                         
                                    .+*:                 ....   .+%*-.  .%-                         
                                   .=*-:--..  :-..  ..:+#*==*: .++:.:+##+%-                         
                                   .-==--*+-**+#+-**+-:..  .-+-==.    .:--.                         
                                         :--.. .-:..        .:+-.                                   
                                                                                                    
                                                                                                    
"""

title = r"""

__________.__                 __     ________.__                    __      ____/\__
\______   \  | _____    ____ |  | __/  _____/|  |__   ____  _______/  |_   /   / /_/
 |    |  _/  | \__  \ _/ ___\|  |/ /   \  ___|  |  \ /  _ \/  ___/\   __\  \__/ / \ 
 |    |   \  |__/ __ \\  \___|    <\    \_\  \   Y  (  <_> )___ \  |  |    / / /   \
 |______  /____(____  /\___  >__|_ \\______  /___|  /\____/____  > |__|   /_/ /__  /
        \/          \/     \/     \/       \/     \/           \/           \/   \/ 

"""
print(title2)
print(title)
print('Welcome to black ghost! this is a doxing toolkit')
if target:
    print("[+] target : " + target )


    
else:
    print("[!] no target")

print("[+] Your IP:" + " " + ip.get())
operating_system_name = operating_system
if operating_system_name == '1':
    print("[+] OS: Windows")
elif operating_system_name == '2':
    print("[+] OS: Linux/Termux")


print("-" * 100)
print("1.- Phone number info gathering")
print("2.- mail info gathering")
print("3.- username search")
print("4.- IP Address information")
print("5.- general OSINT")
print("6.- whitepages")
print("7.- hide URLs")
print("8.- Phishing tools")
print("9.- IP loggers")
print("10.- metadata or image OSINT")
print("11.- Disaposable")
print("12.- fake id")
print("13.- google dorking")
print("14.- social media information gathering.")
print("15.- geolocation OSINT")
print("16.- data breaches")
print("17.- reverse shell generator")
print("18.- WHOIS")
print("\n")
print("99.- version")
print("88.- Suggestions and Bugs")
print("00.- exit")
print("\n")
print("----------(commands)----------")
print("1.- !dox.builder")
print("2.- !target.snipe (coming soon)")
print("\n")
selection = input("--------(-💀-)[GhostDox]/[Select an option] $ ")
print("\n")


if selection == '1':
    print("\n")
    print("-----------(NumTrack)-----------")
    print("\n")
    target_number = input("--------(-💀-)[GhostDox]/[Enter Target Phone number] $ ")
    print("[+] Gathering info, plase wait.. ")
    pepnumber = phonenumbers.parse(target_number)
    location = geocoder.description_for_number(pepnumber, "en")
    print(location)

    from phonenumbers import carrier
    service_pro = phonenumbers.parse(target_number)
    print(carrier.name_for_number(service_pro, "en"))

    from opencage.geocoder import OpenCageGeocode

    key = 'enter_your_key_here'
    geocoder = OpenCageGeocode(key)
    query = str(location)
    results = geocoder.geocode(query)

    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']

    print(lat, lng)

    myMap = folium.Map(location=[lat, lng], zoom_start= 9)
    folium.Marker([lat, lng], popup=location).add_to(myMap)

    myMap.save("tracked.html")
    print("-" * 50)
    totalinfo_phone_sel = input("--------(-💀-)[GhostDox]/[Type Yes if you wanna get more info about the phonenumber] $ ")
    if totalinfo_phone_sel == 'yes':
        print("-" * 50)
        print(results)
        quit()
    else:
        print("Invalid option, QUITTING!")
        quit()
elif selection == '2':
    print("----------------(Mail OSINT)----------------")
    print("1.- Email Address headers")
    print("2.- Epieos")
    print("3.- exposed.lol")
    print("4.- osint industries")
    print("5.- hunter")
    print("6.- intelx")
    print("7.- infotracer.com")
    print("8.- holehe")
    print("9.- sherlockeye")
    print("10- infoga")
    mail_osint_selection = input("--------(-💀-)[GhostDox]/[select an option] $ ")
    if mail_osint_selection == '1':
        webbrowser.open("https://it.umn.edu/services-technologies/how-tos/gmail-view-email-headers/")
        quit()
    elif mail_osint_selection == '2':
        webbrowser.open("https://epieos.com/")
        quit()
    elif mail_osint_selection == '3':
        webbrowser.open("https://exposed.lol/")
        quit()
    elif mail_osint_selection == '4':
        webbrowser.open("https://osint.industries/")
        quit()
    elif mail_osint_selection == '5':
        webbrowser.open("https://hunter.io/")
        quit()
    elif mail_osint_selection == '6':
        webbrowser.open("https://intelx.io/")
        quit()
    elif mail_osint_selection == '7':
        webbrowser.open("https://infotracer.com/")
        quit()
    elif mail_osint_selection == '8':
        webbrowser.open("https://github.com/megadose/holehe/")
        quit()
    elif mail_osint_selection == '9':
        webbrowser.open("https://sherlockeye.io/")
        quit()
    elif mail_osint_selection == '10':
        webbrowser.open("https://github.com/robertswin/Infoga/")
        quit()
    else:
        print("Invalid option, QUITTING!")
        quit()

elif selection == '3':
    if target:
        print("Target:"  + target)
        print("TARGET MODE ON!!!")
        print("\n")
        print("[+] Scanning...")
        print("\n")
        print("Possible tiktok : https://www.tiktok.com/@" + target + "?lang=en")
        print("Possible instagram :  https://www.instagram.com/" + target + "/?hl=en" )
        print("Possible twitter : https://x.com/" + target)
        print("Possible facebook : https://facebook.com/" + target)
        print("Possible reddit : https://www.reddit.com/user/" + target)
        print("Possible snapchat : https://www.snapchat.com/add/" + target)
        print("Possible Youtube : https://www.youtube.com/" + target)
        print("Possible github : https://github.com/" + target)
        print("Possible pinterest : https://www.pinterest.com/" + target)
        print("Possible spotify : https://open.spotify.com/search/" + target)
        quit()
    else:
        print("--------(Username Search)--------")
    print("1.- use blackghost username search")
    print("2.- username search webpages")
    username_search_selection = input("--------(-💀-)[GhostDox]/[Type your selection] $ ")
    if username_search_selection == '1':
        username_to_scan = input("--------(-💀-)[GhostDox]/[Enter username to scan] $ ")
        print("\n")
        print("[+] Scanning...")
        print("\n")
        print("Possible tiktok : https://www.tiktok.com/@" + username_to_scan + "?lang=en")
        print("Possible instagram :  https://www.instagram.com/" + username_to_scan + "/?hl=en" )
        print("Possible twitter : https://x.com/" + username_to_scan)
        print("Possible facebook : https://facebook.com/" + username_to_scan)
        print("Possible reddit : https://www.reddit.com/user/" + username_to_scan)
        print("Possible snapchat : https://www.snapchat.com/add/" + username_to_scan)
        print("Possible Youtube : https://www.youtube.com/" + username_to_scan)
        print("Possible github : https://github.com/" + username_to_scan)
        print("Possible pinterest : https://www.pinterest.com/" + username_to_scan)
        print("Possible spotify : https://open.spotify.com/search/" + username_to_scan)

    elif username_search_selection == '2':
        webbrowser.open("https://github.com/CyberSecurity-root/usernamesearch")
        quit()
elif selection == '4':
    print("\n")
    print("-----------(IPTrack)-----------")
    print("\n")
    target_ip_to_track = input("--------(-💀-)[GhostDox]/[enter target ip address] $ ")
    response_ip_track = requests.get(f"http://ip-api.com/json/{target_ip_to_track}").content
    data_ip_track = json.loads(response_ip_track)
    print(data_ip_track)
elif selection == '5':
    print("\n")
    print("----------------(General OSINT)----------------")
    print("1.- osint framework")
    print("2.- osint industries")
    print("3.- awesome osint")
    print("4.- r/osint reddit")
    general_osint_selection = input("--------(-💀-)[GhostDox]/[select an option] $ ")
    if general_osint_selection == '1':
        webbrowser.open("https://osintframework.com/")
    elif general_osint_selection == '2':
        webbrowser.open("https://osint.industries")
    elif general_osint_selection == '3':
        webbrowser.open("https://github.com/jivoi/awesome-osint")
    elif general_osint_selection == '4':
        webbrowser.open("https://www.reddit.com/r/OSINT/")
    else:
        print("Invalid option, QUITTING!")
        quit()
elif selection == '6':
     webbrowser.open("https://github.com/CyberSecurity-root/whitepages/")
elif selection == '7':
    webbrowser.open("https://github.com/KIKILAK/URLghost/")
elif selection == '8':
    print("\n")
    print("----------------(phishing)----------------")
    print("1.- zphisher")
    print("2.- pyphisher")
    print("3.- blackeye")
    print("4.- phishingX")
    phishing_selection = input("--------(-💀-)[GhostDox]/[select an option] $ ")
    if phishing_selection == '1':
        webbrowser.open("https://github.com/htr-tech/zphisher")
        quit()
    elif phishing_selection == '2':
        webbrowser.open("https://github.com/sneakerhax/PyPhisher/")
        quit()
    elif phishing_selection == '3':
        webbrowser.open("https://github.com/8L4NK/blackeye/")
        quit()
    elif phishing_selection == '4':
        webbrowser.open("https://github.com/deadxfire/PhishingX")
        quit()
    else:
        print("Invalid option, QUITTING!")
        quit
elif selection == '9':
    print("\n")
    print("--------------------(IP loggers)--------------------")
    print("1.- iplogger")
    print("2.- grabify")
    iplogger_selection = input("--------(-💀-)[GhostDox]/[select an option] $ ")
    if iplogger_selection == '1':
        webbrowser.open("https://iplogger.org")
    elif iplogger_selection == '2':
        webbrowser.open("https://grabify.link")
    else:
        print("Invalid option, QUITTING!")
        quit()
elif selection == '10':
    print("---------------(metadata and images)---------------")
    print("1.- metadata")
    print("2.- general OSINT")
    image_osint_selec = input("--------(-💀-)[GhostDox]/[select an option] $ ")
    if image_osint_selec == '1':
        print("1.- jimpl.com")
        print("2.- exiftool")
        metadata_selection = input("--------(-💀-)[GhostDox]/[select an option] $ ")
        if metadata_selection == '1':
            webbrowser.open("https://jimpl.com/")
            quit
        elif metadata_selection == '2':
            webbrowser.open("https://exiftool.org/")
            quit()
        else:
            print("Invalid Selection, QUITTING!")
            quit()
    elif image_osint_selec == '2':
        print("1.- pimeye")
        print("2.- geospy")
        print("3.- creepy")
        general_osint_images = input("--------(-💀-)[GhostDox]/[select an option] $ ")
        if general_osint_images == '1':
            webbrowser.open("https://pimeyes.com/en")
        elif general_osint_images == '2':
            webbrowser.open("https://geospy.web.app/")
        elif general_osint_images == '3':
            webbrowser.open("https://www.geocreepy.com/")
        else:
            print("Invalid Option, QUITTING!")
            quit()
    else:
        print("Invalid option, QUITTING!")
        quit()



elif selection == '11':
    print("----------(disaposable)----------")
    print("1.- SquareX")
    print("2.- Anonymouse mails")
    disaposable = input("--------(-💀-)[GhostDox]/[select an option] $ ")
    if disaposable == '1':
        webbrowser.open("https://chromewebstore.google.com/detail/squarex-be-secure-anonymo/kapjaoifikajdcdehfdlmojlepfpkpoe?hl=en-US")
    elif disaposable == '2':
        webbrowser.open("https://anonymousemail.me/")
    else:
        print("Invalid option, QUITTING!")
        quit()
elif selection == '12':
    print("-------------(fake identity)---------------")
    print("1.- generate random identity")
    print("2.- this person does not exist")
    print("3.- test card numbers")
    selection12 = input("--------(-💀-)[GhostDox]/[select an option] $ ")
    if selection12 == '1':
        webbrowser.open("https://fakenamegenerator.com")
    elif selection12 == '2':
        webbrowser.open("https://thispersondoesnotexist.com")
    elif selection12 == '3':
        webbrowser.open("https://developers.bluesnap.com/reference/test-credit-cards")
    
    elif selection == '13':
         webbrowser.open("https://exploit-db.com/google-hacking-database/")
    quit()
elif selection == '14':
    print("\n")
    print("-------------------(social media information gathering)-------------------")
    

    print("\n")
    print("1.- SnapMap")
    print("2.- Facebook")
    print("3.- Instagram")
    print("4.- LinkedIn")
    print("5.- Twitter")
    print("6.- Pinterest")
    print("7.- Reddit")
    print("8.- Github")
    print("9.- Whatsapp")
    print("10.- Skype")
    print("11.- Discord")
    print("12.- Tiktok")

    smigs = input("--------(-💀-)[GhostDox]/[select an option] $ ")
    if smigs == '1':
        webbrowser.open("https://map.snapchat.com/")
        quit()
    elif smigs == '2':
        webbrowser.open("https://github.com/osintambition/Social-Media-OSINT-Tools-Collection?tab=readme-ov-file#Facebook--")
        quit()
    elif smigs == '3':
        webbrowser.open("https://github.com/osintambition/Social-Media-OSINT-Tools-Collection?tab=readme-ov-file#instagram--")
        quit()
    elif smigs == '4':
        webbrowser.open("https://github.com/osintambition/Social-Media-OSINT-Tools-Collection?tab=readme-ov-file#linkedin--")
        quit()
    elif smigs == '5':
        webbrowser.open("https://github.com/osintambition/Social-Media-OSINT-Tools-Collection?tab=readme-ov-file#twitter--")
        quit()
    elif smigs == '6':
        webbrowser.open("https://github.com/osintambition/Social-Media-OSINT-Tools-Collection?tab=readme-ov-file#pinterest")
        quit()
    elif smigs == '7':
        webbrowser.open("https://github.com/osintambition/Social-Media-OSINT-Tools-Collection?tab=readme-ov-file#reddit")
        quit()
    elif smigs == '8':
        webbrowser.open("https://github.com/osintambition/Social-Media-OSINT-Tools-Collection?tab=readme-ov-file#github")
        quit()
    elif smigs == '9':
        webbrowser.open("https://github.com/osintambition/Social-Media-OSINT-Tools-Collection?tab=readme-ov-file#Whatsapp")
        quit()
    elif smigs == '10':
        webbrowser.open("https://github.com/osintambition/Social-Media-OSINT-Tools-Collection?tab=readme-ov-file#Skype")
        quit()
    elif smigs == '11':
        webbrowser.open("https://github.com/osintambition/Social-Media-OSINT-Tools-Collection?tab=readme-ov-file#Discord")
        quit()
    elif smigs == '12':
        webbrowser.open("https://github.com/osintambition/Social-Media-OSINT-Tools-Collection?tab=readme-ov-file#TikTok")
        quit()

    else:
        print("Invalid option, QUITTING!")
        quit()
elif selection == '15':
    print("-------------(geoOSINT)-------------")
    webbrowser.open("geospy.web.app")
    webbrowser.open("whatismyipaddress.com")
    webbrowser.open("earth.google.com/web/")
    webbrowser.open("www.google.de/maps")
    webbrowser.open("jimpl.com")
    quit()
elif selection == '16':
    print("0.- BlackGhost Breach data search (coming soon)")
    print("1.- intelx.io")
    print("2.- have i been pwned?")
    print("3.- breach directory")


    breach_selection = input("--------(-💀-)[GhostDox]/[select an option] $ ")

    if breach_selection == '1':
        webbrowser.open("https://intelx.io/")
        quit()
    elif breach_selection == '2':
        webbrowser.open("https://haveibeenpwned.com/?os=vb.&ref=app/")
        quit()
    elif breach_selection == '3':
        webbrowser.open("https://breachdirectory.org/")
        quit()
    else:
        print("Invalid option, QUITTING!")
        quit()

elif selection == '17':
    webbrowser.open("https://revshells.com/")
    quit()
elif selection == '18':
    #totalinfo : print(res)
 print("----------(WHOIS)--------")
 print("\n")
 domain = input("Enter the domain to track : ")
 print("=" * 100)
 res = whois.whois(domain)

 print(socket.gethostbyname(domain))
 print(res.domain_name)
 print(res.registrar)
 print(res.creation_date)
 print(res.expiration_date)
 print(res.name_servers)
 print(res.status)
 print(res.emails)
 print(res.dnssec)
 print(res.name)
 print(res.org)
 print(res.address)
 print(res.city)
 print(res.state)
 print(res.registrant_postal_code)
 print(res.country)

 total_info_ = input("type yes if you wanna get extra info $ ")
 if total_info_ == 'yes':
     print(res)
 if total_info_ == 'no':
     print("Exiting...")
     quit()
 else:
     print("Invalid option, QUITTING!")
     quit()
elif selection == '99':
    print("\n")
    print("-" * 10)
    print("V 1.0.0")
    print("-" * 10)
elif selection == '88':
    url_webhook = Discord(url="https://discord.com/api/webhooks/1289790116704944180/0-b_OeARZYfH0c1w41FXALs0uNWFmrlKpOww9x9zMlY8L4-YsFOQoNPkd77ZOiInpZvS")
    print("\n")
    suggest = input("--------(-🌐-)[what do you want to tell us? (bugs, d0xing methods, OSINT tools, suggestions, etc) :b ] : ")
    url_webhook.post(content=suggest)
elif selection == '00':
    print("[+] Exiting the program...")
    quit()
elif selection == '!target.snipe':
    print
elif selection == '!dox.builder':
    print("----------(Dox Builder)----------")
    print("\n")
    main_us = input("Main Username $ ")
    razon = input("--------(-📧-)[Builder]/[dox reason] $ ")
    nombre = input("--------(-📧-)[Builder]/[full name] $ ")
    usernames =  input("--------(-📧-)[Builder]/[usernames] $ ")
    ip = input("--------(-📧-)[Builder]/[all ip addresses] $ ")
    school = input("--------(-📧-)[Builder]/[school] $ ")
    friends = input("--------(-📧-)[Builder]/[friends info] $ ")
    face_photo = input("--------(-📧-)[Builder]/[face photos URLs] $ ")
    house_photo = input("--------(-📧-)[Builder]/[house photos URLs] $ ")
    red = input("--------(-📧-)[Builder]/[network info] $ ")
    user_agent = input("--------(-📧-)[Builder]/[user agent] $ ")
    system = input("--------(-📧-)[Builder]/[operating system] : ")
    device_model = input("--------(-📧-)[Builder]/[model] $ ")
    edad = input("--------(-📧-)[Builder]/[age] $ ")
    redes_publicas = input("--------(-📧-)[Builder]/[public social media] $ ")
    redes_privadas =  input("--------(-📧-)[Builder]/[private social media] $ ")
    family = input("--------(-📧-)[Builder]/[family members] $ ")
    pais =  input("--------(-📧-)[Builder]/[country] $ ")
    ciudad = input("--------(-📧-)[Builder]/[city] $ ")
    documentos_privados = input("--------(-📧-)[Builder]/[private documents URLs] $ ")
    fecha_nacimiento = input("--------(-📧-)[Builder]/[birth] $ ")
    correos = input("--------(-📧-)[Builder]/[Mail Addresses] $ ")
    numero_telefonico = input("--------(-📧-)[Builder]/[Phone numbers] $ ")
    direccion = input("--------(-📧-)[Builder]/[full address] $ ")
    extra = input("--------(-📧-)[Builder]/[extra information] $ ")
    print("\n")
    print("----------------------------------")
    print("       " + "Doxed " + main_us)
    print("----------------------------------")
    print("reason: " + razon)
    print("-" * 50)
    print("Name : " + nombre)
    print("usernames : " + usernames)
    print("IP Addresses : " + ip)
    print("school : " + school)
    print("friends : " + friends)
    print("Face photo URLs : " + face_photo)
    print("house photos : " + house_photo)
    print("Network info : " + red)
    print("User agent : " + user_agent)
    print("OS : " + system)
    print("device model : " + device_model)
    print("Age : " + edad)
    print("Public social media : " + redes_publicas)
    print("Private Social media : " + redes_privadas)
    print("Family members : " + family)
    print("Country : " + pais)
    print("City : " + ciudad)
    print("Private Docs : " + documentos_privados)
    print("Birth : " + fecha_nacimiento)
    print("Mail Addresses : " + correos)
    print("Phone numbers : " + numero_telefonico)
    print("Full Address : " + direccion)
    print("Extra information : " + extra)
    print("-" * 50)
else:
    print("Invalid option, QUITTING!")
    quit()
