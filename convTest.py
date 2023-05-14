import os

#selenium browser imports
from selenium import webdriver
# for edge
'''
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService

BraveDriver = webdriver.Edge(service=EdgeService(
    EdgeChromiumDriverManager().install()))
'''
# for brave

from selenium.webdriver.chrome.service import Service as BraveService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

BraveDriver = webdriver.Chrome(
    service=BraveService(
        ChromeDriverManager(
            chrome_type=ChromeType.BRAVE).install()
            )
        )

#webdriver common imports
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions as EXP

#google translation  
from translateText import transToMarathi

# fetch URL
pageURL = "https://demodata.unipune.ac.in/"
BraveDriver.get(pageURL) #set URL
BraveDriver.maximize_window()
assert "Certificate" in BraveDriver.title


clinkLink = BraveDriver.find_element(By.LINK_TEXT, "Apply to Regular convocation certificate")
clinkLink.click()

#Setting up the form:
prnElement = BraveDriver.find_element(By.XPATH, "//input[@name='PRN']")
prnElement.send_keys("71910009H") # TODO : user input later 

prnButton = BraveDriver.find_element(By.XPATH, "//button[@value='Check PRN Validation'][@type='button']")
prnButton.click()

#wait page to load

BraveDriver.implicitly_wait(3)
'''
infoDialogue= BraveDriver.find_element(By.XPATH, "//div[contains(@class,'modal fade show')][contains(@id,'myModalInfo')]")
#print(type(infoCloseButton))

#infoCloseButton =  BraveDriver.find_element(By.XPATH, "//*[@id='myModalInfo']/div/div/div[3]/button")
# (//button[contains(@class,'close')])[5]
#infoCloseButton.click() 
BraveDriver.implicitly_wait(3)
#BraveDriver.execute_script("arguments[0].click()",infoCloseButton)
infoDialogue.send_keys(Keys.ESCAPE)
closeDialogueWait = WebDriverWait(BraveDriver, 5).until( EC.invisibility_of_element_located((By.XPATH,"//div[contains(@id,'myModalInfo')]")))
# except EXP.TimeoutException():
#    print(" finding close button timed out")
'''
#----------------------------------------------------------#

#set up the form
seatNumber = BraveDriver.find_element(By.XPATH,"//input[@name='SeatNo'][@id='txtSeatNo']")
seatNumber.send_keys("B150324353") # TODO : user input later

genderSelect = Select(BraveDriver.find_element(By.XPATH, "//select[@id='txtGender'][@name='Gender']"))
genderSelect.select_by_value("Male") # TODO : user input Later


SName = "Phadnis Mihir Vinay" 
studentName = BraveDriver.find_element(By.XPATH, "//input[@id='txtStudentName']")
studentName.send_keys(SName)  # TODO : user input later

BraveDriver.implicitly_wait(5)

    #translated text to marathi
studentName_Mr = transToMarathi(SName) # TODO : make this better ?
translatedStudentName = BraveDriver.find_element(By.XPATH, "//input[@id='txtStudentName_M'][@name='StudentName_M']") 
translatedStudentName.send_keys(studentName_Mr)

MName = "Phadnis Harshada Vinay"
motherName = BraveDriver.find_element(By.XPATH, "//input[@id='txtMotherName']")
motherName.send_keys(MName)  # TODO : user input later

BraveDriver.implicitly_wait(5)

# translated text to marathi
motherName_Mr = transToMarathi(MName)
translatedMotherName = BraveDriver.find_element(By.XPATH, "//input[@id='txtMotherName_M'][@name='MotherName_M']")
translatedMotherName.send_keys(motherName_Mr)

#address values :

countrySelect = Select(
    BraveDriver.find_element(
        By.XPATH, "//select[contains(@name,'Country')]")
    )
countrySelect.select_by_visible_text("India") # TODO : user input Later

stateSelect = Select(
    WebDriverWait(BraveDriver, timeout=5).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//select[contains(@name,'State')][contains(@id,'State')]"))
        )
    )
stateSelect.select_by_visible_text("MAHARASHTRA") # TODO : user input Later

districtSelect = Select(
    WebDriverWait(BraveDriver, timeout=5).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//select[contains(@name,'District')]"))
        )
    ) 
districtSelect.select_by_visible_text("PUNE")  # TODO : user input Later

talukaSelect = Select(
    WebDriverWait(BraveDriver, timeout=5).until(
        EC.element_to_be_clickable(
        (By.XPATH, "//select[contains(@name,'Taluka')][contains(@id,'Taluka')]"))
        )
    )
talukaSelect.select_by_visible_text("Pune City") # TODO : user input later

addrPin = BraveDriver.find_element(By.XPATH, "//input[@name='Pincode']")
addrPin.send_keys("411037")  # TODO : user input later

addressField = BraveDriver.find_element(By.XPATH, "//textarea[@name='Address']")
addressField.send_keys("89/708, Maharshi Nagar, behind TMV Colony, Pune") # TODO : user input later

#Contact Information fields
mobileNumber = BraveDriver.find_element(By.XPATH, "//input[@name='Mobile'][@id='txtMobile']")
mobileNumber.send_keys("9673236900")  # TODO : user input later

emailField = BraveDriver.find_element(By.XPATH, "//input[@id='txtEmail']")
emailField.send_keys("mihirphadnis01@gmail.com")  # TODO : user input later

# Course Information 
facultyNameSelect = Select(BraveDriver.find_element(
    By.XPATH, "//select[contains(@name,'FacultyID')]")
    )
facultyNameSelect.select_by_visible_text("Engineering")

courseNameSelect = Select(
    WebDriverWait(BraveDriver, timeout=5).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//select[contains(@name,'CourseID')]"))
        )
    )
courseNameSelect.select_by_visible_text("B.E. (Computer)") # TODO : user input later

passingMonthSelect = Select(
    BraveDriver.find_element(By.XPATH, "//select[contains(@name,'PassingMonth')]")
    )
passingMonthSelect.select_by_value("August") # TODO : user input later

passingYearSelect = Select(
    BraveDriver.find_element(
        By.XPATH, "//select[contains(@name,'PassingYear')]")
    )
passingYearSelect.select_by_value("2022") # TODO : user input later

resultSelect = Select(
    BraveDriver.find_element(
        By.XPATH, "//select[contains(@name,'Result')]")
    )
resultSelect.select_by_value("First Class with Distinction") # TODO : user input later

certificateDeliverySelect = Select(
    BraveDriver.find_element(
        By.XPATH, "//select[contains(@name,'DegreeDeliveryType')]")
    )
certificateDeliverySelect.select_by_value("By Post") # TODO : user input later

#class improvement and Upload Mark sheet

classImprovementBox = BraveDriver.find_element(By.XPATH, "//input[contains(@type,'checkbox')]")
checkboxVal = False # TODO : user input later
if checkboxVal:
    classImprovementBox.click()

uploadMarkSheet = BraveDriver.find_element(By.XPATH, "//input[contains(@type,'file')][contains(@name,'fileMarksheet')]")

script_dir = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(script_dir, "finalResult.pdf")

# filepath = "./finalResult.pdf"
uploadMarkSheet.send_keys(filepath)



''' <input type="file" class="form-control col-md-6 valid" title="search image" id="MarkId" name="fileMarksheet" onchange="showmarksheet(this)" style="outline: green dotted 2px !important;">'''

# college Information

PunCode = BraveDriver.find_element(By.XPATH, "//input[@name='PUNCODE'][@id='txtPuncode']")
PunCode.send_keys("CEGP011350")  # TODO : user input later

#PunCode.get_attribute("value")
PunCodeVal = (PunCode.get_attribute("value"))

CollegeFindLink = BraveDriver.find_element(By.XPATH, "//a[contains(@data-toggle,'modal')][contains(@data-target,'#SecCollegeList')]")

  # WebDriverWait(BraveDriver, timeout=5).until(EC.element_to_be_clickable(mark))

CollegeFindLink.click()  # force it?

# TODO : make this Nicer Later or even a Function.
try:
    collegeSearchElement = WebDriverWait(BraveDriver, timeout=5).until(
        EC.visibility_of_element_located((By.XPATH, "//input[contains(@type, 'search')]"))
        )
except EXP.TimeoutException:
    print("Request Timed out, no such element is present")

collegeSearchElement.send_keys(PunCodeVal)
#collegeSearchElement.send_keys(Keys.RETURN)

try:
    CollegeSelectButton = WebDriverWait(BraveDriver, timeout=5).until(
        EC.visibility_of_element_located(
            (By.XPATH,
                "//button[@class='btnSelect'][contains(.,'Select')]")
        )
    )
    CollegeSelectButton.click()

    #WebDriverWait(BraveDriver, timeout=10).until(EC.invisibility_of_element_located((By.XPATH, "")))
except EXP.TimeoutException:    
    print("Could Not Find requested College!")
    closeListButton = BraveDriver.find_element(
        By.XPATH, "//button[contains(@class,'close closeUQP')]")
    closeListButton.click()
###########################################


if EC.alert_is_present():    
    sw_alert = BraveDriver.switch_to.alert
    sw_alert.accept()

SubmitButton = BraveDriver.find_element(By.XPATH, "//input[contains(@type,'submit')]")
SubmitButton.click()

if EC.alert_is_present():
    sw_alert = BraveDriver.switch_to.alert
    sw_alert.accept()

'''
modelSuccessDisplay = WebDriverWait(BraveDriver, timeout=5).until(
    EC.visibility_of_element_located(
        (By.XPATH, "//div[contains(@class,'modal fade show')][contains(@id,'myModalSuccess')]")
        )
    )
modelSuccessDisplay.send_keys(Keys.ESCAPE)
'''

modalSuccessButton = WebDriverWait(BraveDriver, timeout=5).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[@id='btnModalClose'][@class='btn btn-success elevation-1']"))
    )
modalSuccessButton.click()

BraveDriver.implicitly_wait(10)

payButtonLink = WebDriverWait(BraveDriver, timeout=5).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[contains(@data-original-title,'Please click here to Process this applicatione')]"))
    )
payButtonLink.click()

paymentMethodSelect = Select(
    WebDriverWait(BraveDriver, timeout=10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//select[contains(@name,'PaymentType')]"))
        )
    )
paymentMethodSelect.select_by_visible_text("Offline")

bankValueSelect = Select(
    WebDriverWait(BraveDriver, timeout=10).until(
        EC.presence_of_element_located((
            By.XPATH, "//select[contains(@name,'BankName')]"))
        )
    )
bankValueSelect.select_by_value("1")

submitPaymentProcess = BraveDriver.find_element(By.XPATH, "//input[contains(@type,'submit')]")
submitPaymentProcess.submit()

paymentSuccessDialogue = WebDriverWait(BraveDriver, timeout=10).until(EC.presence_of_element_located(
    (By.XPATH, "//span[contains(.,'Payment Status Update Successfully')]")))

if paymentSuccessDialogue:
    BraveDriver.find_element(
        By.XPATH, "//button[contains(@class,'btn btn-success elevation-1')]").click()

#BraveDriver.implicitly_wait(10)



#collegeFinder(PunCodeVal)
# assert PunCodeVal == collegeFinder(PunCodeVal)

# wait condition
#BraveDriver.implicitly_wait(5)


'''def collegeFinder(PUNCODE):

    searchPunCode = PUNCODE
    CollegeFindLink = BraveDriver.find_element(
        By.XPATH, "//a[contains(@data-toggle,'modal')][contains(@data-target,'#SecCollegeList')]")

    # WebDriverWait(BraveDriver, timeout=5).until(EC.element_to_be_clickable(mark))

    CollegeFindLink.click()  # force it?

    # TODO : make this Nicer Later or even a Function.
    try:
        collegeSearchElement = WebDriverWait(BraveDriver, timeout=5).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@type='search]")))
    except EXP.TimeoutException:
        print("Request Timed out, no such element is present")

    collegeSearchElement.send_keys(searchPunCode)
    collegeSearchElement.send_keys(Keys.RETURN)

    try:
        CollegeSelectButton = WebDriverWait(BraveDriver, timeout=5).until(
            EC.visibility_of_element_located(
                (By.XPATH,
                 "//button[@class='btnSelect'][contains(.,'Select')]")
            )
        )
    except EXP.TimeoutException():
        print("Could Not Find requested College!")
        closeListButton = BraveDriver.find_element(
            By.XPATH, "//button[contains(@class,'close closeUQP')]")
        closeListButton.click()
    ###########################################

    if EC.alert_is_present():
        sw_alert = BraveDriver.switch_to.alert
        sw_alert.accept()

    return searchPunCode
'''
#exit
BraveDriver.close()






