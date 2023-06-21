import requests
import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# def enable_download(driver):
#     driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
#     params = {'cmd':'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': r'C:\Users\lil4sxvl\Desktop\parser'}}
#     driver.execute("send_command", params)

titles = ['BIO']#, 'CISE', 'ENG', 'ERE', 'GEO', 'OIA', 'OISE', 'MPS', 'SBE', 'EDU', 'TIP']
def parse():
    for item in titles:
        response_programs = requests.get('https://beta.nsf.gov/funding/opportunities/' + item)
        programs = bs(response_programs.content, 'html.parser')
        programs_csv = programs.find('div', {'class': 'csv-feed views-data-export-feed'}).find('a').get('href')
        #r = requests.get(programs_csv, allow_redirects=True)
        #open(item + '.csv', 'wb').write(r.content)
        print(programs_csv)
        program_links = programs.find_all('h3', {'class': 'teaser--title'})
        for link in program_links:
            link_of_program = link.find('a').get('href')
            print(link_of_program)
            name_of_program = link_of_program.split('/')[-1]
            print(name_of_program)
            response_programs_page = requests.get('https://beta.nsf.gov' + link_of_program)
            programs_page = bs(response_programs_page.content, 'html.parser')
            link_to_projects = programs_page.find('section', {'class': 'program__award-url program__section'}).find('a').get('href')
            print(link_to_projects)
            options = Options()
            #options.add_argument('--headless')
            options.add_argument('--no-proxy-server')
            options.add_argument("--proxy-server='direct://'")
            options.add_argument("--proxy-bypass-list=*")
            driver = webdriver.Chrome(options=options)
            # enable_download(driver)
            driver.get(link_to_projects)
            time.sleep(1)
            driver.find_element('id', 'x-auto-30').click()
            time.sleep(20)
            driver.close()

parse() 