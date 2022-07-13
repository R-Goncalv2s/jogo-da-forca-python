print("---Jogo da forca---")
print("Dica:Sua palavra é uma série")

p1='Friends';p2='Euphoria';p3='Cobra Kai';p4='Black Mirron';p5='Lucifer';

import random
palavra = ['Friends', 'Euphoria', 'Cobra Kai', 'Black Mirron', 'Lucifer']
def selectRandom(palavra):
  return random.choice(palavra)
a=selectRandom(palavra)

if a==p1:
    b=a.replace('Friends','_ _ _ _ _ _ _')
    x1=b[:1]
    x2=b[2:3]
    x3=b[4:5]
    x4=b[6:7]
    x5=b[8:9]
    x6=b[10:11]
    x7=b[12:]
    print("A palavra é:",b)
    cont=0
    while cont!=6:
        if x1!='_' and x2!='_'and x3!='_' and x4!='_' and x5!='_' and \
        x6!='_' and x7!='_':
            print("Você ganhou!")
            break
        
        letra=input("Digite uma letra:")
        
        if letra=='f' or letra=='F':
            x1='F'
        elif letra=='r' or letra=='R':
            x2='r'
        elif letra=='i' or letra=='I':
            x3='i'
        elif letra=='e' or letra=='E':
            x4='e'
        elif letra=='n' or letra=='N':
            x5='n'
        elif letra=='d' or letra=='D':
            x6='d'
        elif letra=='s' or letra=='S':
            x7='s'
        else:
            cont+=1
            chances=6-cont
            print("Você errou!",end='')
            print(f'Número de chanches restantes=',chances)
        if cont==6:
            print(x1, x2, x3, x4, x5,x6, x7)
            print("Você perdeu!")
            break
        
        print(x1, x2, x3, x4, x5,x6, x7)
elif a==p2:
    b=a.replace('Euphoria','_ _ _ _ _ _ _ _')
    x1=b[:1]
    x2=b[2:3]
    x3=b[4:5]
    x4=b[6:7]
    x5=b[8:9]
    x6=b[10:11]
    x7=b[12:13]
    x8=b[14:]
    print("A palavra é:",b)
    cont=0
    while cont!=6:
        if x1!='_' and x2!='_'and x3!='_' and x4!='_' and x5!='_' and \
        x6!='_' and x7!='_' and x8!='_':
            print("Você ganhou!")
            break
        
        letra=input("Digite uma letra:")
        
        if letra=='e' or letra=='E':
            x1='E'
        elif letra=='u' or letra=='U':
            x2='u'
        elif letra=='p' or letra=='P':
            x3='p'
        elif letra=='h' or letra=='H':
            x4='h'
        elif letra=='o' or letra=='O':
            x5='o'
        elif letra=='r' or letra=='R':
            x6='r'
        elif letra=='i' or letra=='I':
            x7='i'
        elif letra=='a' or letra=='A':
            x8='a'
        else:
            cont+=1
            chances=6-cont
            print("Você errou!",end='')
            print(f'Número de chanches restantes=',chances)
        if cont==6:
            print(x1, x2, x3, x4, x5,x6, x7, x8)
            print("Você perdeu!")
            break
            
        print(x1, x2, x3, x4, x5,x6, x7, x8)
elif a==p3:
    b=a.replace('Cobra Kai','_ _ _ _ _  _ _ _')
    x1=b[:1]
    x2=b[2:3]
    x3=b[4:5]
    x4=b[6:7]
    x5=b[8:9]
    x6=b[11:12]
    x7=b[13:14]
    x8=b[15:]
    print("A palavra é:",b)
    cont=0
    while cont!=6:
        if x1!='_' and x2!='_'and x3!='_' and x4!='_' and x5!='_' and \
        x6!='_' and x7!='_' and x8!='_':
            print("Você ganhou!")
            break
        
        letra=input("Digite uma letra:")
        
        if letra=='c' or letra=='C':
            x1='C'
        elif letra=='o' or letra=='o':
            x2='o'
        elif letra=='b' or letra=='B':
            x3='b'
        elif letra=='r' or letra=='R':
            x4='r'
        elif letra=='a' or letra=='A':
            x5='a'
            x7='a'
        elif letra=='k' or letra=='K':
            x6='K'
        elif letra=='i' or letra=='I':
            x8='i'
        else:
            cont+=1
            chances=6-cont
            print("Você errou!",end='')
            print(f'Número de chanches restantes=',chances)
        if cont==6:
            print(x1, x2, x3, x4, x5,x6, x7, x8)
            print("Você perdeu!")
            break
            
        
        print(x1, x2, x3, x4, x5,x6, x7, x8)
elif a==p4:
    b=a.replace('Black Mirron','_ _ _ _ _  _ _ _ _ _ _')
    x1=b[:1]
    x2=b[2:3]
    x3=b[4:5]
    x4=b[6:7]
    x5=b[8:9]
    x6=b[11:12]
    x7=b[13:14]
    x8=b[15:16]
    x9=b[17:18]
    x10=b[19:20]
    x11=b[21:]
    print("A palavra é:",b)
    cont=0
    while cont!=6:
        
        if x1!='_' and x2!='_'and x3!='_' and x4!='_' and x5!='_' and \
        x6!='_' and x7!='_' and x8!='_' and x9!='_' and x10!='_' and x11!='_':
            print("Você ganhou!")
            break
        
        letra=input("Digite uma letra:")
        
        if letra=='b' or letra=='B':
            x1='B'
        elif letra=='l' or letra=='L':
            x2='l'
        elif letra=='a' or letra=='A':
            x3='a'
        elif letra=='c' or letra=='C':
            x4='c'
        elif letra=='k' or letra=='K':
            x5='k'
        elif letra=='m' or letra=='M':
            x6='M'
        elif letra=='i' or letra=='I':
            x7='i'
        elif letra=='r' or letra=='R':
            x8='r'
            x9='r'
        elif letra=='o' or letra=='O':
            x10='o'
        elif letra=='n' or letra=='N':
            x11='n'
        else:
            cont+=1
            chances=6-cont
            print("Você errou!",end='')
            print(f'Número de chanches restantes=',chances)
        if cont==6:
            print(x1, x2, x3, x4, x5,x6, x7, x8, x9, x10,x11)
            print("Você perdeu!")
            break
            
        print(x1, x2, x3, x4, x5,x6, x7, x8, x9, x10,x11)
elif a==p5:
    b=a.replace('Lucifer','_ _ _ _ _ _ _ ')
    x1=b[:1]
    x2=b[2:3]
    x3=b[4:5]
    x4=b[6:7]
    x5=b[8:9]
    x6=b[10:11]
    x7=b[12:]
    print("A palavra é:",b)
    cont=0
    while cont!=6:
        
        if x1!='_' and x2!='_'and x3!='_' and x4!='_' and x5!='_' and \
        x6!='_' and x7!='_':
            print("Você ganhou!")
        
        letra=input("Digite uma letra:")
        
        if letra=='l' or letra=='L':
            x1='L'
        elif letra=='u' or letra=='U':
            x2='u'
        elif letra=='c' or letra=='C':
            x3='c'
        elif letra=='i' or letra=='I':
            x4='i'
        elif letra=='f' or letra=='F':
            x5='f'
        elif letra=='e' or letra=='E':
            x6='e'
        elif letra=='r' or letra=='R':
            x7='r'
        else:
            cont+=1
            chances=6-cont
            print("Você errou!",end='')
            print(f'Número de chanches restantes=',chances)
        if cont==6:
            print(x1, x2, x3, x4, x5,x6, x7)
            print("Você perdeu!")
            break
        
        print(x1, x2, x3, x4, x5,x6, x7)

