#Import
import os
import sys

#Get directory of script

scriptDir = os.path.dirname(os.path.realpath(__file__))
scriptDir = scriptDir.replace("\\","/")






#Recieve info from drawUI.py
print(sys.argv)
weaponName = sys.argv[1]
weaponName = weaponName.lower()
weaponDescription = sys.argv[2]
weaponCategory = sys.argv[3]
ammoCategory = sys.argv[4]
folderDirectory = sys.argv[5]
damageNear = sys.argv[6]
damageFar = sys.argv[7]
ammoClip = sys.argv[8]
fireRate = sys.argv[9]
reloadTime = sys.argv[10]
burstClipAmount = 1

playlistFile = f"{folderDirectory}/platform/playlists_r5_patch.txt"


    
if ammoCategory == "HEAVY":
    ammoType = "highcal"
    
if ammoCategory == "LIGHT":
    ammoType = "bullet"
    
if ammoCategory == "ENERGY":
    ammoType = "special"


#Create strings
weaponNameStr =      f'	   "printname"   									"{weaponName}"'
weaponNameStrShort = f'	   "shortprintname"   									"{weaponName}"'
weaponDescStr =      f'    "description"   								"{weaponDescription}"'
weaponDescLongStr =  f'    "longdesc"										"{weaponDescription}"'
ammoCategoryStr =    f'    "ammo_pool_type"								"{ammoType}"'
damageNearStr =      f'    "damage_near_value"   							"{damageNear}"'
damageFarStr =       f'    "damage_far_value"   							"{damageFar}"'
ammoClipStr =        f'    "ammo_clip_size"   								"{ammoClip}"'
if(int(burstClipAmount) > 1):
    burstAmountStr = str(f'    "burst_fire_count"								"{burstClipAmount}"\n   "burst_fire_delay"								"0.32"')
else:
    burstAmountStr = ""
fireRateStr =        f'    "fire_rate"   									"{fireRate}"'


#Create the function that finds the type of weapon and matches it to its type in types/

def generate():
    if(weaponCategory == "RIFLE"):
        output_file = f"output/platform/scripts/weapons/mp_weapon_{weaponName}.txt"
        try:
            print("Trying to copy file types/mp_weapon_rifle.txt to output/mp_")
            # Copy the source file to the output file
            with open(f"{scriptDir}/class/rifle.txt", 'r') as src, open(output_file, 'w') as dest:
                for line in src:
                    # Replace "replace{num}" with the info
                    line = line.replace("replace1", weaponNameStr)
                    line = line.replace("replace2", weaponNameStrShort)
                    line = line.replace("replace3", weaponDescStr)
                    line = line.replace("replace4", weaponDescLongStr)
                    line = line.replace("replace5", ammoCategoryStr)
                    line = line.replace("replace6", damageNearStr)
                    line = line.replace("replace7", damageFarStr)
                    line = line.replace("replace8", ammoClipStr)
                    line = line.replace("replace9", fireRateStr)
                    line = line.replace("replaceme1", burstAmountStr)
                    
                    
                    dest.write(line)

            print(f"File types/mp_weapon_rifle.txt copied and modified to '{output_file}' successfully.")
            generatePlaylist()
        except FileNotFoundError:
            print(f"Error: File rifle.txt not found.")

def generatePlaylist():
     global playlistStr, playlistStr2
     #Make generatedWeapons.txt
     with open("generatedWeapons.txt", 'a') as f:
        with open("generatedWeapons.txt", 'r') as f:
            global generatedWeapons
            generatedWeapons = f.read().strip()

     print(generatedWeapons)
     
     playlistStr = f'custom_weapon_list "mp_weapon_volt_smg mp_weapon_sentinel' + " " + generatedWeapons + f" mp_weapon_{weaponName}" + '"'

     #Store generated weapon in generatedWeapons.txt but don't overwrite 
     if os.path.isfile("generatedWeapons.txt"):
        with open("generatedWeapons.txt", 'a') as f:
            f.write(f"mp_weapon_{weaponName} ")


     #Store weapon category in _mapspawn.gnut
     if weaponCategory == "RIFLE":
         weaponCategoryMain = "assault"
     playlistStr2 = f'mp_weapon_{weaponName}_class                     "{weaponCategoryMain}"'

    #Copy mapSpawn file to /output/_mapspawn.gnut and store mapSpawnStr in it
     with open(playlistFile, 'r') as src, open("output/platform/playlists_r5_patch.txt", 'w') as f:
        print("Opened Playlist File")
        #Use for loop to get line number
        lineNum = 0
        for line in src:
            lineNum += 1
            if lineNum == 68:
                #Delete line
                
                f.write("\n                " + playlistStr + "\n")
                f.write("\n                " + playlistStr2)
            else:
                f.write(line)
    
    
    
generate()