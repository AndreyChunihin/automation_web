from pages.main_page import MainPage
from locators.elements_dashboar_page import DashboardWidgets


class DashboardPage(MainPage):
    locators = DashboardWidgets

    # Time at Work
    def widget_t_a_w(self):
        widget_element = self.find_element(self.locators.TimeAtWorkWidget.WIDGET_NAME)
        widget_name = widget_element.text
        return widget_name

        # My Actions

    class WidgetTWA:
        def __init__(self, parent):
            self.parent = parent

        def check_widget_name(self):
            widget_element = self.parent.element_is_visible(self.parent.locators.TimeAtWorkWidget.WIDGET_NAME)
            widget_name = widget_element
            return widget_name

        def CHECK_PENDING_SELF_REVIEW_LINK(self):
            self.parent.element_is_visible(self.parent.locators.MyActionsWIDGET.PENDING_SELF_REVIEW).click()

        def CHECK_TIMESHEETS_TO_APPROVE_LINK(self):
            self.parent.element_is_visible(self.parent.locators.MyActionsWIDGET.TIMESHEETS_TO_APPROVE).click()

        def CHECK_CANDIDATES_TO_INTERVIEW_LINK(self):
            self.parent.element_is_visible(self.parent.locators.MyActionsWIDGET.CANDIDATES_TO_INTERVIEW).click()

        def CHECK_LEAVE_REQUESTS_TO_APPROVE_LINK(self):
            self.parent.element_is_visible(self.parent.locators.MyActionsWIDGET.LEAVE_REQUESTS_TO_APPROVE).click()

        # Quick Launch

    def widget_q_l(self):
        self.find_element(self.locators.QuickLaunchWIDGET.WIDGET_NAME)
        self.scroll_to_element(self.locators.QuickLaunchWIDGET.WIDGET_NAME)
        self.element_is_visible(self.locators.QuickLaunchWIDGET.WIDGET_NAME)
        self.element_is_visible(self.locators.QuickLaunchWIDGET.MY_LEAVE_BUTTON).click()
        self.element_is_visible(self.locators.QuickLaunchWIDGET.LEAVE_LIST_BUTTON).click()
        self.element_is_visible(self.locators.QuickLaunchWIDGET.TIMESHEETS_BUTTON).click()
        self.element_is_visible(self.locators.QuickLaunchWIDGET.APPLY_LEAVE_BUTTON).click()
        self.element_is_visible(self.locators.QuickLaunchWIDGET.ASSIGN_LEAVE_BUTTON).click()
        self.element_is_visible(self.locators.QuickLaunchWIDGET.MY_TIMESHEETS_BUTTON).click()

        # Buzz Latest Posts

    def widget_b_l_p(self):
        self.find_element(self.locators.BuzzLatestPosts.WIDGET_NAME)
        self.scroll_to_element(self.locators.BuzzLatestPosts.WIDGET_NAME)
        self.element_is_visible(self.locators.BuzzLatestPosts.WIDGET_NAME)

        # Employees on Leave Today

    def widget_e_o_l_t(self):
        self.find_element(self.locators.EmployeesOnLeaveToday.WIDGET_NAME)
        self.scroll_to_element(self.locators.EmployeesOnLeaveToday.WIDGET_NAME)
        self.element_is_visible(self.locators.EmployeesOnLeaveToday.WIDGET_NAME)

        # Employee Distribution by Sub Unit

    def widget_e_d_b_s_u(self):
        self.find_element(self.locators.EmployeeDistributionBySubUnit.WIDGET_NAME)
        self.scroll_to_element(self.locators.EmployeeDistributionBySubUnit.WIDGET_NAME)
        self.element_is_visible(self.locators.EmployeeDistributionBySubUnit.WIDGET_NAME)

        # Employee Distribution by Location

    def widget_e_d_b_l(self):
        self.find_element(self.locators.EmployeeDistributionByLocation.WIDGET_NAME)
        self.scroll_to_element(self.locators.EmployeeDistributionByLocation.WIDGET_NAME)
        self.element_is_visible(self.locators.EmployeeDistributionByLocation.WIDGET_NAME)
