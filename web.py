import json
import os
import subprocess
import sys
import time
from csv import writer
import environ

from PySide6.QtCore import (
    QRunnable,
    Slot,
)
from _socket import gaierror
from urllib3.exceptions import MaxRetryError, NewConnectionError

from needpermissions import CheckPermissons
from signals import WorkerSignals
from userdata import user, behavior_control
import requests

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

# Take environment variables from .env file
environ.Env.read_env()

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)


class Downloader(QRunnable):

    def __init__(self):
        super().__init__()
        self.signals = WorkerSignals()

    @Slot()
    def run(self):
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            self.signals.error.emit('running in a PyInstaller bundle')
            application_path = os.getcwd()  # sys.argv[0] #sys._MEIPASS
        else:
            self.signals.error.emit('running in a normal Python process')
            application_path = os.path.dirname(os.path.abspath(__file__))

        def read_json():
            if os.path.exists("credentials.json"):
                with open('credentials.json') as json_file:
                    data = json.load(json_file)
            else:
                data = {}

            return data

        def get_list():
            data = read_json()

            base_url = 'https://www.it-fitness.de/redaktion/core/usersystem/login.php'
            credentials = {'UserName': data['name_it-fitness-Redaktion'], 'PassWort': data['passwd_it-fitness-Redaktion']}

            session = requests.Session()

            try:
                session.post(base_url, data=credentials)
                self.signals.error.emit(session.cookies)
            except requests.exceptions.ConnectionError:
                self.signals.error.emit("❌ Keine Verbindung zur Webseite")
                print("Keine Verbindung zur Webseite")
                return
            # print(session.cookies)

            file_url = 'https://www.it-fitness.de/redaktion/ext/modules/EmailTemplates/redaktion/show.php?id=20&export'

            try:
                resp = session.get(file_url, stream=True)

                if resp.status_code == 200:
                    filename = 'Anmeldung Kurs.csv'
                    with open(filename, 'wb') as f:
                        for chunk in resp.iter_content(chunk_size=1024):
                            if chunk:
                                f.write(chunk)

                    self.signals.finished.emit()  # fires on success, read list afterwards
                else:
                    self.signals.error.emit("❌ Keine Verbindung zur Webseite")
            except ConnectionError:
                self.signals.error.emit("❌ Keine Verbindung zur Webseite")
                print("Keine Verbindung zur Webseite")
                return

            self.signals.progress.emit(100)

        def runner():

            self.signals.progress.emit(0)
            get_list()
            # finally:
            #    return

        runner()

# class GetList(QRunnable):
#     """
#     Get new Account List with Selenium
#     """
#
#     def __init__(self):
#         super().__init__()
#         self.signals = WorkerSignals()
#
#     @Slot()
#     def run(self):
#
#         if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
#             self.signals.error.emit('running in a PyInstaller bundle')
#             application_path = os.getcwd()  # sys.argv[0] #sys._MEIPASS
#         else:
#             self.signals.error.emit('running in a normal Python process')
#             application_path = os.path.dirname(os.path.abspath(__file__))
#
#         # self.signals.error.emit(os.getcwd())
#
#         def resource_path(relative_path):
#             try:
#                 base_path = sys._MEIPASS
#             except Exception:
#                 base_path = os.path.dirname(__file__)
#             return os.path.join(base_path, relative_path)
#
#         options = Options()
#         options.headless = behavior_control['headless_browser']
#
#         # dir_path = os.path.dirname(os.path.realpath(__file__))
#         prefs = {'download.default_directory': application_path}
#         options.add_experimental_option('prefs', prefs)
#
#         if sys.platform == "win32":
#             driver = webdriver.Chrome(resource_path('./driver/chromedriver.exe'), options=options)
#         else:
#             driver = webdriver.Chrome('/opt/homebrew/bin/chromedriver', options=options)
#
#         driver.implicitly_wait(5)
#
#         def login():
#             try:
#                 self.signals.progress.emit(5)
#                 driver.get("about:blank")
#                 # driver.get("https://www.it-fitness.de/redaktion")
#                 driver.get("https://www.it-fitness.de/redaktion/core/usersystem/login.php")
#                 self.signals.progress.emit(10)
#             except:
#                 self.signals.error.emit("❌ Keine Verbindung zur Webseite")
#                 print("Keine Verbindung zur Webseite")
#                 return
#
#             try:
#                 driver.find_element(By.XPATH, '//input').find_element(By.XPATH, "//input[@id='UserName']").send_keys(
#                     env('USERNAME'))
#                 driver.find_element(By.XPATH, '//input').find_element(By.XPATH, "//input[@id='PassWort']").send_keys(
#                     env('PASSWORD') + Keys.ENTER)
#                 # name = 'beuster@helliwood.com'
#                 # driver.find_element(By.XPATH, "//*[@id='UserName']").sendKeys(name)
#                 # name.send_keys("beuster@helliwood.com")
#                 # driver.find_element(By.ID, 'UserName').send_keys("beuster@helliwood.com")
#                 # //*[@id="UserName"]
#                 # /html/body/div/div[2]/form/div/div/div[1]/input
#                 self.signals.progress.emit(25)
#             except:
#                 self.signals.error.emit("❌ Fehler bei Login")
#                 print('Element(e) zum Login nicht gefunden')
#                 time.sleep(1)
#                 driver.quit()
#                 return
#
#             try:
#                 # content = driver.find_element_by_class_name("textrot")
#                 content = driver.find_element(By.CLASS_NAME, "textrot")
#
#                 self.dialog = None
#                 self.login = "Redaktion"
#
#                 self.permission = CheckPermissons(self.dialog, self.login)
#                 self.permission.get_permissions()
#                 print("finished permission check")
#                 login()
#                 return
#             except:
#                 print("login ok")
#                 # pass
#
#                 self.signals.progress.emit(25)
#                 get_kurs_liste()
#                 return
#
#             # except:
#             #    self.signals.error.emit("❌ Fehler bei Login")
#             #    print("Fehler bei Login")
#             #    return
#
#         def get_kurs_liste():
#             try:
#                 driver.get(
#                     "https://www.it-fitness.de/redaktion/ext/modules/EmailTemplates/redaktion/show.php?id=20&export")
#                 driver.get(
#                     "https://www.it-fitness.de/redaktion/ext/modules/EmailTemplates/redaktion/show.php?id=25&export")
#                 self.signals.progress.emit(50)
#                 time.sleep(3)
#                 self.signals.progress.emit(100)
#                 # self.signals.error.emit(resource_path(''))
#                 self.signals.error.emit("✅ Aktuelle Liste geladen")
#             except:
#                 self.signals.error.emit("❌ Fehler bei Download der Liste")
#                 print("Fehler bei Download der Liste")
#                 return
#             return
#
#         def runner():
#             try:
#                 self.signals.progress.emit(0)
#                 login()
#             finally:
#                 driver.quit()
#
#             return
#
#         runner()
#
#
# class WebHelper(QRunnable):
#     """
#     Add license
#     """
#
#     def __init__(self):
#         super().__init__()
#         self.signals = WorkerSignals()
#
#     @Slot()
#     def run(self):
#
#         options = Options()
#         options.headless = behavior_control['headless_browser']
#
#         def resource_path(relative_path):
#             try:
#                 base_path = sys._MEIPASS
#             except Exception:
#                 base_path = os.path.dirname(__file__)
#             return os.path.join(base_path, relative_path)
#
#         if sys.platform == "win32":
#             driver = webdriver.Chrome(resource_path('./driver/chromedriver.exe'), options=options)
#         else:
#             driver = webdriver.Chrome('/opt/homebrew/bin/chromedriver', options=options)
#
#         # sometimes the website is reeeeeeealy slow. So this value is needed
#         # implicit wait
#         driver.implicitly_wait(60)
#
#         # explicit wait
#         wait = WebDriverWait(driver, 5)
#
#         # user = userdata.user
#         # row_content = userdata.row_content
#
#         self.signals.progress.emit(25)
#
#         def login():
#             driver.get("https://admin.microsoft.com/AdminPortal")
#
#             time.sleep(1)
#
#             try:
#                 driver.find_element_by_name("loginfmt").send_keys(env('AKADEMIE_USERNAME') + Keys.ENTER)
#             except:
#                 login()
#                 return
#
#             self.signals.progress.emit(27)
#
#             time.sleep(1)
#
#             try:
#                 driver.find_element_by_name("passwd").send_keys(env('AKADEMIE_PASSWORD') + Keys.ENTER)
#             except:
#                 login()
#                 return
#
#             time.sleep(1)
#
#             self.signals.progress.emit(29)
#
#             try:
#                 driver.find_element_by_css_selector("input[type='submit']").click()
#             except:
#                 login()
#                 return
#
#             self.signals.progress.emit(30)
#
#             print("Login ok -> addLicense")
#             addLicense()
#             return
#
#         def addLicense():
#             # driver.get("about:blank")
#             self.signals.progress.emit(35)
#
#             try:
#                 driver.get("https://admin.microsoft.com/AdminPortal/?#/users/:/UserDetails/{}/LicensesAndApps".format(
#                     user['objectID']))
#                 print("loaded site")
#             except:
#                 addLicense()
#                 return
#
#             self.signals.progress.emit(40)
#
#             # self.signals.progress.emit(40)
#
#             # domain = "@innovative-students.de"
#             # username = user['it_mail'] + domain
#
#             # try:
#             #     element = driver.find_element_by_css_selector("input[data-automation-id='UserListV2,CommandBarSearchInputBox']")
#             #     element.send_keys(username + Keys.ENTER)
#             #     time.sleep(2)
#             #     element.send_keys(Keys.ENTER)
#             #     print("clicked two times")
#             # except:
#             #     self.signals.error.emit("Eingabe in Suchmaske hat nicht geklappt")
#             #     print("enter something into search mask not wokred")
#             #     addLicense()
#             #     return
#
#             # self.signals.progress.emit(45)
#
#             # time.sleep(2)
#
#             # #driver.find_element_by_css_selector("//span[text()='{}']".format(username)).click()
#             #     # there should be only one (highlander mode)
#             # #child = driver.find_element_by_css_selector("//div[data-automation-key='Username']")
#             # #parent = child.find_element_by_xpath('..')
#             # #parent.click()
#             # driver.find_element_by_css_selector("span[title='{} {}']".format(user['fname'], user['lname'])).click()
#             # print("clicked title to open next step")
#             # #except NoSuchElementException as ex:
#             # #    #time.sleep(3)
#             # #    print("looping through groups_setup()...")
#             # #    self.signals.error.emit("Account nicht gefunden: Neuer Versuch")
#             # #addLicense()
#             # #    return
#
#             # self.signals.progress.emit(50)
#             # time.sleep(4)
#
#             # try:
#             #     driver.find_element_by_css_selector("//span[text()='Licenses and apps']").click()
#             # except NoSuchElementException as ex:
#             #     #time.sleep(3)
#             #     print("Can not click Licenses and apps")
#             #     self.signals.error.emit("Kann 'Licenses and apps' nicht klicken")
#             #     addLicense()
#             #     return
#
#             self.signals.progress.emit(50)
#
#             try:
#                 # driver.find_element_by_xpath("//div[text()='Office 365 A1 for students']").click()
#                 driver.find_element(By.XPATH, "//div[text()='Office 365 A1 for students']").click()
#                 # driver.find_element_by_css_selector("//div[text()='Office 365 A1 for students']").click()
#                 print("clicked 'Office 365 A1 for students'")
#             except:
#                 # time.sleep(3)
#                 print("Can not click on Office 365 A1 for students")
#                 self.signals.error.emit("❌ Kann 'Office 365 A1 for students' nicht klicken")
#                 time.sleep(3)
#                 self.signals.error.emit("❌ Wenn Fehler wiederholt autritt, das Passwort ändern")
#                 time.sleep(3)
#                 addLicense()
#                 return
#
#             self.signals.progress.emit(55)
#
#             try:
#                 # driver.find_element_by_xpath("//span[text()='Save changes']").click()
#                 driver.find_element(By.XPATH, "//span[text()='Save changes']").click()
#                 print("clicked 'Save changes'")
#             except:
#                 # time.sleep(3)
#                 print("Can not click on Save changes")
#                 self.signals.error.emit("❌ Kann 'Save changes' nicht klicken")
#                 addLicense()
#                 return
#
#             self.signals.progress.emit(60)
#
#             waittime = 0
#             while (waittime < 60):
#                 print("wait: " + str(waittime) + "s")
#                 self.signals.error.emit("⌛ Warte auf die Lizenz: " + str(waittime) + "s")
#                 time.sleep(1)
#                 status, output = subprocess.getstatusoutput(
#                     "az ad user show --id {} --query assignedLicenses --output tsv 2>nul".format(user['principalName']))
#                 waittime += 1
#
#                 if output != "":
#                     self.signals.error.emit("Lizenz wurde zugewiesen")
#                     print("✅ License ok")
#                     print('License: ')
#                     print(output)
#
#                     driver.quit()
#                     return
#
#                 else:
#                     print("try again to add license")
#                     self.signals.error.emit("⚠️ Das hat nicht funktioniert - versuche es erneut.")
#                     addLicense()
#                     return
#
#         def setup_process():
#             try:
#                 try:
#                     driver.get("https://admin.microsoft.com/AdminPortal/#/users")
#                 except WebDriverException:
#                     WebWorker.close_driver()
#                     print("Can not reach login site.")
#                     self.signals.progress.emit(70)
#                     self.signals.error.emit("Kann Webseite nicht erreichen: Abbruch")
#                     return
#
#                 login()
#
#                 # registration()
#
#                 # groups_setup()
#
#             finally:
#                 driver.quit()
#             return
#
#         setup_process()
#
#
# class WebWorker(QRunnable):
#
#     def __init__(self):
#         super().__init__()
#         self.signals = WorkerSignals()
#
#     @Slot()
#     def run(self):
#
#         options = Options()
#         options.headless = behavior_control['headless_browser']
#
#         def resource_path(relative_path):
#             try:
#                 base_path = sys._MEIPASS
#             except Exception:
#                 base_path = os.path.dirname(__file__)
#             return os.path.join(base_path, relative_path)
#
#         if sys.platform == "win32":
#             driver = webdriver.Chrome(resource_path('./driver/chromedriver.exe'), options=options)
#         else:
#             driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=options)
#
#         # sometimes the website is reeeeeeealy slow. So this value is needed
#         # implicit wait
#         driver.implicitly_wait(5)
#
#         # explicit wait
#         wait = WebDriverWait(driver, 5)
#
#         # user = userdata.user
#         # row_content = userdata.row_content
#         row_content = [''] * 30
#         print(row_content)
#
#         self.signals.progress.emit(10)
#
#         def login():
#             driver.get("about:blank")
#             driver.get("https://admin.microsoft.com/AdminPortal/#/users")
#             try:
#                 driver.find_element_by_name("loginfmt").send_keys("beuster@innovative-students.de" + Keys.ENTER)
#             except:
#                 login()
#                 return
#
#             # time.sleep(1)
#             # driver.find_element_by_css_selector("input[type='submit']").click()
#             time.sleep(1)
#
#             try:
#                 driver.find_element_by_name("passwd").send_keys("-------" + Keys.ENTER)
#             except:
#                 login()
#                 return
#
#             time.sleep(1)
#
#             # time.sleep(2)
#             try:
#                 driver.find_element_by_css_selector("input[type='submit']").click()
#             except:
#                 login()
#                 return
#
#             self.signals.progress.emit(15)
#
#             # put fnmae and lname into csv, if something not working, it can be fixed afterwards
#             row_content[0] = user['fname']
#             row_content[1] = user['lname']
#             row_content[2] = user['facility']
#             row_content[3] = ''
#             row_content[4] = ''
#             row_content[5] = user['role']
#             row_content[6] = str(user['telephone'])
#             row_content[7] = user['mail']
#             row_content[8] = user['uid'].replace(".", "")
#
#             self.signals.progress.emit(20)
#
#             registration()
#             return
#
#         def registration():
#             driver.get("about:blank")
#             try:
#                 driver.get("https://admin.microsoft.com/AdminPortal/Home#/users/:/adduser")
#             except InvalidSessionIdException as ex:
#                 setup_process()
#                 return
#
#             self.signals.progress.emit(30)
#
#             try:
#                 driver.find_element_by_css_selector("input[data-automation-id='AddUserWizard_firstName']").send_keys(
#                     user['fname'])
#             except NoSuchElementException:
#                 self.signals.error.emit("Namensfeld nicht gefunden: Neuer Versuch")
#                 print("fname not found")
#                 registration()
#                 return
#
#             try:
#                 driver.find_element_by_css_selector("input[data-automation-id='AddUserWizard_lastName']").send_keys(
#                     user['lname'])
#             except:
#                 print("lname not found")
#                 registration()
#                 return
#
#             try:
#                 driver.find_element_by_css_selector("input[data-automation-id='AddUserWizard_displayName']").click()
#             except:
#                 print("displayName not found not found")
#                 registration()
#                 return
#
#             try:
#                 driver.find_element_by_css_selector("input[data-automation-id='AddUserWizard_userName']").send_keys(
#                     user['it_mail'])
#             except:
#                 print("userName not found")
#                 registration()
#                 return
#
#             # gone
#             try:
#                 driver.find_element_by_xpath("//span[text()='Automatically create a password']").click()
#             except NoSuchElementException as ex:
#                 print("password field not found")
#                 pass
#
#             try:
#                 driver.find_element_by_css_selector("input[data-automation-id='AddUserWizard_password']").send_keys(
#                     user['passwd'])
#             except:
#                 print("self choosen password field not found")
#                 registration()
#                 return
#
#             # gone
#             try:
#                 driver.find_element_by_xpath(
#                     "//input[@aria-label='Require this user to change their password when they first sign in'][@aria-checked='false']").click()
#             except NoSuchElementException as ex:
#                 print("button to check password change on first login not found")
#                 pass
#
#             try:
#                 errormsg = driver.find_element_by_css_selector("div[class*='errorString']").text
#                 # errormsg = str(wait.until(EC.presence_of_element_located(By.CSS_SELECTOR, '//div[class*="errorString"]')))
#                 print(errormsg)
#             except NoSuchElementException as ex:
#                 print("no error message found")
#                 pass
#
#             self.signals.progress.emit(40)
#
#             try:
#                 driver.find_element_by_xpath("//span[text()='Next']").click()
#             except ElementClickInterceptedException as ex:
#                 print("Not able to click next because of preceeding error: Username already known maybe?")
#                 # print("Everything fine: User not already known.")
#                 row_content[9] = "Email wird bereits verwendet"
#                 row_content[10] = "neue Gruppe(n) zugewiesen"
#                 # write_csv()
#                 # close_driver()
#                 # self.signals.progress.emit(100)
#                 self.signals.error.emit("Account vorhanden: weise Gruppen zu ...")
#                 groups_setup()
#                 return
#
#             # time.sleep(1)
#             # print("Adding A1 license...")
#             try:
#                 driver.find_element_by_css_selector(
#                     "div[data-automation-id='LicenseText_Office 365 A1 for students']").click()
#                 # print("Done!")
#             except InvalidSessionIdException as ex:
#                 # time.sleep(2)
#                 # pass
#                 self.signals.error.emit("Lizenz Fehler: Neuer Versuch.")
#                 setup_process()
#                 return
#
#             # time.sleep(1)
#             try:
#                 driver.find_element_by_xpath("//span[text()='Next']").click()
#             except InvalidSessionIdException as ex:
#                 print("Not able to click next because of preceeding error: 2")
#                 # registration()
#                 self.signals.error.emit("Fehler Account: 2")
#                 setup_process()
#                 return
#
#             # time.sleep(1)
#
#             try:
#                 errormsg = driver.find_element_by_css_selector("div[class*='summaryPageSubHeading']").text
#                 print(errormsg)
#                 # close_driver()
#                 setup_process()
#                 return
#             except NoSuchElementException as ex:
#                 pass
#
#             try:
#                 driver.find_element_by_xpath("//span[text()='Next']").click()
#             except ElementClickInterceptedException as ex:
#                 print("Not able to click next because of preceeding error: 3")
#                 # close_driver()
#                 self.signals.error.emit("Fehler Account: 3")
#                 setup_process()
#                 return
#
#             # time.sleep(1)
#             try:
#                 driver.find_element_by_xpath("//span[text()='Finish adding']").click()
#             except:
#                 registration()
#                 return
#
#             # time.sleep(1)
#             try:
#                 driver.find_element_by_xpath("//span[text()='Close']").click()
#             except:
#                 pass
#
#             # after success adding it mail and passwd to csv
#             row_content[9] = user['it_mail'] + '@innovative-students.de'
#             row_content[10] = user['passwd']
#
#             self.signals.progress.emit(50)
#             self.signals.error.emit("Email angelegt")
#
#             groups_setup()
#             return
#
#         def groups_setup():
#             if (row_content[10] != "Account nicht angelegt"):
#
#                 driver.get("about:blank")
#                 try:
#                     driver.get("https://admin.microsoft.com/AdminPortal/Home?#/users")
#                 except:
#                     groups_setup()
#                     return
#
#                 self.signals.progress.emit(60)
#
#                 # try:
#                 #    # vorherigen Eintrag löschen, wenn vorhanden
#                 #    driver.find_element_by_css_selector("button[automationid='splitbuttonprimary']").click()
#                 # except NoSuchElementException as ex:
#                 #    pass
#                 try:
#                     element = driver.find_element_by_css_selector(
#                         "input[data-automation-id='UserListV2,CommandBarSearchInputBox']")
#                     element.send_keys(user['fname'], " ", user['lname'])
#                 except:
#                     groups_setup()
#                     return
#
#                 # time.sleep(1)
#                 try:
#                     element.send_keys(Keys.ENTER)
#                 except:
#                     groups_setup()
#                     return
#
#                 self.signals.progress.emit(65)
#
#                 time.sleep(2)
#                 try:
#                     driver.find_element_by_css_selector(
#                         "span[title='{} {}']".format(user['fname'], user['lname'])).click()
#                 except NoSuchElementException as ex:
#                     # time.sleep(3)
#                     print("looping through groups_setup()...")
#                     self.signals.error.emit("Account nicht gefunden: Neuer Versuch")
#                     groups_setup()
#                     return
#
#                 self.signals.progress.emit(70)
#
#                 time.sleep(2)
#                 try:
#                     element = driver.find_element_by_css_selector(
#                         "button[data-automation-id='UserDetailPanelRegion,ManageGroupsLink']")
#                 except NoSuchElementException as ex:
#                     self.signals.error.emit("Teams verwalten Fehler: Neuer Versuch")
#                     groups_setup()
#                     return
#
#                 try:
#                     element.click()
#                 except:
#                     groups_setup()
#                     return
#
#                 # print("Clicked: Manage Groups!")
#                 time.sleep(2)
#                 try:
#                     element.click()
#                     print("Clicked second time, starting again with setup!")
#                     self.signals.error.emit("Teams Link nicht klickbar: Neuer Versuch")
#                     groups_setup()
#                     return
#                 except ElementClickInterceptedException as ex:
#                     pass
#
#                 self.signals.progress.emit(75)
#
#                 # crazy stuff: MSFT changed group list in a way, that any click on the name, disables clicks the other selected checkboxes
#                 # and all values change every time the website reloads
#                 # when even looking for another value, every checkmark get deleted
#                 # so this hack needs to be done:
#                 # search for all "aria-selected=true" (sic!) values
#                 # get for every result the data-focuszone-id
#                 # click on every group that should be enabled
#                 # also get those data focuszone stuff
#                 # append those values to a list
#                 # dismiss the first value (this entry was enabled, before anything was clicked on this site)
#                 # click on every value in the list
#                 # done (easy peasy)
#                 # ok, a few hours now in this problem, and this is not doable, so now every single group is assigned one by one, sad :(
#                 # I have an idea how to fix that, but it needs to work now and the fix needs more time and it's not clear if even that will work
#                 # The best would be to get access to Cloud Shell and make this huge hack redundant
#                 # it would be more fun to build more functions into the program than to fix this stupid web stuff
#
#                 # ok here is the dirty fix:
#
#                 # Ignore it, it is still not working. BUT: Cloud Shell is! Horray!
#                 # There is still a little exception: adding a license is still a web process. But its much much faster now and even more robust.
#                 # Only two buttons needed to be clicked
#
#                 # Some distant future somebody may help me to fix this problem by giving me the rights to do that or
#                 # by adding the license to the Empfang group. Maybe some day...
#                 # I need a license administrator, user administrator, or global administrator account.
#                 # I'm account admin.
#
#                 group_list = []
#
#                 if user['empfang'] == 2:
#                     group_list.append("Empfang")
#                     row_content[11] = 'x'
#                 if user['kundenservice'] == 2:
#                     group_list.append("Kundenservice")
#                     row_content[12] = 'x'
#                 if user['it_support'] == 2:
#                     group_list.append("IT-Support")
#                     row_content[13] = 'x'
#                 if user['grafikdesign'] == 2:
#                     group_list.append("Grafikdesign")
#                     row_content[14] = 'x'
#                 if user['diversity'] == 2:
#                     group_list.append("Diversity")
#                     row_content[15] = 'x'
#                 if user['finanzanalyse'] == 2:
#                     group_list.append("Finanzanalyse")
#                     row_content[16] = 'x'
#                 if user['dig_arbeitsplatz'] == 2:
#                     group_list.append("Digitaler Arbeitsplatz")
#                     row_content[17] = 'x'
#                 if user['it_administration'] == 2:
#                     group_list.append("IT-Administration")
#                     row_content[18] = 'x'
#                 if user['projektmanagement'] == 2:
#                     group_list.append("Projektmanagement")
#                     row_content[19] = 'x'
#                 if user['dig_marketing'] == 2:
#                     group_list.append("Digitales Marketing")
#                     row_content[20] = 'x'
#                 if user['mc_adf'] == 2:
#                     group_list.append("Azure Data")
#                     row_content[21] = 'x'
#                 if user['vertrieb_verkauf'] == 2:
#                     group_list.append("Vertrieb")
#                     row_content[22] = 'x'
#                 if user['mc_af'] == 2:
#                     group_list.append("Azure")
#                     row_content[23] = 'x'
#                 if user['soft_skills'] == 2:
#                     group_list.append("Soft Skills")
#                     row_content[24] = 'x'
#                 if user['jobcoaching'] == 2:
#                     group_list.append("Jobsuche")
#                     row_content[25] = 'x'
#                 if user['mc_aaf'] == 2:
#                     group_list.append("Azure AI")
#                     row_content[26] = 'x'
#                 if user['softwareentwicklung'] == 2:
#                     group_list.append("Softwareentwicklung")
#                     row_content[27] = 'x'
#                 if user['datenanalyse'] == 2:
#                     group_list.append("Datenanalyse")
#                     row_content[28] = 'x'
#                 else:
#                     self.signals.error.emit("Keine Gruppen ausgewählt!")
#
#                 self.signals.progress.emit(80)
#
#                 self.signals.error.emit("Es werden " + str(len(group_list)) + " Gruppen zugewiesen.")
#
#                 for nr, entry in enumerate(group_list):
#                     driver.find_element_by_xpath("//span[text()='Assign memberships']").click()
#                     driver.find_element_by_xpath("//div[text()='{}']".format(entry)).click()
#                     driver.find_element_by_xpath("//span[starts-with(text()='Add')]").click()
#                     self.signals.error.emit("Gruppe " + entry + " hinzugefügt.")
#                     self.signals.progress.emit(80 + nr)
#
#                 # # driver.find_element_by_css_selector("div[data-focuszone-id='{}']").format(test[1].get_attribute("data-focuszone-id")).click()
#
#                 # #time.sleep(3)
#                 # try:
#                 #     driver.find_element_by_xpath("//span[text()='Assign memberships']").click()
#                 #     #driver.find_element_by_css_selector("button[data-hint='Admin_EditUserGroups']").click()
#                 #     #driver.find_element_by_id("AddMemberships").click()
#                 #     #driver.find_element_by_xpath("//div[contains(., 'Add memberships')]").click()
#                 # except:
#                 #     pass
#                 #     #print("Can't click Button: AddMemebership... starting over again!")
#                 #     #groups_setup()
#
#                 # self.signals.progress.emit(80)
#
#                 # checklist = driver.find_elements_by_css_selector("div[aria-selected='true']")
#
#                 # driver.find_element_by_xpath("//span[start-with(text()='Add')]").click()
#                 # driver.find_element_by_id("id__1142").click()
#
#                 try:
#                     errormsg = driver.find_element_by_xpath("//p[text()='Please select a group.']").text
#                     print(errormsg)
#                     row_content[10] = "keine Änderung"
#                     write_csv()
#                     self.signals.error.emit("Keine neuen Gruppen zugewiesen.")
#                     close_driver()
#                     self.signals.progress.emit(100)
#                     return
#                 except:
#                     pass
#
#                 self.signals.progress.emit(90)
#
#                 try:
#                     errormsg = ''
#                     errormsg = driver.find_element_by_xpath("//div[contains(., 'Failed  for:')]")
#                     print(errormsg)
#                     self.signals.error.emit("Teams Zuweisungfehler: Neuer Versuch")
#                     if (errormsg != ''):
#                         groups_setup()
#                         return
#                 except NoSuchElementException as ex:
#                     write_csv()
#                     self.signals.error.emit("Account erfolgreich eingerichtet")
#                     close_driver()
#                     self.signals.progress.emit(100)
#                     return
#
#         def delete_user():
#             driver.get("https://admin.microsoft.com/AdminPortal/Home?#/users")
#
#             element = driver.find_element_by_css_selector(
#                 "input[data-automation-id='UserListV2,CommandBarSearchInputBox']")
#             element.send_keys(user['fname'], " ", user['lname'])
#             element.send_keys(Keys.ENTER)
#             # time.sleep(2)
#             driver.find_element_by_css_selector("span[title='{} {}']".format(user['fname'], user['lname'])).click()
#
#             # time.sleep(2)
#             driver.find_element_by_css_selector("span[title='TestVorname TestNachname']").click()
#
#             driver.find_element_by_xpath("//span[text()='Delete user']").click()
#
#             driver.find_element_by_xpath("//span[text()='Delete user']").click()
#
#             driver.find_element_by_css_selector("i[data-icon-name='ChromeClose']").click()
#
#             try:
#                 driver.find_element_by_css_selector("button[data-automationid='splitbuttonprimary']").click()
#                 print("Clear search box")
#             except NoSuchElementException as ex:
#                 pass
#
#         def close_driver():
#             # time.sleep(1)
#             print(row_content)
#             driver.quit()
#             print("Browser closed.")
#
#         def append_list_as_row(file_name, row_content):
#             # Open file in append mode
#             with open(file_name, encoding='utf-8', mode='a+', newline='') as write_obj:
#                 # Create a writer object from csv module
#                 csv_writer = writer(write_obj)
#                 # Add contents of list as last row in the csv file
#                 csv_writer.writerow(row_content)
#
#         def write_csv():
#             append_list_as_row('newAccounts.csv', row_content)
#             increase_row_by_one()
#
#         def get_row_number():
#             row_number = open("row_number.txt", encoding='utf-8', mode='r')
#             content = row_number.readline()
#             row_number.close()
#             return content
#
#         def increase_row_by_one():
#             if (behavior_control['read_from_list'] == True):
#                 row_number = int(get_row_number())
#                 row_number += 1
#
#                 row_text_file = open("row_number.txt", encoding='utf-8', mode='w')
#                 row_text_file.write(str(row_number))
#                 row_text_file.close()
#                 print("New row number: ")
#                 behavior_control['read_from_list'] = False
#                 print(row_number)
#
#         def get_ready_again():
#             import gui
#             gui.MainWindow().button_toggle()
#
#         def setup_process():
#             try:
#                 try:
#                     driver.get("https://admin.microsoft.com/AdminPortal/#/users")
#                 except WebDriverException:
#                     close_driver()
#                     print("Can not reach login site.")
#                     self.signals.progress.emit(0)
#                     self.signals.error.emit("Kann Webseite nicht erreichen: Abbruch")
#                     return
#
#                 login()
#
#                 # registration()
#
#                 # groups_setup()
#
#             finally:
#                 driver.quit()
#
#             return
#
#         setup_process()
#
#         # delete_user()
#
#         # close_driver()
#
#         # get_ready_again()
