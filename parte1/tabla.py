from time import sleep 
from pynput import keyboard as kb 

dy = 10

def PrintMenu(item, select, title):
    print('\n'* 5)
    l = len(item)
    margin = int((dy - (5 + l)) / 2)
    mt = margin if dy%2 == 0 else (margin +1)
    mb = margin
    
    print('=' * 20, 'Menu', '='*20)
    print('\n'* (mt-1))
    print(f'[  {title}  ]\n')
    for i in range(len(item)):
        print(f'{">" if i == select else " "} {item[i]}')
    
    print('\n'* mb)
    print('=' * 46)
   
def PrintGraph(item, l=1):
    print('\n'* 5)
    margin = int((dy - (3 + l)) / 2)
    mt = margin if dy%2 == 0 else (margin +1)
    mb = margin
    print('=' * 20, 'Menu', '='*20)
    print('\n'* (mt-1))

    print(item)

    print('\n'* mb)
    print('=' * 46)
    
def PrintTable(title, item, encabezado, num):
    print('\n'* 5)
    l = len(item)
    margin = int((dy - (8 + l)) / 2)
    mt = margin if dy%2 == 0 else (margin +1)
    mb = margin
    print('=' * 20, 'Menu', '='*20)
    print('\n'* (mt-1))
    print(f'[  {title}  ]\n')
    
    print(f'{(" " if num else "")}  ', end='')
    for i in encabezado:
        print(f'{i:10}', end='')
    print('\n')
    for y in range(len(item)):
        for x in range(len(item[y])): 
            print(f'{((y+1)if num else "")if x ==0 else ""}  {item[y][x]:7}', end='')
        print('',end='\n')
    print('\n'* mb)
    print('=' * 46)
        
    # config rondas
def Menu():
    pos = 0
    level = [
        [
            'Menu',
            ['Graph', 0, 2],
            ['Table', 0, 1, ['stats', [['nul', 100],['nul', 100],['nul', 100],['nul', 10],['nul', 50]], ['name ', 'socore '], True]],
            # ['config', 2],
            ['exit', -1]
        ],
        [
            'CONFIG',
            ['rondas [20]', 2, 20],
            ['tiempo [5]', 2, 5],
            ['atras', 1]
        ],
        [
            'PLAYER',
            ['name player', 2],
            ['atras', 2]
        ],
        [
            'STATS',
            ['stats', 2],
            ['atras', 1]
        ]
    ]
    m = 1 # 1: menu principal, 2: blablabla
    fn = [0, 0]
    while True:
        if m == -1:
            break
        elif m == 0:
            if level[fn[0]-1][fn[1]+1][2] == 1:
                t, it, l, e = [a for a in level[fn[0]-1][fn[1]+1][3]] 
                PrintTable(t,it,l,e)
                while True:
                    sleep(0.5)
                    btn = detectButtons()
                    if True in btn:
                        fn = [0, 0]
                        m = 1 
                        pos = 0
                        break
            elif level[fn[0]-1][fn[1]+1][2] == 2:
                PrintMenu(['Cantidad de jugadores','',''], 0, 'GAME')
                cj = int(input('Cantidad de jugadores :'))
                player = [f"player {o+1}" for o in range(cj)]
                for i in range(cj):
                    PrintMenu([f'{player[l]}' for l in range(cj)], i, 'GAME')
                    player[i] = input(f'name player {i+1} :')
                for play in player:
                    PrintMenu(['star','',''], 0, f'Es el turno de {play}')
                    while True:
                        btn = detectButtons()
                        if True in btn:
                            PrintGraph('\t_____\n\t|___ /\n\t  |_ \ \n\t ___) |\n\t|____/\n', 6)
                            sleep(1)
                            PrintGraph('\t ___ \n\t|___ \ \n\t  __) |\n\t / __/\n\t|_____|', 5)
                            sleep(1)
                            PrintGraph('\t   _\n\t  / |\n\t  | |\n\t  | |\n\t  |_|', 5)
                            sleep(1)
                            PrintGraph('      __ _    ___\n     / _` |  / _ \ \n    | (_| | | (_) |\n     \__, |  \___/\n     |___/', 5)
                            sleep(1)
                            break
                    for ronda in range(level[1][1][2]):
                        PrintMenu([f'Ronda {ronda +1} ','',''], 0, f'Es el turno de {play}')
                        while True:
                            btn = detectButtons()
                            if True in btn:
                                break
                m=1
                pos=0
        else: 
            PrintMenu([t[0] for t in level[m-1]][1:], pos, level[m-1][0])
        
            while True:
                sleep(0.5)
                btn = detectButtons()
                if btn[0]:
                    pos = (len(level[m-1])-2) if pos == 0 else pos -1
                    break
                elif btn[1]:
                    pos = 0 if pos == (len(level[m-1])-2) else pos +1
                    break
                elif btn[4]:
                    if level[m-1][pos+1][1] != m:
                      fn = [m,pos]
                      m = level[m-1][pos+1][1] 
                      pos = 0
                      break
                    else:
                      change = int(input(f'{level[m-1][pos+1][0]} :'))
                      level[m-1][pos+1][0] = f"{level[m-1][pos+1][0].split(' ')[0]} [{change}]"
                      level[m-1][pos+1][2] = change
                      break
        # rondas, etc
    return 'test'
#PrintTable('test', [['nul', 100],['nul', 10],['nul', 50]], ['name ', 'socore '], True)