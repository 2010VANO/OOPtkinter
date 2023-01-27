class Button:
    def __init__(self, clicks):
        self.clicks = clicks

    def click(self):
        self.clicks += 1

    def click_count(self):
        return self.clicks

    def reset(self):
        self.clicks = 0




click1 = Button(0)
click1.click()
click1.click_count()
print(click1.clicks)
click1.reset()
click1.click_count()
print(click1.clicks)







