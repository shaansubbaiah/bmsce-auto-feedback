from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass

WEBCAMPUS_URL = 'https://webcampus.bmsce.in/student'
FEEDBACK_BASE_URL = 'https://webcampus.bmsce.in/student/feedbackFaculty/'

RATING = 'Excellent' # 'Excellent', 'Very Good', 'Good', 'Fair', 'Poor'


def screamErrorAndQuit(msg):
    print(f'ERROR: {msg}')
    driver.quit()
    exit(1)

def autoFeedback(user_usn, user_pass):
    # set webdriver to browser you intend to run this on
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox()

    driver.get(WEBCAMPUS_URL)

    usn_field = driver.find_element_by_id('usn')
    usn_field.send_keys(user_usn)

    pass_field = driver.find_element_by_id('password')
    pass_field.send_keys(user_pass)

    signin_btn = driver.find_element_by_xpath('/html/body/div/div/div/form/div/div/button')
    signin_btn.click()

    try:
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "page-profile"))
        )
    except:
        screamErrorAndQuit('Wrong login details!')
    print('Signed in.')

    feedback_page_url = ''
    # feedback_btn = driver.find_element_by_partial_link_text('https://webcampus.bmsce.in/student/feedbackFaculty/')
    view_btns = driver.find_elements_by_partial_link_text('View')
    for view_btn in view_btns:
        # print(view_btn.get_attribute('href'))
        if FEEDBACK_BASE_URL in view_btn.get_attribute('href'):
            feedback_page_url = view_btn.get_attribute('href')
            # feedback_btn = view_btn
    
    # feedback_btn.click()
    driver.get(feedback_page_url)

    # try:
    #     element = WebDriverWait(driver, 20).until(
    #         EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Back to Feedback List'))
    #     )
    # except:
    #     # screamErrorAndQuit("Couldn't get to feedback page :(")
    #     print('rip')
    print('In feedback page.')

    feedback_urls = []
    course_btns = driver.find_elements_by_link_text('Give Feedback')
    for course_btn in course_btns:
        # if course_btn.get_attribute('href')
        # driver.get()
        feedback_urls.append(course_btn.get_attribute('href'))
    
    feedback_count = len(feedback_urls)
    print('Found', str(feedback_count), 'courses that need feedback.')
    # driver.get(feedback_urls[0])
    if feedback_count > 0:
        print('Submitting feedback...')
        for feedback_url in feedback_urls:

            driver.get(feedback_url)

            breadcrumb = driver.find_element_by_class_name('breadcrumb')
            course_name = breadcrumb.find_elements_by_tag_name('li')[-1].text

            #  body > div.content.content-fixed.content-height > div > div.d-sm-flex.align-items-center.justify-content-between.mg-b-20.mg-lg-b-20.mg-xl-b-20 > div:nth-child(1) > nav > ol > li:nth-child(4)

            feedback_form = driver.find_element_by_id('js_dataTable1')
            rows = feedback_form.find_elements_by_css_selector('tbody tr')
            # print('rows = ', str(len(rows)))
            
            rating_val = {'Excellent':1, 'Very Good':2, 'Good':3, 'Fair':4, 'Poor':5}
            
            # rows 0-7 -> selection; row 8 -> custom feedback message; row 9 -> submit btn
            for row in rows[:-2]:
                cols = row.find_elements_by_tag_name('td')
                # print('cols = ', str(len(cols)))
                # cols 0,1 -> s.no, competency; cols 2-6 -> excellent, vgood, good, fair, poor 
                
                # print(cols)

                # radio_btn = cols[2].find_element_by_class_name('custom-control-input')
                radio_btn = cols[1+rating_val[RATING]]
                radio_btn.click()
            
            feedback_form.find_element_by_id('submit_feedback').click()
            print('-- Feedback for' , course_name, 'submitted.')

        print("And we're done.")
    else:
        print('Nothing to do :/')

    driver.quit()

def main():
    print('Starting bmsce-auto-feedback')
    
    print('Attempting sign in.')
    user_usn = input('-- Enter USN: ')
    user_pass = getpass('-- Enter Password: ')

    autoFeedback(user_usn, user_pass)

if __name__ == "__main__":
    main()