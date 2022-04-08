import sys
import demo as dm
import hashingPassword as hp
from Connector import mydb
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.Qt import Qt
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

#SIMPLE USER
class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("login.ui", self)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccButton.clicked.connect(self.gotocreate)
        # connects the button with a function

    def loginfunction(self):
        username = self.username.text()
        password = self.password.text()
        # connect with database here
        global ROLE 
        cursor = mydb.cursor()# connect with database here
        exists = '''SELECT COUNT(*) FROM users WHERE Usersusername = %s'''
        cursor.execute(exists, (username, ))
        count = cursor.fetchone()

        if count[0] == 0:
            QMessageBox.about(self, "Error", "Username does not exist!")
        else:
            word = '''SELECT Userspwd FROM users WHERE Usersusername = %s''' #return from select is a tuple
            cursor.execute(word, (username, ))
            storedPass = cursor.fetchone()
            if hp.verify_password(storedPass[0], password):
                id = '''SELECT UsersId FROM users WHERE Usersusername = %s '''
                cursor.execute(id, (username, ))
                storedId = cursor.fetchone()
                global ID 
                ID = storedId[0]
                #print("Stored : ", storedId[0] , "tuple: ", storedId , "ID" , ID)
                #print(type(ID))
                role ='''SELECT role_id FROM user_roles WHERE user_id = %s '''
                cursor.execute(role, (ID,))
                storedRole = cursor.fetchone()
                
                ROLE = storedRole[0]
                #print(type(ROLE), ROLE)
                
                if ROLE == 0:
                    self.gotohomescreen()
                elif ROLE == 1:
                    self.gotoBusiness() 
            else:
                QMessageBox.about(self, "Error", "Wrong password! ")
                
    def gotocreate(self):
        createacc = CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentWidget(createacc)

    def gotohomescreen(self):
        #exec('HomeScreen.py')
        homescreen = HomeScreen()
        widget.addWidget(homescreen)
        widget.setCurrentWidget(homescreen)
        print("Successfully logged in")

    def gotoBusiness(self):
        businessHome = BusinessHome()
        widget.addWidget(businessHome)
        widget.setCurrentWidget(businessHome)


class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc, self).__init__()
        loadUi("Register.ui", self)
        self.signupbutton.clicked.connect(self.registration)
        self.gotologinButton.clicked.connect(self.gotologin)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.repeatpassword.setEchoMode(QtWidgets.QLineEdit.Password)

    # Checkboxes
        self.checkBox.stateChanged.connect(self.uncheck)
        self.checkBox2.stateChanged.connect(self.uncheck)

    def registration(self):
        username = self.username.text() #username from registration form
        email = self.email.text() #email from registration form
        password = self.password.text()
        repeatpassword = self.repeatpassword.text()

        cursor = mydb.cursor()# connect with database here
        exists = '''SELECT COUNT(*) FROM users WHERE Usersusername = %s OR Usersemail = %s'''
        cursor.execute(exists, (username, email))
        count = cursor.fetchone()

        print(type(count))
        print(count[0] == 1)
        print(count[0] == 0)

        if count[0] == 1:
            QMessageBox.about(self, "Error", "Username or email already exists")
        else:
            if dm.check_blank(username,email,password,repeatpassword) != True or (self.checkBox.isChecked() == False and self.checkBox2.isChecked() == False):
                QMessageBox.about(self, "Error", "Fill all the lines and Checkboxes")
            else:
                if password != repeatpassword:
                    QMessageBox.about(self, "Error", "Passwords don't match!")
                elif dm.checker(password) != True:
                    QMessageBox.about(self, "Error", "Password must contain at least 8 characters, one number, one capital and a special character.")
                elif dm.valemail(email) is not True:
                    QMessageBox.about(self, "Error", "Email doesn't exist or is not in the right structure!")
                else:  # Resize
                    password_hash = hp.hash_password(password)# utf-8
                    insert = '''INSERT INTO users(Usersusername, Usersemail, Userspwd) VALUES('{}', '{}', '{}')'''.format(username,email,password_hash)#alternative way of structing sql INSERT query
                    cursor.execute(insert) 
                    mydb.commit() #only for INSERT
                    
                    select = '''SELECT UsersId FROM users WHERE Usersusername = %s''' 
                    cursor.execute(select, (username,)) # username passes to %s as a string
                    result = cursor.fetchone() #user Id to result (tuple)

                    if self.checkBox.isChecked():
                        cursor.execute('''INSERT INTO user_roles(user_id, role_id) VALUES (%d, 0) ''' %result)
                        mydb.commit() #result is a tuple with one integer element and passes as a digit number with %d
                    elif self.checkBox2.isChecked():
                        cursor.execute('''INSERT INTO user_roles(user_id, role_id) VALUES (%d, 1) ''' %result)
                        mydb.commit()

                    self.gotologin()
                
    def uncheck(self, state): #Explaination
        if state == Qt.Checked:
            if self.sender() == self.checkBox:
                self.checkBox2.setChecked(False)
            elif self.sender() == self.checkBox2:
                self.checkBox.setChecked(False) 
    
    def gotologin(self):
        login = Login()
        widget.addWidget(login)
        widget.setCurrentWidget(login)


#SIMPLE USER

class HomeScreen(QDialog):
    def __init__(self):
        super(HomeScreen, self).__init__()
        loadUi("HomeScreen.ui", self)
        
        self.FlightsButton.clicked.connect(self.createSearch)
        #self.ForumsButton.clicked.connect(self.createSearch)
        #self.HomeButton.clicked.connect(self.createSearch)
        self.SearchButton.clicked.connect(self.createSearch)
        self.FavoritesButton.clicked.connect(self.createFavorites)
        #self.ProfileButton.clicked.connect(self.createSearch)

        # ComboBoxes
        self.comboBoxAccomodation.currentIndexChanged.connect(self.combochanged)
        self.comboBoxAttractions.currentIndexChanged.connect(self.combochanged)
        self.comboBoxRestaurants.currentIndexChanged.connect(self.combochanged)
        self.comboBoxTransport.currentIndexChanged.connect(self.combochanged)

    def combochanged(self):
        print(self.comboBoxAccomodation.currentIndex())
        index = self.createSearch()
        if self.comboBoxAccomodation.currentIndex() == 1:
            pass 
            #filter database for Accomodation tables
        elif self.comboBoxAccomodation.currentIndex() == 2:
            pass
        elif self.comboBoxAccomodation.currentIndex() == 3:
            pass
        elif self.comboBoxAccomodation.currentIndex() == 4:
            pass

        if self.comboBoxAttractions.currentIndex() == 1:
            pass
            #filter database for Attractions tables
        elif self.comboBoxAttractions.currentIndex() == 2:
            pass
        elif self.comboBoxAttractions.currentIndex() == 3:
            pass
        elif self.comboBoxAttractions.currentIndex() == 4:
            pass

        if self.comboBoxRestaurants.currentIndex() == 1:
            pass
            #filter database for Restaurants tables
        elif self.comboBoxRestaurants.currentIndex() == 2:
            pass
        elif self.comboBoxRestaurants.currentIndex() == 3:
            pass
        elif self.comboBoxRestaurants.currentIndex() == 4:
            pass

        if self.comboBoxTransport.currentIndex() == 1:
            pass
            #filter database for Transport tables
        elif self.comboBoxTransport.currentIndex() == 2:
            pass
        elif self.comboBoxTransport.currentIndex() == 3:
            pass
        elif self.comboBoxTransport.currentIndex() == 4:
            pass
        print("value Changed")

    def createSearch(self):
        search = Search()
        widget.addWidget(search)
        widget.setCurrentWidget(search)

    def createFavorites(self):
        favorites = Favorites()
        widget.addWidget(favorites)
        widget.setCurrentWidget(favorites)

class Favorites(QDialog):
    def __init__(self):
        super(Favorites, self).__init__()
        loadUi("Favorites.ui", self)
        self.BackButton.clicked.connect(self.backHome)

    def backHome(self):
        backHome = HomeScreen()
        widget.addWidget(backHome)
        widget.setCurrentWidget(backHome)


class Profile(QDialog):
    def __init__(self):
        super(Profile, self).__init__()
        loadUi("Profile.ui", self)
        self.BackButton.clicked.connect(self.gotoBusinessHome)
        self.HomeButton.clicked.connect(self.gotoBusinessHome)
        
    def gotoBusinessHome(self):
        #if :
        businessHome = BusinessHome()
        widget.addWidget(businessHome)
        widget.setCurrentWidget(businessHome)
        #elif:
            #pass

    def addBusiness(self):
        addBusiness = AddBusiness()
        widget.addWidget(addBusiness)
        widget.setCurrentWidget(addBusiness)
        
#BUSINESSMAN        

class BusinessHome(QDialog):
    def __init__(self):
        super(BusinessHome, self).__init__()
        loadUi("BusinessHome.ui", self)
        self.AddBusinessButton.clicked.connect(self.addBusiness)
        self.ProfileButton.clicked.connect(self.gotoProfile)

    def createSearch(self):
        search = Search()
        widget.addWidget(search)
        widget.setCurrentWidget(search)

    def addBusiness(self):
        addBusiness = AddBusiness()
        widget.addWidget(addBusiness)
        widget.setCurrentWidget(addBusiness)

    def gotoProfile(self):
        profile = Profile()
        widget.addWidget(profile)
        widget.setCurrentWidget(profile)


class AddBusiness(QDialog):
    def __init__(self):
        super(AddBusiness, self).__init__()
        loadUi("BusinessList.ui", self)
        self.BackButton.clicked.connect(self.gotoBusinessHome)
        self.AccomodationButton.clicked.connect(self.gotoAccForm)
        self.FlightsButton.clicked.connect(self.gotoFligthsForm)
        self.RestaurantsButton.clicked.connect(self.gotoRestForm)
        self.AttractionsButton.clicked.connect(self.gotoAttrForm)
        self.TrasportationButton.clicked.connect(self.gotoTransForm)
        self.HomeButton.clicked.connect(self.gotoBusinessHome)
        self.ProfileButton.clicked.connect(self.gotoProfile)

    def gotoBusinessHome(self):
        businessHome = BusinessHome()
        widget.addWidget(businessHome)
        widget.setCurrentWidget(businessHome)

    def gotoAccForm(self):
        accForm = AccomodationForm()
        widget.addWidget(accForm)
        widget.setCurrentWidget(accForm)

    def gotoFligthsForm(self):
        flightsForm = FlightsForm()
        widget.addWidget(flightsForm)
        widget.setCurrentWidget(flightsForm)

    def gotoAttrForm(self):
        attrForm = AttractionsForm()
        widget.addWidget(attrForm)
        widget.setCurrentWidget(attrForm)

    def gotoRestForm(self):
        restForm = RestaurantsForm()
        widget.addWidget(restForm)
        widget.setCurrentWidget(restForm)

    def gotoTransForm(self):
        transForm = TrasportationForm()
        widget.addWidget(transForm)
        widget.setCurrentWidget(transForm)

    def gotoProfile(self):
        profile = Profile()
        widget.addWidget(profile)
        widget.setCurrentWidget(profile)

    def createSearch(self):
        search = Search()
        widget.addWidget(search)
        widget.setCurrentWidget(search)


class Search(QDialog):
    def __init__(self):
        super(Search, self).__init__()
        loadUi("Search.ui", self)
        self.BackButton.clicked.connect(self.backHome)

    def backHome(self):
            backHome = HomeScreen()
            widget.addWidget(backHome)
            widget.setCurrentWidget(backHome)

    def keyPressEvent(self, e):
        if e.key() == 16777220:  #  To 16777220 einai to int gia to enter
            self.searchregion()

    def searchregion(self):
        place = self.City.text().title()  #  To title einai gia to prwto gramma na einai kefalaio kai ta alla mikra
        cursor = mydb.cursor()

        exists = '''SELECT City_Id FROM city WHERE City_Name = %s'''
        print("This is exists"+exists)
        cursor.execute(exists, (place,))
        count = cursor.fetchall()
        print(len(count))
        print(count)

        if len(count) == 0:
            QMessageBox.about(self, "Error", "Place doesnt exist!")
        else:
            QMessageBox.about(self, "Error", "Place!")

class AccomodationForm(QDialog):
    def __init__(self):
        super(AccomodationForm, self).__init__()
        loadUi("BusinessFormAcc.ui", self)
        self.BackButton.clicked.connect(self.gotoAddBusiness)
        self.HomeButton.clicked.connect(self.gotoBusinessHome)
        #self.name.setText("Hello")
        self.ProfileButton.clicked.connect(self.gotoProfile)
        self.submitButton.clicked.connect(self.insertAccomondation)

    def gotoAddBusiness(self):
        addBusiness = AddBusiness()
        widget.addWidget(addBusiness)
        widget.setCurrentWidget(addBusiness)

    def gotoBusinessHome(self):
        businessHome = BusinessHome()
        widget.addWidget(businessHome)
        widget.setCurrentWidget(businessHome)

    def createSearch(self):
        search = Search()
        widget.addWidget(search)
        widget.setCurrentWidget(search)

    def gotoProfile(self):
        profile = Profile()
        widget.addWidget(profile)
        widget.setCurrentWidget(profile)

    def insertAttraction(self):
        name = self.Name.text()
        surname = self.Surname.text()
        businessName = self.BusinessName.text()
        city = self.City.text()
        country = self.Country.text()
        postalCode = self.PostalCode.text()
        email = self.Email.text()
        address = self.Address.text()
        contactNumber = self.ContactNumber.text()
        siteURL = self.SiteURL.text()
        pricesFrom = self.PricesFROM.text()
        pricesTo = self.PricesTO.text()
        noOfComp = self.NumberOfCompartments.text()
        description = self.AccDescription.text()

        cursor = mydb.cursor() #connect with database here

        exist1 = '''SELECT COUNT(*) FROM country WHERE Country_Name = %s ''' 
        cursor.execute(exist1, (country,))
        count1 = cursor.fetchone()

        exist2 = '''SELECT COUNT(*) FROM city WHERE City_Name = %s'''
        cursor.execute(exist2, (city,))
        count2 = cursor.fetchone()

        exist3 = '''SELECT COUNT(*) FROM company WHERE Company_Name = %s'''
        cursor.execute(exist3, (businessName,))
        count3 = cursor.fetchone()

        
        if dm.check_blank3(name, surname, businessName, city, country, postalCode, email, address, contactNumber, siteURL, pricesFrom, pricesTo, noOfComp, description) != True:
            QMessageBox.about(self, "Error", "Please fill all the spaces in the form.")
        elif count3[0] == 1:
            QMessageBox.about(self, "Error", "Business name already exists.")
        elif dm.valemail(email) is not True:
            QMessageBox.about(self, "Error", "Email doesn't exist or is not in the right structure!")
        elif len(contactNumber) < 10:
            QMessageBox.about(self, "Error", "Contact number does not seem correct. Try again.")
        elif dm.is_string_an_url(siteURL) != True:
            QMessageBox.about(self, "Error", "Site URL is not in the right form!")
        else:    
            if count1[0] == 1 & count2[0] == 1:
                newCompany = '''INSERT INTO company(Company_Name, Email, City_Id, Company_address, Details, Name, Surname, SiteURL, Contact_Number, Number_of_Compartments) VALUES ('{}', '{}', (SELECT City_Id FROM city WHERE City_Name = %s), '{}', '{}', '{}', '{}', '{}', '{}', '{}')'''.format(businessName, email, address, description, name, surname, siteURL, contactNumber, noOfComp)
                cursor.execute(newCompany, (city,))
                mydb.commit()
                QMessageBox.about(self, "Success", "Your business has been successfully registered!")
                self.gotoAddBusiness()
            else:
                QMessageBox.about(self, "Error", "An error occurred.")

class FlightsForm(QDialog):
    def __init__(self):
        super(FlightsForm, self).__init__()
        loadUi("BusinessFormFlig.ui", self)
        self.BackButton.clicked.connect(self.gotoAddBusiness)
        self.HomeButton.clicked.connect(self.gotoBusinessHome)
        self.ProfileButton.clicked.connect(self.gotoProfile)

    def gotoAddBusiness(self):
        addBusiness = AddBusiness()
        widget.addWidget(addBusiness)
        widget.setCurrentWidget(addBusiness)

    def gotoBusinessHome(self):
        businessHome = BusinessHome()
        widget.addWidget(businessHome)
        widget.setCurrentWidget(businessHome)

    def createSearch(self):
        search = Search()
        widget.addWidget(search)
        widget.setCurrentWidget(search)

    def gotoProfile(self):
        profile = Profile()
        widget.addWidget(profile)
        widget.setCurrentWidget(profile)


class AttractionsForm(QDialog):
    def __init__(self):
        super(AttractionsForm, self).__init__()
        loadUi("BusinessFormAttr.ui", self)
        self.BackButton.clicked.connect(self.gotoAddBusiness)
        self.HomeButton.clicked.connect(self.gotoBusinessHome)
        self.ProfileButton.clicked.connect(self.gotoProfile)
        self.submitButton.clicked.connect(self.insertAttraction)

    def gotoAddBusiness(self):
        addBusiness = AddBusiness()
        widget.addWidget(addBusiness)
        widget.setCurrentWidget(addBusiness)

    def gotoBusinessHome(self):
        businessHome = BusinessHome()
        widget.addWidget(businessHome)
        widget.setCurrentWidget(businessHome)

    def createSearch(self):
        search = Search()
        widget.addWidget(search)
        widget.setCurrentWidget(search)

    def gotoProfile(self):
        profile = Profile()
        widget.addWidget(profile)
        widget.setCurrentWidget(profile)

    def insertAttraction(self):
        name = self.Name.text()
        surname = self.Surname.text()
        businessName = self.BusinessName.text()
        city = self.City.text()
        country = self.Country.text()
        postalCode = self.PostalCode.text()
        email = self.Email.text()
        address = self.Address.text()
        contactNumber = self.ContactNumber.text()
        siteURL = self.SiteURL.text()
        pricesFrom = self.PricesFROM.text()
        pricesTo = self.PricesTO.text()
        description = self.AttrDescription.text()
        radioB1 = self.radioButton1.isChecked()
        radioB2 = self.radioButton2.isChecked()
        radioB3 = self.radioButton3.isChecked()
        radioB4 = self.radioButton4.isChecked()

        cursor = mydb.cursor() # connect with database here
        
        exist1 = '''SELECT COUNT(*) FROM country WHERE Country_Name = %s ''' 
        cursor.execute(exist1, (country,))
        count1 = cursor.fetchone()

        exist2 = '''SELECT COUNT(*) FROM city WHERE City_Name = %s'''
        cursor.execute(exist2, (city,))
        count2 = cursor.fetchone()
        
        exist3 = '''SELECT COUNT(*) FROM company WHERE Company_Name = %s'''
        cursor.execute(exist3, (businessName,))
        count3 = cursor.fetchone()
        
        if dm.check_blank2(name, surname, businessName, city, country, postalCode, email, address, contactNumber, siteURL, pricesFrom, pricesTo, description) != True:
           QMessageBox.about(self, "Error", "Please fill all the spaces in the form.") 
        elif count3[0] == 1:
            QMessageBox.about(self, "Error", "Business name already exists.")
        elif dm.valemail(email) is not True:
            QMessageBox.about(self, "Error", "Email doesn't exist or is not in the right structure!")
        elif len(contactNumber) < 10:
           QMessageBox.about(self, "Error", "Contact number does not seem correct. Try again.")
        elif dm.is_string_an_url(siteURL) != True:
            QMessageBox.about(self, "Error", "Site URL is not in the right form!")
        elif radioB1 != True and radioB2 != True and radioB3 != True and radioB4 != True:
           QMessageBox.about(self, "Error", "Visitor's time selection must be filled.")
        else:
            if count1[0] == 1 & count2[0] == 1:
                newCompany = '''INSERT INTO company(Company_Name, Email, City_Id, Company_address, Details, Name, Surname, SiteURL, Contact_Number) VALUES ('{}', '{}', (SELECT City_Id FROM city WHERE City_Name = %s), '{}', '{}', '{}', '{}', '{}', '{}')'''.format(businessName, email, address, description, name, surname, siteURL, contactNumber)
                cursor.execute(newCompany, (city,))
                mydb.commit()
                QMessageBox.about(self, "Success", "Your business has been successfully registered!")
                self.gotoAddBusiness()
            else:
                QMessageBox.about(self, "Error", "An error occurred.")  
            
'''na min uparxei idio business name *DONE
validate email
contact number 10psifio
na min uparxoun kena pedia check_Blank
na allazei to index (na min einai 0)
radio-button selection
 '''
class RestaurantsForm(QDialog):
    def __init__(self):
        super(RestaurantsForm, self).__init__()
        loadUi("BusinessFormRest.ui", self)
        self.BackButton.clicked.connect(self.gotoAddBusiness)
        self.HomeButton.clicked.connect(self.gotoBusinessHome)
        self.ProfileButton.clicked.connect(self.gotoProfile)
        self.submitButton.clicked.connect(self.insertRestaurant)

    def gotoAddBusiness(self):
        addBusiness = AddBusiness()
        widget.addWidget(addBusiness)
        widget.setCurrentWidget(addBusiness)

    def gotoBusinessHome(self):
        businessHome = BusinessHome()
        widget.addWidget(businessHome)
        widget.setCurrentWidget(businessHome)

    def createSearch(self):
        search = Search()
        widget.addWidget(search)
        widget.setCurrentWidget(search)

    def gotoProfile(self):
        profile = Profile()
        widget.addWidget(profile)
        widget.setCurrentWidget(profile)

    def insertRestaurant(self):
        name = self.Name.text()
        surname = self.Surname.text()
        businessName = self.BusinessName.text()
        city = self.City.text()
        country = self.Country.text()
        postalCode = self.PostalCode.text()
        email = self.Email.text()
        address = self.Address.text()
        contactNumber = self.ContactNumber.text()
        siteURL = self.SiteURL.text()
        pricesFrom = self.PricesFROM.text()
        pricesTo = self.PricesTO.text()
        foodType = self.FoodType.text()
        description = self.DescriptionRest.text()

        cursor = mydb.cursor() # connect with database here

        exist1 = '''SELECT COUNT(*) FROM country WHERE Country_Name = %s ''' 
        cursor.execute(exist1, (country,))
        count1 = cursor.fetchone()

        exist2 = '''SELECT COUNT(*) FROM city WHERE City_Name = %s'''
        cursor.execute(exist2, (city,))
        count2 = cursor.fetchone()

        exist3 = '''SELECT COUNT(*) FROM company WHERE Company_Name = %s'''
        cursor.execute(exist3, (businessName,))
        count3 = cursor.fetchone()

        if dm.check_blank3(name, surname, businessName, city, country, postalCode, email, address, contactNumber, siteURL, pricesFrom, pricesTo, foodType, description) != True:
           QMessageBox.about(self, "Error", "Please fill all the spaces in the form.") 
        elif count3[0] == 1:
            QMessageBox.about(self, "Error", "Business name already exists.")
        elif dm.valemail(email) is not True:
            QMessageBox.about(self, "Error", "Email doesn't exist or is not in the right structure!")
        elif len(contactNumber) < 10:
            QMessageBox.about(self, "Error", "Contact number does not seem correct. Try again.")
        elif dm.is_string_an_url(siteURL) != True:
            QMessageBox.about(self, "Error", "Site URL is not in the right form!")
        else:
            if count1[0] == 1 & count2[0] == 1:    
                newCompany = '''INSERT INTO company(Company_Name, Email, City_Id, Company_address, Details, Name, Surname, SiteURL, Contact_Number, Food_Type) VALUES ('{}', '{}', (SELECT City_Id FROM city WHERE City_Name = %s), '{}', '{}', '{}', '{}', '{}', '{}', '{}')'''.format(businessName, email, address, description, name, surname, siteURL, contactNumber, foodType)
                cursor.execute(newCompany, (city,))
                mydb.commit()
                QMessageBox.about(self, "Success", "Your business has been successfully registered!")
                self.gotoAddBusiness()
            else:
                QMessageBox.about(self, "Error", "An error occurred.")


class TrasportationForm(QDialog):
    def __init__(self):
        super(TrasportationForm, self).__init__()
        loadUi("BusinessFormTrans.ui", self)
        self.BackButton.clicked.connect(self.gotoAddBusiness)
        self.HomeButton.clicked.connect(self.gotoBusinessHome)
        self.ProfileButton.clicked.connect(self.gotoProfile)

    def gotoAddBusiness(self):
        addBusiness = AddBusiness()
        widget.addWidget(addBusiness)
        widget.setCurrentWidget(addBusiness)

    def gotoBusinessHome(self):
        businessHome = BusinessHome()
        widget.addWidget(businessHome)
        widget.setCurrentWidget(businessHome)

    def createSearch(self):
        search = Search()
        widget.addWidget(search)
        widget.setCurrentWidget(search)

    def gotoProfile(self):
        profile = Profile()
        widget.addWidget(profile)
        widget.setCurrentWidget(profile)


app = QApplication(sys.argv)
mainwindow = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(421)
widget.setFixedHeight(721)
widget.show()
app.exec_()
