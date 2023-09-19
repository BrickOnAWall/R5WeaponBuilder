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
            os.makedirs("output/platform/scripts/vscripts")
            os.makedirs("output/platform/scripts/vscripts/ai")
        

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
        
        
        # Add a label for ammoClipLabel
        ammoClipLabel = QLabel("Ammo Clip:")
        weaponLayout.addWidget(ammoClipLabel)
        
        # Add ammoClipLine to the Make New Weapon tab
        global ammoClipLine, ammoClip
        ammoClipLine = QLineEdit()
        weaponLayout.addWidget(ammoClipLine)
        ammoClip = ammoClipLine.text()
        
        
        # Add a button to the tool bar that allows the user to generate a weapon
        toolBarButton = QToolButton()
        
        
        # Start generation in background
        generateButton = QPushButton("Generate Weapon")
        generateButton.clicked.connect(self.generateWeapon)
        weaponLayout.addWidget(generateButton)
        
    def selectFolder(self):
        # Get the selected folder directory
        folderDirectory = QFileDialog.getExistingDirectory(self, "Select Folder Directory")
        #Output the selected folder directory to config.txt
        f = open("config.txt", "w")
        f.write(folderDirectory)
        f.close()
        

        
        
        

    def generateWeapon(self):
        
        # Check if ammoclipline is number and no letters or space
        if ammoClipLine.text() == "" or ammoClipLine.text() == "":
            QMessageBox.warning(self, "Error", "Please fill in all fields!")
            return
        
        #Check if ammoclipline is number and no letters or space
        if not ammoClipLine.text().isdigit():
            QMessageBox.warning(self, "Error", "Ammo clip must be a number!")
            return
        
        #Check if ammoclipline is number and no letters or space
        if int(ammoClipLine.text()) < 0:
            QMessageBox.warning(self, "Error", "Ammo clip must be a positive number!")
            return
        
        #Check if ammoclipline contains letters or space
        if ammoClipLine.text().isalpha():
            QMessageBox.warning(self, "Error", "Ammo clip cannot contain letters!")
            return
        
        # Check if damages have number and no letters or space
        if damageNearLine.text() == "" or damageFarLine.text() == "":
            QMessageBox.warning(self, "Error", "Please fill in all fields!")
            return
        
        #Check if damages have number and no letters or space
        if not damageNearLine.text().isdigit() or not damageFarLine.text().isdigit():
            QMessageBox.warning(self, "Error", "Damages must be numbers!")
            return
        
        #Check if damages have number and no letters or space
        if int(damageNearLine.text()) < 0 or int(damageFarLine.text()) < 0:
            QMessageBox.warning(self, "Error", "Damages must be positive numbers!")
            return
        
        
        #Check if all fields are filled in
        if weaponNameLine.text() == "" or weaponDescriptionLine.text() == "" or weaponCategoryList.currentItem().text() == "" or ammoCategoryList.currentItem().text() == "":
            QMessageBox.warning(self, "Error", "Please fill in all fields!")
            return
        
        #Check if name is less than 3 characters but less than 12
        if len(weaponNameLine.text()) < 3 or len(weaponNameLine.text()) > 12:
            QMessageBox.warning(self, "Error", "Weapon name must be between 3 and 12 characters!")
            return
        
        #Check if description is less more than 3 characters but less than 12
        if len(weaponDescriptionLine.text()) < 3 or len(weaponDescriptionLine.text()) > 36:
            QMessageBox.warning(self, "Error", "Weapon description must be between 3 and 36 characters!")
            return
        
        #Check if folder directory is selected
        if folderDirectory == "":
            QMessageBox.warning(self, "Error", "Please select a folder directory!")
            return
        
        #Replace spaces with underscores
        weaponNameLine.setText(weaponNameLine.text().replace(" ", "_"))
        weaponDescriptionLine.setText(weaponDescriptionLine.text().replace(" ", "_"))
        
        #Send weapon info to generateWeapon.py
        weaponName = weaponNameLine.text()
        weaponDescription = str(weaponDescriptionLine.text())
        weaponCategory = weaponCategoryList.currentItem().text()
        ammoCategory = ammoCategoryList.currentItem().text()
        
        #Create dictionary to send to generateWeapon.py
        damageNear = damageNearLine.text()
        damageFar = damageFarLine.text()
        
        #Send weapon info to generateWeapon.py
        os.system("python generateWeapon.py " + weaponName + " " + weaponDescription + " " + weaponCategory + " " + ammoCategory + " " + folderDirectory + " " + damageNear + " " + damageFar)
        
       # os.system("python generateWeapon.py " + weaponName + " " + weaponDescription + " " + weaponCategory + " " + ammoCategory + " " + folderDirectory)
        

        
    

def main():
    #Check if config file exists
    if os.path.isfile("config.txt"):
        #Assign folderDirectory from config file
        global folderDirectory
        folderDirectory = open("config.txt", "r").read()
        print(folderDirectory)

    
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()