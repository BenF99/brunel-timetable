from webbot import Browser

class viewTimetable():

    def __init__(self, student_id, password): 
        self.student_id = student_id
        self.password = password

    def loginBrunel(self):
        driver = Browser()
        driver.go_to('https://teaching.brunel.ac.uk/SWS-1920/login.aspx')
        driver.type(self.student_id , id = 'tUserName')
        driver.type(self.password , id = 'tPassword')
        driver.click('Login')
        driver.click(id = 'LinkBtn_mystudentsettimetable')
        driver.click('View Timetable')
        driver.save_screenshot(PATH)

        
lb = viewTimetable(STUDENT_ID, PASSWORD)
lb.loginBrunel()
          
    


        
        
        

        
          
    
