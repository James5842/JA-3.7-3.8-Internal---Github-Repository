import random
import time
import tkinter as tk
from data import questions
window = tk.Tk()
window.title("               Quiz")
window.geometry("400x300")
display = tk.Text (window, width=50, height=13)
display.place (x=20, y=1020)
display.config(state='disabled')
instructions = tk.Label (window, text="Enter # of chosen answer into the box, then press submit", fg="black", width=45)
instructions.place (x=18, y=1230)
answer_box = tk.Entry (window, width=30)
answer_box.place (x=20, y=1255)
quiz_questions=[]
quiz_questions.append("Placeholder")
n=50
qn=[]
qc=[]
Correct_answers=[]
Correct_answers.append(0)
question_order=[]
global question_1, question_2, question_3, question_4, question_5, question_6, question_7, question_8, question_9, question_10, question_11, question_12, question_13, question_14, question_15, question_16, question_17, question_18, question_19, question_20
question_1=100
question_2=200
question_3=300
question_4=400
question_5=500
question_6=600
question_7=700
question_8=800
question_9=900
question_10=1000
question_11=1100
question_12=1200
question_13=1300
question_14=1400
question_15=1500
question_16=1600
question_17=1700
question_18=1800
question_19=1900
question_20=2000

def numgen ():
  exec("q1()")
  exec("q2()")
  exec("q3()")
  exec("q4()")
  exec("q5()")
  exec("q6()")
  exec("q7()")
  exec("q8()")
  exec("q9()")
  exec("q10()")
  exec("q11()")
  exec("q12()")
  exec("q13()")
  exec("q14()")
  exec("q15()")
  exec("q16()")
  exec("q17()")
  exec("q18()")
  exec("q19()")
  exec("q20()")
  print(question_order)
def q1 ():
  question_1=(random.randint(1,n))
  question_order.append(question_1)
def q2 ():
  question_2=(random.randint(1,n))
  if question_2 in question_order:
    exec("q2()")
  else:
    question_order.append(question_2)
def q3 ():
  question_3=(random.randint(1,n))
  if question_3 in question_order:
    exec("q3()")
  else:
    question_order.append(question_3)
def q4 ():
  question_4=(random.randint(1,n))
  if question_4 in question_order:
    exec("q4()")
  else:
    question_order.append(question_4)
def q5 ():
  question_5=(random.randint(1,n))
  if question_5 in question_order:
    exec("q5()")
  else:
    question_order.append(question_5)
def q6 ():
  question_6=(random.randint(1,n))
  if question_6 in question_order:
    exec("q6()")
  else:
    question_order.append(question_6)
def q7 ():
  question_7=(random.randint(1,n))
  if question_7 in question_order:
    exec("q7()")
  else:
    question_order.append(question_7)
def q8 ():
  question_8=(random.randint(1,n))
  if question_8 in question_order:
    exec("q8()")
  else:
    question_order.append(question_8)
def q9 ():
  question_9=(random.randint(1,n))
  if question_9 in question_order:
    exec("q9()")
  else:
    question_order.append(question_9)
def q10 ():
  question_10=(random.randint(1,n))
  if question_10 in question_order:
    exec("q10()")
  else:
    question_order.append(question_10)
def q11 ():
  question_11=(random.randint(1,n))
  if question_11 in question_order:
    exec("q11()")
  else:
    question_order.append(question_11)
def q12 ():
  question_12=(random.randint(1,n))
  if question_12 in question_order:
    exec("q12()")
  else:
    question_order.append(question_12)
def q13 ():
  question_13=(random.randint(1,n))
  if question_13 in question_order:
    exec("q13()")
  else:
    question_order.append(question_13)
def q14 ():
  question_14=(random.randint(1,n))
  if question_14 in question_order:
    exec("q14()")
  else:
    question_order.append(question_14)
def q15 ():
  question_15=(random.randint(1,n))
  if question_15 in question_order:
    exec("q15()")
  else:
    question_order.append(question_15)
def q16 ():
  question_16=(random.randint(1,n))
  if question_16 in question_order:
    exec("q16()")
  else:
    question_order.append(question_16)
def q17 ():
  question_17=(random.randint(1,n))
  if question_17 in question_order:
    exec("q17()")
  else:
    question_order.append(question_17)
def q18 ():
  question_18=(random.randint(1,n))
  if question_18 in question_order:
    exec("q18()")
  else:
    question_order.append(question_18)
def q19 ():
  question_19=(random.randint(1,n))
  if question_19 in question_order:
    exec("q19()")
  else:
    question_order.append(question_19)
def q20 ():
  question_20=(random.randint(1,n))
  if question_20 in question_order:
    exec("q20()")
  else:
    question_order.append(question_20)
def DQ():
  qc.clear()
  qc.append(question_order[qn[0]])
  for question in questions:
    if question['name']==qc[0]:
      display.config(state='normal')
      display.delete("0.0",tk.END)
      display.insert(tk.END,(question['title']) +'\n')
      display.config(state='disabled')
      i = 1
      for answer in question['answers']:
        display.config(state='normal')
        display.insert(tk.END, str(i) + ". " + answer['answer'] + '\n')
        display.config(state='disabled')
        i += 1
    else:
      pass

def submit():
  for question in questions:
      i = 0
      for answer in question['answers']:
        i += 1
  response = answer_box.get()
  if response.isdigit():
      response = int(response)
      response -= 1
      if response >= 0 and response < i:
        for question in questions:
          if question['name']==qc[0]:
            if question['answers'][response]['correct'] == 10:
              display.config(state='normal')
              display.delete("0.0",tk.END)
              display.insert(tk.END,"Correct!")
              answer_box.delete("0",tk.END)
              display.config(state='disabled')
              window.update()
              count2=Correct_answers[0]+1
              Correct_answers.clear()
              Correct_answers.append(count2)
              time.sleep(1)
            if question['answers'][response]['correct'] == 0:
              display.config(state='normal')
              display.delete("0.0",tk.END)
              display.insert(tk.END,"Incorrect!")
              answer_box.delete("0",tk.END)
              display.config(state='disabled')
              window.update()
              time.sleep(1)
        count=qn[0]+1
        qn.clear()
        qn.append(count)
        if qn[0] >= quiz_questions[0]-1:
          instructions.place (x=18, y=1230)
          answer_box.place (x=20, y=1255)
          submit_button.place (x=270, y=1250)
          display.config(state='normal')
          display.delete("0.0",tk.END)
          display.insert(tk.END,"Quiz over, you got ")
          display.insert(tk.END,Correct_answers)
          display.insert(tk.END,"/")
          display.insert(tk.END,quiz_questions)
          display.insert(tk.END," Correct")
          answer_box.delete("0",tk.END)
          display.config(state='disabled')
        else:
          exec("DQ()")
      else:
        display.config(state='normal')
        display.delete("0.0",tk.END)
        display.insert(tk.END,"Please enter a number between 1 and ")
        display.insert(tk.END,i)
        answer_box.delete("0",tk.END)
        display.config(state='disabled')
        window.update()
        time.sleep(1)
        print("Please enter a number between 1 and", i - 1)
        exec("DQ()")
  else:
    display.config(state='normal')
    display.delete("0.0",tk.END)
    display.insert(tk.END,"Please enter an actual number")
    answer_box.delete("0",tk.END)
    display.config(state='disabled')
    window.update()
    time.sleep(1)
    print("That's not a number!")
    exec("DQ()")


  
submit_button = tk.Button(window, text="SUBMIT", command=submit, width=10)
submit_button.place (x=270, y=1250)

def start():
  if quiz_questions[0]==10 or quiz_questions[0]==15 or quiz_questions[0]==20:
    qn.clear()
    qn.append(0)
    display.place (x=20, y=20)
    instructions.place (x=18, y=230)
    answer_box.place (x=20, y=255)
    submit_button.place (x=270, y=250)
    start_button.place (x=167.5, y=1130)
    short_quiz_button.place (x=20, y=1080)
    medium_quiz_button.place (x=145, y=1080)
    long_quiz_button.place (x=270, y=1080)
    quiz_length.place (x=92, y=1020)
    choice.place (x=20.5, y=1060)
    exec("numgen()")
    display.config(state='normal')
    exec("DQ()")
  else:
    if quiz_questions[0]=="Placeholder":
      quiz_length.config(state='normal')
      quiz_length.delete("0.0",tk.END)
      quiz_length.insert(tk.END,"Select a length for the quiz")
      quiz_length.config(state='disabled')
    else:
      quiz_length.config(state='normal')
      quiz_length.delete("0.0",tk.END)
      quiz_length.insert(tk.END,"Something has gone very wrong")
      quiz_length.config(state='disabled')

def SL ():
  quiz_length.config(state='normal')
  quiz_questions.clear()
  quiz_questions.append(10)
  quiz_length.delete("0.0",tk.END)
  quiz_length.insert(tk.END,"Quiz will be 10 questions long")
  print(quiz_questions)
  quiz_length.config(state='disabled')
  pass
def ML ():
  quiz_length.config(state='normal')
  quiz_questions.clear()
  quiz_questions.append(15)
  quiz_length.delete("0.0",tk.END)
  quiz_length.insert(tk.END,"Quiz will be 15 questions long")
  print(quiz_questions)
  quiz_length.config(state='disabled')
  pass
def LL ():
  quiz_length.config(state='normal')
  quiz_questions.clear()
  quiz_questions.append(20)
  quiz_length.delete("0.0",tk.END)
  quiz_length.insert(tk.END,"Quiz will be 20 questions long")
  print(quiz_questions)
  quiz_length.config(state='disabled')
  pass

choice = tk.Label(window, text="Choose quiz length:", font=("Arial", 10), fg="black", width=39)
choice.place (x=20.5, y=60)
qn.append(1)
quiz_length = tk.Text (window, width=24, height=1, font=("Arial", 17))
quiz_length.place (x=16, y=20)
quiz_length.config(state='disabled')

short_quiz_button = tk.Button(window, text="Short, 10", width=10, command=SL)
short_quiz_button.place (x=20, y=80)
medium_quiz_button = tk.Button(window, text="Medium, 15", width=10, command=ML)
medium_quiz_button.place (x=145, y=80)
long_quiz_button = tk.Button(window, text="Long, 20", width=10, command=LL)
long_quiz_button.place (x=270, y=80)
start_button = tk.Button(window, text="START", command=start)
start_button.place (x=167.5, y=130)

#exec("numgen2()")