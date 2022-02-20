from tkinter import *
from tkinter import messagebox
import random
# .txt file open and readmode
file = open("Student.txt", "r")
# read and split 
wordlist = file.read().split()

root = Tk()
root.title("Hangman Game")
root.geometry("800x500+300+100")
root.configure(background = "Black")

def Hangman():
    global wordfromlist,lengthofwordstar,ss1,n,temp,showstar,character
    # chaches the characters that a user have input
    character = user_input.get()
    # delete Everything written on the input box
    input1.delete(0,END)
    if(n>0):
        #checking chracter in wordfromlist
        if(character in wordfromlist):
            for i in range(ss1):
                #it compares index of the character entered and index of *
                if(wordfromlist[i] == character and lengthofwordstar[i] == '*'):
                    lengthofwordstar.pop(i)
                    lengthofwordstar.insert(i,wordfromlist[i])
                    Concat = ''.join(lengthofwordstar)
                    wordfromlist = list(wordfromlist)
                    wordfromlist.pop(i)
                    wordfromlist.insert(i,"*")
                    wordlabel.configure(text = Concat)
                    if(Concat==temp):
                        result.configure(text='Congratulations YOU WON')
                        res = messagebox.askyesno("Notification",'Congratulations You won The game......\n want to play again ?')
                        if (res == True):
                            Word_list()
                        else:
                            root.destroy()

        else:
            n -= 1
            leftchances.configure(text = f'Left Chances: {n}')
    if(n<=0):
        result.configure(text='OOPS YOU LOSS')
        res = messagebox.askyesno("Notification", 'OOPS YOU LOSS \n want to play again ?')
        if (res == True):
            Word_list()
        else:
            root.destroy()
    
#*_______________Labels___________________*
# heading Label
introlabel = Label(root, text = "Welcome to Hangman",background = "Blue",font = ("Times New Roman", 28, 'bold'))
introlabel.place(x = 220, y = 0)
        
# Word Label to show number of words in star that a user have to guess
wordlabel = Label(root, text = "",font = ('Times New Roman',25),background = "Black",foreground = 'Blue')
wordlabel.place(x = 350, y = 100)

# this label shows Number of chances left
leftchances = Label(root, text = "",font = ('Times New Roman',15),background = "Black",foreground = 'red')
leftchances.place(x = 0, y = 100)

# This Label will show wether we won or lose
result = Label(root, text = "",
               font = ('Times New Roman',15),
               background = "Black",foreground = 'Blue')
result.place(x = 300, y = 350)
        
#*____________Entry Boxes____________*
# saving user input
user_input = StringVar()
# Word that user will input
input1 = Entry(root, font = ('Times New Roman',15),relief = 'sunken',border = 4,width = 25,background = "green",foreground = "white",justify = 'center',textvariable = user_input)
input1.focus_set()
input1.place(x = 260, y = 200)

#*______________Button_______________*
bt1 = Button(root, text = "Guess",font = ('Times New Roman',15,'bold'),
             background = 'red',activebackground = 'blue',activeforeground = 'white',
             width = 12,border = 4,command = Hangman)
bt1.place(x = 310, y = 250)


def Word_list():
    global wordfromlist,lengthofwordstar,ss1,n,temp,showstar
    #random word selected from .txt file
    wordfromlist = random.choice(wordlist)
    lengthofwordstar = ['*' for i in wordfromlist]
    ss1 = len(wordfromlist)
    #length of word from the random list
    n = ss1
    temp = wordfromlist
    leftchances.configure(text = f"Left Chances: {n}")
    # LENGTH OF star in "lengthofwordstar" WILL BE ADDED TO THIS
    showstar = ''
    for i in lengthofwordstar:
        # adding star label to show
        showstar += i+' '
    wordlabel.configure(text=showstar)
    result.configure(text = '')
        
Word_list()
root.mainloop()