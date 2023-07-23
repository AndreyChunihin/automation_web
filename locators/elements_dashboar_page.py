from selenium.webdriver.common.by import By


class DashboardWidgets:
    class TimeAtWorkWidget:
        WIDGET = (By.XPATH,"//body/div[@id='app']"
                           "/div[@class='oxd-layout']"
                           "/div[@class='oxd-layout-container --collapse']"
                           "/div[@class='oxd-layout-context']"
                           "/div[@class='oxd-grid-3 "
                           "orangehrm-dashboard-grid']/div[1]/div[1]")
        WIDGET_NAME = (By.XPATH, "//p[normalize-space()='Time at Work']")

    class MyActionsWIDGET:
        WIDGET_NAME = (By.XPATH, "//p[normalize-space()='My Actions']")
        LEAVE_REQUESTS_TO_APPROVE = (By.XPATH, "//p[normalize-space()='(8) Leave Requests to Approve']")
        TIMESHEETS_TO_APPROVE = (By.XPATH, "//p[normalize-space()='(9) Timesheets to Approve']")
        PENDING_SELF_REVIEW = (By.XPATH, "//p[normalize-space()='(1) Pending Self Review']")
        CANDIDATES_TO_INTERVIEW = (By.XPATH, "//p[normalize-space()='(2) Candidates to Interview']")

    class QuickLaunchWIDGET:
        WIDGET_NAME = (By.XPATH, "//p[normalize-space()='Quick Launch']")
        ASSIGN_LEAVE_BUTTON = (By.XPATH, "//button[@title='Assign Leave']//*[@role='presentation']")
        LEAVE_LIST_BUTTON = (By.XPATH, "//button[@title='Leave List']//*[@role='presentation']")
        TIMESHEETS_BUTTON = (By.XPATH, "//button[@title='Timesheets']//*[@role='presentation']")
        APPLY_LEAVE_BUTTON = (By.XPATH, "//button[@title='Apply Leave']//*[@role='presentation']")
        MY_LEAVE_BUTTON = (By.XPATH, "//button[@title='My Leave']//*[@role='presentation']")
        MY_TIMESHEETS_BUTTON = (By.XPATH, "//button[@title='My Timesheet']//*[@role='presentation']")

    class BuzzLatestPosts:
        WIDGET_NAME = (By.XPATH, "//p[normalize-space()='Buzz Latest Posts']")

    class EmployeesOnLeaveToday:
        WIDGET_NAME = (By.XPATH, "//p[normalize-space()='Employees on Leave Today']")

    class EmployeeDistributionBySubUnit:
        WIDGET_NAME = (By.XPATH, "//p[normalize-space()='Employee Distribution by Sub Unit']")

    class EmployeeDistributionByLocation:
        WIDGET_NAME = (By.XPATH, "//p[normalize-space()='Employee Distribution by Location']")
