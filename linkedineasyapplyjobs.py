from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import math


class Linkedin:
    def __init__(self):
        linkprofile = webdriver.FirefoxProfile('')
        self.driver = webdriver.Firefox(linkprofile)
        #self.driver.get('https://www.linkedin.com/mynetwork/')
        time.sleep(10)

    def Link_job_apply(self):
        count_application = 0
        count_job = 0
        jobs_per_page = 25
        easy_apply = "?f_AL=true"
        location = "Israel"  # "Worldwide"
        exceptions = "%20NOT%20native%20NOT%20senior%20NOT%20lead%20NOT%20angular%20NOT%20php%20NOT%20vue"
        keywords = [
            "react" + exceptions,
            "web%20developer" + exceptions,
            "frontend%20developer" + exceptions,
            "backend%20developer" + exceptions
            ]
        for indexpag in range(len(keywords)):
            self.driver.get(
                'https://www.linkedin.com/jobs/search/' + easy_apply + '&keywords=' + keywords[indexpag] + "&" + location)
            numofjobs = self.driver.find_element_by_xpath(
                '//small').text  # get number of results
            space_ind = numofjobs.index(' ')
            total_jobs = (numofjobs[0:space_ind])
            total_jobs_int = int(total_jobs.replace(',', ''))
            number_of_pages = math.ceil(total_jobs_int/jobs_per_page)
            print(number_of_pages)
            for i in range(number_of_pages):
                cons_page_mult = 25 * i
                url = 'https://www.linkedin.com/jobs/search/' + easy_apply + \
                    '&keywords=' + keywords[indexpag] + \
                    "&" + location + "&start=" + str(cons_page_mult)
                self.driver.get(url)
                time.sleep(15)
                links = self.driver.find_elements_by_xpath(
                    '//div[@data-job-id]')  # needs to be scrolled down
                IDs = []
                for link in links:
                    try:
                        temp = link.get_attribute("data-job-id")
                        jobID = temp.split(":")[-1]
                        IDs.append(int(jobID))
                    except:
                        print("🔴 Error occurred getting the job ID")
                IDs = set(IDs)
                jobIDs = [x for x in IDs]
                for jobID in jobIDs:
                    try:
                        job_page = 'https://www.linkedin.com/jobs/view/' + \
                        str(jobID)
                        self.driver.get(job_page)
                        count_job += 1
                        time.sleep(7)
                    except:
                        print("🔴 Error occurred getting the job")
                    try:
                        button = self.driver.find_elements_by_xpath(
                            '//button[contains(@class, "jobs-apply-button")]/span[1]')
                        if button[0].text in "Easy Apply" :
                            EasyApplyButton = button[0]
                    except:
                        EasyApplyButton = False
                    button = EasyApplyButton
                    if button is not False:
                        string_easy = "* has Easy Apply Button"
                        time.sleep(2)
                        try:
                            button.click()
                        except:
                            print("🔴 Couldn't click Easy Apply, skipped.")
                        time.sleep(2)
                        try:
                            self.driver.find_element_by_css_selector(
                                "button[aria-label='Submit application']").click()
                            time.sleep(3)
                            count_application += 1
                            print("🟢 Applied to this job: " + job_page)
                        except:
                            try:
                                button = self.driver.find_element_by_css_selector(
                                    "button[aria-label='Continue to next step']").click()
                                time.sleep(3)
                                percen = self.driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div/span").text
                                percen_numer = int(percen[0:percen.index("%")])
                                if int(percen_numer) < 25:
                                    print(
                                        "🔴 More than 5 pages, won't apply to this job: " + job_page)
                                elif int(percen_numer) < 30:
                                    try:
                                        self.driver.find_element_by_css_selector(
                                        "button[aria-label='Continue to next step']").click()
                                        time.sleep(3)
                                        self.driver.find_element_by_css_selector(
                                        "button[aria-label='Continue to next step']").click()
                                        time.sleep(3)
                                        self.driver.find_element_by_css_selector(
                                        "button[aria-label='Review your application']").click()
                                        time.sleep(3)
                                        self.driver.find_element_by_css_selector(
                                        "button[aria-label='Submit application']").click()
                                        count_application += 1
                                        print("🟢 Applied to this job: " + job_page)
                                    except:
                                        print(
                                            "🔴 4 Pages, won't apply to this job! Extra info needed. Link: " + job_page)
                                elif int(percen_numer) < 40:
                                    try: 
                                        self.driver.find_element_by_css_selector(
                                        "button[aria-label='Continue to next step']").click()
                                        time.sleep(3)
                                        self.driver.find_element_by_css_selector(
                                        "button[aria-label='Review your application']").click()
                                        time.sleep(3)
                                        self.driver.find_element_by_css_selector(
                                        "button[aria-label='Submit application']").click()
                                        count_application += 1
                                        print("🟢 Applied to this job: " + job_page)
                                    except:
                                        print(
                                            "🔴 3 Pages, won't apply to this job! Extra info needed. Link: " + job_page)
                                elif int(percen_numer) < 60:
                                    try:
                                        self.driver.find_element_by_css_selector(
                                        "button[aria-label='Review your application']").click()
                                        time.sleep(3)
                                        self.driver.find_element_by_css_selector(
                                        "button[aria-label='Submit application']").click()
                                        count_application += 1
                                        print("🟢 Applied to this job: " + job_page)
                                    except:
                                        print(
                                            "🔴 2 Pages, won't apply to this job: " + job_page)
                            except:
                                print("🔴 Cannot apply to this job: " + job_page)
                    else:
                        print("🔵 Already applied!")
                    time.sleep(2)
            print("-----------------------------")
            # print("➖ Category: ", keywords)
            print("➖ Applied to: " + str(count_application) + " jobs out of " + str(count_job) + ".")
            print("-----------------------------")


start_time = time.time()
ed = Linkedin()
ed.Link_job_apply()
end = time.time()
print("🚩 Finished in: " + str(round((time.time() - start_time)/60)) + " minute(s).")

