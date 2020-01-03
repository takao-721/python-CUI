import numpy as np

n=0
turn=0

numb=['[0] ','[1] ','[2] ','[3] ',
      '[4] ','[5] ','[6] ','[7] ',
      '[8] ','[9] ','[10]','[11]',
      '[12]','[13]','[14]','[15]']

#マス目の出力 0からスタート
mass=['・','・','・','・',
      '・','白','黒','・',
      '・','黒','白','・',
      '・','・','・','・']#空白

mass_save=['・','・','・','・',
           '・','白','黒','・',
           '・','黒','白','・',
           '・','・','・','・']

while n==0:

    cou=0
    for i in range(16):
        print (numb[i], end="")#改行無し文字列の表示
        cou+=1
        if cou%4==0:#改行
            print ('\n')

    cou=0
    for i in range(16):
        print (mass[i], end="")#改行無し文字列の表示
        mass_save[i]=mass[i]
        cou+=1
        if cou%4==0:#改行
            print ('\n')

    if turn==0:
        while True:
            print('入力してください！白')
            a = input()
            a = int(a)
            if a<16 and mass[a]=='・':
                break
        mass[a]='白'
        turn=1
        if a==0 or a==1 or a==4:
            if mass[a+1]=='黒' and mass[a+2]=='白':
                mass[a+1]='白'
            if mass[a+4]=='黒' and mass[a+8]=='白':
                mass[a+4]='白'
            if mass[a+5]=='黒' and mass[a+10]=='白':
                mass[a+5]='白'

        if a==2 or a==3 or a==7:
            if mass[a-1]=='黒' and mass[a-2]=='白':
                mass[a-1]='白'
            if mass[a+3]=='黒' and mass[a+6]=='白':
                mass[a+3]='白'
            if mass[a+4]=='黒' and mass[a+8]=='白':
                mass[a+4]='白'

        if a==8 or a==12 or a==13:
            if mass[a+1]=='黒' and mass[a+2]=='白':
                mass[a+1]='白'
            if mass[a-3]=='黒' and mass[a-6]=='白':
                mass[a-3]='白'
            if mass[a-4]=='黒' and mass[a-8]=='白':
                mass[a-4]='白'

        if a==11 or a==14 or a==15:
            if mass[a-1]=='黒' and mass[a-2]=='白':
                mass[a-1]='白'
            if mass[a-4]=='黒' and mass[a-8]=='白':
                mass[a-4]='白'
            if mass[a-5]=='黒' and mass[a-10]=='白':
                mass[a-5]='白'

        if a==1 or a==2:
            if mass[a+4]=='黒' and mass[a+8]=='黒' and mass[a+12]=='白':
                mass[a+4]='白'
                mass[a+8]='白'

        if a==13 or a==14:
            if mass[a-4]=='黒' and mass[a-8]=='黒' and mass[a-12]=='白':
                mass[a-4]='白'
                mass[a-8]='白'

        if a==4 or a==8:
            if mass[a+1]=='黒' and mass[a+2]=='黒' and mass[a+3]=='白':
                mass[a+1]='白'
                mass[a+2]='白'

        if a==7 or a==11:
            if mass[a-1]=='黒' and mass[a-2]=='黒' and mass[a-3]=='白':
                mass[a-1]='白'
                mass[a-2]='白'

        if a==0:
            if mass[a+1]=='黒' and mass[a+2]=='黒' and mass[a+3]=='白':
                mass[a+1]='白'
                mass[a+2]='白'
            if mass[a+5]=='黒' and mass[a+10]=='黒' and mass[a+15]=='白':
                mass[a+5]='白'
                mass[a+10]='白'
            if mass[a+4]=='黒' and mass[a+8]=='黒' and mass[a+12]=='白':
                mass[a+4]='白'
                mass[a+8]='白'

        if a==3:
            if mass[a-1]=='黒' and mass[a-2]=='黒' and mass[a-3]=='白':
                mass[a-1]='白'
                mass[a-2]='白'
            if mass[a+3]=='黒' and mass[a+6]=='黒' and mass[a+9]=='白':
                mass[a+3]='白'
                mass[a+6]='白'
            if mass[a+4]=='黒' and mass[a+8]=='黒' and mass[a+12]=='白':
                mass[a+4]='白'
                mass[a+8]='白'

        if a==12:
            if mass[a-4]=='黒' and mass[a-8]=='黒' and mass[a-12]=='白':
                mass[a-4]='白'
                mass[a-8]='白'
            if mass[a-3]=='黒' and mass[a-6]=='黒' and mass[a-9]=='白':
                mass[a-3]='白'
                mass[a-6]='白'
            if mass[a+1]=='黒' and mass[a+2]=='黒' and mass[a+3]=='白':
                mass[a+1]='白'
                mass[a+2]='白'

        if a==15:
            if mass[a-4]=='黒' and mass[a-8]=='黒' and mass[a-12]=='白':
                mass[a-4]='白'
                mass[a-8]='白'
            if mass[a-5]=='黒' and mass[a-10]=='黒' and mass[a-15]=='白':
                mass[a-5]='白'
                mass[a-10]='白'
            if mass[a-1]=='黒' and mass[a-2]=='黒' and mass[a-3]=='白':
                mass[a-1]='白'
                mass[a-2]='白'

    else:
        while True:
            print('入力してください！黒')
            b = input()
            b = int(b)
            if b<16 and mass[b]=='・':
                break
        mass[b]='黒'
        turn=0

        if b==0 or b==1 or b==4:
            if mass[b+1]=='白' and mass[b+2]=='黒':
                mass[b+1]='黒'
            if mass[b+4]=='白' and mass[b+8]=='黒':
                mass[b+4]='黒'
            if mass[b+5]=='白' and mass[b+10]=='黒':
                mass[b+5]='黒'

        if b==2 or b==3 or b==7:
            if mass[b-1]=='白' and mass[b-2]=='黒':
                mass[b-1]='黒'
            if mass[b+3]=='白' and mass[b+6]=='黒':
                mass[b+3]='黒'
            if mass[b+4]=='白' and mass[b+8]=='黒':
                mass[b+4]='黒'

        if b==8 or b==12 or b==13:
            if mass[b+1]=='白' and mass[b+2]=='黒':
                mass[b+1]='黒'
            if mass[b-3]=='白' and mass[b-6]=='黒':
                mass[b-3]='黒'
            if mass[b-4]=='白' and mass[b-8]=='黒':
                mass[b-4]='黒'

        if b==11 or b==14 or b==15:
            if mass[b-1]=='白' and mass[b-2]=='黒':
                mass[b-1]='黒'
            if mass[b-4]=='白' and mass[b-8]=='黒':
                mass[b-4]='黒'
            if mass[b-5]=='白' and mass[b-10]=='黒':
                mass[b-5]='黒'

        if b==1 or b==2:
            if mass[b+4]=='白' and mass[b+8]=='白' and mass[b+12]=='黒':
                mass[b+4]='黒'
                mass[b+8]='黒'

        if b==13 or b==14:
            if mass[b-4]=='白' and mass[b-8]=='白' and mass[b-12]=='黒':
                mass[b-4]='黒'
                mass[b-8]='黒'

        if b==4 or b==8:
            if mass[b+1]=='白' and mass[b+2]=='白' and mass[b+3]=='黒':
                mass[b+1]='黒'
                mass[b+2]='黒'

        if b==7 or b==11:
            if mass[b-1]=='白' and mass[b-2]=='白' and mass[b-3]=='黒':
                mass[b-1]='黒'
                mass[b-2]='黒'

        if b==0:
            if mass[b+1]=='白' and mass[b+2]=='白' and mass[b+3]=='黒':
                mass[b+1]='黒'
                mass[b+2]='黒'
            if mass[b+5]=='白' and mass[b+10]=='白' and mass[b+15]=='黒':
                mass[b+5]='黒'
                mass[b+10]='黒'
            if mass[b+4]=='白' and mass[b+8]=='白' and mass[b+12]=='黒':
                mass[b+4]='黒'
                mass[b+8]='黒'

        if b==3:
            if mass[b-1]=='白' and mass[b-2]=='白' and mass[b-3]=='黒':
                mass[b-1]='黒'
                mass[b-2]='黒'
            if mass[b+3]=='白' and mass[b+6]=='白' and mass[b+9]=='黒':
                mass[b+3]='黒'
                mass[b+6]='黒'
            if mass[b+4]=='白' and mass[b+8]=='白' and mass[b+12]=='黒':
                mass[b+4]='黒'
                mass[b+8]='黒'

        if b==12:
            if mass[b-4]=='白' and mass[b-8]=='白' and mass[b-12]=='黒':
                mass[b-4]='黒'
                mass[b-8]='黒'
            if mass[b-3]=='白' and mass[b-6]=='白' and mass[b-9]=='黒':
                mass[b-3]='黒'
                mass[b-6]='黒'
            if mass[b+1]=='白' and mass[b+2]=='白' and mass[b+3]=='黒':
                mass[b+1]='黒'
                mass[b+2]='黒'

        if b==15:
            if mass[b-4]=='白' and mass[b-8]=='白' and mass[b-12]=='黒':
                mass[b-4]='黒'
                mass[b-8]='黒'
            if mass[b-5]=='白' and mass[b-10]=='白' and mass[b-15]=='黒':
                mass[b-5]='黒'
                mass[b-10]='黒'
            if mass[b-1]=='白' and mass[b-2]=='白' and mass[b-3]=='黒':
                mass[b-1]='黒'
                mass[b-2]='黒'

    equal_cou=0
    flag_num=0
    i=0
    for i in range(16):
        if mass_save[i]!=mass[i]:
            equal_cou+=1
            flag_num=i

    if equal_cou==1:
        mass[flag_num]='・'
        if turn==1:
            turn=0
        elif turn==0:
            turn=1

    i=0
    fin_check=0
    for i in range(16):
        if mass[i]=='・':
            fin_check+=1

    #print(fin_check)

    if fin_check==0:
        print('終了です')
        break
