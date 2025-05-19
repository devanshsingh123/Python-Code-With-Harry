# Create a program capable of displaying qyuestion to the user like KBC
# Use List Data type to store the questions and there answers
# Display the final amount the person is taking home after playing the game


Questionlist = [["Question 1",[["A","Option 1",False],["B","Option 2",True],["C","Option 3",False],["D","Option 4",False]]],["Question 2",[["A","Option 1",False],["B","Option 4",True],["C","Option 3",False],["D","Option 4",False]]],["Question 3",[["A","Option 1",False],["B","Option 4",True],["C","Option 3",False],["D","Option 4",False]]],["Question 4",[["A","Option 1",False],["B","Option 4",True],["C","Option 3",False],["D","Option 4",False]]],["Question 5",[["A","Option 1",False],["B","Option 4",True],["C","Option 3",False],["D","Option 4",False]]],["Question 6",[["A","Option 1",False],["B","Option 4",True],["C","Option 3",False],["D","Option 4",False]]],["Question 7",[["A","Option 1",False],["B","Option 4",True],["C","Option 3",False],["D","Option 4",False]]],["Question 8",[["A","Option 1",False],["B","Option 4",True],["C","Option 3",False],["D","Option 4",False]]],["Question 9",[["A","Option 1",False],["B","Option 4",True],["C","Option 3",False],["D","Option 4",False]]],["Question 10",[["A","Option 1",False],["B","Option 4",True],["C","Option 3",False],["D","Option 4",False]]],["Question 11",[["A","Option 1",False],["B","Option 4",True],["C","Option 3",False],["D","Option 4",False]]],["Question 12",[["A","Option 1",False],["B","Option 4",True],["C","Option 3",False],["D","Option 4",False]]],["Question 13",[["A","Option 1",False],["B","Option 4",True],["C","Option 3",False],["D","Option 4",False]]],["Question 14",[["A","Option 1",False],["B","Option 4",True],["C","Option 3",False],["D","Option 4",False]]],["Question 15",[["A","Option 1",False],["B","Option 4",True],["C","Option 3",False],["D","Option 4",False]]],["Question 16",[["A","Option 1",False],["B","Option 4",True],["C","Option 3",False],["D","Option 4",False]]]]
user_answer = 
count = 0
Questions = [["Question 1",[["A","Option 1"],["B","Option 2"],["C","Option 3"],["D","Option 4"]],"B"],["Question 2",[["A","Option 1"],["B","Option 2"],["C","Option 3",["D","Option 4"]]],"C"]]
for index,question in enumerate(Questions):
    correct_ans = question[2]
    print(index,": ",question[0],"\n",question[1][0][0],": ",question[1][0][1],"\n",question[1][1][0],": ",question[1][1][1],"\n",question[1][2][0],": ",question[1][2][1],"\n",question[1][3][0],": ",question[1][3][1])
    user_answer = input("Guess the correct response")
    if(correct_ans != user_answer):
        print("Galat JAWAB, MAAF KIJIYE APKA SAFAR YHI KHATAM HOTA HAI!")
        count = index
        break
    elif(user_answer == "QUIT"):
        print("APKE SATH KHEL KR BAHOT ACHA LGA, AAPKE FUTURE K LIYE BAHOT BAHOT SHUBKAMNAYE!")
    else:
         print("SAHI JAWAB, CONGRATULATIONS , AGAY BADTHAY HAI AGLE SAWAL KI ORE!")



wining_LOT = [10000,30000,60000,120000,350000,800000,1600000,2500000,5000000,7500000,10000000]

if(user_answer == "QUIT"):
    print("AAP JITETE HAI : ",wining_LOT[count],"BAHAUT BAHUT SHUBKAMANAYE")
elif(count+1<4):
    print("CHAAR SAY KM SHI JAWAB KA UTAR DENE KI WAJAH SAY AAJ AAP KOI BHI RAASHI NHI JEET PAAYE")
elif(count+1 >=4 and count+1 < 7):
    print("AAP JITETE HAI : ",wining_LOT[3],"BAHAUT BAHUT SHUBKAMANAYE")
