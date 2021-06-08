from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WEBCAMPUS_URL = 'https://webcampus.bmsce.in/student'
FEEDBACK_URL = 'https://webcampus.bmsce.in/student/feedbackFaculty/'
USN = 'your_usn'
PASSWORD = 'your_password'

# set webdriver to browser you intend to run this on
driver = webdriver.Chrome()
# driver = webdriver.Firefox()

def screamErrorAndQuit(msg):
    print(f'ERROR: {msg}')
    driver.quit()
    exit(1)

def autoFeedback():
    driver.get(WEBCAMPUS_URL)

    usn_field = driver.find_element_by_id('usn')
    usn_field.send_keys(USN)

    pass_field = driver.find_element_by_id('password')
    pass_field.send_keys(PASSWORD)

    signin_btn = driver.find_element_by_xpath('/html/body/div/div/div/form/div/div/button')
    signin_btn.click()

    try:
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "page-profile"))
        )
    except:
        screamErrorAndQuit('Wrong login details!')
    print('signed in')

    print('ok')
    # feedback_btn = driver.find_element_by_partial_link_text('https://webcampus.bmsce.in/student/feedbackFaculty/')
    view_btns = driver.find_elements_by_partial_link_text('View')
    for view_btn in view_btns:
        print(view_btn.get_attribute('href'))
        if FEEDBACK_URL in view_btn.get_attribute('href'):
            feedback_btn = view_btn
    
    feedback_btn.click()

    try:
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Back to Feedback List'))
        )
    except:
        # screamErrorAndQuit("Couldn't get to feedback page :(")
        print('rip')
    print('In feedback page')

    feedback_urls = []
    course_btns = driver.find_elements_by_link_text('Give Feedback')
    for course_btn in course_btns:
        # if course_btn.get_attribute('href')
        # driver.get()
        feedback_urls.append(course_btn.get_attribute('href'))
    
    print(feedback_urls)
    driver.get(feedback_urls[0])
    
    feedback_form = driver.find_element_by_id('js_dataTable1')
    rows = feedback_form.find_elements_by_tag_name('tr')
    for row in rows:
        col = row.find_elements_by_tag_name('td')
        # print(col.text)




def main():
    autoFeedback()

if __name__ == "__main__":
    main()