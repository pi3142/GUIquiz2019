import thorpy, pygame

#Dynamic varables
spinSensorVal = 0
global correct
correct = False

class QuizMain(object):
    def checkAns1(self):
        global correct
        #Todo: check if entered ans matched ans
        #For now, this function returns correct all the time
        correct = True
        self.correctQns += 1
        print(correct)
        thorpy.functions.quit_menu_func()

    def checkAns2(self):
        global correct
        #Todo: check if entered ans matched ans
        #For now, this function returns correct all the time
        self.correctQns += 1
        correct = True
        print(correct)
        thorpy.functions.quit_menu_func()

    def checkAns3(self):
        global correct
        #Todo: check if entered ans matched ans
        #For now, this function returns correct all the time
        self.correctQns += 1
        correct = True
        print(correct)
        thorpy.functions.quit_menu_func()

    def checkAns4(self):
        global correct
        #Todo: check if entered ans matched ans
        #For now, this function returns correct all the time
        self.correctQns += 1
        correct = True
        print(correct)
        thorpy.functions.quit_menu_func()

    def createQuizElements(self):
        if self.pupilLevel == 1:
            self.questionText = thorpy.make_text(self.P1_2Qn[spinSensorVal], 40, (255, 255, 255, 160))
            row = self.P1_2Op[spinSensorVal].split(',')
            print(self.P1_2Op[spinSensorVal])
            print(row)
            self.Op1Button = thorpy.make_button(row[0], func=self.checkAns1)
            self.Op2Button = thorpy.make_button(row[1], func=self.checkAns2)
            self.Op3Button = thorpy.make_button(row[2], func=self.checkAns3)
            self.Op4Button = thorpy.make_button(row[3], func=self.checkAns4)
        elif self.pupilLevel == 3:
            self.questionText = thorpy.make_text(self.P3_4Qn[spinSensorVal], 40, (255, 255, 255, 160))
            row = self.P3_4Op[spinSensorVal].split(',')
            self.Op1Button = thorpy.make_button(row[0], func=self.checkAns1)
            self.Op2Button = thorpy.make_button(row[1], func=self.checkAns2)
            self.Op3Button = thorpy.make_button(row[2], func=self.checkAns3)
            self.Op4Button = thorpy.make_button(row[3], func=self.checkAns4)
        else:
            self.questionText = thorpy.make_text(self.P5_6Qn[spinSensorVal], 40, (255, 255, 255, 160))
            row = self.P5_6Op[spinSensorVal].split(',')
            self.Op1Button = thorpy.make_button(row[0], func=self.checkAns1)
            self.Op2Button = thorpy.make_button(row[1], func=self.checkAns2)
            self.Op3Button = thorpy.make_button(row[2], func=self.checkAns3)
            self.Op4Button = thorpy.make_button(row[3], func=self.checkAns4)

        self.Op1Button.center()
        self.Op1Button.set_topleft((None, 160))
        self.Op2Button.center()
        self.Op2Button.set_topleft((None, 200))
        self.Op3Button.center()
        self.Op3Button.set_topleft((None, 240))
        self.Op4Button.center()
        self.Op4Button.set_topleft((None, 280))
        self.questionText.center()
        self.questionText.set_topleft((None, 6))

    def OKPressed(self):
        print("OK button pressed")
        thorpy.functions.quit_menu_func()

    def P1_2(self):
        self.pupilLevel = 1
        print(self.pupilLevel)
        thorpy.functions.quit_menu_func()

    def P3_4(self):
        self.pupilLevel = 3
        print(self.pupilLevel)
        thorpy.functions.quit_menu_func()

    def P5_6(self):
        self.pupilLevel = 5
        print(self.pupilLevel)
        thorpy.functions.quit_menu_func()

    def __init__(self):
        #Initiate ThorPy
        self.application = thorpy.Application(size=(800, 480), caption='Recess Quiz')

        #The working varables of the game
        self.correctQns = 0
        self.pupilLevel = None #Level of the pupil
        self.maxtime = 25 #Time player has per qn
        self.P1_2Qn = ('What is compost?', 'Why should we save food?', 'How do we make sure we only \nbuy what we need?', 'How many bowls of rice are wasted \non average per day in one household?', 'Q5', 'Q6')
        self.P3_4Qn = ('What are the harmful effects \nof food waste when it rots?', 'Who will be affected by food wastage?', 'What can we do to prevent \nfood waste? Name 2', 'What do supermarkets do to \nreduce food waste?', 'Q5', 'Q6')
        self.P5_6Qn = ('What can you do when you cannot finish your food?', 'What are the causes of food waste?', 'What organisation collects unfinished food and distrobutes them to needy people?', 'Q4', 'Q5', 'Q6')
        self.P1_2Op = ('Water,Soil,Rotten remains of food,Rotten meat', "Doing so can reduce global warming,It's fun,It is time-consuming,You can earn money", "O1,O2,O3,O4", "Two bowls,One bowl,Five bowls,Ten bowls", "O1,O2,O3,O4", "O1,O2,O3,O4")
        self.P3_4Op = ('It creates water which causes flooding,It gives off methane which contributes to global warming,It gives off oxygen which kills plants,It gives off carbon dioxide', 'Growth of plants,Us and animals,Seaweed,Cats and Dogs', 'O1,O2,O3,O4', 'Sell less visually appealing food at a lower price instead of throwing it away,Pick out less appealing food and throw it away,Compost less visually appealing food,Sell less visually appealing food at a hiigher price instead of throwing it away.', 'O1,O2,O3,O4', 'O1,O2,O3,O4')
        self.P5_6Op = ('Throw it away,Give it to your pet,Create compost with it,Donate it to Foodbank', 'Growing food,Eating expired food,Preserving uneaten food,Throwing away uneaten food', 'Ordering too much food and throwing away the leftovers,Sharing your food with your friends,Throwing away uneaten food,Finishing all your food', 'O1,O2,O3,O4', 'O1,O2,O3,O4', 'O1,O2,O3,O4')

        #The static elements
        #Text elements
        self.spinWheelText = thorpy.make_text("Spin the colour wheel!", 60, (255, 255, 255, 160))
        self.firstText = thorpy.make_text("First, let's start with your level.", 60, (0, 255, 0))
        self.infoText = thorpy.make_text("Instructions", 60, (255, 255, 255, 160))
        self.questionText = None
        self.levelText = thorpy.make_text("Your level of study is... ", 20, (255, 0, 255))
        self.nextQuestion = thorpy.make_text("Get ready for the next question!", 40, (4, 2, 158, 100))
        #level buttons for first page
        self.P1_2Level = thorpy.make_button("P1 or 2", func=self.P1_2)
        self.P3_4Level = thorpy.make_button("P3 or 4", func=self.P3_4)
        self.P5_6Level = thorpy.make_button("P5 or 6", func=self.P5_6)
        #Action elements(i.e. OK, quit)
        self.OKbutton2 = thorpy.make_button("Collect my prize(s)!", func=self.OKPressed)
        self.OKPlaceholder = thorpy.make_button("Continue (Just a placeholder)", func=self.OKPressed)
        self.OKbutton = thorpy.make_button("Continue", func=self.OKPressed)
        self.OKbutton1 = thorpy.make_button("Continue", func=self.OKPressed)
        self.quit1 = thorpy.make_button("Quit", func=self.gameLauncher)
        self.quit2 = thorpy.make_button("Quit", func=self.gameLauncher)
        self.quit3 = thorpy.make_button("Quit", func=self.gameLauncher)
        self.quit4 = thorpy.make_button("Quit", func=self.gameLauncher)
        #Instructions
        # self.instructions = thorpy.make_text("When you click on the continue button at the \nbottom of the screen, you will be prompted \nto spin the wheel to select the question. \nAfter you have done that, a question and four \noptions would appear on the screen. Once \nyou have clicked on one of the options, you \nwould be told if your answer is correct. After that, \nthis process would be repeated once. At the end of the \ngame, you would get lucky stars corresponding \nto the number of questions you correctly answered.", 30, (4, 2, 158, 100))
        self.instructions = thorpy.make_text("Click the CONTINUE button below. \nSpin the colour wheel to get a question. \nFor each question, tap one of the four \noptions for your answer. You have 25 \nseconds to answer each question. \nAnswer two questions and get lucky \nstars corresponding to the number of \ncorrect answers.", 30, (4, 2, 158, 100))
        self.spinWheelInfo = thorpy.make_text("Please spin the colour wheel to get a question.\n(Currently, the wheel is not wired up yet.)", 30, (4, 2, 158, 100))

        #Static element configuration
        #Instructions page
        self.infoText.center()
        self.infoText.set_topleft((None, 6))
        self.instructions.center()
        self.instructions.set_topleft((None, 60))
        self.OKbutton.center()
        self.OKbutton.set_topleft((None, 350))
        self.quit1.center()
        self.quit1.set_topleft((None, 385))
        #Spin-the-wheel page
        self.spinWheelText.center()
        self.spinWheelText.set_topleft((None, 6))
        self.spinWheelInfo.center()
        self.spinWheelInfo.set_topleft((None, 60))
        self.quit2.center()
        self.quit2.set_topleft((None, 195))
        self.OKPlaceholder.center()
        self.OKPlaceholder.set_topleft((None, 160))
        #Quiz page
        self.quit3.center()
        self.quit3.set_topleft((None, 370))
        #Results page
        self.nextQuestion.center()
        self.nextQuestion.set_topleft((None, 180))
        self.OKbutton1.center()
        self.OKbutton1.set_topleft((None, 250))
        self.quit4.center()
        self.quit4.set_topleft((None, 285))

        #First screen box configuration
        self.elements = [self.levelText, self.P1_2Level, self.P3_4Level, self.P5_6Level]
        self.central_box = thorpy.Box(elements=self.elements)
        self.central_box.fit_children(margins=(10,10)) #We want small margins
        self.central_box.center() #Center on screen
        self.central_box.set_main_color((220,220,220,180)) #set box color and opacity

        self.gameLauncher()

        #Done: Draw the instructions page

        #Todo: Draw the gameLoader page

    def givePrizesLoader(self):
        #This page prints the number of prizes the pupil gets
        print("Reached Here - Prize loader page")
        if self.correctQns == 0:
            self.encouragementText = thorpy.make_text('Good try, but you did not get \nany questions correct.', 50, (0, 0, 0, 100))
        else:
            self.encouragement = 'Great job! You got ' + str(self.correctQns) + ' questions correct!'
            self.encouragementText = thorpy.make_text(self.encouragement, 50, (0, 0, 0, 100))

        self.encouragementText.center()
        self.encouragementText.set_topleft((None, 6))

        self.prizesToGive = self.correctQns
        if self.correctQns == 2:
            self.prizesToGive = self.prizesToGive + 1
        self.textPrizesToGive = 'You get ' + str(self.prizesToGive) + ' prizes!'
        self.prizesToGiveElement = thorpy.make_text(self.textPrizesToGive, 40, (4, 2, 158, 100))

        self.givePrizesBox = thorpy.Box(elements=[self.prizesToGiveElement, self.OKbutton2])
        self.givePrizesBox.fit_children(margins=(10,10)) #We want small margins
        self.givePrizesBox.center() #Center on screen
        self.givePrizesBox.set_topleft((None, 60))
        self.givePrizesBox.set_main_color((220,220,220,180)) #set box color and opacity

        self.givePrize = thorpy.Background(image="/Users/kxzv/quiz/prize.jpg", elements=[self.encouragementText, self.givePrizesBox])

        self.givePrizePage = thorpy.Menu(self.givePrize)
        self.givePrizePage.play()

    def quiz_resultsLoader(self):
        print("Reached Here - Quiz page")
        self.createQuizElements()
        self.quizGame = thorpy.Background(image='/Users/kxzv/quiz/quizAbstract.jpg', elements=[self.questionText, self.Op1Button, self.Op2Button, self.Op3Button, self.Op3Button, self.Op4Button, self.quit3])
        self.quizGamePage = thorpy.Menu(self.quizGame)
        self.quizGamePage.play()

        global correct
        print("Reached Here - Results page")
        print(correct)
        if correct == True:
            self.resultText = thorpy.make_text("Correct! Fantastic!", 60, (0, 0, 0, 160))
            correct = False
        else:
            self.resultText = thorpy.make_text("Good try! \nYou might get it right next time.", 60, (0, 0, 0, 160))
        self.resultText.center()
        self.resultText.set_topleft((None, 30))
        self.resultsBG = thorpy.Background(image='/Users/kxzv/quiz/abstract.jpg', elements=[self.resultText, self.nextQuestion, self.OKbutton1, self.quit4])
        self.resultsPage = thorpy.Menu(self.resultsBG)
        self.resultsPage.play()

    def gameLauncher(self):
        # self.firstBackground = thorpy.Background(image=thorpy.style.EXAMPLE_IMG, elements=[self.firstText, self.levelSlider, self.OKbutton, self.instructions])
        self.firstBackground = thorpy.Background(image='/Users/kxzv/quiz/quiz.jpg', elements=[self.firstText, self.central_box])
        thorpy.store(self.firstBackground)

        self.startScreen = thorpy.Menu(self.firstBackground)
        self.startScreen.play()
        print("Reached Here - End of level page")

        #Write Instructions to screen
        self.instructionsPage = thorpy.Background(image='/Users/kxzv/quiz/abstract.jpg', elements=[self.infoText, self.instructions, self.OKbutton, self.quit1])
        print("Reached Here - Background instructions page")

        self.infoScreen = thorpy.Menu(self.instructionsPage)
        self.infoScreen.play()

        print("Reached Here - Spin the wheel page")
        self.spinWheel = thorpy.Background(image='/Users/kxzv/quiz/abstract.jpg', elements=[self.spinWheelText, self.spinWheelInfo, self.quit2, self.OKPlaceholder])
        self.spinWheelPage = thorpy.Menu(self.spinWheel)
        self.spinWheelPage.play()

        self.quiz_resultsLoader()

        print("Reached Here - Second spin the wheel page")
        self.spinWheel = thorpy.Background(image='/Users/kxzv/quiz/abstract.jpg', elements=[self.spinWheelText, self.spinWheelInfo, self.quit2, self.OKPlaceholder])
        self.spinWheelPage = thorpy.Menu(self.spinWheel)
        self.spinWheelPage.play()

        print("Reached Here - Second question and result")
        self.createQuizElements()
        self.quizGame = thorpy.Background(image='/Users/kxzv/quiz/quizAbstract.jpg', elements=[self.questionText, self.Op1Button, self.Op2Button, self.Op3Button, self.Op3Button, self.Op4Button, self.quit3])
        self.quizGamePage = thorpy.Menu(self.quizGame)
        self.quizGamePage.play()

        print("Reached Here - Second results page")
        global correct
        print(correct)
        if correct == True:
            self.resultText = thorpy.make_text("Correct! Fantastic!", 60, (0, 0, 0, 160))
            correct = False
        else:
            self.resultText = thorpy.make_text("Good try! \nYou might get it right next time.", 60, (0, 0, 0, 160))
        self.resultText.center()
        self.resultText.set_topleft((None, 30))
        self.resultsBG = thorpy.Background(image='/Users/kxzv/quiz/abstract.jpg', elements=[self.resultText, self.OKbutton1, self.quit4])
        self.resultsPage = thorpy.Menu(self.resultsBG)
        self.resultsPage.play()

        self.givePrizesLoader()

        #Cleanly exit application
        print("Quitting")
        self.application.quit()

# application = thorpy.Application(size=(800, 480), caption="Quiz")
quiz = QuizMain()
