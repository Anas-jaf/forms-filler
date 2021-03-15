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
            wizard_morning_session_P2P()
            # fill_daily_standup
            wizard_fill_daily_standup()

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

def wizard_morning_session_P2P():
    while(1):
        print("Please select your role during this Morning Session. ")
        print("1- Master of the meeting\n2- Presenter\n3- Code Reviewer")
        role_input = int(input("choose one : "))
        if role_input == 1:
            role_input = '//*[@id="new_code_review_session"]/div[1]/div[2]/div/label[1]'
        elif role_input == 2:
            role_input = '//*[@id="new_code_review_session"]/div[1]/div[2]/div/label[2]'
            
        elif role_input == 3:
            role_input = '//*[@id="new_code_review_session"]/div[1]/div[2]/div/label[3]'
            
        else:
            print("Invalid option")

    print("Did the presenter speak loud enough?\n1- yes\n2- no")
    presenter_sound_level_input = int(input("choose number : "))
    if presenter_sound_level_input == 1:
        presenter_sound_level_input = '//*[@id="new_code_review_session"]/div[1]/div[3]/div/label[1]'
    elif presenter_sound_level_input ==2:
        presenter_sound_level_input = '//*[@id="new_code_review_session"]/div[1]/div[3]/div/label[2]'
    else : 
        print("invalid option")
                
    print("Presenter performance - on a scale of 1-5 (1 - very difficult, 5 -very easy), how easy it was to understand the presenter's wording?")
    preseneter_understand_level_input = int(input("choose number : "))
    if preseneter_understand_level_input == 0 :
        preseneter_understand_level_input ='//*[@id="new_code_review_session"]/div[1]/div[4]/div/label[1]'
    elif preseneter_understand_level_input == 1 :
        preseneter_understand_level_input ='//*[@id="new_code_review_session"]/div[1]/div[4]/div/label[2]'
    elif preseneter_understand_level_input == 2 :
        preseneter_understand_level_input ='//*[@id="new_code_review_session"]/div[1]/div[4]/div/label[3]'
    elif preseneter_understand_level_input == 3 :
        preseneter_understand_level_input ='//*[@id="new_code_review_session"]/div[1]/div[4]/div/label[4]'
    elif preseneter_understand_level_input == 4 :
        preseneter_understand_level_input ='//*[@id="new_code_review_session"]/div[1]/div[4]/div/label[5]'
    elif preseneter_understand_level_input == 4 :
        preseneter_understand_level_input ='//*[@id="new_code_review_session"]/div[1]/div[4]/div/label[6]'
    else : 
        print("invalid option")

    print("Did the presenter provide a clear description of the project context?")
    print("1-Yes, the presentation was well structured and easy to follow.")
    print("2-Yes, but we needed to ask a few additional questions.")
    print("3-Not really, we needed to ask a lot of questions to guide the presenter.")
    print("4-Not at all, the impression was that presenter is not talking about their own work.")
    presenter_clear_context_input = int(input("choose number : "))
    if preseneter_understand_level_input == 1 :
        presenter_clear_context_input = '//*[@id="new_code_review_session"]/div[1]/div[5]/div/label[1]'
    elif preseneter_understand_level_input == 2 :
        presenter_clear_context_input = '//*[@id="new_code_review_session"]/div[1]/div[5]/div/label[2]'
    elif preseneter_understand_level_input == 3 :
        presenter_clear_context_input = '//*[@id="new_code_review_session"]/div[1]/div[5]/div/label[3]'
    elif preseneter_understand_level_input == 4 :
        presenter_clear_context_input = '//*[@id="new_code_review_session"]/div[1]/div[5]/div/label[4]'
    else : 
        print("invalid option")

    print("Did the presenter give a clear presentation of the code?")
    print("1- Yes, the presentation was well structured and easy to follow.")
    print("2- Yes, but we needed to ask a few additional questions.")
    print("3- Not really, we needed to ask a lot of questions to guide the presenter.")
    print("4- Not at all, the impression was that presenter is not talking about their own work.")
    presenter_clear_code_input = int(input("choose number : "))
    if presenter_clear_code_input ==1:
        preseneter_understand_level_input='//*[@id="new_code_review_session"]/div[1]/div[6]/div/label[1]'
    elif presenter_clear_code_input ==2:
        preseneter_understand_level_input='//*[@id="new_code_review_session"]/div[1]/div[6]/div/label[2]'
    elif presenter_clear_code_input ==3:
        preseneter_understand_level_input='//*[@id="new_code_review_session"]/div[1]/div[6]/div/label[3]'
    elif presenter_clear_code_input ==4:
        preseneter_understand_level_input='//*[@id="new_code_review_session"]/div[1]/div[6]/div/label[4]'
    else : 
        print("invalid option")

    print("How did the presenter respond to the given feedback?")
    print("1- The presenter was super happy because they were stuck and given feedback help them to move forward.")
    print("2- The presenter was happy to discover some room for improvements.")
    print("3- The presenter was unhappy with the given feedback but was discussing it in a polite way.")
    print("4- The presenter was unhappy with given feedback and rude to other team members.")
    presenter_feedback_respond_input = int(input("choose number : "))
    if presenter_feedback_respond_input == 1:
        presenter_feedback_respond_input = '//*[@id="new_code_review_session"]/div[1]/div[7]/div/label[1]'
    elif presenter_feedback_respond_input == 2:
        presenter_feedback_respond_input = '//*[@id="new_code_review_session"]/div[1]/div[7]/div/label[2]'
    elif presenter_feedback_respond_input == 3:
        presenter_feedback_respond_input = '//*[@id="new_code_review_session"]/div[1]/div[7]/div/label[3]'
    elif presenter_feedback_respond_input == 4:
        presenter_feedback_respond_input = '//*[@id="new_code_review_session"]/div[1]/div[7]/div/label[4]'
    else : 
        print("invalid option")        

    gh_link_input = input("Please enter the link to a Github issue you created with your team.")

    print("How would you rate this Morning Session?")
    print("1- 😃\n2- 🙂\n3- 😐\n4- 🙁\n")
    rate_session_input = int(input("choose number : "))
    if rate_session_input == 1:
        rate_session_input= '//*[@id="new_code_review_session"]/div[1]/div[9]/div/label[1]'
    elif rate_session_input == 2:
        rate_session_input= '//*[@id="new_code_review_session"]/div[1]/div[9]/div/label[2]'
    elif rate_session_input == 3:
        rate_session_input= '//*[@id="new_code_review_session"]/div[1]/div[9]/div/label[3]'
    elif rate_session_input == 4:
        rate_session_input= '//*[@id="new_code_review_session"]/div[1]/div[9]/div/label[4]'                        
    else : 
        print("invalid option")
        
    anything_to_add = input("Do you have anything you’d like to add about this Morning Session? (Optional) ")
    # role_input ="/html/body/div[1]/div/main/div/div/div/div/form/div[1]/div[2]/div/label[3]"
    # presenter_sound_level_input ="/html/body/div[1]/div/main/div/div/div/div/form/div[1]/div[3]/div/label[1]"
    # preseneter_understand_level_input ="/html/body/div[1]/div/main/div/div/div/div/form/div[1]/div[4]/div/label[4]"
    # presenter_clear_context_input ="/html/body/div[1]/div/main/div/div/div/div/form/div[1]/div[5]/div/label[2]"
    # presenter_clear_code_input ="/html/body/div[1]/div/main/div/div/div/div/form/div[1]/div[6]/div/label[2]"
    # presenter_feedback_respond_input ="/html/body/div[1]/div/main/div/div/div/div/form/div[1]/div[7]/div/label[2]"
    # gh_link_input ="code_review_session_github_link"
    # rate_session_input ="overall_rating_1"
    # anything_to_add ="code_review_session_comments"

    fill_morning_session_P2P(role_input, presenter_sound_level_input, preseneter_understand_level_input, presenter_clear_context_input, presenter_clear_code_input, presenter_feedback_respond_input, gh_link_input, rate_session_input, anything_to_add)
    
def wizard_fill_daily_standup():
    print("Did you achieve your goals from yesterday?")
    print("1- Yes, all of them \n2- Some of them \n3- None of them ")
    achive_opts_select = int(input("choose one : "))
    if achive_opts_select not in set((1,2,3)):
        print("invalid option")

    went_well_input = input("What went well today?")
    
    print("What (if anything) blocked you from achieving your goals today")
    print("1- None\n")
    print("2- Coding Partner Issues\n")
    print("3- Personal Problems\n")
    print("4- Financial Problems\n")
    print("5- Not reaching out for help from others\n")
    print("6- Low Productivity\n")
    print("7- Low Confidence\n")
    print("8- High Stress Levels\n")
    print("9- Tiredness\n")
    print("10- Low Understanding of Topic\n")
    print("11- Low English Ability\n")
    print("12- Poor Time Management\n")
    print("13- Low Motivation\n")
    print("14- Being Absent\n")
    print("15- Illness\n")
    print("16- Electricity Problems\n")
    print("17- Internet Problems\n")
    print("18- Hardware Issues\n")
    print("19- Waiting for Re-pair\n")
    print("20- Working Alone\n")
    print("21- Problematic Code Reviews\n")
    print("22- Waiting for Code Reviews\n")
    print("23- Inadequate Learning Materials\n")
    sth_blocked_you_select_input_xpath = int(input("choose one : "))
    if sth_blocked_you_select_input_xpath == 1 :
        sth_blocked_you_select_input_xpath = '//*[@id="new_standup"]/div[1]/div[4]/div/div[1]/div[1]'
    elif sth_blocked_you_select_input_xpath == 2 :
        sth_blocked_you_select_input_xpath = '//*[@id="new_standup"]/div[1]/div[4]/div/div[1]/div[2]'
    elif sth_blocked_you_select_input_xpath == 3 :
        sth_blocked_you_select_input_xpath = '//*[@id="new_standup"]/div[1]/div[4]/div/div[1]/div[3]'
    elif sth_blocked_you_select_input_xpath == 4 :
        sth_blocked_you_select_input_xpath = '//*[@id="new_standup"]/div[1]/div[4]/div/div[1]/div[4]'
    elif sth_blocked_you_select_input_xpath == 5 :
        sth_blocked_you_select_input_xpath = '//*[@id="new_standup"]/div[1]/div[4]/div/div[1]/div[5]'
    elif sth_blocked_you_select_input_xpath == 6 :
        sth_blocked_you_select_input_xpath = '//*[@id="new_standup"]/div[1]/div[4]/div/div[1]/div[6]'

    elif sth_blocked_you_select_input_xpath == 7 :
        sth_blocked_you_select_input_xpath = '//*[@id="new_standup"]/div[1]/div[4]/div/div[2]/div[1]'
    elif sth_blocked_you_select_input_xpath == 8 :
        sth_blocked_you_select_input_xpath = '//*[@id="new_standup"]/div[1]/div[4]/div/div[2]/div[2]'
    elif sth_blocked_you_select_input_xpath == 9 :
        sth_blocked_you_select_input_xpath = '//*[@id="new_standup"]/div[1]/div[4]/div/div[2]/div[3]'
    elif sth_blocked_you_select_input_xpath == 10 :
        sth_blocked_you_select_input_xpath = '//*[@id="new_standup"]/div[1]/div[4]/div/div[2]/div[4]'
    elif sth_blocked_you_select_input_xpath == 11 :
        sth_blocked_you_select_input_xpath = '//*[@id="new_standup"]/div[1]/div[4]/div/div[2]/div[5]'
    elif sth_blocked_you_select_input_xpath == 12 :
        sth_blocked_you_select_input_xpath = '//*[@id="new_standup"]/div[1]/div[4]/div/div[2]/div[6]'        

    elif sth_blocked_you_select_input_xpath == 13 :
        sth_blocked_you_select_input_xpath = '//*[@id="new_standup"]/div[1]/div[4]/div/div[3]/div[1]'
    elif sth_blocked_you_select_input_xpath == 14 :
        sth_blocked_you_select_input_xpath = '//*[@id="new_standup"]/div[1]/div[4]/div/div[3]/div[2]'
    elif sth_blocked_you_select_input_xpath == 15 :
        sth_blocked_you_select_input_xpath = '//*[@id="new_standup"]/div[1]/div[4]/div/div[3]/div[3]'
    elif sth_blocked_you_select_input_xpath == 16 :
        sth_blocked_you_select_input_xpath = '//*[@id="new_standup"]/div[1]/div[4]/div/div[3]/div[4]'
    elif sth_blocked_you_select_input_xpath == 17 :
        sth_blocked_you_select_input_xpath = '//*[@id="new_standup"]/div[1]/div[4]/div/div[3]/div[5]'
    elif sth_blocked_you_select_input_xpath == 18 :
        sth_blocked_you_select_input_xpath = '//*[@id="new_standup"]/div[1]/div[4]/div/div[3]/div[6]'

    elif sth_blocked_you_select_input_xpath == 19 :
        sth_blocked_you_select_input_xpath = '//*[@id="new_standup"]/div[1]/div[4]/div/div[4]/div[1]'
    elif sth_blocked_you_select_input_xpath == 20 :
        sth_blocked_you_select_input_xpath = '//*[@id="new_standup"]/div[1]/div[4]/div/div[4]/div[2]'
    elif sth_blocked_you_select_input_xpath == 21 :
        sth_blocked_you_select_input_xpath = '//*[@id="new_standup"]/div[1]/div[4]/div/div[4]/div[3]'
    elif sth_blocked_you_select_input_xpath == 22 :
        sth_blocked_you_select_input_xpath = '//*[@id="new_standup"]/div[1]/div[4]/div/div[4]/div[4]'
    elif sth_blocked_you_select_input_xpath == 23 :
        sth_blocked_you_select_input_xpath = '//*[@id="new_standup"]/div[1]/div[4]/div/div[4]/div[5]'

    print("What are your three goals for tomorrow? ")
    print(" goal 1 ?")
    goal_1_input = input("goal 1 ? ")
    goal_2_input = input("goal 2 ? ")
    goal_3_input = input("goal 3 ? ")

    print("What will you do tomorrow to ensure you reach your goals? ")
    to_ensure_input = input("please enter here :")

    print("What was your overall motivation level today?")
    print("1- 😃\n2- 🙂\n3- 😐\n4- 🙁\n")
    emotion_select_option = int(input("choose one : "))
    if emotion_select_option  == 1:
        emotion_select_option = 'motivation_0'
    elif emotion_select_option  == 2:
        emotion_select_option = 'motivation_2'
    elif emotion_select_option  == 3:
        emotion_select_option = 'motivation_3'
    elif emotion_select_option  == 4:
        emotion_select_option = 'motivation_4'
    # achive_opts_select = 1 
    # went_well_input = almost every thing
    # sth_blocked_you_select_input_xpath =
    # goal_1_input = "complete my curriculum learning"
    # goal_2_input = "work in the project milestone"
    # goal_3_input = "finishing the the project review"
    # to_ensure_input = "i will work more "
    # emotion_select_option = "motivation_1"  
    
    fill_daily_standup(achive_opts_select , went_well_input ,sth_blocked_you_select_input_xpath ,goal_1_input ,goal_2_input ,goal_3_input ,to_ensure_input ,emotion_select_option)

def wizard_fill_retrospective():
    # Select(achived_goals).
    print("Did you achieve your goals this week?")
    
    # sth_blocked_u
    print("What (if anything) blocked you from achieving your goals today")
    print("1- None\n")
    print("2- Coding Partner Issues\n")
    print("3- Personal Problems\n")
    print("4- Financial Problems\n")
    print("5- Not reaching out for help from others\n")
    print("6- Low Productivity\n")
    print("7- Low Confidence\n")
    print("8- High Stress Levels\n")
    print("9- Tiredness\n")
    print("10- Low Understanding of Topic\n")
    print("11- Low English Ability\n")
    print("12- Poor Time Management\n")
    print("13- Low Motivation\n")
    print("14- Being Absent\n")
    print("15- Illness\n")
    print("16- Electricity Problems\n")
    print("17- Internet Problems\n")
    print("18- Hardware Issues\n")
    print("19- Waiting for Re-pair\n")
    print("20- Working Alone\n")
    print("21- Problematic Code Reviews\n")
    print("22- Waiting for Code Reviews\n")
    print("23- Inadequate Learning Materials\n")
    sth_blocked_you_select_input_xpath = int(input("choose one : "))
    if sth_blocked_you_select_input_xpath == 1 :
        sth_blocked_you_select_input_xpath = "retrospective_blockers_none"
    elif sth_blocked_you_select_input_xpath == 2 :
        sth_blocked_you_select_input_xpath = "retrospective_blockers_i_did_not_set_goals_last_week"
    elif sth_blocked_you_select_input_xpath == 3 :
        sth_blocked_you_select_input_xpath = "retrospective_blockers_coding_partner_issues"
    elif sth_blocked_you_select_input_xpath == 4 :
        sth_blocked_you_select_input_xpath = "retrospective_blockers_partners_electricity"
    elif sth_blocked_you_select_input_xpath == 5 :
        sth_blocked_you_select_input_xpath = "retrospective_blockers_partners_absence"
    elif sth_blocked_you_select_input_xpath == 6 :
        sth_blocked_you_select_input_xpath = "retrospective_blockers_partners_internetelectricity"

    elif sth_blocked_you_select_input_xpath == 7 :
        sth_blocked_you_select_input_xpath = "retrospective_blockers_partners_hardware_problems"
    elif sth_blocked_you_select_input_xpath == 8 :
        sth_blocked_you_select_input_xpath = "retrospective_blockers_partners_english_level"
    elif sth_blocked_you_select_input_xpath == 9 :
        sth_blocked_you_select_input_xpath = "retrospective_blockers_partners_pace"
    elif sth_blocked_you_select_input_xpath == 10 :
        sth_blocked_you_select_input_xpath = "retrospective_blockers_personal_problems"
    elif sth_blocked_you_select_input_xpath == 11 :
        sth_blocked_you_select_input_xpath = "retrospective_blockers_financial_problems"
    elif sth_blocked_you_select_input_xpath == 12 :
        sth_blocked_you_select_input_xpath = "retrospective_blockers_not_reaching_out_for_help_from_others"

    elif sth_blocked_you_select_input_xpath == 13 :
        sth_blocked_you_select_input_xpath = "retrospective_blockers_low_productivity"
    elif sth_blocked_you_select_input_xpath == 14 :
        sth_blocked_you_select_input_xpath = "retrospective_blockers_low_confidence"
    elif sth_blocked_you_select_input_xpath == 15 :
        sth_blocked_you_select_input_xpath = "retrospective_blockers_high_stress_levels"
    elif sth_blocked_you_select_input_xpath == 16 :
        sth_blocked_you_select_input_xpath = "retrospective_blockers_tiredness"
    elif sth_blocked_you_select_input_xpath == 17 :
        sth_blocked_you_select_input_xpath = "retrospective_blockers_low_understanding_of_topic"
    elif sth_blocked_you_select_input_xpath == 18 :
        sth_blocked_you_select_input_xpath = "retrospective_blockers_low_english_ability"

    elif sth_blocked_you_select_input_xpath == 19 :
        sth_blocked_you_select_input_xpath = "retrospective_blockers_poor_time_management"
    elif sth_blocked_you_select_input_xpath == 20 :
        sth_blocked_you_select_input_xpath = "retrospective_blockers_low_motivation"
    elif sth_blocked_you_select_input_xpath == 21 :
        sth_blocked_you_select_input_xpath = "retrospective_blockers_being_absent"
    elif sth_blocked_you_select_input_xpath == 22 :
        sth_blocked_you_select_input_xpath = "retrospective_blockers_illness"
    elif sth_blocked_you_select_input_xpath == 23 :
        sth_blocked_you_select_input_xpath = "retrospective_blockers_electricity_problems"

    elif sth_blocked_you_select_input_xpath == 24 :
        sth_blocked_you_select_input_xpath = "retrospective_blockers_internet_problems"
    elif sth_blocked_you_select_input_xpath == 25 :
        sth_blocked_you_select_input_xpath = "retrospective_blockers_hardware_issues"
    elif sth_blocked_you_select_input_xpath == 26 :
        sth_blocked_you_select_input_xpath = "retrospective_blockers_waiting_for_re-pair"
    elif sth_blocked_you_select_input_xpath == 27 :
        sth_blocked_you_select_input_xpath = "retrospective_blockers_working_alone"
    elif sth_blocked_you_select_input_xpath == 28 :
        sth_blocked_you_select_input_xpath = "retrospective_blockers_problematic_code_reviews"

    elif sth_blocked_you_select_input_xpath == 29 :
        sth_blocked_you_select_input_xpath = "retrospective_blockers_waiting_for_code_reviews"
    elif sth_blocked_you_select_input_xpath == 30 :
        sth_blocked_you_select_input_xpath = "retrospective_blockers_inadequate_learning_materials"
    else :
        print("invalid option ")

    # went_well
    print("What went well this week?")
    
    print("What are your three goals for the next week?")
    # next_goal_1
    print("next_goal_1")
    # next_goal_2
    print("next_goal_2")
    # next_goal_3
    print("next_goal_3")

    # to_ensure
    print("What will you do next week to ensure you reach your goals? ")

    # coding_partner_is
    
    # pair_programming
    
    # my_mentor_is
    print("My mentor is... \n Select all that apply")
    print("1- Meeting with me weekly")
    print("2- Not Meeting with me weekly")
    print("3- Not checking on me")
    print("4- Patient")
    print("5- Helpful")
    print("6- Friendly")
    print("7- Unfriendly")
    print("8- Supportive")
    print("9- Kind")
    print("10- Always missing our meetings")
    print("11- I don't have a mentor")
    my_mentor_is = int(input("choose one : "))
    if my_mentor_is is 1:
        my_mentor_is = "retrospective_mentor_feedback_meeting_with_me_weekly"
    elif my_mentor_is is 2:
        my_mentor_is = "retrospective_mentor_feedback_not_meeting_with_me_weekly"
    elif my_mentor_is is 3:
        my_mentor_is = "retrospective_mentor_feedback_not_checking_on_me"
    elif my_mentor_is is 4:
        my_mentor_is = "retrospective_mentor_feedback_patient"
    elif my_mentor_is is 5:
        my_mentor_is = "retrospective_mentor_feedback_helpful"
    elif my_mentor_is is 6:
        my_mentor_is = "retrospective_mentor_feedback_friendly"
    elif my_mentor_is is 7:
        my_mentor_is = "retrospective_mentor_feedback_unfriendly"
    elif my_mentor_is is 8:
        my_mentor_is = "retrospective_mentor_feedback_supportive"
    elif my_mentor_is is 9:
        my_mentor_is = "retrospective_mentor_feedback_kind"
    elif my_mentor_is is 10:
        my_mentor_is = "retrospective_mentor_feedback_always_missing_our_meetings"
    elif my_mentor_is is 11:
        my_mentor_is = "retrospective_mentor_feedback_i_dont_have_a_mentor"
    else:
        print("invalid option")

    # Select(standupteam_injoyment)
    print("How much do you enjoy your Standup Team? ")
    standupteam_injoyment_select = int(input("choose number : "))
    if standupteam_injoyment_select not in set((1,2,3,4,5,6,7,8,9,10,11)):
        print("invalid option")

    # Select(follow_daily_structure)
    print("My Standup Team follows the Daily Structure...")
    print("1- Always\n2- Often\n3- Rarely\n4-Never \n")
    follow_daily_structure_select = int(input("choose number : "))
    if follow_daily_structure_select not in set((1,2,3,4)):
        print("invalid option")

    # Select(network_activity)
    print("Have you performed any networking activities this week? ")
    print("1- None")
    print("2- In-person meeting")
    print("3- Online networking ")
    print("4- Other ")
    network_activity_select = int(input("choose number : "))
    if network_activity_select not in set((1,2,3,4)):
        print("invalid option")

    # Select(recommend_microverse)
    print("On a scale of 1-10, how likely are you to recommend Microverse to a friend or colleague? ")
    recommend_microverse_select = int(input("choose number : "))
    if standupteam_injoyment_select not in set((1,2,3,4,5,6,7,8,9,10,11)):
        print("invalid option")

def fill_daily_standup(start=None , achive_opts_select = 1 , went_well_input = "almost every thing", sth_blocked_you_select_input_xpath = '//*[@id="blockers_none"]', goal_1_input = "complete my curriculum learning", goal_2_input = "work in the project milestone", goal_3_input = "finishing the the project review", to_ensure_input = "i will work more ", emotion_select_option = "motivation_1"):
    # ~ driver.get("https://dashboard.microverse.org/standups/new")
    driver.get("https://dashboard.microverse.org/standups/new?submitted_date=2021-03-%s" %start) 
    wait = WebDriverWait(driver, 30)
    wait.until(EC.presence_of_element_located((By.ID , "standup_achieved_goals")))
    
    achive_opts_select = driver.find_element(By.ID ,"standup_achieved_goals")
    went_well = driver.find_element(By.ID , "standup_upsides") 
    sth_blocked_you_select = driver.find_element(By.XPATH , sth_blocked_you_select_input_xpath)
    goal_1 = driver.find_element(By.ID ,"goals_1")
    goal_2 = driver.find_element(By.ID ,"goals_2")
    goal_3 = driver.find_element(By.ID ,"goals_3")
    to_ensure = driver.find_element(By.ID ,"standup_goals_confidence")
    emotion_select = driver.find_element(By.ID , emotion_select_option)
    submite = driver.find_element(By.CLASS_NAME ,"form-submit-button")
    # ==================================================================================
    drp = Select(achive_opts_select)
    drp.select_by_index(achive_opts_select)
    # ~ sth_blocked_you_select.click()
    went_well.send_keys(went_well_input)
    sth_blocked_you_select.click()
    goal_1.send_keys(goal_1_input)
    goal_2.send_keys(goal_2_input)
    goal_3.send_keys(goal_3_input)

    to_ensure.send_keys(to_ensure_input)

    emotion_select.click()

    submite.click()

def fill_morning_session_P2P(start=None, role_input ="/html/body/div[1]/div/main/div/div/div/div/form/div[1]/div[2]/div/label[3]", presenter_sound_level_input ="/html/body/div[1]/div/main/div/div/div/div/form/div[1]/div[3]/div/label[1]", preseneter_understand_level_input ="/html/body/div[1]/div/main/div/div/div/div/form/div[1]/div[4]/div/label[4]", presenter_clear_context_input ="/html/body/div[1]/div/main/div/div/div/div/form/div[1]/div[5]/div/label[2]", presenter_clear_code_input ="/html/body/div[1]/div/main/div/div/div/div/form/div[1]/div[6]/div/label[2]", presenter_feedback_respond_input ="/html/body/div[1]/div/main/div/div/div/div/form/div[1]/div[7]/div/label[2]", gh_link_input ="code_review_session_github_link", rate_session_input ='//*[@id="new_code_review_session"]/div[1]/div[9]/div/label[2]', anything_to_add ="code_review_session_comments"):
    # https://dashboard.microverse.org/code_review_sessions/new?submitted_date=2021-02-16
    # driver.get("https://dashboard.microverse.org/code_review_sessions/new?submitted_date=2021-02-16")
    # ~ driver.get("https://dashboard.microverse.org/code_review_sessions/new?submitted_date=2021-02-%d" %start)
    # ~ driver.get("https://dashboard.microverse.org/code_review_sessions/new?submitted_date=2021-03-%s" %start)
    driver.get("https://dashboard.microverse.org/code_review_sessions/new")
    role = driver.find_element(By.XPATH , role_input)
    presenter_sound_level = driver.find_element(By.XPATH , presenter_sound_level_input)
    preseneter_understand_level = driver.find_element(By.XPATH , preseneter_understand_level_input)
    presenter_clear_context = driver.find_element(By.XPATH , presenter_clear_context_input)
    presenter_clear_code = driver.find_element(By.XPATH , presenter_clear_code_input)
    presenter_feedback_respond = driver.find_element(By.XPATH , presenter_feedback_respond_input)
    gh_link = driver.find_element(By.ID , "code_review_session_github_link")
    rate_session = driver.find_element(By.ID , rate_session_input)
    anything_to_add = driver.find_element(By.ID , "code_review_session_comments")
    submite = driver.find_element(By.CLASS_NAME ,"form-submit-button")
    # ==========================================================================
    role.click()
    presenter_sound_level.click()
    preseneter_understand_level.click()
    presenter_clear_context.click()
    presenter_clear_code.click()
    presenter_feedback_respond.click()
    gh_link.send_keys(gh_link_input)
    rate_session.click()
    anything_to_add.send_keys(anything_to_add)
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

    # go_to_dashboard()
    # fill_daily_standup()
    # ~ for x in (18 , 25 , 27):
        # ~ x= str(x).zfill(2)
        # ~ fill_morning_session_P2P(x)
        # ~ fill_daily_standup(x)
    # ~ 2/19 2/26 1/3 12/3

    fill_morning_session_P2P()

            
    # x=5
    # month="03"  
    # x= str(x).zfill(2)
    # fill_retrospective(month , x)
        
    # ~ fill_morning_session_P2P()
    # ~ fill_retrospective()
