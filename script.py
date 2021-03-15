from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyvirtualdisplay import Display
import pickle
import time
import json
import os

# global variable
driver = webdriver.Chrome()

def headless():
    display = Display(visible=0, size=(800, 600))
    display.start()
    options= Options()
    options.add_argument("--headless")

def screen_clear():
       # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

def ask_user ():
        while(1):
            x = input("Do you want to fill the form with default values ? [Y/n] ")
        if x  in set(("Y","y","")): 
            print("filling the forms with the default values")
            print("pleas wait ....")
        elif x in set(("n","no","No","N")):
            print("changing to fill the forms manually ......")
            screen_clear()
            # fill_morning_session_P2P
            input_morning_session_P2P()
            # fill_daily_standup
            input_fill_daily_standup()
            
def input_morning_session_P2P():
    print("Please select your role during this Morning Session.")
    print("1-Master of the meeting\n2- Presenter\n3-Code Reviewer")
    global role
    print("Did the presenter speak loud enough? [Yes/No]")
    global presenter_sound_level
    print("Presenter performance - on a scale of 1-5 (1 - very difficult, 5 -very easy), how easy it was to understand the presenter's wording?")
    global preseneter_understand_level
    print("Did the presenter provide a clear description of the project context?")
    print("1-Yes, the presentation was well structured and easy to follow.")
    print("2-Yes, but we needed to ask a few additional questions.")
    print("3-Not really, we needed to ask a lot of questions to guide the presenter.")
    print("4-Not at all, the impression was that presenter is not talking about their own work.")
    global presenter_clear_context
    global presenter_clear_code
    global presenter_feedback_respond
    global gh_link
    global rate_session
    global anything_to_add

    role.click()
    presenter_sound_level.click()
    preseneter_understand_level.click()
    presenter_clear_context.click()
    presenter_clear_code.click()
    presenter_feedback_respond.click()
    gh_link.send_keys("https://github.com/Anas-jaf")
    rate_session.click()
    anything_to_add.send_keys("I Have Nothing to Add")


def input_fill_daily_standup():
    global achive_opts_select
    global went_well
    global sth_blocked_you_select
    global goal_1
    global goal_2
    global goal_3
    global to_ensure
    global emotion_select

def go_to_dashboard ():
    driver.get("https://dashboard.microverse.org/")
    load_cookie()
    try:
        load_cookie
    except:
        create_cookie()
        load_cookie()
        
def create_cookie():
    f= open("cookie.json","w+")
    f.close()
    cookies = pickle.load(open("cookie.json", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
        with open('cookie.json', 'r', newline='') as inputdata:
            cookies = json.loads(inputdata.read())
    curcookie = cookies[0].pop('sameSite')
    input("Enter your login credintials and press any key ...")
    pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))

def load_cookie():
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    # ~ driver.add_cookie(curcookie)
    print("adding the microverse cookie !")
    # ~ time.sleep(5)

def fill_daily_standup(start=None):
    # ~ driver.get("https://dashboard.microverse.org/standups/new")
    driver.get("https://dashboard.microverse.org/standups/new?submitted_date=2021-03-%s" %start) 
    wait = WebDriverWait(driver, 30)
    wait.until(EC.presence_of_element_located((By.ID , "standup_achieved_goals")))
    
    achive_opts_select = driver.find_element(By.ID ,"standup_achieved_goals")
    went_well = driver.find_element(By.ID ,"standup_upsides") 
    sth_blocked_you_select = driver.find_element_by_xpath('//*[@id="blockers_none"]')

    goal_1 = driver.find_element(By.ID ,"goals_1")
    goal_2 = driver.find_element(By.ID ,"goals_2")
    goal_3 = driver.find_element(By.ID ,"goals_3")
    to_ensure = driver.find_element(By.ID ,"standup_goals_confidence")
    emotion_select = driver.find_element(By.ID ,"motivation_1")
    submite = driver.find_element(By.CLASS_NAME ,"form-submit-button")

    # ==================================================================================
    drp = Select(achive_opts_select)
    drp.select_by_index(1)
    # ~ sth_blocked_you_select.click()
    went_well.send_keys("almost every thing")
    sth_blocked_you_select.click()
    goal_1.send_keys("complete my curriculum learning")
    goal_2.send_keys("work in the project milestone")
    goal_3.send_keys("finishing the the project review")

    to_ensure.send_keys("i will work more ")

    emotion_select.click()

    submite.click()

def fill_morning_session_P2P(start=None):
    # https://dashboard.microverse.org/code_review_sessions/new?submitted_date=2021-02-16
    # driver.get("https://dashboard.microverse.org/code_review_sessions/new?submitted_date=2021-02-16")
    # ~ driver.get("https://dashboard.microverse.org/code_review_sessions/new?submitted_date=2021-02-%d" %start)
    # ~ driver.get("https://dashboard.microverse.org/code_review_sessions/new?submitted_date=2021-03-%s" %start)
    driver.get("https://dashboard.microverse.org/code_review_sessions/new")
    role = driver.find_element(By.XPATH , "/html/body/div[1]/div/main/div/div/div/div/form/div[1]/div[2]/div/label[3]")
    presenter_sound_level = driver.find_element(By.XPATH , "/html/body/div[1]/div/main/div/div/div/div/form/div[1]/div[3]/div/label[1]")
    preseneter_understand_level = driver.find_element(By.XPATH , "/html/body/div[1]/div/main/div/div/div/div/form/div[1]/div[4]/div/label[4]")
    presenter_clear_context = driver.find_element(By.XPATH , "/html/body/div[1]/div/main/div/div/div/div/form/div[1]/div[5]/div/label[2]")
    presenter_clear_code = driver.find_element(By.XPATH , "/html/body/div[1]/div/main/div/div/div/div/form/div[1]/div[6]/div/label[2]")
    presenter_feedback_respond = driver.find_element(By.XPATH , "/html/body/div[1]/div/main/div/div/div/div/form/div[1]/div[7]/div/label[2]")
    gh_link = driver.find_element(By.ID , "code_review_session_github_link")
    rate_session = driver.find_element(By.ID , "overall_rating_1")
    anything_to_add = driver.find_element(By.ID , "code_review_session_comments")
    submite = driver.find_element(By.CLASS_NAME ,"form-submit-button")
    # ==========================================================================
    role.click()
    presenter_sound_level.click()
    preseneter_understand_level.click()
    presenter_clear_context.click()
    presenter_clear_code.click()
    presenter_feedback_respond.click()
    gh_link.send_keys("https://github.com/Anas-jaf")
    rate_session.click()
    anything_to_add.send_keys("I Have Nothing to Add")
    submite.click()

def fill_retrospective(month=None , day=None):
    driver.get("https://dashboard.microverse.org/retrospectives/new?submitted_date=2021-%s-%s" % (month ,day))
    # https://dashboard.microverse.org/retrospectives/new?submitted_date=2021-02-19
    achived_goals = driver.find_element(By.ID , "retrospective_goal_achievement" )
    sth_blocked_u = driver.find_element(By.ID , "retrospective_blockers_none")
    went_well = driver.find_element(By.ID , "retrospective_upsides")
    next_goal_1 = driver.find_element(By.ID , "retrospective_goals_1")
    next_goal_2 = driver.find_element(By.ID , "retrospective_goals_2")
    next_goal_3 = driver.find_element(By.ID , "retrospective_goals_3")
    to_ensure = driver.find_element(By.ID , "retrospective_action_items")
    coding_partner_is = driver.find_element(By.ID , "retrospective_partner_learn_style_feedback_a_good_communicator")
    pair_programming = driver.find_element(By.ID , "retrospective_switch_roles_sometimes")
    my_mentor_is = driver.find_element(By.ID , "retrospective_mentor_feedback_helpful")
    standupteam_injoyment = driver.find_element(By.ID , "retrospective_standup_enjoyment")
    follow_daily_structure = driver.find_element(By.ID , "retrospective_standup_team_alignment_feedback")
    network_activity = driver.find_element(By.ID , "retrospective_networking_activity")
    recommend_microverse = driver.find_element(By.ID , "retrospective_recommend_microverse")
    submite = driver.find_element(By.CLASS_NAME ,"form-submit-button")
    # ====================================================================================================
    Select(achived_goals).select_by_index(1)
    sth_blocked_u.click()
    went_well.send_keys("almost everything")
    next_goal_1.send_keys("finishing all projects of the week")
    next_goal_2.send_keys("doing at least 10 coding challenges")
    next_goal_3.send_keys("finishing the professional projects or tasks")
    to_ensure.send_keys("I will make sure to work more and learn more")
    coding_partner_is.click()
    pair_programming.click()
    my_mentor_is.click()
    Select(standupteam_injoyment).select_by_index(6)
    Select(follow_daily_structure).select_by_index(2)
    Select(network_activity).select_by_index(1)
    Select(recommend_microverse).select_by_index(8)
    # ~ submite.click() 

if __name__ == "__main__":

    go_to_dashboard()
    # fill_daily_standup()
    # ~ for x in (18 , 25 , 27):
        # ~ x= str(x).zfill(2)
        # ~ fill_morning_session_P2P(x)
        # ~ fill_daily_standup(x)
    # ~ 2/19 2/26 1/3 12/3



            
    # x=5
    # month="03"  
    # x= str(x).zfill(2)
    # fill_retrospective(month , x)
        
    # ~ fill_morning_session_P2P()
    # ~ fill_retrospective()
