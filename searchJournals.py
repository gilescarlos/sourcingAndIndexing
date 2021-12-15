from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import Resources

def ExtractTitles(lst):
    return [item[1] for item in lst]

titlesAuthorsJournals = Resources.getTitlesWithAuthors()               # Get list of lists containing a title, an author, and a journal 
titles = ExtractTitles(titlesAuthorsJournals)                          # Create list of titles from the list above

start = int(input("Paper number to start from: ")) - 2                 # Ask user what paper to start from
end = int(input("Paper number to end at: ")) - 1                       # Ask user what paper to end at

journalsToFind = titles[start:end]                                     # From the list of titles, create list of journals to find with user inputs

driver = webdriver.Chrome('resources\chromedriver.exe')                # Chrome Driver 

for i in range(end - start):                                           # For every title the user wants to find
    driver.execute_script("window.open('');")                          # Open a new tab
    driver.get("https://google.com")                                   # Go to Google
    search = driver.find_element_by_name('q')                          # Click on the search bar
    search.send_keys(journalsToFind[i])                                # Input the current title to find
    search.send_keys(Keys.RETURN)                                      # Press enter
    driver.switch_to.window(driver.window_handles[i+1])                # Go to next tab

