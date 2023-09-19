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

devfile = f"{folderDirectory}/platform/scripts/vscripts/ai/sh_dev_npc_settings.gnut"
mapSpawn = f"{folderDirectory}/platform/scripts/vscripts/_mapspawn.gnut"

    
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
                    
                    dest.write(line)

            print(f"File types/mp_weapon_rifle.txt copied and modified to '{output_file}' successfully.")
            generateMapSpawn()
            generateDevFile()
        except FileNotFoundError:
            print(f"Error: File rifle.txt not found.")

def generateMapSpawn():
    mapSpawnStr = f'PrecacheWeapon( $"mp_weapon_{weaponName}" )'
    #Copy mapSpawn file to /output/_mapspawn.gnut and store mapSpawnStr in it
    with open(mapSpawn, 'r') as src, open("output/platform/scripts/vscripts/_mapspawn.gnut", 'w') as f:
        #Use for loop to get line number
        lineNum = 0
        for line in src:
            lineNum += 1
            if lineNum == 285:
                f.write("\n    " + mapSpawnStr + "\n")
            else:
                f.write(line)
    
def generateDevFile():
    devfileStr = f'SetupDevCommand( "{weaponCategory}: {weaponName}", "give mp_weapon_{weaponName}" )'
    
    #Copy mapSpawn file to /output/_mapspawn.gnut and store mapSpawnStr in it
    with open(devfile, 'r') as src, open("output/platform/scripts/vscripts/ai/sh_dev_npc_settings.gnut", 'w') as f:
        #Use for loop to get line number
        lineNum = 0
        for line in src:
            lineNum += 1
            if(weaponCategory == "RIFLE"):
                if lineNum == 59:
                    f.write("\n    " + devfileStr + "\n")
                else:
                    f.write(line)
    
    
generate()