#Import modules

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys, os, shutil

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        #Remove output folder if it already exists
        if os.path.exists("output"):
            shutil.rmtree("output")
        
        if not os.path.exists("output"):
            os.makedirs("output")
            os.makedirs("output/platform")
            os.makedirs("output/platform/scripts")
            os.makedirs("output/platform/scripts/weapons")

        

        self.setWindowTitle("R5 Reloaded | Weapon Maker")
        self.setGeometry(100, 100, 800, 600)

        # Create a QTabWidget
        tab_widget = QTabWidget(self)
        self.setCentralWidget(tab_widget)

        # Create the first tab (Home)
        homeTab = QWidget()
        tab_widget.addTab(homeTab, "Home")
        homeLayout = QVBoxLayout()
        homeTab.setLayout(homeLayout)

        # Create the second tab (Make New Weapon)
        weaponTab = QWidget()
        tab_widget.addTab(weaponTab, "Make New Weapon")
        weaponLayout = QVBoxLayout()
        weaponTab.setLayout(weaponLayout)
        
        # Create the third tab (Browse Sounds)
        soundsTab = QWidget()
        tab_widget.addTab(soundsTab, "Browse Sounds")
        soundsLayout = QVBoxLayout()
        soundsTab.setLayout(soundsLayout)


        # Add a label with a description to the Home tab
        description = QLabel("R5 Reloaded | Weapon Maker is a tool for making new weapons. It allows you to easily create new weapons, easily find weapon models, easily add sounds to your weapon and more!")
        description.setWordWrap(True)  # Enable text wrapping for long descriptions
        description.setStyleSheet("font-size: 22px; margin: 20px;")
        

        # Add an image to the Home tab (you can replace 'your_image_path' with your image file)
        image_label = QLabel()
        pixmap = QPixmap("icon.png")
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        homeLayout.addWidget(image_label)
        homeLayout.addWidget(description)
        
        # Add weaponNameLabel to the Make New Weapon tab
        weaponNameLabel = QLabel("Weapon Name:")
        weaponLayout.addWidget(weaponNameLabel)
        
        
        # Add weaponNameLine to the Make New Weapon tab
        global weaponNameLine
        weaponNameLine = QLineEdit()
        weaponLayout.addWidget(weaponNameLine)
        
        # Add weaponDescriptionLabel to the Make New Weapon tab
        weaponDescriptionLabel = QLabel("Weapon Description:")
        weaponLayout.addWidget(weaponDescriptionLabel)
        
        # Add weaponDescriptionLine to the Make New Weapon tab
        global weaponDescriptionLine 
        weaponDescriptionLine = QLineEdit()
        weaponLayout.addWidget(weaponDescriptionLine)
        
        # Add weaponCategoryLabel to the Make New Weapon tab
        weaponCategoryLabel = QLabel("Weapon Category:")
        weaponLayout.addWidget(weaponCategoryLabel)
        
        # Create weaponCategory list
        global weaponCategoryList
        weaponCategoryList = QListWidget()
        weaponCategoryList.addItems(["RIFLE"])
        weaponLayout.addWidget(weaponCategoryLabel)
        weaponLayout.addWidget(weaponCategoryList)
        
        # Add ammoCategoryLabel to the Make New Weapon tab
        ammoCategoryLabel = QLabel("Ammo Category:")
        weaponLayout.addWidget(ammoCategoryLabel)
        
        # Create ammoCategory list
        global ammoCategoryList
        ammoCategoryList = QListWidget()
        ammoCategoryList.addItems(["HEAVY", "LIGHT", "ENERGY"])
        weaponLayout.addWidget(ammoCategoryList)
        
        
        
        
        
        
        # Create a tool bar that allows the user to select folder directory
        toolBar = QToolBar()
        toolBar.setMovable(False)
        toolBar.setFloatable(False)
        toolBar.setOrientation(Qt.Orientation.Horizontal)
        toolBar.setContentsMargins(0, 0, 0, 0)
        self.addToolBar(toolBar)
        
        # Add a button to the tool bar that allows the user to select folder directory
        toolBarButton = QToolButton()
        toolBarButton.setText("Select Folder")
        toolBarButton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon) # Set the button style
        toolBarButton.setArrowType(Qt.ArrowType.RightArrow) # Set the arrow type
        toolBarButton.clicked.connect(self.selectFolder)
        toolBar.addWidget(toolBarButton)
        

        #Add a label for damageNearLabel
        damageNearLabel = QLabel("Damage Near:")
        weaponLayout.addWidget(damageNearLabel)
        
        # Add damageNearLine to the Make New Weapon tab
        global damageNearLine, damageNear
        damageNearLine = QLineEdit()
        weaponLayout.addWidget(damageNearLine)
        
        
        # Add damageFarLabel to the Make New Weapon tab
        damageFarLabel = QLabel("Damage Far:")
        weaponLayout.addWidget(damageFarLabel)
        
        # Add damageFarLine to the Make New Weapon tab
        global damageFarLine, damageFar
        damageFarLine = QLineEdit()
        weaponLayout.addWidget(damageFarLine)
        
        # Add a label for fireRateLabel
        fireRateLabel = QLabel("Fire Rate:")
        weaponLayout.addWidget(fireRateLabel)
        
        # Add fireRateLine to the Make New Weapon tab
        global fireRateLine, fireRate
        fireRateLine = QLineEdit()
        weaponLayout.addWidget(fireRateLine)
        
        
        # Add a label for reloadTimeLabel
        reloadTimeLabel = QLabel("Reload Time:")
        weaponLayout.addWidget(reloadTimeLabel)
        
        # Add reloadTimeLine to the Make New Weapon tab
        global reloadTimeLine, reloadTime
        reloadTimeLine = QLineEdit()
        weaponLayout.addWidget(reloadTimeLine)
        
        
        # Add a label for ammoClipLabel
        ammoClipLabel = QLabel("Ammo Clip:")
        weaponLayout.addWidget(ammoClipLabel)
        
        # Add ammoClipLine to the Make New Weapon tab
        global ammoClipLine, ammoClip
        ammoClipLine = QLineEdit()
        weaponLayout.addWidget(ammoClipLine)
        

        # Create a label for burstClipLabel
        burstClipLabel = QLabel("Fire/Burst Count | Leave at one for full auto:")
        weaponLayout.addWidget(burstClipLabel)
        
        # Create a line edit for burstClipList
        global burstClipList, burstClipAmount
        burstClipList = QLineEdit()
        weaponLayout.addWidget(burstClipList)
    
        
        
        # Add a button to the tool bar that allows the user to generate a weapon
        toolBarButton = QToolButton()
        
        
        # Start generation in background
        generateButton = QPushButton("Generate Weapon")
        generateButton.clicked.connect(self.generateWeapon)
        weaponLayout.addWidget(generateButton)
        
    def selectFolder(self):
        # Get the selected folder directory
        global folderDirectory
        folderDirectory = QFileDialog.getExistingDirectory(self, "Select Folder Directory")
        #Output the selected folder directory to config.txt
        f = open("config.txt", "w")
        f.write(folderDirectory)
        f.close()
        

        
        
        

    def generateWeapon(self):
        
        # Check if all fields are filled in
        if weaponNameLine.text() == "" or weaponDescriptionLine.text() == "" or weaponCategoryList.currentItem().text() == "" or ammoCategoryList.currentItem().text() == "" or damageNearLine.text() == "" or damageFarLine.text() == "" or ammoClipLine.text() == "" or fireRateLine.text() == "" or reloadTimeLine.text() == "" or burstClipList.text() == "":
            QMessageBox.warning(self, "Error", "Please fill in all fields!")
            return
        
        # Check if damage near, damage far, ammo clip, fire rate, reload time, and burst clip fields are filled in as numbers
        try:
            damageNear = int(damageNearLine.text())
            damageFar = int(damageFarLine.text())
            ammoClip = int(ammoClipLine.text())
            fireRate = int(fireRateLine.text())
            reloadTime = int(reloadTimeLine.text())
            burstClipAmount = int(burstClipList.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "You have a letter in a field that only allows numbers!")
            return

        
        #Replace spaces with underscores
        weaponNameLine.setText(weaponNameLine.text().replace(" ", "_"))
        weaponDescriptionLine.setText(weaponDescriptionLine.text().replace(" ", "_"))
        
        #Send weapon info to generateWeapon.py
        weaponName = weaponNameLine.text()
        weaponDescription = str(weaponDescriptionLine.text())
        weaponCategory = weaponCategoryList.currentItem().text()
        ammoCategory = ammoCategoryList.currentItem().text()
        
        #Create values
        damageNear = damageNearLine.text()
        damageFar = damageFarLine.text()
        ammoClip = ammoClipLine.text()
        fireRate = fireRateLine.text()
        reloadTime = reloadTimeLine.text()
        burstClipAmount = burstClipList.text()

        
        #Send weapon info to generateWeapon.py
        os.system("python generateWeapon.py " + weaponName + " " + weaponDescription + " " + weaponCategory + " " + ammoCategory + " " + folderDirectory + " " + damageNear + " " + damageFar + " " + ammoClip + " " + fireRate + " " + reloadTime + " " + burstClipAmount)
        
       # os.system("python generateWeapon.py " + weaponName + " " + weaponDescription + " " + weaponCategory + " " + ammoCategory + " " + folderDirectory)
        

        
    

def main():
    #Check if config file exists
    if os.path.isfile("config.txt"):
        #Assign folderDirectory from config file
        global folderDirectory
        folderDirectory = open("config.txt", "r").read()

    
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
