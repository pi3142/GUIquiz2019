import thorpy, pygame, os #ThorPy for basic GUI functionality, PyGame for low-level interface with video device, OS for executing terminal commands

from threading import Timer

#Dynamic varables
spinSensorVal = 4
global correct
correct = False

import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization
p.ChangeDutyCycle(14.5)

#try:
#  while True:
#    print('Closed')
#    p.ChangeDutyCycle(14.5)
#    time.sleep(0.5)
#    print('Opened')
#    p.ChangeDutyCycle(12.5)
#    time.sleep(0.5)
    # time.sleep(0.1)
    # p.ChangeDutyCycle(10)
#except KeyboardInterrupt:
#  p.stop()
#  GPIO.cleanup()

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

class QuizMain(object):
    def openServoOnce(self):
        print('Closed')
        p.ChangeDutyCycle(12.5)
        time.sleep(0.5)
        print('Opened')
        p.ChangeDutyCycle(14.5)
        time.sleep(0.5)


    def dispensePrize(self):
        for x in range(0, self.prizesToGive):
            print("We're on time %d" % (x))
            self.openServoOnce()

    #These 'checkAns' functions take the quiz option button input and checks if answer is correct.
    def checkAns1(self):
        global correct
        #Done: check if entered ans matched ans
        if self.pupilLevel == 1:
            self.testAns = self.P1_2CorrectAns
        elif self.pupilLevel == 3:
            self.testAns = self.P3_4CorrectAns
        else:
            self.testAns = self.P5_6CorrectAns
        if int(self.testAns[spinSensorVal]) == 1:
            self.correctQns += 1
            correct = True
            print(correct)
            thorpy.functions.quit_menu_func()
        else:
            correct = False
            print(correct)
            thorpy.functions.quit_menu_func()

    def checkAns2(self):
        global correct
        #Done: check if entered ans matched ans
        if self.pupilLevel == 1:
            self.testAns = self.P1_2CorrectAns
        elif self.pupilLevel == 3:
            self.testAns = self.P3_4CorrectAns
        else:
            self.testAns = self.P5_6CorrectAns
        if int(self.testAns[spinSensorVal]) == 2:
            self.correctQns += 1
            correct = True
            print(correct)
            thorpy.functions.quit_menu_func()
        else:
            correct = False
            print(correct)
            thorpy.functions.quit_menu_func()

    def checkAns3(self):
        global correct
        #Done: check if entered ans matched ans
        if self.pupilLevel == 1:
            self.testAns = self.P1_2CorrectAns
        elif self.pupilLevel == 3:
            self.testAns = self.P3_4CorrectAns
        else:
            self.testAns = self.P5_6CorrectAns
        if int(self.testAns[spinSensorVal]) == 3:
            self.correctQns += 1
            correct = True
            print(correct)
            thorpy.functions.quit_menu_func()
        else:
            correct = False
            print(correct)
            thorpy.functions.quit_menu_func()

    def checkAns4(self):
        global correct
        #Done: check if entered ans matched ans
        if self.pupilLevel == 1:
            self.testAns = self.P1_2CorrectAns
        elif self.pupilLevel == 3:
            self.testAns = self.P3_4CorrectAns
        else:
            self.testAns = self.P5_6CorrectAns
        if int(self.testAns[spinSensorVal]) == 4:
            self.correctQns += 1
            correct = True
            print(correct)
            thorpy.functions.quit_menu_func()
        else:
            correct = False
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

        #Timer text element
        self.timeTextString = 'Time left: ' + str(self.timeLeft) + ' seconds'
        self.timeLeftText = thorpy.make_text(self.timeTextString, 25, (255, 255, 255, 100))
        self.timeLeftText.center()
        self.timeLeftText.set_topleft((6, 400))

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
        self.OK == True
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
        self.prizesToGive = 0
        self.OK = False
        self.correctQns = 0
        self.pupilLevel = None #Level of the pupil
        self.maxTime = 25 #Time player has per qn
        self.timeLeft = self.maxTime + 0.125
        self.P1_2Qn = ('What is compost?', 'Why should we save food?', 'How do we make sure we only \nbuy what we need?', 'How many bowls of rice are wasted \non average per day in one household?', 'Name a simple way to save \nfood at home.', 'Q6')
        self.P3_4Qn = ('What are the harmful effects \nof food waste when it rots?', 'Who will be affected by food wastage?', 'What can we do to prevent \nfood waste? Name 1', 'What do supermarkets do to \nreduce food waste?', 'What can compost be used for?', 'Q6')
        self.P5_6Qn = ('What can you do when you \ncannot finish your food?', 'What is one of the cause of food waste?', 'What organisation collects unfinished food \nand distrobutes them to needy people?', 'What percentage of food is wasted in the world?', 'Q5', 'Q6')
        self.P1_2Op = ('Water,Soil,Rotten remains of food,Rotten meat', "Doing so can reduce global warming,It's fun,It is time-consuming,You can earn money", "Buy food on impulse,Do not buy foods which are not visually appealing,Throw away the excess food that you have bought,Check what food you already have to make a shopping list", "Two bowls,One bowl,Five bowls,Ten bowls", "Cook way too much food,Store leftover food for cosumption in the future,Do not eat any food cooked at home,Throw away any leftovers", "O1,O2,O3,O4")
        self.P3_4Op = ('It creates water which causes flooding,It gives off methane which contributes to global warming,It gives off oxygen which kills plants,It gives off carbon dioxide', 'Growth of plants,Everybody,Seaweed,Cats and Dogs', 'Eat out everyday,Cook too little food for your family,Use Olio to give partially eaten food to neighbours,Eat leftovers for the next meal', 'Sell less visually appealing food at a lower price instead of throwing it away,Pick out less appealing food and throw it away,Compost less visually appealing food,Sell less visually appealing food at a hiigher price instead of throwing it away.', 'Soil for plants,Add flavour to your food,Fertiliser for plants,Sell away for money', 'O1,O2,O3,O4')
        self.P5_6Op = ('Throw it away,Give it to your pet,Create compost with it,Donate it to Foodbank', 'Growing food,Eating expired food,Preserving uneaten food,Throwing away uneaten food', 'Foodbank,Bloodbank,Fairprice,Olio', 'About 10%,About 30%,About 20%,About 35%', 'O1,O2,O3,O4', 'O1,O2,O3,O4')
        self.P1_2CorrectAns = ('3', '1', '4', '1', '2', 'False')
        self.P3_4CorrectAns = ('2', '2', '4', '1', '3', 'False')
        self.P5_6CorrectAns = ('3', '4', '1', '2', 'False', 'False')

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

        #Done: Draw the gameLoader page

    def givePrizesLoader(self):
        #This page prints the number of prizes the pupil gets
        print("Reached Here - Prize loader page")
        if self.correctQns == 0:
            self.encouragementText = thorpy.make_text('Good try, but you did not get \nany questions correct.', 50, (0, 0, 0, 100))
        else:
            self.encouragement = 'Great job! You got ' + str(self.correctQns) + ' question(s) correct!'
            self.encouragementText = thorpy.make_text(self.encouragement, 50, (0, 0, 0, 100))

        self.encouragementText.center()
        self.encouragementText.set_topleft((None, 6))

        self.prizesToGive = self.correctQns
        if self.correctQns == 2:
            self.prizesToGive = self.prizesToGive + 1
        self.textPrizesToGive = 'You get ' + str(self.prizesToGive) + ' prize(s)!'
        self.prizesToGiveElement = thorpy.make_text(self.textPrizesToGive, 40, (4, 2, 158, 100))

        self.givePrizesBox = thorpy.Box(elements=[self.prizesToGiveElement, self.OKbutton2])
        self.givePrizesBox.fit_children(margins=(10,10)) #We want small margins
        self.givePrizesBox.center() #Center on screen
        self.givePrizesBox.set_topleft((None, 60))
        self.givePrizesBox.set_main_color((220,220,220,180)) #set box color and opacity

        self.givePrize = thorpy.Background(image="prize.jpg", elements=[self.encouragementText, self.givePrizesBox])

        self.givePrizePage = thorpy.Menu(self.givePrize)
        self.givePrizePage.play()

    def startQuizGameBG(self):
        if self.timeLeft == 0:
            self.rt.stop()
        self.timeLeft -= 0.125
        self.quizGame = thorpy.Background(image='quizAbstract.jpg', elements=[self.questionText, self.Op1Button, self.Op2Button, self.Op3Button, self.Op3Button, self.Op4Button, self.quit3])
        self.quizGamePage = thorpy.Menu(self.quizGame)
        self.quizGamePage.play()

    def quiz_resultsLoader(self):
        print("Reached Here - Quiz page")
        self.createQuizElements()
        #self.rt = RepeatedTimer(0.1246, self.startQuizGameBG) #Initiate a 1-second non-blocking timer
        self.startQuizGameBG()

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
        self.resultsBG = thorpy.Background(image='abstract.jpg', elements=[self.resultText, self.nextQuestion, self.OKbutton1, self.quit4])
        self.resultsPage = thorpy.Menu(self.resultsBG)
        self.resultsPage.play()

    def gameLauncher(self):
        # self.firstBackground = thorpy.Background(image=thorpy.style.EXAMPLE_IMG, elements=[self.firstText, self.levelSlider, self.OKbutton, self.instructions])
        self.firstBackground = thorpy.Background(image='quiz.jpg', elements=[self.firstText, self.central_box])
        thorpy.store(self.firstBackground)

        self.startScreen = thorpy.Menu(self.firstBackground)
        self.startScreen.play()
        print("Reached Here - End of level page")

        #Write Instructions to screen
        self.instructionsPage = thorpy.Background(image='abstract.jpg', elements=[self.infoText, self.instructions, self.OKbutton, self.quit1])
        print("Reached Here - Background instructions page")

        self.infoScreen = thorpy.Menu(self.instructionsPage)
        self.infoScreen.play()

        print("Reached Here - Spin the wheel page")
        self.spinWheel = thorpy.Background(image='abstract.jpg', elements=[self.spinWheelText, self.spinWheelInfo, self.quit2, self.OKPlaceholder])
        self.spinWheelPage = thorpy.Menu(self.spinWheel)
        self.spinWheelPage.play()

        self.quiz_resultsLoader()

        print("Reached Here - Second spin the wheel page")
        self.spinWheel = thorpy.Background(image='abstract.jpg', elements=[self.spinWheelText, self.spinWheelInfo, self.quit2, self.OKPlaceholder])
        self.spinWheelPage = thorpy.Menu(self.spinWheel)
        self.spinWheelPage.play()

        print("Reached Here - Second question and result")
        self.createQuizElements()
        self.quizGame = thorpy.Background(image='quizAbstract.jpg', elements=[self.questionText, self.Op1Button, self.Op2Button, self.Op3Button, self.Op3Button, self.Op4Button, self.quit3])
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
        self.resultsBG = thorpy.Background(image='abstract.jpg', elements=[self.resultText, self.OKbutton1, self.quit4])
        self.resultsPage = thorpy.Menu(self.resultsBG)
        self.resultsPage.play()

        self.givePrizesLoader()

        self.dispensePrize()

        self.gameLauncher()

        #Cleanly exit application
        print("Quitting")
        self.application.quit()

# application = thorpy.Application(size=(800, 480), caption="Quiz")
quiz = QuizMain()
