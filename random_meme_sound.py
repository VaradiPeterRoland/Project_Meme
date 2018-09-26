from selenium import webdriver
import time


def get_random_meme_sound():
    driver = webdriver.Chrome('/home/owen/Downloads/chrome_driver/chromedriver')
    driver.get('https://www.randommemes.website/sounds.html#/')
    button_element = driver.find_element_by_xpath('//*[@id="header-wrapf"]/div[3]/a[2]')
    time.sleep(2)
    button_element.click()


def main():
    get_random_meme_sound()


if __name__ == '__main__':
    main()
