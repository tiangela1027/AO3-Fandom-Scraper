#! C:\Users\Angela\AppData\Local\Programs\Python\Python37

from selenium import webdriver
from selenium.webdriver.firefox.options import Options  
from bs4 import BeautifulSoup
from sys import argv
from itertools import islice
from datetime import datetime
from tkinter import *
from tkinter.scrolledtext import ScrolledText

class AO3Scraper:
    def __init__(self):
        self.window = Tk()
        self.window.title("AO3 Scraper")

        # limit
        self.limitFrame = Frame(self.window)
        self.limitFrame.grid(row=0, column=1)

        self.limitVar = IntVar(value=1000)
        self.initLimitFrame(1)

        # message
        self.output = ""
        self.messageVar = StringVar()

        # fandom options
        self.optionsFrame = Frame(self.window)
        self.optionsFrame.grid(row=0, column=0)

        self.animeURL = "https://archiveofourown.org/media/Anime%20*a*%20Manga/fandoms"
        self.moviesURL = "https://archiveofourown.org/media/Movies/fandoms"
        self.showsURL = "https://archiveofourown.org/media/TV%20Shows/fandoms"
        self.gamesURL = "https://archiveofourown.org/media/Video%20Games/fandoms"

        self.urlVar = StringVar(value=self.animeURL)
        self.initOptionsFrame()

        # submit button
        self.submitFrame = Frame(self.window)
        self.submitFrame.grid(row=3, column=1, sticky=E)

        self.statusVar = StringVar()

        Label(self.submitFrame, textvariable=self.statusVar).grid(row=0, column=0, sticky=E)
        Button(self.submitFrame, text="Submit", command=self.submit).grid(row=0, column=1, sticky=E)

        self.txt = ScrolledText(self.window)
        self.txt.grid(row=4, columnspan=2)

    def initLimitFrame(self, row):
        Label(self.limitFrame, text="Lower Bound").grid(row=row, column=0)
        Entry(self.limitFrame, textvariable=self.limitVar).grid(row=row, column=1, sticky=W)

    def initOptionsFrame(self):
        Label(self.optionsFrame, text="Genre").grid(rowspan=4)
        Radiobutton(self.optionsFrame, value=self.animeURL, text="Anime & Manga", variable=self.urlVar).grid(row=0, column=1, sticky=W)
        Radiobutton(self.optionsFrame, value=self.moviesURL, text="Movies", variable=self.urlVar).grid(row=1, column=1, sticky=W)
        Radiobutton(self.optionsFrame, value=self.showsURL, text="TV Shows", variable=self.urlVar).grid(row=2, column=1, sticky=W)
        Radiobutton(self.optionsFrame, value=self.gamesURL, text="Video Games", variable=self.urlVar).grid(row=3, column=1, sticky=W)

    def prepareDriver(self):
        options = Options()  
        options.add_argument("--headless")  
        self.driver = webdriver.Firefox(executable_path=r'C:\Users\Angela\Documents\geckodriver\geckodriver.exe',
            options=options)

        self.driver.get(self.urlVar.get())
        self.content = self.driver.page_source

    def quitDriver(self):
        self.driver.quit()

    def getFandoms(self):
        self.fandoms = dict()
        soup = BeautifulSoup(self.content, features="html.parser")

        for a in soup.find_all('a', href=True, attrs={'class': 'tag'}):
            gen = a.parent.stripped_strings
            count = int(next(islice(gen, 1, None))[1:-1])
            self.fandoms[a.string] = count

    def setFandomList(self):
        self.getFandoms()
        
        try:
            for fandom in self.fandoms.keys():
                if self.fandoms[fandom] >= self.limitVar.get():
                    line = f"{fandom}: {self.fandoms[fandom]}\n"
                    self.output += line
            self.messageVar.set(self.output)
            self.statusVar.set("Success!")
            self.txt.insert(INSERT, self.output)
        except:
            self.statusVar.set("Failed!")

    def submit(self): 
        self.prepareDriver()

        self.txt.delete("1.0", END)
        self.output = ""

        self.setFandomList()
        self.quitDriver()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    scraper = AO3Scraper()
    scraper.run()