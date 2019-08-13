#-------------------------SUDOKU---------------------#

#casas do tabuleiro, com algumas casas ja preenchidas#
casa=[[0,6,0,8,0,0,0,0,3],
     [7,8,9,0,1,0,0,0,6],
     [0,0,0,0,0,6,1,0,0],
     [0,0,7,0,0,0,0,5,0],
     [5,0,8,0,0,9,3,0,4],
     [0,4,0,0,0,0,2,0,0],
     [0,0,3,2,0,0,6,8,0],
     [8,0,0,0,7,0,4,3,9],
     [0,0,0,0,0,1,0,0,0]]

#lista das casas com a respostas para poder parar o loop#
ans=[[1,6,5,8,4,7,9,2,3],
    [7,8,9,3,1,2,5,4,6],
    [4,3,2,5,9,6,1,7,8],
    [2,9,7,4,6,3,8,5,1],
    [5,1,8,7,2,9,3,6,4],
    [3,4,6,1,5,8,2,9,7],
    [9,7,3,2,8,4,6,1,5],
    [8,2,1,6,7,5,4,3,9],
    [6,5,4,9,3,1,7,8,2]]

#variável p para as posicoes que seria um atalho para os indices das casas#
p={'1-1':(0,0),'1-2':(0,1),'1-3':(0,2),'1-4':(0,3),'1-5':(0,4),'1-6':(0,5),'1-7':(0,6),'1-8':(0,7),'1-9':(0,8),
   '2-1':(1,0),'2-2':(1,1),'2-3':(1,2),'2-4':(1,3),'2-5':(1,4),'2-6':(1,5),'2-7':(1,6),'2-8':(1,7),'2-9':(1,8),
   '3-1':(2,0),'3-2':(2,1),'3-3':(2,2),'3-4':(2,3),'3-5':(2,4),'3-6':(2,5),'3-7':(2,6),'3-8':(2,7),'3-9':(2,8),
   '4-1':(3,0),'4-2':(3,1),'4-3':(3,2),'4-4':(3,3),'4-5':(3,4),'4-6':(3,5),'4-7':(3,6),'4-8':(3,7),'4-9':(3,8),
   '5-1':(4,0),'5-2':(4,1),'5-3':(4,2),'5-4':(4,3),'5-5':(4,4),'5-6':(4,5),'5-7':(4,6),'5-8':(4,7),'5-9':(4,8),
   '6-1':(5,0),'6-2':(5,1),'6-3':(5,2),'6-4':(5,3),'6-5':(5,4),'6-6':(5,5),'6-7':(5,6),'6-8':(5,7),'6-9':(5,8),
   '7-1':(6,0),'7-2':(6,1),'7-3':(6,2),'7-4':(6,3),'7-5':(6,4),'7-6':(6,5),'7-7':(6,6),'7-8':(6,7),'7-9':(6,8),
   '8-1':(7,0),'8-2':(8,1),'8-3':(7,2),'8-4':(7,3),'8-5':(7,4),'8-6':(7,5),'8-7':(7,6),'8-8':(7,7),'8-9':(7,8),
   '9-1':(8,0),'9-2':(8,1),'9-3':(8,2),'9-4':(8,3),'9-5':(8,4),'9-6':(8,5),'9-7':(8,6),'9-8':(8,7),'9-9':(8,8)}

#dicionario para funcao de verificar se a casa ta disponivel para preencher#
cd={'1-1':(True),'1-2':('False'),'1-3':(True),'1-4':('False'),'1-5':(True),'1-6':(True),'1-7':(True),'1-8':(True),'1-9':('False'),
   '2-1':('False'),'2-2':('False'),'2-3':('False'),'2-4':(True),'2-5':('False'),'2-6':(True),'2-7':(True),'2-8':(True),'2-9':('False'),
   '3-1':(True),'3-2':(True),'3-3':(True),'3-4':(True),'3-5':(True),'3-6':('False'),'3-7':('False'),'3-8':(True),'3-9':(True),
   '4-1':(True),'4-2':(True),'4-3':('False'),'4-4':(True),'4-5':(True),'4-6':(True),'4-7':(True),'4-8':('False'),'4-9':(True),
   '5-1':('False'),'5-2':(True),'5-3':('False'),'5-4':(True),'5-5':(True),'5-6':('False'),'5-7':('False'),'5-8':(True),'5-9':('False'),
   '6-1':(True),'6-2':('False'),'6-3':(True),'6-4':(True),'6-5':(True),'6-6':(True),'6-7':('False'),'6-8':(True),'6-9':(True),
   '7-1':(True),'7-2':(True),'7-3':('False'),'7-4':('False'),'7-5':(True),'7-6':(True),'7-7':('False'),'7-8':('False'),'7-9':(True),
   '8-1':('False'),'8-2':(True),'8-3':(True),'8-4':(True),'8-5':('False'),'8-6':(True),'8-7':('False'),'8-8':('False'),'8-9':('False'),
   '9-1':(True),'9-2':(True),'9-3':(True),'9-4':(True),'9-5':(True),'9-6':('False'),'9-7':(True),'9-8':(True),'9-9':(True)}

#função casa disponivel--------------------------------#
def cad(a):
     g=cd[a]
     if g==('False'):
          return False
     else:
          return True

#função preenche casa----------------------------------#
def pc(a,b):
     pos=p[a]
     l=pos[0]
     c=pos[1]
     casa[l][c]=b

#função para imprimir o tabuleiro----------------------#
def table():
     print('  ║ 1 2 3 ║ 4 5 6 ║ 7 8 9 ║')
     print(' ═║═══════║═══════║═══════║═')
     print('1','║',casa[0][0] if casa[0][0]!=0 else ' ',casa[0][1],casa[0][2]if casa[0][2]!=0 else ' ','║',casa[0][3],casa[0][4]if casa[0][4]!=0 else ' ',casa[0][5]if casa[0][5]!=0 else ' ','║',casa[0][6]if casa[0][6]!=0 else ' ',casa[0][7]if casa[0][7]!=0 else ' ',casa[0][8],'║')
     print('2','║',casa[1][0],casa[1][1],casa[1][2],'║',casa[1][3]if casa[1][3]!=0 else ' ',casa[1][4],casa[1][5]if casa[1][5]!=0 else ' ','║',casa[1][6]if casa[1][6]!=0 else ' ',casa[1][7]if casa[1][7]!=0 else ' ',casa[1][8],'║')
     print('3','║',casa[2][0]if casa[2][0]!=0 else ' ',casa[2][1]if casa[2][1]!=0 else ' ',casa[2][2]if casa[2][2]!=0 else ' ','║',casa[2][3]if casa[2][3]!=0 else ' ',casa[2][4]if casa[2][4]!=0 else ' ',casa[2][5],'║',casa[2][6],casa[2][7]if casa[2][7]!=0 else ' ',casa[2][8]if casa[2][8]!=0 else ' ','║')  
     print(" ═║═══════║═══════║═══════║═")
     print('4','║',casa[3][0]if casa[3][0]!=0 else ' ',casa[3][1]if casa[3][0]!=0 else ' ',casa[3][2],'║',casa[3][3]if casa[3][3]!=0 else ' ',casa[3][4]if casa[3][4]!=0 else ' ',casa[3][5]if casa[3][4]!=0 else ' ','║',casa[3][6]if casa[3][6]!=0 else ' ',casa[3][7],casa[3][8]if casa[3][8]!=0 else ' ','║')
     print('5','║',casa[4][0],casa[4][1]if casa[4][1]!=0 else ' ',casa[4][2],'║',casa[4][3]if casa[4][3]!=0 else ' ',casa[4][4]if casa[4][4]!=0 else ' ',casa[4][5],'║',casa[4][6],casa[4][7]if casa[4][7]!=0 else ' ',casa[4][8],'║')
     print('6','║',casa[5][0]if casa[5][0]!=0 else ' ',casa[5][1],casa[5][2]if casa[5][2]!=0 else ' ','║',casa[5][3]if casa[5][3]!=0 else ' ',casa[5][4]if casa[5][4]!=0 else ' ',casa[5][5]if casa[5][5]!=0 else ' ','║',casa[5][6],casa[5][7]if casa[5][7]!=0 else ' ',casa[5][8]if casa[5][8]!=0 else ' ','║')
     print(" ═║═══════║═══════║═══════║═")
     print('7','║',casa[6][0]if casa[6][0]!=0 else ' ',casa[6][1]if casa[6][1]!=0 else ' ',casa[6][2],'║',casa[6][3],casa[6][4]if casa[6][4]!=0 else ' ',casa[6][5]if casa[6][5]!=0 else ' ','║',casa[6][6],casa[6][7],casa[6][8]if casa[6][8]!=0 else ' ','║')
     print('8','║',casa[7][0],casa[7][1]if casa[7][1]!=0 else ' ',casa[7][2]if casa[7][2]!=0 else ' ','║',casa[7][3]if casa[7][3]!=0 else ' ',casa[7][4],casa[7][5]if casa[7][5]!=0 else ' ','║',casa[7][6],casa[7][7],casa[7][8],'║')
     print('9','║',casa[8][0]if casa[8][0]!=0 else ' ',casa[8][1]if casa[8][1]!=0 else ' ',casa[8][2]if casa[8][2]!=0 else ' ','║',casa[8][3]if casa[8][3]!=0 else ' ',casa[8][4]if casa[8][4]!=0 else ' ',casa[8][5],'║',casa[8][6]if casa[8][6]!=0 else ' ',casa[8][7]if casa[8][7]!=0 else ' ',casa[8][8]if casa[8][8]!=0 else ' ','║')
     print(' ═║═══════║═══════║═══════║═')

#função menu-------------------------------------------#
def menu():
     game=input('P for play or Q for quit: ')
     if game==('P'):
          return False
     else:
          return True
          

#print da parte bonitinha------------------------------#
print('═════════S═U═D═O═K═U═════════')
print('')
while menu()==False:
     print('')
     table()

#loop do jogo------------------------------------------#
     while (casa) != (ans):
         print (' ')
         a=input('pos: ')
         b=int(input('num: '))
         print ('')
         while cad(a)==False:
              a=input('tente outra casa, essa nao pode: ')
         pc(a,b)
         table()
     if (casa)==(ans):
          print (' ')
          print ('▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽')
          print ('        U       W I N ')
          print ('△△△△△△△△△△△△△△△△')
          print ('')
          menu()
          casa=[[0,1,0,8,0,0,0,0,3],
                [7,8,9,0,1,0,0,0,6],
                [0,0,0,0,0,6,1,0,0],
                [0,0,7,0,0,0,0,5,0],
                [5,0,8,0,0,9,3,0,4],
                [0,4,0,0,0,0,2,0,0],
                [0,0,3,2,0,0,6,8,0],
                [8,0,0,0,7,0,4,3,9],
                [0,0,0,0,0,1,0,0,0]]

print ('')
print ('bye :(')
