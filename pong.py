from tkinter import *
from random import randint as rand

def menu():
	global canvasMenu , welcomeMsg , startButton , bgImage, playerInput , nameButton , window
	window['background']='white'
	canvasMenu = Canvas(window,width=width,height=height,bg= 'white')
	labelImage = Label(window,image=bgImage,width=width/4,height=height/4)
	labelImage.place(x=1045,y=520)
	welcomeMsg = Label(window,text='PyPong Game',bg='white',fg='black',font="Edo 50 bold")
	welcomeMsg.pack(pady=40)
	startButton = Button(canvasMenu,text= 'Start Game',width=25,fg= 'green',font= 'Arial 30 bold',command= destroy)
	startButton.pack()
	helpButton = Button(canvasMenu,text= 'Help',font='Arial 30 bold',width=25,command= help)
	helpButton.pack()
	quitButton = Button(canvasMenu,text= 'Quit Game',fg= 'red',font= 'Arial 30 bold',width=25,command= quit)
	quitButton.pack()
	leaderButton = Button(canvasMenu,text= 'Leader Board',fg= 'orange',font= 'Arial 30 bold',width=25,command= leaderBoard)
	leaderButton.pack()
	canvasMenu.pack()
def canvasName():
	global nameCanvas , playerInput , nameButton , welcomeMsg , nameCanvas , window
	window['background']='black'
	nameCanvas = Canvas(window,width=width/4,height=height/4,bg= 'black')
	welcomeMsg = Label(window,text='PyPong Game',bg='black',fg='white',font="Arial 50 bold")
	welcomeMsg.pack(pady=40)
	nameCanvas['background']='black'
	playerInput = Entry(nameCanvas,fg= 'white',bg= 'black', font= 'Arial 30 bold',width=25,borderwidth= 3)
	playerInput.pack()
	nameButton = Button(nameCanvas,text='Enter your name ',font= 'Arial 30 bold',bg='black',fg='black',width=25, command=name)
	nameButton.pack()
	nameCanvas.pack()

leader_Board= {}
playerList = []
def name():
	global playerName
	playerName = playerInput.get()
	welcome = Toplevel(window)
	welcome.geometry('280x170')
	welcome['background']='black'
	playerInput.destroy()
	nameButton.destroy()
	welcome.title('Welcome Message')
	l1 = Label(welcome,text= 'Hello '+ str(playerName) + ' ! ', font= 'Arial 17 bold',fg='white',bg='black').pack()
	l2 = Label(welcome,text= 'WELCOME TO PYPONG ! ', font= 'Arial 17 bold',fg= 'white',bg='black').pack()
	l3 = Label(welcome,text= 'CLICK START TO', font= 'Arial 17 bold',fg='white',bg='black').pack()
	l4 = Label(welcome,text= 'PLAY', font= 'Arial 20 bold',fg='green',bg='black').pack()
	nameCanvas.destroy()
	welcomeMsg.destroy()
	menu()

def leaderboardData():
	global leader_Board , playerList , playerName , lastScore
	with open("leaderBoard.txt","a") as file:
		leader_Board[playerName]= lastScore
		for x,y in leader_Board.items():
			file.write(str(x) + ':' + str(y) + '\n')
			file.close()
def leaderBoard():
	global sortedScores , leader_Board , history , player1
	board = Toplevel()
	board.title('Leader Board')
	board.geometry('600x600')
	board['background']='black'
	a = open('leaderBoard.txt')
	history = a.readlines()
	for lines in history:
		key , value = lines.strip('\n').split(':')
		leader_Board[key] = value
		print(leader_Board)
	sortedT = sorted(leader_Board.items(),key= lambda x: int(x[1]),reverse= True)
	sortedScores = {k: v for k, v in sortedT}
	print(sortedScores)
	labelBoard = Label(board, text = 'TOP SCORES', font= 'Arial 40 bold', fg='yellow',bd=1,relief='sunken',bg='black')
	labelBoard.pack(pady=10,ipadx=10,ipady=10)
	count = 1
	for x ,y in sortedScores.items():
		labelBoard2 = Label(board, text=str(count) + '.' + x + ':' + y, font= 'Courier 20 bold' , bd = 1 , relief='sunken',bg='black',fg= 'white')
		labelBoard2.pack(pady=10,ipadx=10,ipady=10)
		count += 1
	board.mainloop()
def quit():
	window.destroy()
def help():
	helpK = Toplevel(window)
	helpK.geometry('480x270')
	helpK.title('need help?')
	how = Label(helpK,text= 'How to play?', font= 'Arial 17 bold').pack()
	instructions= Label(helpK,text= 'Move your paddle to hit the ball against the wall, if the ball fall' , font= 'Arial 10 bold').pack()
	lose = Label(helpK,text= 'YOU LOSE!' , font= 'Arial 15 bold').pack()
	yourScore = Label(helpK,text= 'if not' , font= 'Arial 10 bold').pack()
	scorePlus = Label(helpK,text= 'your score --> +1 ' , font= 'Arial 15 bold').pack()
	pauseHelp = Label(helpK,text= '1. Pause: spacebar ' , font= 'Arial 10 bold')
	pauseHelp.place(x=0,y=130)
	resumeHelp = Label(helpK,text= '2. Resume: u' , font= 'Arial 10 bold')
	resumeHelp.place(x=0,y=150)
	bossHelp = Label(helpK,text= '3. Boss "this will pop up a window page": b ' , font= 'Arial 10 bold')
	bossHelp.place(x=0,y=170)
	bossHelp = Label(helpK,text= '4. Cheat Code: c ' , font= 'Arial 10 bold')
	bossHelp.place(x=0,y=190)
	helplabel = Label(helpK,image=helpImage,width=240,height=135)
	helplabel.place(x=300,y=50)

def bossKey(event):
	global  width

	bossK = Toplevel(window) #create window
	bossK.geometry('1280x720')
	bossK.title('') #title of window
	bossLabel = Label(bossK,image=bossImage)
	bossLabel.place(x=0,y=0,relwidth=1,relheight=1)
	bossLabel.pack()
	pause(event=None)


def pause(event):
	global pauseGAME , pauseGametxt , game_over , canvas , lastScore
	if pauseGAME == False:
		pauseGAME = True
		pauseGametxt = canvas.create_text(480,380,font=' Arial 20 bold',text = 'Press "U" to resume', fill= 'red')
	if game_over == True:
		canvas.delete(pauseGametxt)
		lastScore = score
		print(lastScore)
		leaderboardData()

def unpause(event):
	global pauseGAME , pauseGametxt , canvas
	if pauseGAME== True:
		pauseGAME = False
		canvas.delete(pauseGametxt)
		window.after(1, ballMotion)
		print('clicked')
def GameEnd():
	# window.destroy()
	global window , canvas
	exitButton.destroy()
	canvas.destroy()
	menu()

def destroy():
	canvasMenu.destroy()
	welcomeMsg.destroy()
	startButton.destroy()
	diffuculty()

def diffuculty():
	global canvasDifficulty, levelMsg , easyButton , mediumButton , hardButton
	canvasDifficulty = Canvas(window,width=width,height=height,bg= 'white')
	levelMsg = Label(window,text='Please choose a level: ',bg='white',fg='black',font="Edo 50 bold")
	levelMsg.pack(pady=40)
	easyButton = Button(canvasDifficulty,text='EASY',font= 'Arial 30 bold',fg='green',width=25, command= easy)
	easyButton.pack()
	mediumButton = Button(canvasDifficulty,text= 'MEDUIM',width=25,fg= 'orange',font= 'Arial 30 bold',command= medium)
	mediumButton.pack()
	hardButton = Button(canvasDifficulty,text= 'HARD',font='Arial 30 bold',fg='red',width=25,command= hard)
	hardButton.pack()
	canvasDifficulty.pack()
def cheatCode(event):
	global paddle , canvas , ballX , ballY
	canvas.delete(paddle)
	paddle = canvas.create_rectangle(600, 610, 1000,640, fill = "yellow")
	ballX = 0.2
	ballY = 0.2


def easy():
	global paddle , canvas
	canvasDifficulty.destroy()
	easyButton.destroy()
	levelMsg.destroy()
	GameStart()
	canvas.delete(paddle)
	paddle = canvas.create_rectangle(500, 610, 800, 640, fill = "green")


def medium():
	global paddle , canvas , ballX, ballY
	canvasDifficulty.destroy()
	mediumButton.destroy()
	levelMsg.destroy()
	GameStart()
	canvas.delete(paddle)
	canvas.delete(ballX)
	canvas.delete(ballY)
	paddle = canvas.create_rectangle(460, 610, 610, 640, fill = "orange")
	ballX = 0.5
	ballY = 0.5


def hard():
	global paddle , score , speed , direction , ballX , ballY , canvas
	canvasDifficulty.destroy()
	hardButton.destroy()
	levelMsg.destroy()
	GameStart()
	canvas.delete(paddle)
	canvas.delete(ballX)
	canvas.delete(ballY)
	paddleH = canvas.create_rectangle(60, 610, 110, 640, fill = "Red")
	paddle = paddleH
	ballX = 0.7
	ballY = 0.7

def GameStart():
	global canvas , paddle , startX , ball , scoreTxt , gameOverTxt , exitButton , exitButton
	global speed , direction , ballX , ballY , score , BossCanvas , bossImage , decoy , playerPosition
	speed = 1
	direction = 0
	ballX = 0.2
	ballY = 0.2
	score = 0
	canvas = Canvas(window, width = width, height = height)
	paddle = canvas.create_rectangle(460, 610, 610, 640, fill = "Red")
	startX = rand(10, 900)
	ball = canvas.create_oval(40,40,20,20,fill='black')
	exitButton = Button(window,text= 'Exit Game',fg= 'red', font='Arial 30 bold', command=GameEnd)
	exitButton.pack()
	scoreTxt = canvas.create_text(75,20, text = "Score: 0", fill = "Black",font='Arial 30 bold')
	gameOverTxt = canvas.create_text(635,360, text = "", fill = "Black")
	canvas.pack()
	canvas.bind('<Left>', leftKey)
	canvas.bind('<KeyRelease-Left>', release)
	canvas.bind('<Right>', rightKey)
	canvas.bind('<KeyRelease-Right>', release)
	window.bind('<b>',bossKey)
	canvas.bind('<space>',pause)
	canvas.bind('<u>',unpause)
	canvas.bind('<c>',cheatCode)
	canvas.focus_set()
	paddleMotion()
	ballMotion()

def paddleMotion():
	global direction
	global speed
	global playerPosition
	global paddle
	global canvas
	playerPosition = canvas.coords(paddle)
	if (playerPosition[0] < 0 or playerPosition[2] > width):
		direction = -direction
	canvas.move(paddle, direction * speed, 0)
	window.after(1, paddleMotion)


def ballMotion():
	global ballX
	global ballY
	global score
	global game_over
	global pauseGametxt
	global canvas
	ballPosition = canvas.coords(ball)
	ballColl = canvas.find_overlapping(ballPosition[0], ballPosition[1], ballPosition[2], ballPosition[3])
	ballColl = list(ballColl)
	try:
		ballColl.remove(scoreTxt)
	except:
		pass

	try:
		ballColl.remove(gameOverTxt)
	except:
		pass
	try:
		ballColl.remove(bossLabel)
	except:
		pass
	if(len(ballColl) > 1):
		score += 1
		canvas.itemconfig(scoreTxt, text = ("Score: "+ str(score)))
		ballX = ballX * 1.2
		ballY = ballY * 1.2
		ballY = -ballY
	if(ballPosition[1] < 0):
		ballY = -ballY
	if(ballPosition[0] < 0 or ballPosition[2] > width):
		ballX = -ballX
	if(ballPosition[3] > height):
		canvas.itemconfig(gameOverTxt, text = "GAME OVER!", font = ("Arial", 50))
		game_over = True
		try:
			canvas.delete(pauseGametxt)
		except:
			pass
	if pauseGAME == False:
		window.after(1, ballMotion)
		canvas.move(ball, ballX, ballY)
	elif pauseGAME== True:
		window.update()

def leftKey(event):
	global direction
	direction = -1

def rightKey(event):
	global direction
	direction = 1

def release(event):
	global direction
	direction = 0

def setWindowDimensions(w,h):
  window = Tk() #create window
  window['background']='white'
  window.title('Pypong') #title of window
  ws = window.winfo_screenwidth() #computer screen size
  hs = window.winfo_screenheight()
  x = (ws/2) - (w/2) #calculates the center
  y = (hs/2) - (h/2)
  window.geometry('%dx%d+%d+%d' % (w,h,x,y)) #window size
  window.state("normal")
  return window

width = 1280 # width of snake’s world
height = 720 # height of snake’s world
window = setWindowDimensions(width,height)
bossImage = PhotoImage(file = "bosskey2.png")
bgImage = PhotoImage(file = "p4.png")
helpImage = PhotoImage(file = "help.png")
pauseGAME = False
game_over = False
canvasName()
window.mainloop()
