import pygame,pgzrun,os,time,shutil,win32api,win32con,random

class ProgramData:
    name = 'Rysim'
    version = '0.0.4_alpha_241005'#version = '0.0.4_alpha_240930'
    author = 'MC-BA---bee'
    author_email = 'mc571526@163.com / lizixuan815@gmail.com'
    website = 'https://github.com/MC-BA-Bee/Rysim'
    description = 'Rysim is a music game based on pygame.'#程序数据
TITLE=ProgramData.name+' v'+ProgramData.version#标题
#pygame.event.set_grab(True)
ICON='icon.png'#图标
# 加载图标文件并创建Surface对象
icon = pygame.image.load(os.getcwd()+"/icon.png").convert_alpha()
# 设置窗口的新图标
pygame.display.set_icon(icon)
WIDTH = 1280#宽度
HEIGHT = 720#高度
os.environ ['SDL_VIDEO_CENTERED'] ='1'#窗口居中
def switch_to_english():
    # 切换到英文输入法
    win32api.LoadKeyboardLayout('00000409', 1)
    # 发送 Ctrl + Shift 组合键，确保输入法已经切换到英文
    win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)
    win32api.keybd_event(win32con.VK_SHIFT, 0, 0, 0)
    win32api.keybd_event(win32con.VK_SHIFT, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)
# 调用函数将输入法切换到英文
switch_to_english()
def PlayMusic(file):
    pygame.mixer.music.load(file)
    #pygame.mixer.music.fadein()
    pygame.mixer.music.play(-1)
def SoundsPlay(file):
    pygame.mixer.Sound(file).play()
def CheckRank(scores):
        scores=int(scores)
        if scores>=1000000:
            rank='Φ'
        elif 999999>=scores>=940000:
            rank='V'
        elif 959999>=scores>=920000:
            rank='S'
        elif 919999>=scores>=880000:
            rank='A'
        elif 879999>=scores>=820000:
            rank='B'
        elif 819999>=scores>=700000:
            rank='C'
        else:
            rank='F'
        return rank
class read_f():
    def saves():
        ######print('saves')
        paths = os.walk(os.getcwd()+'//files//saves')
        for path, dir_lst, file_lst in paths:
            for file_name in file_lst:
                ########print(os.path.join(path, file_name))
                ui.select.SavesList.append(os.path.join(file_name))
        #filePath
        ######print(ui.select.SavesList)
        ui.ScoresSaves=[]
        for i in range(len(ui.select.SavesList)):
            f=open(os.getcwd()+'/files/saves/'+str(ui.select.SavesList[i]),'r',encoding='utf-8')
            a=list(f.read())
            strs=''
            strlist=[]
            for i in range(len(a)):
                if a[i]=='#':
                    strlist.append(int(strs))
                    strs=''
                else:
                    strs+=a[i]
            ui.ScoresSaves.append(strlist)
            f.close()
    def pm():
        global pms
        pms=[]
        for i in range(4):
            if read_f.gameread()!='None':
                pms.append(read_f.MusicGame(read_f.gameread(),i))#读取谱面信息
    def pospone():
        f=open(os.getcwd()+'/pospone.txt','r',encoding='utf-8')
        a=f.read()
        f.close()
        ####print(int(a))
        return int(a)
    def gameread():#读取播放歌曲信息
        file=open(os.getcwd()+'//files//playing.txt',encoding='utf-8')
        return file.read()
    def MusicGame(name,i):#读取游戏谱面
        global adress
        adress=os.getcwd()+'//files//resourse//'+name
        data=[];o=0
        with open(adress+'//L'+str(i)+'.txt', encoding='utf-8') as f:
            data=f.readlines()
        for i in data:
            data[o]=i.strip('\n')
            o+=1
        output=[]
        if data==['']:
            return 'None'
        for i in range(2):
            lists=list(str(data[i]))
            txt='';output1=[]
            for i in range(len(lists)):
                if lists[i]!=',':
                    txt+=lists[i]
                else:
                    output1.append(int(txt))
                    txt=''
            output.append(output1)
        return output
class act():
    Logo=Actor(os.getcwd()+'/images/logo.png')
    bg=Actor(os.getcwd()+'/images/author.png')
    k=[]
    kwantx=[]
    kwanty=[]
    for i in range(10):#添加10个过场动画素材角色
        k.append(Actor(os.getcwd()+'/images/k1.png',[-1280,-1280]))
        kwantx.append(0)
        kwanty.append(0)
    bt=[]
    #选择界面的列表按钮
    posbts=0
    bts=[]
    btswanty=[]
    #################
    btpos=[]
    for i in range(10):
        bt.append(Actor(os.getcwd()+'/images/bt1.png'))
    class select:
        PerfectLine=Actor(os.getcwd()+'/images/gold1l.png')
        GoodLine=Actor(os.getcwd()+'/images/blue1l.png')
        BadLine=Actor(os.getcwd()+'/images/red1l.png')
        MissLine=Actor(os.getcwd()+'/images/black1l.png')
    class settings:
        experiment=Actor(os.getcwd()+'/images/skipbtf.png')
        autoplay=Actor(os.getcwd()+'/images/skipbtf.png')
    class game:
        good=[]
        perfect=[]
        ProgressLine=Actor(os.getcwd()+'/images/white1.png',[WIDTH-5,0])
        pauseui=Actor(os.getcwd()+'/images/pauseui.png')
        bmouse=Actor(os.getcwd()+'/images/bmouse.png')
        b=[]
        for i in range(4):#判定线
            b.append(Actor(os.getcwd()+'/images/b'+str(i+1)+'.png',[250,200+i*120]))
            b[i].x=300
        mb=Actor(os.getcwd()+'/images/mb.png')
        keys=[[],[],[],[]]
        goodimage=[[],[],[],[]]
        perfectimage=[[],[],[],[]]
class ui:
    ui='start'
    settings=False
    times=0
    lst=time.strftime('%S')
    ScoresSaves=[]
    PerfectSaves=[]
    GoodSaves=[]
    BadSaves=[]
    class select:
        SoundsList=[]
        SavesList=[]
    class score:
        score=0#总分
        TapScore=0#点击得分
        ComboScore=0#连击得分
        MaxCombo=0#最大连击数
        Count=0#物量
    class game:
        read_f.pm()
        speed=1
        speedwant=speed
        pospone=0
        progress=0
        length=0
        keys=[]
        perfect=0
        good=0
        bad=0
        miss=0
        combo=0
        keydownState=[False,False,False,False]
        def check(road,keys,types):
            global pms
            pm=pms[road]
            if keys>=len(pm[0]):
                return
            perfect=[-80*ui.game.speed,100*ui.game.speed]
            good=[-150*ui.game.speed,250*ui.game.speed]
            bad=[250*ui.game.speed,350*ui.game.speed]
            x=act.game.keys[road][keys].x
            if act.game.keys[road][keys].y<0:
                return
            if act.game.keys[road][keys].image=='tap'+str(int(road)+1)+'.png' and types==0:
                if act.game.b[road].x+perfect[0]<x<act.game.b[road].x+perfect[1]:
                    ui.score.TapScore+=(1/ui.score.Count)*1*900000
                    #print(act.game.keys[road][keys].image,'tap'+str(road)+'.png')
                    SoundsPlay(os.getcwd()+'\\sounds\\click.ogg')
                    ui.game.perfect+=1
                    ui.game.keys[road]+=1
                    act.game.perfect[road][keys].x=act.game.b[road].x
                    act.game.perfect[road][keys].y=act.game.b[road].y
                    act.game.perfectimage[road][keys]=1
                    act.game.keys[road][keys].y=-90000
                    ui.game.combo+=1  
                elif act.game.b[road].x+good[0]<x<act.game.b[road].x+good[1]:
                    ui.score.TapScore+=(1/ui.score.Count)*0.65*900000
                    SoundsPlay(os.getcwd()+'\\sounds\\click.ogg')
                    ui.game.good+=1
                    ui.game.keys[road]+=1
                    act.game.good[road][keys].x=act.game.b[road].x
                    act.game.good[road][keys].y=act.game.b[road].y
                    act.game.goodimage[road][keys]=1
                    act.game.keys[road][keys].y=-90000
                    ui.game.combo+=1
                elif act.game.b[road].x+bad[0]<x<act.game.b[road].x+bad[1]:
                    ui.game.bad+=1
                    ui.game.keys[road]+=1
                    act.game.keys[road][keys].image='key1miss.png'
                    ui.game.combo=0
            elif act.game.keys[road][keys].image=='drag'+str(int(road)+1)+'.png':
                print(road,30303022)
                if act.game.b[road].x-15<x<act.game.b[road].x+15:
                    SoundsPlay(os.getcwd()+'\\sounds\\drag.ogg')
                    ui.score.TapScore+=(1/ui.score.Count)*1*900000
                    #print(act.game.keys[road][keys].image,'tap'+str(road)+'.png')
                    #SoundsPlay(os.getcwd()+'\sounds\click.ogg')
                    ui.game.perfect+=1
                    ui.game.keys[road]+=1
                    act.game.perfect[road][keys].x=act.game.b[road].x
                    act.game.perfect[road][keys].y=act.game.b[road].y                    
                    act.game.perfectimage[road][keys]=1
                    act.game.keys[road][keys].y=-90000
                    ui.game.combo+=1  
            if ui.game.combo>=ui.score.MaxCombo:
                ui.score.MaxCombo=ui.game.combo
                ui.score.ComboScore=ui.score.MaxCombo/ui.score.Count*100000
            ui.score.score=ui.score.TapScore+ui.score.ComboScore
            if int(ui.score.score)==999999:
                ui.score.score=1000000
        def autocheck(road,keys):
            global pms
            pm=pms[road]
            if keys>=len(pm[0]):
                return
            perfect=[-80,100]
            good=[-150,250]
            bad=[250,350]
            x=act.game.keys[road][keys].x
            ui.score.TapScore+=(1/ui.score.Count)*1*900000
            if act.game.keys[road][keys].image=='tap'+str(int(road)+1)+'.png':
                SoundsPlay(os.getcwd()+'\\sounds\\click.ogg')
            elif act.game.keys[road][keys].image=='drag'+str(int(road)+1)+'.png':
                SoundsPlay(os.getcwd()+'\\sounds\\drag.ogg')
            ui.game.perfect+=1
            ui.game.keys[road]+=1
            act.game.perfect[road][keys].x=act.game.b[road].x
            act.game.perfect[road][keys].y=act.game.b[road].y
            act.game.perfectimage[road][keys]=1
            act.game.keys[road][keys].y=-90000
            ui.game.combo+=1
            if ui.game.combo>=ui.score.MaxCombo:
                ui.score.MaxCombo=ui.game.combo
                ui.score.ComboScore=ui.score.MaxCombo/ui.score.Count*100000
            ui.score.score=ui.score.TapScore+ui.score.ComboScore
            if int(ui.score.score)==999999:
                ui.score.score=1000000
        pause=False
        pos=0
        musictime=0
        postime=0
        MusicName=read_f.gameread()
class settings:
    autoplay=False
    experiment=False
def draw():
    screen.clear()
    if ui.ui=='settings':
        act.bg.image='settings.png'
        act.bg.draw()
        for i in range(10):
            act.k[i].image='k1.png'
            act.k[i].draw()
        act.bt[1].x=act.k[4].x+480
        act.bt[1].y=60
        act.bt[1].image='bt2.png'
        act.bt[1].draw()
        act.settings.autoplay.pos=[act.bt[1].x+550,act.bt[1].y+120]
        act.settings.autoplay.draw()
        act.settings.experiment.pos=[act.bt[1].x+550,act.bt[1].y+240]
        act.settings.experiment.draw()
        screen.draw.text('返回',center=[act.bt[1].x+190,act.bt[1].y],fontname='siyuanblod1',fontsize=30,color='white', shadow=(1.0,1.0),scolor=(105,105,105),owidth=0.5,ocolor=(105,105,105))
        screen.draw.text('奥托普雷先生',topleft=[act.settings.autoplay.x-300,act.settings.autoplay.y-25],fontname='siyuanblod1',fontsize=40,color='white', shadow=(1.0,1.0),scolor=(105,105,105),owidth=0.5,ocolor=(105,105,105))
        screen.draw.text('实验性玩法',topleft=[act.settings.experiment.x-300,act.settings.experiment.y-25],fontname='siyuanblod1',fontsize=40,color='white', shadow=(1.0,1.0),scolor=(105,105,105),owidth=0.5,ocolor=(105,105,105))
    elif ui.ui=='start':
        screen.fill((0,0,0))
        act.bg.image='author.png'
        act.bg.draw()
        for i in range(4):
            act.k[i].image='k1.png'
            act.k[i].draw()
        for i in range(4):
            act.bt[i].x=act.k[3].x-80-43*i
            act.bt[i].y=600+100*i
            act.bt[i].draw()
    elif ui.ui=='main':
        act.bg.image='main.png'
        act.bg.draw()
        for i in range(4):
            act.k[i].image='k1.png'
            act.k[i].draw()
        for i in range(4):
            act.bt[i].x=act.k[3].x-100-43*i
            act.bt[i].y=350+100*i
            act.bt[i].image='bt1.png'
            act.bt[i].draw()
        screen.draw.text('快速开始:  '+ui.game.MusicName,topleft=[act.bt[0].x-180,act.bt[0].y-20],fontname='siyuanblod1',fontsize=35)
        screen.draw.text('进入游戏',topleft=[act.bt[1].x-180,act.bt[1].y-20],fontname='siyuanblod1',fontsize=35)
        screen.draw.text('设置',topleft=[act.bt[2].x-180,act.bt[2].y-20],fontname='siyuanblod1',fontsize=35)
        screen.draw.text('退出游戏',topleft=[act.bt[3].x-180,act.bt[3].y-20],fontname='siyuanblod1',fontsize=35)
        #screen.draw.text('Rysim',center=[act.k[3].x-900,170],fontname='siyuanblod1',fontsize=200,shadow=(0.5,0.5), scolor=(105,105,105),owidth=0.5,ocolor=(105,105,105))
        act.Logo.x=act.k[3].x-950
        act.Logo.y=170
        act.Logo.draw()
    elif ui.ui=='select':
        act.bg.draw()
        for i in range(10):
            act.k[i].image='k1.png'
            act.k[i].draw()
        if ui.game.MusicName+'.txt' in ui.select.SavesList:
            scores=ui.ScoresSaves[ui.select.SavesList.index(ui.game.MusicName+'.txt')][0]
        else:
            scores=0
        rank=CheckRank(scores)
        scores=str(scores)
        for i in range(7-len(list(str(scores)))):
            scores='0'+scores
        screen.draw.text(str(scores),topleft=[30,85],fontname='siyuanblod1',fontsize=180,color='white',shadow=(0.5,0.5), scolor=(105,105,105),owidth=0.5,ocolor=(105,105,105))
        act.k[0].draw()
        act.k[9].draw()
        screen.draw.text(rank,topleft=[act.k[9].x+300,300],fontname='siyuanblod1',fontsize=300,shadow=(0.5,0.5), scolor=(105,105,105),owidth=0.5,ocolor=(105,105,105))
        screen.draw.text('RANK',topleft=[act.k[9].x+280,600],fontname='siyuanblod1',fontsize=100,shadow=(1.0,1.0), scolor=(105,105,105),owidth=0.5,ocolor=(105,105,105))
        for i in range(len(ui.select.SoundsList)):
            act.bts[i].x=int((act.bts[i].y-1739)/-2.31)+400+act.btpos[i]-50
            act.btswanty[i]=(150+100*i)+act.posbts
            act.bts[i].image='bt1.png'
            act.bts[i].draw()
            if ui.select.SoundsList[i]+'.txt' in ui.select.SavesList:
                new=''
            else:
                new='      new!'
            screen.draw.text(ui.select.SoundsList[i]+new,topleft=[act.bts[i].x-225,act.bts[i].y-20],fontname='siyuan1',fontsize=30,color='white',shadow=(1.0,1.0), scolor=(105,105,105),owidth=0.5,ocolor=(105,105,105))
        act.bt[0].x=act.k[2].x+320-43*0
        act.bt[0].y=650+100*0
        act.bt[0].draw()
        act.bt[2].x=act.k[2].x+320-43*-1
        act.bt[2].y=650+100*0-100
        act.bt[2].draw()
        act.bt[1].x=act.k[4].x+480
        act.bt[1].y=60
        act.bt[1].image='bt2.png'
        act.bt[1].draw()
        screen.draw.text('返回',center=[act.bt[1].x+190,act.bt[1].y],fontname='siyuanblod1',fontsize=30,color='white', shadow=(1.0,1.0),scolor=(105,105,105),owidth=0.5,ocolor=(105,105,105))
        screen.draw.text('随机',center=[act.bt[2].x-180,act.bt[2].y],fontname='siyuanblod1',fontsize=30,color='white', shadow=(1.0,1.0),scolor=(105,105,105),owidth=0.5,ocolor=(105,105,105))
        screen.draw.text('开始',center=[act.bt[0].x-180,act.bt[0].y],fontname='siyuanblod1',fontsize=30,color='white', shadow=(1.0,1.0),scolor=(105,105,105),owidth=0.5,ocolor=(105,105,105))
        if ui.game.MusicName+'.txt' in ui.select.SavesList:
            act.select.PerfectLine.draw()
            act.select.GoodLine.draw()
            act.select.BadLine.draw()
            act.select.MissLine.draw()
            allcombo=int(ui.ScoresSaves[ui.select.SavesList.index(ui.game.MusicName+'.txt')][2])+int(ui.ScoresSaves[ui.select.SavesList.index(ui.game.MusicName+'.txt')][3])+int(ui.ScoresSaves[ui.select.SavesList.index(ui.game.MusicName+'.txt')][4])+int(ui.ScoresSaves[ui.select.SavesList.index(ui.game.MusicName+'.txt')][5])
            PerfectPer=int(ui.ScoresSaves[ui.select.SavesList.index(ui.game.MusicName+'.txt')][2])/allcombo
            GoodPer=int(ui.ScoresSaves[ui.select.SavesList.index(ui.game.MusicName+'.txt')][3])/allcombo
            BadPer=int(ui.ScoresSaves[ui.select.SavesList.index(ui.game.MusicName+'.txt')][4])/allcombo
            MissPer=int(ui.ScoresSaves[ui.select.SavesList.index(ui.game.MusicName+'.txt')][5])/allcombo
            act.select.MissLine.y=HEIGHT*(MissPer)+HEIGHT/2-HEIGHT
            act.select.BadLine.y=HEIGHT*(BadPer+MissPer)+HEIGHT/2-HEIGHT
            act.select.GoodLine.y=HEIGHT*(BadPer+MissPer+GoodPer)+HEIGHT/2-HEIGHT
            act.select.PerfectLine.y=HEIGHT*(BadPer+MissPer+GoodPer+PerfectPer)+HEIGHT/2-HEIGHT
            screen.draw.text('perfect:'+str(ui.ScoresSaves[ui.select.SavesList.index(ui.game.MusicName+'.txt')][2]),topleft=[440, 298],fontname='siyuanblod1',fontsize=30,color='gold',shadow=(0.5,0.5), scolor=(105,105,105),owidth=0.5,ocolor=(105,105,105))
            screen.draw.text('good:'+str(ui.ScoresSaves[ui.select.SavesList.index(ui.game.MusicName+'.txt')][3]),topleft=[420, 338],fontname='siyuanblod1',fontsize=30,color=(0,162,232),shadow=(0.5,0.5), scolor=(105,105,105),owidth=0.5,ocolor=(105,105,105))
            screen.draw.text('bad:'+str(ui.ScoresSaves[ui.select.SavesList.index(ui.game.MusicName+'.txt')][4]),topleft=[400, 378],fontname='siyuanblod1',fontsize=30,color=(179,0,27),shadow=(0.5,0.5), scolor=(105,105,105),owidth=0.5,ocolor=(105,105,105))
            screen.draw.text('miss:'+str(ui.ScoresSaves[ui.select.SavesList.index(ui.game.MusicName+'.txt')][5]),topleft=[380, 418],fontname='siyuanblod1',fontsize=30,color='gray',shadow=(0.5,0.5), scolor=(105,105,105),owidth=0.5,ocolor=(105,105,105))
    elif ui.ui=='game':
        act.bg.draw()
        act.game.mb.draw()
        scores=''
        for i in range(7-len(list(str(int(ui.score.score))))):
            scores='0'+scores
        scores+=str(int(ui.score.score))
        if ui.game.combo>=3:
            screen.draw.text(str(ui.game.combo),center=[WIDTH/2-20,40],fontname='siyuan1',fontsize=70)
            if settings.autoplay:
                    screen.draw.text('AUTOPLAY',center=[WIDTH/2-20,45+40],fontname='siyuan1',fontsize=25)
            elif ui.game.bad==0 and ui.game.miss==0:
                if ui.game.good==0:
                    screen.draw.text('All Perfect',center=[WIDTH/2-20,45+40],fontname='siyuan1',fontsize=25)
                else:
                    screen.draw.text('Full Combo',center=[WIDTH/2-20,45+40],fontname='siyuan1',fontsize=25)
            else:
                screen.draw.text('Combo',center=[WIDTH/2-20,45+40],fontname='siyuan1',fontsize=25)
        for i in range(4):
            act.game.b[i].draw()
            for f in range(len(act.game.keys[i])):
                if -100<act.game.keys[i][f].x<1400:
                    act.game.keys[i][f].draw()
                if act.game.b[i].x-400<act.game.keys[i][f].x<act.game.b[i].x+400:
                    act.game.good[i][f].draw()
                    act.game.perfect[i][f].draw()
                #screen.draw.text(str(f),center=[act.game.keys[i][f].x,act.game.keys[i][f].y-100],fontsize=70)
        act.game.bmouse.draw()
        act.game.ProgressLine.draw()
        screen.draw.text(ui.game.MusicName,topleft=[15,HEIGHT-35],fontname='siyuan1',fontsize=25)
        screen.draw.text(scores,topleft=[10,10],fontname='siyuan1',fontsize=30)
        for i in range(4):
            act.k[i].image='k1.png'
            act.k[i].draw()
        if ui.game.pause:
            act.game.pauseui.draw()
    elif ui.ui=='end':
        filePath = os.getcwd()+'//files//resourse'
        for i,j,k in os.walk(filePath):
            SoundsList=j
            break
        ui.select.SoundsList=SoundsList
        act.bg.image='s'+str(ui.select.SoundsList.index(ui.game.MusicName))+'.png'
        act.bg.draw()
        for i in range(10):
            act.k[i].image='k1.png'
            act.k[i].draw()
        act.bt[0].x=act.k[3].x+100-43*0
        act.bt[0].y=650+100*0
        act.bt[0].draw()
        act.bt[1].x=act.k[9].x-80
        act.bt[1].y=60
        act.bt[1].image='bt2.png'
        act.bt[1].draw()
        screen.draw.text('重玩',center=[act.bt[1].x+180,act.bt[1].y],fontname='siyuanblod1',fontsize=30,color='white')
        screen.draw.text('继续',center=[act.bt[0].x-150,act.bt[0].y],fontname='siyuanblod1',fontsize=30,color='white')
        screen.draw.text('最终成绩',topleft=[act.k[0].x-50,60],fontname='siyuanblod1',fontsize=100,color='gray')
        scores1=str(int(ui.score.score))
        for i in range(7-len(list(str(int(ui.score.score))))):
            scores1='0'+scores1
        screen.draw.text(str(int(scores1)),topleft=[act.k[0].x-50,180],fontname='siyuanblod1',fontsize=80,color='gray')
        screen.draw.text('MAX Combo:  '+str(ui.score.MaxCombo),topleft=[act.k[0].x-85,280],fontname='siyuanblod1',fontsize=40,color='gray')
        screen.draw.text('Perfect:  '+str(ui.game.perfect),topleft=[act.k[0].x-110,360],fontname='siyuanblod1',fontsize=40,color='gray')
        screen.draw.text('Good:  '+str(ui.game.good),topleft=[act.k[0].x-145,440],fontname='siyuanblod1',fontsize=40,color='gray')
        screen.draw.text('Bad:  '+str(ui.game.bad),topleft=[act.k[0].x-180,520],fontname='siyuanblod1',fontsize=40,color='gray')
        screen.draw.text('Miss:  ' +str(ui.game.miss),topleft=[act.k[0].x-215,600],fontname='siyuanblod1',fontsize=40,color='gray')
        if ui.game.MusicName+'.txt' in ui.select.SavesList:

            scores=ui.ScoresSaves[ui.select.SavesList.index(ui.game.MusicName+'.txt')][0]
        else:
            scores=0
        rank=CheckRank(scores1)
        screen.draw.text(rank,topleft=[act.k[9].x+200,300],fontname='siyuanblod1',fontsize=300,shadow=(0.5,0.5), scolor=(105,105,105),owidth=0.5,ocolor=(105,105,105))
        screen.draw.text('RANK',topleft=[act.k[9].x+180,600],fontname='siyuanblod1',fontsize=100,shadow=(1.0,1.0), scolor=(105,105,105),owidth=0.5,ocolor=(105,105,105))
        scores=ui.ScoresSaves[ui.select.SavesList.index(ui.game.MusicName+'.txt')][0]
        if settings.autoplay:
            screen.draw.text('AUTOPLAY模式不记录成绩',topleft=[act.k[9].x+300,300],fontname='siyuanblod1',fontsize=50,color='white')
        elif scores<=int(ui.score.score):
            screen.draw.text('New Best!',topleft=[act.k[9].x+300,300],fontname='siyuanblod1',fontsize=50,color='gold')#,shadow=(0.5,0.5), scolor='white',owidth=0.5,ocolor='gold')
class init():
    def StartToMainCartoon():
    
        for i in range(4):
            act.k[i].x=1500
            act.k[i].y=HEIGHT/2
            act.k[i].image='k1.png'
            act.kwantx[i]=900+i*100
            act.kwanty[i]=HEIGHT/2
    def settings():
        ui.ui='settings'
        for i in range(3,10,1):
            act.k[i].x=-800
            act.k[i].y=HEIGHT/2
            act.kwantx[i]=-700+i*30
            act.k[9].x=-568
            act.kwantx[9]=-165
            act.kwanty[i]=HEIGHT/2
        for i in range(4):
            act.k[i].x=900+i*100
            act.k[i].y=HEIGHT/2
            act.k[i].image='k1.png'
            act.kwantx[i]=900+i*100
            act.kwantx[0]=767
            act.kwanty[i]=HEIGHT/2
    def start():
        ui.times=0
        for i in range(4):
            act.k[i].x=-2000
            act.k[i].y=HEIGHT/2
            act.k[i].image='k1.png'
            act.kwantx[i]=-2100
    def main():
        PlayMusic(os.getcwd()+'/sounds/arcaea.wav')
        #PlayMusic(os.getcwd()+'/sounds/Theme_01_short.wav')
        init.StartToMainCartoon()
        ui.game.MusicName=read_f.gameread()
        ui.ui='main'
    def select():
        filePath = os.getcwd()+'//files//resourse'
        for i,j,k in os.walk(filePath):
            SoundsList=j
            break
        ui.select.SoundsList=SoundsList
        ui.select.SavesList=[]
        read_f.saves()#这玩意的位置千万别乱搞！不然存档都读不出来！
        for i in range(4):
            act.k[i].x=900+i*100
            act.k[i].y=HEIGHT/2
            act.k[i].image='k1.png'
            act.kwantx[i]=1000+i*30
            act.kwantx[0]=767
            act.kwanty[i]=HEIGHT/2
        for f in range(len(ui.select.SoundsList)):
            shutil.copy(str(os.getcwd()+'/files/resourse/'+ui.select.SoundsList[f]+'/1.png'),str(os.getcwd()+'/images/s'+str(f)+'.png'))
        for f in range(len(act.bts)):
            act.btpos[f]=0
        for i in range(3,10,1):
            act.k[i].x=-800
            act.k[i].y=HEIGHT/2
            act.kwantx[i]=-700+i*30
            act.k[9].x=-568
            act.kwantx[9]=-165
            act.kwanty[i]=HEIGHT/2
        act.btpos=[]
        act.bts=[]
        act.btswanty=[]
        for i in range(len(ui.select.SoundsList)):
            act.btpos.append(0)
            act.bts.append(Actor(os.getcwd()+'/images/bt1.png'))
            act.btswanty.append(0)
        i=ui.select.SoundsList.index(ui.game.MusicName)
        act.btpos[i]-=50
        act.bg.image=os.getcwd()+'/images/s'+str(i)+'.png'
        f=open(str(os.getcwd()+'/files/playing.txt'),'w',encoding='utf-8')
        f.write(str(ui.select.SoundsList[i]))
        f.close()
        ui.game.MusicName=read_f.gameread()
        PlayMusic(os.getcwd()+'//files//resourse//'+ui.game.MusicName+'//1.mp3')
        ui.ui='select'
        print(act.bts[ui.select.SoundsList.index(ui.game.MusicName)].y,12323.333)
    def game():
        ui.game.MusicName=read_f.gameread()
        shutil.copy(str(os.getcwd()+'/files/resourse/'+ui.game.MusicName+'/1.png'),str(os.getcwd()+'/images/'))
        os.unlink(os.getcwd()+'/images/1.png')
        shutil.copy(str(os.getcwd()+'/files/resourse/'+ui.game.MusicName+'/1.png'),str(os.getcwd()+'/images/'))
        filePath = os.getcwd()+'//files//resourse'
        read_f.pm()
        for i,j,k in os.walk(filePath):
            SoundsList=j
            break
        ui.select.SoundsList=SoundsList
        act.bg.image='s'+str(ui.select.SoundsList.index(ui.game.MusicName))+'.png'
        k1='k1.png'
        for i in range(4):
            act.kwantx[i]=-2100
            act.kwanty[i]=HEIGHT/2
            act.k[i].image=k1
        ui.ui='game'
        ui.times=0
        ui.game.pospone=read_f.pospone()
        ui.game.keys=[]
        ui.game.pos=0
        ui.game.postime=0
        ui.game.musictime=0
        ui.game.perfect=0
        ui.game.good=0
        ui.game.bad=0
        ui.game.miss=0
        ui.game.combo=0
        act.game.perfect=[[],[],[],[]]
        act.game.good=[[],[],[],[]]
        act.game.keys=[[],[],[],[]]
        act.game.perfectimage=[[],[],[],[]]
        act.game.goodimage=[[],[],[],[]]
        for i in range(len(act.game.b)):
            ui.game.keys.append(0)
        adress=os.getcwd()+'//files//resourse//'+ui.game.MusicName
        name=adress+'//1.mp3'
        pygame.mixer.init()
        pygame.mixer.music.load(name)
        pygame.mixer.music.set_volume(1)
        ui.score.Count=0
        for i in range(len(act.game.b)):
            global pms
            pm=pms[i]
            for f in range(len(pm[0])):
                if str(pm[1][f])=='0':
                    act.game.keys[i].append(Actor('tap'+str(i+1)+'.png',[0,200+120*i]))#蓝键
                elif str(pm[1][f])=='1':
                    act.game.keys[i].append(Actor('drag'+str(i+1)+'.png',[0,200+120*i]))#黄键
                '''if random.choice([True,False]):
                    act.game.keys[i].append(Actor('tap'+str(i+1)+'.png',[0,200+120*i]))#蓝键
                else:
                    act.game.keys[i].append(Actor('drag'+str(i+1)+'.png',[0,200+120*i]))#黄键'''
                act.game.good[i].append(Actor('good12.png',[-500,-500]))#Good特效
                act.game.perfect[i].append(Actor('perfect12.png',[-500,-500]))#Perfect特效
                act.game.perfectimage[i].append(8)#Perfect特效编号
                act.game.goodimage[i].append(8)#Good特效编号
                ui.score.Count+=1#物量
        pygame.mixer.music.play()
        pygame.mixer.music.pause()
        ui.times=0
        ui.score.score=0
        ui.score.TapScore=0
        ui.score.ComboScore=0
        ui.score.MaxCombo=0
        ui.game.pause=False
    def end():
        ui.ui='end'
        filePath = os.getcwd()+'//files//resourse'
        for i,j,k in os.walk(filePath):
            SoundsList=j
            break
        ui.select.SoundsList=SoundsList
        act.bg.image='s'+str(ui.select.SoundsList.index(ui.game.MusicName))+'.png'
        for i in range(3,10,1):
            act.k[i].x=-2000
            act.k[i].y=HEIGHT/2
            act.kwantx[i]=-1000+i*80
            act.kwantx[9]=-32
            act.kwanty[i]=HEIGHT/2
        init.StartToMainCartoon()
        read_f.saves()
        if ui.game.MusicName+'.txt' in ui.select.SavesList:
            f=open(os.getcwd()+'/files/saves/'+ui.game.MusicName+'.txt','r',encoding='utf-8')
            #####print(1111111111111111111111111)
            scores=ui.ScoresSaves[ui.select.SavesList.index(ui.game.MusicName+'.txt')][0]
            if scores<=int(ui.score.score) and settings.autoplay==False:
                ####print(2222222222222222)
                f=open(os.getcwd()+'/files/saves/'+ui.game.MusicName+'.txt','w',encoding='utf-8')
                ####print(str(int(ui.score.score))+"#"+str(ui.score.MaxCombo)+"#"+str(ui.game.perfect)+"#"+str(ui.game.good)+"#"+str(ui.game.bad)+"#"+str(ui.game.miss)+'#',2)
                f.write(str(int(ui.score.score))+"#"+str(ui.score.MaxCombo)+"#"+str(ui.game.perfect)+"#"+str(ui.game.good)+"#"+str(ui.game.bad)+"#"+str(ui.game.miss)+'#')
                f.close()
                read_f.saves()
        else:
            f=open(os.getcwd()+'/files/saves/'+ui.game.MusicName+'.txt','w',encoding='utf-8')
            f.write(str(int(ui.score.score))+"#"+str(ui.score.MaxCombo)+"#"+str(ui.game.perfect)+"#"+str(ui.game.good)+"#"+str(ui.game.bad)+"#"+str(ui.game.miss)+'#')
            ####print(3333333333333333333333333)
            ####print(str(int(ui.score.score))+"#"+str(ui.score.MaxCombo)+"#"+str(ui.game.perfect)+"#"+str(ui.game.good)+"#"+str(ui.game.bad)+"#"+str(ui.game.miss)+'#',3)
            f.close()
            read_f.saves()
        PlayMusic(os.getcwd()+'/sounds/LevelOver0.wav')
def setk1():
    #if ui.ui=='game':
        #return
    x=int(ui.game.speedwant*100)/100-int(ui.game.speed*100)/100
    #####print(x)
        #if x>0:
    if x>0.01:
        ui.game.speed+=0.01
    if x<-0.01:
        ui.game.speed-=0.01
    for i in range(10):
        x=act.kwantx[i]-act.k[i].x
        y=act.kwanty[i]-act.k[i].y
        if -5<x<=-1:
            act.k[i].x-=1
        elif -20<x<=-5:
            act.k[i].x-=3
        elif -50<x<=-20:
            act.k[i].x-=6
        elif -110<x<=-50:
            act.k[i].x-=12
        elif -225<x<=-110:
            act.k[i].x-=25
        elif x<=-225:
            act.k[i].x-=50
        if -5<y<=-1:
            act.k[i].y-=1
        elif -20<y<=-5:
            act.k[i].y-=2
        elif -50<y<=-20:
            act.k[i].y-=5
        elif -110<y<=-50:
            act.k[i].y-=10
        elif -225<y<=-110:
            act.k[i].y-=20
        elif y<=-225:
            act.k[i].y-=50
        if 1<x<=5:
            act.k[i].x+=1
        elif 5<x<=20:
            act.k[i].x+=3
        elif 20<x<=50:
            act.k[i].x+=6
        elif 50<x<=110:
            act.k[i].x+=12
        elif 110<x<=225:
            act.k[i].x+=25
        elif x>=225:
            act.k[i].x+=50
        if 1<y<=5:
            act.k[i].y+=1
        elif 5<y<=20:
            act.k[i].y+=2
        elif 20<y<=50:
            act.k[i].y+=5
        elif 50<y<=110:
            act.k[i].y+=10
        elif 110<y<=225:
            act.k[i].y+=20
        elif y>=225:
            act.k[i].y+=50
    clock.schedule_unique(setk1,0.02)
def update():
    #print(str(ui.game.keydownState[0])+str(ui.game.keydownState[1])+str(ui.game.keydownState[2])+str(ui.game.keydownState[3]))
    if time.strftime('%S')!=ui.lst:
        ui.times+=1
        ui.lst=time.strftime('%S')
        if ui.times%2==0 and settings.experiment:
            if ui.ui=='game':
                ui.game.speedwant=random.randint(5,15)/10
            ####print('123sadsaf334')
    if ui.ui=='start':
        if ui.times>=3:
            ui.times=0
            init.main()
    if ui.ui=='select':
        act.select.PerfectLine.x=int((act.select.PerfectLine.y-1739)/-2.41)#-10#+400#+act.btpos[i]-50
        act.select.GoodLine.x=int((act.select.GoodLine.y-1739)/-2.41)#-10#+400#+act.btpos[i]-50
        act.select.BadLine.x=int((act.select.BadLine.y-1739)/-2.41)#-10#+400#+act.btpos[i]-50
        act.select.MissLine.x=int((act.select.MissLine.y-1739)/-2.41)#-10#+400#+act.btpos[i]-50
        for i in range(len(ui.select.SoundsList)):
            y=act.btswanty[i]-act.bts[i].y
            if -5<y<=-1:
                act.bts[i].y-=1
            elif -20<y<=-5:
                act.bts[i].y-=2
            elif -50<y<=-20:
                act.bts[i].y-=5
            elif -110<y<=-50:
                act.bts[i].y-=10
            elif -225<y<=-110:
                act.bts[i].y-=20
            elif y<=-225:
                act.bts[i].y-=50
            if 1<y<=5:
                act.bts[i].y+=1
            elif 5<y<=20:
                act.bts[i].y+=2
            elif 20<y<=50:
                act.bts[i].y+=5
            elif 50<y<=110:
                act.bts[i].y+=10
            elif 110<y<=225:
                act.bts[i].y+=20
            elif y>=225:
                act.bts[i].y+=50
    elif ui.ui=='game':
        #global TITLE;TITLE=str(ui.game.keys[0])+str(ui.game.keys[1])+str(ui.game.keys[2])+str(ui.game.keys[3])
        if ui.game.pause:
            return
        for i in range(4):
            #print(i)
            if ui.game.keydownState[i]:
                ui.game.check(i,ui.game.keys[i],1)
        x,y=pygame.mouse.get_pos()
        act.game.bmouse.y=y
        act.bg.x=WIDTH/2
        ui.game.progress=((ui.game.musictime/10)/ui.game.length)
        act.game.ProgressLine.y=HEIGHT-HEIGHT*ui.game.progress+HEIGHT/2
        if 1>=int(ui.game.musictime-ui.game.length*10)>=-1:
            init.end()
        if ui.times==3: 
            pygame.mixer.music.unpause()
            ui.game.pause=False
        a=pygame.mixer.music.get_pos()
        ui.game.musictime=a/100
        ui.game.postime=a
        ui.game.pos=-ui.game.postime
        ####print(ui.game.pos)
        for i in range(4):
            global pms
            pm=pms[i]
            for f in range(len(act.game.keys[i])):
                if act.game.perfectimage[i][f]<=11:
                    act.game.perfectimage[i][f]+=1
                    act.game.perfect[i][f].image='perfect'+str(act.game.perfectimage[i][f])+'.png'
                if act.game.goodimage[i][f]<=11:
                    act.game.goodimage[i][f]+=1
                    act.game.good[i][f].image='good'+str(act.game.goodimage[i][f])+'.png'
                act.game.keys[i][f].x=(pm[0][f]*100+act.game.b[i].x+ui.game.pos)*ui.game.speed-ui.game.pospone+ui.game.speed*100
                if settings.autoplay:
                    if -25<act.game.keys[i][f].x<act.game.b[i].x+25 and 720>act.game.keys[i][f].y>0:
                        ui.game.autocheck(i,ui.game.keys[i])
                if act.game.keys[i][f].x<WIDTH and act.game.keys[i][f].y>0:
                    if act.game.b[i].x<act.game.keys[i][f].x<act.game.b[i].x+50:
                        if str(act.game.keys[i][f].image)=='key1miss.png' or str(act.game.keys[i][f].image)=='key2miss.png':
                            act.game.keys[i][f].y=-10000
                            return
                    if act.game.b[i].x-200<act.game.keys[i][f].x<act.game.b[i].x-150:
                        if act.game.keys[i][f].image=='tap'+str(i+1)+'.png':
                            act.game.keys[i][f].image='key1miss.png'
                        elif act.game.keys[i][f].image=='drag'+str(i+1)+'.png':
                            act.game.keys[i][f].image='key2miss.png'
                    elif act.game.keys[i][f].x<act.game.b[i].x-250:
                        ui.game.miss+=1
                        ui.game.keys[i]+=1
                        act.game.keys[i][f].y=-10000
                        ui.game.combo=0
    #draw()
def on_key_down(key):
    if ui.ui=='game':
        if key==32:
            if ui.game.pause:
                ui.game.pause=False
                pygame.mixer.music.unpause()
            else:
                ui.game.pause=True
                pygame.mixer.music.pause()
        if ui.game.pause or settings.autoplay:
            return
        if key==102:
            ui.game.keydownState[0]=True
            ui.game.check(0,ui.game.keys[0],0)
        if key==103:
            ui.game.keydownState[1]=True
            ui.game.check(1,ui.game.keys[1],0)
        if key==104:
            ui.game.keydownState[2]=True
            ui.game.check(2,ui.game.keys[2],0)
        if key==106:
            ui.game.keydownState[3]=True
            ui.game.check(3,ui.game.keys[3],0)
def on_key_up(key):
    if ui.ui=='game':
        if key==102:
            ui.game.keydownState[0]=False
        if key==103:
            ui.game.keydownState[1]=False
        if key==104:
            ui.game.keydownState[2]=False
        if key==106:
            ui.game.keydownState[3]=False
def on_mouse_up(pos,button):
    ####print(pos,button)
    switch_to_english()
    if button!=1:
        return
    if ui.ui=='settings':
        if act.bt[1].collidepoint(pos):
            SoundsPlay(os.getcwd()+'/sounds/tap1.wav')
            pygame.mixer.music.fadeout(100)
            init.main()
        elif act.settings.autoplay.collidepoint(pos):
            if settings.autoplay:
                settings.autoplay=False
            else:
                settings.autoplay=True
        elif act.settings.experiment.collidepoint(pos):
            if settings.experiment:
                settings.experiment=False
            else:
                settings.experiment=True
    elif ui.ui=='main':
        if act.bt[0].collidepoint(pos):
            pygame.mixer.music.pause()
            time.sleep(0.05)
            ui.game.length=pygame.mixer.Sound('files//resourse//'+ui.game.MusicName+'//1.mp3').get_length()
            SoundsPlay(os.getcwd()+'/sounds/tap7.wav')
            ui.game.length=pygame.mixer.Sound('files//resourse//'+ui.game.MusicName+'//1.mp3').get_length()
            init.game()
        elif act.bt[1].collidepoint(pos):
            pygame.mixer.music.fadeout(200)
            SoundsPlay(os.getcwd()+'/sounds/tap1.wav')
            init.select()
        elif act.bt[2].collidepoint(pos):
            pygame.mixer.music.fadeout(1000)
            SoundsPlay(os.getcwd()+'/sounds/tap1.wav')
            ####print('settings')
            init.settings()
        elif act.bt[3].collidepoint(pos):
            SoundsPlay(os.getcwd()+'/sounds/tap1.wav')
            time.sleep(0.05)
            exit()
    elif ui.ui=='select':
        for i in range(len(ui.select.SoundsList)):
            if act.bts[i].collidepoint(pos):
                if act.btpos[i]==-50:
                    return
                else:
                    SoundsPlay(os.getcwd()+'/sounds/tap1.wav')
                    for f in range(len(ui.select.SoundsList)):
                        act.btpos[f]=0
                    act.btpos[i]-=50
                    act.bg.image='s'+str(i)+'.png'
                    f=open(str(os.getcwd()+'/files/playing.txt'),'w',encoding='utf-8')
                    f.write(str(ui.select.SoundsList[i]))
                    f.close()
                    ui.game.MusicName=read_f.gameread()
                    PlayMusic(os.getcwd()+'//files//resourse//'+ui.game.MusicName+'//1.mp3')
        if act.bt[0].collidepoint(pos):
            ui.game.length=pygame.mixer.Sound('files//resourse//'+ui.game.MusicName+'//1.mp3').get_length()
            SoundsPlay(os.getcwd()+'/sounds/tap7.wav')
            pygame.mixer.music.pause()
            time.sleep(0.05)
            ui.game.MusicName=read_f.gameread()
            init.game()
        elif act.bt[1].collidepoint(pos):
            SoundsPlay(os.getcwd()+'/sounds/tap1.wav')
            pygame.mixer.music.fadeout(100)
            init.main()
        elif act.bt[2].collidepoint(pos):
            SoundsPlay(os.getcwd()+'/sounds/tap1.wav')
            randomsls=[]
            for i in range(len(ui.select.SoundsList)):
                if i!=ui.select.SoundsList.index(ui.game.MusicName):
                    randomsls.append(i)
            randoms=random.choice(randomsls)
            for i in range(len(ui.select.SoundsList)):
                if i==randoms:
                    if act.btpos[i]==-50:
                        return
                    else:
                        SoundsPlay(os.getcwd()+'/sounds/tap1.wav')
                        for f in range(len(ui.select.SoundsList)):
                            act.btpos[f]=0
                        act.btpos[i]-=50
                        act.bg.image='s'+str(i)+'.png'
                        f=open(str(os.getcwd()+'/files/playing.txt'),'w',encoding='utf-8')
                        f.write(str(ui.select.SoundsList[i]))
                        f.close()
                        ui.game.MusicName=read_f.gameread()
                        PlayMusic(os.getcwd()+'//files//resourse//'+ui.game.MusicName+'//1.mp3')
        act.posbts+=350-act.bts[ui.select.SoundsList.index(ui.game.MusicName)].y
    elif ui.ui=='game':
        if ui.game.pause:
            if 310<pos[1]<370 and 510<pos[0]<575:
                SoundsPlay(os.getcwd()+'/sounds/tap1.wav')
                pygame.mixer.music.pause()
                init.select()
            elif 310<pos[1]<370 and 620<pos[0]<685:
                ui.game.length=pygame.mixer.Sound('files//resourse//'+ui.game.MusicName+'//1.mp3').get_length()
                SoundsPlay(os.getcwd()+'/sounds/tap1.wav')
                pygame.mixer.music.pause()
                init.game()
            elif 310<pos[1]<370 and 740<pos[0]<1005:
                SoundsPlay(os.getcwd()+'/sounds/tap1.wav')
                pygame.mixer.music.pause()
                if ui.game.pause:
                    ui.game.pause=False
                    pygame.mixer.music.unpause()
                else:
                    ui.game.pause=True
                    pygame.mixer.music.pause()
        else: 
            for i in range(4):
                if act.game.b[i].collidepoint(pos) and settings.autoplay==False:
                    ui.game.check(i,ui.game.keys[i],0)
    elif ui.ui=='end':
        if act.bt[0].collidepoint(pos):
            SoundsPlay(os.getcwd()+'/sounds/tap1.wav')
            pygame.mixer.music.fadeout(100)
            init.select()
        if act.bt[1].collidepoint(pos):
            ui.game.length=pygame.mixer.Sound('files//resourse//'+ui.game.MusicName+'//1.mp3').get_length()
            SoundsPlay(os.getcwd()+'/sounds/tap1.wav')
            pygame.mixer.music.pause()
            init.game()
    if settings.autoplay:
        act.settings.autoplay.image='skipbtt.png'
    else:
        act.settings.autoplay.image='skipbtf.png'
    if settings.experiment:
        act.settings.experiment.image='skipbtt.png'
    else:
        act.settings.experiment.image='skipbtf.png'
init.start()
setk1()
ui.game.speedwant=1.2
os.environ['PGZERO_ICON'] = 'icon.ico'
init.main()
pgzrun.go()