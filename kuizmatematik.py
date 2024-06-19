import time
print("**********************************")

#ucapan selamat datang
print("SELAMAT DATANG KE KUIZ MATEMATIK!")
time.sleep(1)
print("**********************************")

#Chances
chances=1
print("Anda perlu memilih", chances,"jawapan yang betul.\nAnda akan mendapat 1 markah jika menjawab jawapan yang betul.\n")
time.sleep(2)

#skor kuiz
score=0

#soalan 1
print("==================================================")
question_1=print("1) 20 + 15 + (-34)\n(A) 69\n(B) -1\n(C) 1\n(D) -69\n\n")
answer_1= "c"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_1):
        print("JAWAPAN ANDA BETUL! TAHNIAH!\n")
        score = score + 1
        break
    else:
        print("MAAF, JAWAPAN ANDA SALAH!\n")
        time.sleep(0.5)
        print("JAWAPAN YANG BETUL IALAH", answer_1, "\n\n")

time.sleep(2)

#soalan 2
print("==================================================")
question_2 = print("2)-1-(-4)?\n(A) 3\n(B) 4\n(C) 5\n(D) 6\n\n")  
answer_2 = "a"

for i in range(chances):
    answer = input("answer: ")
    if (answer.lower() == answer_2):
        print("JAWAPAN ANDA BETUL! TAHNIAH!\n")
        score = score + 1
        break
    else:
        print("JAWAPAN ANDA SALAH!\n ")
        time.sleep(0.5)
        print("JAWAPAN YANG BETUL IALAH", answer_2, "\n\n")

time.sleep(2)

#soalan 3
print("==================================================")
question_3 =print("3)  7+2(-3)?\n(A) 0\n(B) 1\n(C) 2\n(D) 3\n\n")
answer_3= "b"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_3):
        print("JAWAPAN ANDA BETUL! TAHNIAH!\n")
        score = score + 1
        break
    else:
        print("JAWAPAN ANDA SALAH!\n")
        time.sleep(0.5)
        print("JAWAPAN YANG BETUL IALAH", answer_3, "\n\n")

time.sleep(2)

#soalan 4
print("==================================================")
question_4 =print("4)  -8X(-2+3)?\n(A) -6\n(B) -7\n(C) -8\n(D) -9\n\n")
answer_4= "C"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_4):
        print("JAWAPAN ANDA BETUL! TAHNIAH!\n")
        score = score + 1
        break
    else:
        print("JAWAPAN ANDA SALAH!\n")
        time.sleep(0.5)
        print("JAWAPAN YANG BETUL IALAH",answer_4, "\n\n")

time.sleep(2)

#soalan 5
print("==================================================")
question_5 =print("5)  -230 +(-360) +(-3)+400?\n(A) -193\n(B) -196\n(C) -198\n(D) -200\n\n")
answer_5= "a"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_5):
        print("JAWAPAN ANDA BETUL! TAHNIAH!\n")
        score = score + 1
        break
    else:
        print("JAWAPAN ANDA SALAH!\n")
        time.sleep(0.5)
        print("JAWAPAN YANG BETUL IALAH", answer_5, "\n\n")

time.sleep(2)

#paparan untuk skor akhir
print("==================================================")
while score >=2:
    print("TAHNIAH! SKOR ANDA IALAH", score)
    break

while score <2:
    print("CUBA LAGI! SKOR ANDA IALAH",score)
    break

#mesej terima kasih
print("TERIMA KASIH KERANA MENJAWAB KUIZ MATEMATIK!")
BaseException