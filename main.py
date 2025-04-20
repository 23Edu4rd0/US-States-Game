import turtle 
import pandas as pd
import tkinter.messagebox

SCORE = 0

df = pd.read_csv('50_states.csv')

screen = turtle.Screen()
screen.title('U.S. States Game')

image = 'blank_states_img.gif'
turtle.addshape(image)
turtle.shape(image)

guessed_states = []


while len(guessed_states) < 50:
    title = f'{SCORE} / 50 States Correct'
    answer_state = turtle.textinput(title=title, prompt='What\'s the state\'s name?').title()
    
   
        
    if answer_state in df['state'].values and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        print('True')
        SCORE += 1
        state = df[df['state'] == answer_state]
        x = int(state['x'].iloc[0])
        y = int(state['y'].iloc[0])

        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        writer.goto(x, y)
        writer.write(answer_state, align='center', font=('Arial', 8, 'bold'))
        
        if len(guessed_states) == 50:
            tkinter.messagebox.showinfo(title='Congratulations!', message='You guessed all 50 states!')
            break
            
    elif answer_state == 'Exit':
        tkinter.messagebox.showinfo(title='Goodbye', message='Thanks for playing! We created a file with the states you missed.')
        states_missed = df[df['state'].isin(guessed_states) == False]
        states_missed.to_csv('states_to_learn.csv', index=False)
        break
    
    elif answer_state in guessed_states:
        tkinter.messagebox.showinfo(title='Already Guessed', message = f'You already guessed {answer_state}!')
    
    else:
        print('False')
    

    



screen.exitonclick()