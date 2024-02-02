from seleniumbase import Driver
from time import *
from loguru import logger
from random import *
from selenium.webdriver import ActionChains

EXTENSION_PATH = r"G:\metamask-chrome-11.2.0"

F = open(r"G:\cripta\Proxy.txt")
pr = [x.replace("\n", "") for x in F.readlines()]
F = open(r"G:\cripta\useragent.txt")
ag = [x.replace("\n", "") for x in F.readlines()]
F = open(r"G:\cripta\mata_pass.txt")
pasm = [x.replace("\n", "") for x in F.readlines()]
# F = open(r"D:\cripta\60\open_key.txt")
# okey = [x.replace("\n", "") for x in F.readlines()]
F = open(r"G:\cripta\name.txt")
name = [x.replace("\n", "") for x in F.readlines()]
follow = 'tryme'
nz = 2
kz = 3

logger.add("beoble.log", format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}", colorize=True)

# for i in range(0, 5):
#     driver = Driver(uc=True, proxy=f"user58612:jos2ea@{pr[i]}", user_data_dir=rf"G:\cripta\session\{i + 1}", extension_dir=EXTENSION_PATH, agent=
#     ag[i])  #, multi_proxy=True, headless2=True  , headless2=True  headless2=Trueagent=UserAgent().getChrome,
#     driver.maximize_window()
#     sleep(uniform(nz, kz))
#     driver.switch_to.window(driver.window_handles[0])
#     driver.close()
#     driver.switch_to.window(driver.window_handles[0])
#     sleep(uniform(nz, kz))
#     # input()
#
#     if driver.get_text("/html/body/div[1]/div/div[1]/div/div/button/p", by="xpath") != "Ethereum Mainnet":
#         driver.click_if_visible("/html/body/div[1]/div/div[1]/div/div/button", by="xpath", timeout=1)
#         driver.click_if_visible("/html/body/div[3]/div[3]/div/section/div[3]/div[1]/div[2]/button", by="xpath", timeout=1)
#         sleep(uniform(0.5, 1))
#         driver.click_if_visible("/html/body/div[3]/div[3]/div/section/div[2]/div[1]/div[2]/button", by="xpath", timeout=1)
#     sleep(uniform(0.5, 1))
#     driver.type("/html/body/div[1]/div/div[2]/div/div/form/div/div/input", pasm[i], by="xpath", timeout=20)
#     sleep(uniform(0.5, 1))
#     driver.click("/html/body/div[1]/div/div[2]/div/div/button", by="xpath", timeout=20)
#
#     ###############
#
#     driver.switch_to.new_window("tab")
#     driver.open("https://reiki.web3go.xyz")
#     # driver.open("https://galxe.com/Berachain/campaign/GCTN3ttM4T")
#     # driver.open("https://bridge.katla.taiko.xyz")
#
#     input(f"----{i + 1}----")
#     driver.quit()

def if_click(path, to):
    try:
        driver.click(path, by="xpath", timeout=to)
        return True
    except:
        return False
def metamask():
    try:
        sleep(uniform(nz, kz))
        driver.switch_to.window(driver.window_handles[0])
        sleep(uniform(nz, kz))
        driver.refresh()
        sleep(uniform(nz, kz))
        while not driver.is_element_visible('/html/body/div[1]/div/div[3]/div/div/div/div[2]/div/ul/li[3]/button', by="xpath"):
            if_click("/html/body/div[1]/div/div/div/div[2]/div/button[2]", 0.2)
            if_click("/html/body/div[2]/div/div/section/div[3]/button", 0.2)
            if_click("/html/body/div[2]/div/div/section/div[2]/div/div[2]/div/button", 0.2)
            if_click("/html/body/div[1]/div/div[3]/div/div[5]/footer/button[2]", 0.2)
            if_click("/html/body/div[1]/div/div/div/div[3]/div[2]/footer/button[2]", 0.2)
            if_click("/html/body/div[1]/div/div[3]/div/div[3]/div[3]/footer/button[2]", 0.2)
            if_click("/html/body/div[1]/div/div[3]/div/div[9]/footer/button[2]", 0.2)
            if_click("/html/body/div[1]/div/div[3]/div/div[10]/footer/button[2]", 0.2)
            if_click("/html/body/div[1]/div/div[3]/div/div[3]/div[3]/footer/button[2]", 0.2)
            if_click("/html/body/div[1]/div/div/div/div[2]/div/button[2]", 0.2)
            if_click("/html/body/div[1]/div/div/div/div[3]/div[2]/footer/button[2]", 0.2)
            if_click("/html/body/div[1]/div/div/div/div[2]/div/button[2]", 0.2)
            if_click("/html/body/div[1]/div/div/div/div[3]/div[2]/footer/button[2]", 0.2)
            if_click("/html/body/div[1]/div/div[3]/div/div[9]/footer/button[2]", 0.2)
            if_click("/html/body/div[1]/div/div[3]/div/div[3]/div[3]/footer/button[2]", 0.2)
            if_click("/html/body/div[1]/div/div[3]/div/div[10]/footer/button[2]", 0.2)
            if_click("/html/body/div[2]/div/div/section/div[3]/button", 0.2)
            if_click("/html/body/div[1]/div/div/div/div[1]/div[3]/button[2]", 0.2)
            if_click("/html/body/div[1]/div/div[3]/div/div[3]/div[2]/div/div/div[1]/div/div/button", 0.2)
            if_click("/html/body/div[1]/div/div[3]/div/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/button", 0.2)
            if_click("/html/body/div[1]/div/div[3]/div/div[4]/footer/button[2]", 0.2)
            if_click("/html/body/div[2]/div/div/section/div[1]/div/button", 0.2)
            # if_click("", 0.2)
            # driver.refresh()
            sleep(uniform(1, 1.5))
        driver.switch_to.window(driver.window_handles[1])
        sleep(uniform(nz, kz))
    except:
        pass
w = [x for x in range(0, 5)]
shuffle(w)

    # for i in range(1, 60):
for i in w:
    driver = Driver(uc=True, proxy=f"user58612:jos2ea@{pr[i]}", user_data_dir=rf"G:\cripta\session\{i + 1}", extension_dir=EXTENSION_PATH, agent=
    ag[i])  # , headless2=True  headless2=Trueagent=UserAgent().getChrome,
    driver.maximize_window()
    sleep(uniform(nz, kz))
    driver.switch_to.window(driver.window_handles[0])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    sleep(uniform(nz, kz))
    # input()

    if driver.get_text("/html/body/div[1]/div/div[1]/div/div/button/p", by="xpath") != "Ethereum Mainnet":
        driver.click_if_visible("/html/body/div[1]/div/div[1]/div/div/button", by="xpath", timeout=1)
        driver.click_if_visible("/html/body/div[3]/div[3]/div/section/div[3]/div[1]/div[2]/button", by="xpath", timeout=1)
        sleep(uniform(0.5, 1))
        driver.click_if_visible("/html/body/div[3]/div[3]/div/section/div[2]/div[1]/div[2]/button", by="xpath", timeout=1)
    sleep(uniform(0.5, 1))
    driver.type("/html/body/div[1]/div/div[2]/div/div/form/div/div/input", pasm[i], by="xpath", timeout=20)
    sleep(uniform(0.5, 1))
    driver.click("/html/body/div[1]/div/div[2]/div/div/button", by="xpath", timeout=20)
    # input()

    try:
        driver.switch_to.new_window("tab")
        try:
            try:
                driver.switch_to.window(driver.window_handles[1])
                sleep(uniform(nz, kz))
                driver.open("https://reiki.web3go.xyz")
                # driver.open("https://reiki.web3go.xyz/aiweb/home")
                sleep(uniform(nz, kz))
                if if_click("/html/body/div[1]/div/div[1]/div/div/div[1]/div[2]/div[5]/div", 4):
                    sleep(uniform(nz, kz))
                    if_click("/html/body/div[8]/div[2]/div/div[2]/div/div/div[3]/div[1]", 2)
                    if_click("/html/body/div[9]/div[2]/div/div[2]/div/div/div[3]/div[1]", 2)
                    sleep(uniform(nz, kz))

                    driver.switch_to.window(driver.window_handles[0])
                    sleep(uniform(nz, kz))
                    driver.refresh()
                    sleep(uniform(nz, kz))
                    if_click("/html/body/div[1]/div/div/div/div[2]/div/button[2]", 10)
                    sleep(uniform(nz, kz))
                    driver.refresh()
                    sleep(uniform(nz, kz))
                    if_click("/html/body/div[2]/div/div/section/div[3]/button", 5)  # /html/body/div[2]/div/div/section/div[2]/div/div[2]/div/button
                    sleep(uniform(nz, kz))
                    if_click("/html/body/div[1]/div/div[3]/div/div[5]/footer/button[2]", 10)
                    sleep(uniform(nz, kz))
                    driver.switch_to.window(driver.window_handles[1])
                    sleep(15)

                sleep(uniform(nz, kz))
                driver.click("/html/body/div[1]/div/div[1]/div/div/div[1]/div[2]/img[2]", by="xpath", timeout=20)
                sleep(uniform(nz, kz))
                driver.click("/html/body/div[1]/div/main/div[2]/div[2]/div/div[2]/div[2]/div/div[3]/div[3]/a", by="xpath", timeout=20)
                r2 = "YES"
                sleep(uniform(nz, kz))
            except:
                driver.switch_to.window(driver.window_handles[1])
                sleep(uniform(nz, kz))
                driver.open("https://reiki.web3go.xyz")
                # driver.open("https://reiki.web3go.xyz/aiweb/home")
                sleep(uniform(nz, kz))
                if if_click("/html/body/div[1]/div/div[1]/div/div/div[1]/div[2]/div[5]/div", 4):
                    sleep(uniform(nz, kz))
                    if_click("/html/body/div[8]/div[2]/div/div[2]/div/div/div[3]/div[1]", 2)
                    if_click("/html/body/div[9]/div[2]/div/div[2]/div/div/div[3]/div[1]", 2)
                    sleep(uniform(nz, kz))

                    driver.switch_to.window(driver.window_handles[0])
                    sleep(uniform(nz, kz))
                    driver.refresh()
                    sleep(uniform(nz, kz))
                    if_click("/html/body/div[1]/div/div/div/div[2]/div/button[2]", 10)
                    sleep(uniform(nz, kz))
                    driver.refresh()
                    sleep(uniform(nz, kz))
                    if_click("/html/body/div[2]/div/div/section/div[3]/button", 5)  # /html/body/div[2]/div/div/section/div[2]/div/div[2]/div/button
                    sleep(uniform(nz, kz))
                    if_click("/html/body/div[1]/div/div[3]/div/div[5]/footer/button[2]", 10)
                    sleep(uniform(nz, kz))
                    driver.switch_to.window(driver.window_handles[1])
                    sleep(15)

                sleep(uniform(nz, kz))
                driver.click("/html/body/div[1]/div/div[1]/div/div/div[1]/div[2]/img[2]", by="xpath", timeout=20)
                sleep(uniform(nz, kz))
                driver.click("/html/body/div[1]/div/main/div[2]/div[2]/div/div[2]/div[2]/div/div[3]/div[3]/a", by="xpath", timeout=20)
                r2 = "YES"
                sleep(uniform(nz, kz))
        except:
            r2 = "NOO---"
       # if r2 == "NOO---": driver.save_screenshot(rf"D:\cripta\screen\{i + 1}web{r2}.png")

        try:
            try:
                driver.switch_to.window(driver.window_handles[1])
                sleep(uniform(nz, kz))
                driver.open("https://galxe.com/Berachain/campaign/GCTN3ttM4T")
                sleep(uniform(nz, kz))
                sleep(uniform(nz, kz))

                # metamask
                sleep(uniform(nz, kz))
                driver.switch_to.window(driver.window_handles[0])
                sleep(uniform(nz, kz))
                driver.refresh()
                sleep(uniform(nz, kz))
                if_click("/html/body/div[1]/div/div[3]/div/div[5]/footer/button[2]", 2)
                sleep(uniform(nz, kz))
                if_click("/html/body/div[1]/div/div[3]/div/div[5]/footer/button[2]", 2)
                sleep(uniform(nz, kz))
                driver.switch_to.window(driver.window_handles[1])
                sleep(uniform(nz, kz))

                driver.click("/html/body/div/div/div/div[3]/div[1]/main/div/div/div/div[2]/div/div[1]/div[2]/div[1]/div[2]/div[4]/div[2]/div/div[1]/div/div/div[2]/div/div/div/button/div[1]/div[2]", by="xpath", timeout=20)
                sleep(uniform(25, 27))
                driver.switch_to.window(driver.window_handles[1])
                sleep(uniform(nz, kz))
                if_click("/html/body/div/div/div/div[3]/div[1]/main/div/div/div/div[2]/div/div[1]/div[2]/div[1]/div[2]/div[4]/div[2]/div/div[1]/div/div/div[2]/div/div/div/button/div[2]/div/div/div/div/div", 10)
                sleep(uniform(nz, kz))
                driver.click("/html/body/div/div/div/div[3]/div[1]/main/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div/button", by="xpath", timeout=20)
                sleep(uniform(2 * nz, 2 * kz))
                r3 = "YES"
            except:
                driver.switch_to.window(driver.window_handles[1])
                sleep(uniform(nz, kz))
                driver.open("https://galxe.com/Berachain/campaign/GCTN3ttM4T")
                sleep(uniform(nz, kz))
                sleep(uniform(nz, kz))

                # metamask
                sleep(uniform(nz, kz))
                driver.switch_to.window(driver.window_handles[0])
                sleep(uniform(nz, kz))
                driver.refresh()
                sleep(uniform(nz, kz))
                if_click("/html/body/div[1]/div/div[3]/div/div[5]/footer/button[2]", 2)
                sleep(uniform(nz, kz))
                if_click("/html/body/div[1]/div/div[3]/div/div[5]/footer/button[2]", 2)
                sleep(uniform(nz, kz))
                driver.switch_to.window(driver.window_handles[1])
                sleep(uniform(nz, kz))

                driver.click("/html/body/div/div/div/div[3]/div[1]/main/div/div/div/div[2]/div/div[1]/div[2]/div[1]/div[2]/div[4]/div[2]/div/div[1]/div/div/div[2]/div/div/div/button/div[1]/div[2]", by="xpath", timeout=20)
                sleep(uniform(25, 27))
                driver.switch_to.window(driver.window_handles[1])
                sleep(uniform(nz, kz))
                if_click("/html/body/div/div/div/div[3]/div[1]/main/div/div/div/div[2]/div/div[1]/div[2]/div[1]/div[2]/div[4]/div[2]/div/div[1]/div/div/div[2]/div/div/div/button/div[2]/div/div/div/div/div", 10)
                sleep(uniform(nz, kz))
                driver.click("/html/body/div/div/div/div[3]/div[1]/main/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div/button", by="xpath", timeout=20)
                sleep(uniform(2 * nz, 2 * kz))
                r3 = "YES"
        except:
            r3 = "NOO---"
            sleep(uniform(nz, kz))

       # if r3 == "NOO---": driver.save_screenshot(rf"D:\cripta\screen\gal\{i + 1}.png")

        # logger.info(f"{i + 1} - {r1}, {r2}, {r3}")
        logger.info(f"{i + 1} - {r2}, {r3}")
        # logger.info(f"{i + 1} - {r1}")

        # sleep(uniform(1, 2))
        # chime.info(sync=True)
        # input(22)
        # driver.close()
        driver.quit()
        sleep(uniform(nz, kz))

    except:
        # logger.exception(f"{i + 1} - NOOOO!!!")
        logger.info(f"{i + 1} - NOOOO!!!(реакции)")
      #  driver.save_screenshot(rf"D:\cripta\screen\{i + 1}(NOOOO)beo.png")
        # chime.info(sync=True)
        # input("noo")
        # driver.close()
        driver.quit()
        sleep(uniform(nz, kz))