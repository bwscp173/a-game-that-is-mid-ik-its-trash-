
import random
import time
from colorama import Fore
#index body help
#0=head
#1=body
#2=larmw
#3=rarm
#4=lleg
#5=rleg
g=Fore.LIGHTGREEN_EX
r=Fore.RED
y=Fore.LIGHTYELLOW_EX
w=Fore.WHITE
temp=True
money=50
#a is ment to be the spaces to make the colums organised

weapon={#never used
  "hand":[100,1],
  "spear":[60,1.5],
  "sword":[80,1.2],
  "dagger":[70,1.1]
}
#accuracy,damage increase,

bpartstat={
  "head":[50,90,50],
  "body":[200,15,200],
  "larm":[75,30,75],
  "rarm":[75,30,75],
  "lleg":[75,30,75],
  "rleg":[75,30,75]
}#bodypart, hp, dodge chance, max hp(DO NOT CHANGE MAX HP!!!!!) #use updatedi(what,new,index) to change hp and dodge chance

aibpart={
  "aihead":[50,90,50],
  "aibody":[250,15,250],
  "ailarm":[75,30,75],
  "airarm":[75,30,75],
  "ailleg":[75,30,75],
  "airleg":[75,30,75]
}
#william harrold watches cbbs "charly and loba" this is very important information
def rules():
  print("your goal is to kill your oppenent")
  print("you can do this by killing 2 non vital organs such as arms and legs")
  print("or you can win faster by killing 1 vital organ such as head and body.")
  print("each turn the ai will take an attack on you")
  print("you have a chance to dodge the attack")
  print("after the ai's turn you will get a chance to attack the ai")
  print("type the body part you would like to attack when prompted to")
  print("lleg means left leg and rarm mean right arm")
  print("tips-the more hp a body part has the lower the dodge chance")
  print(f"          {g}this is you{w}                     {r}this is the enemy{w}    ")
def endgame():
  print("you have died due to death")
  print("git gud")
  print("restart the game because im to lazy to code it my self")
  time.sleep(99999)
  print("why tf are you still here")

def getfpart(index):
  return list(bpartstat.items())[index][0]

def aigetpart(index):
  return list(aibpart.items())[index][0]

def getweapon(index):
  return list(weapon.items())[index][0]

def updatedi(what,new,index):# when it says what it means "body" e.g. updatedi("body",150,0)
  bpartstat[str(what)][int(index)]=int(new)

def updatediai(what,new,index):
  aibpart[str(what)][int(index)]=int(new)

def getwname(index):
  x=getweapon(index)
  return str(x)

def getaihp(index):
  x=aigetpart(index)
  x=aibpart[x]
  x=x[0]
  return x

def getaidodge(index):
  x=aigetpart(index)
  x=aibpart[x]
  x=x[1]
  return x
def getaccuracy(index):
  x=getfpart(index)
  x=bpartstat[x]
  x=x[0]
  return x

def getdamageincrease(index):
  x=getfpart(index)
  x=bpartstat[x]
  x=x[1]
  return x

def gethp(index):
  x=getfpart(index)
  x=bpartstat[x]
  x=x[0]
  return x

def getdodge(index):
  x=getfpart(index)
  x=bpartstat[x]
  x=x[1]
  return x

def getmaxhp(index):
  x=getfpart(index)
  x=bpartstat[x]
  x=x[2]
  return x

def getaimaxhp(index):
  x=aigetpart(index)
  x=aibpart[x]
  x=x[2]
  return x

def changew(index):#testing gloabal
  global cw
  cw="testing123"

def restart():
  rules()
  updatedi("head",getmaxhp(0),0)
  updatedi("body",getmaxhp(1),0)
  updatedi("larm",getmaxhp(2), 0)
  updatedi("rarm",getmaxhp(3), 0)
  updatedi("lleg",getmaxhp(4), 0)
  updatedi("rleg",getmaxhp(5), 0)
  
  updatediai("aihead",getaimaxhp(0),0)
  updatediai("aibody",getaimaxhp(1),0)
  updatediai("ailarm",getaimaxhp(2), 0)
  updatediai("airarm",getaimaxhp(3), 0)
  updatediai("ailleg",getaimaxhp(4), 0)
  updatediai("airleg",getaimaxhp(5), 0)
restart()

def winround():
  print("=============================")
  print("you have killed your aponent")
  print("")
  print("now restarting your game")
  print("")
  print("=============================")
  time.sleep(3)
  restart()

def aicolour(index):
  i=int(index)
  max=getaimaxhp(i)
  base=getaihp(i)
  if int(base)==max:
    return g
  if int(base)<max and int(base)>0:
    return y
  if int(base)<0 or int(base)==0:
    return r 

def colour(index):
  i=int(index)
  max=getmaxhp(i)
  base=gethp(i)
  if int(base)==max:
    return g
  if int(base)<max and int(base)>0:
    return y
  if int(base)<0 or int(base)==0:
    return r

def checkhp():#=============work on this=====returns true if any bpart dies should only return if body or head or 2 bparts are dead.
  temp=False
  for i in range(2):
    hp=gethp(i)
    if hp<0 or hp==0:
      temp+=2
  for i in range(4):
    hp=gethp(i+2)
    if hp<0 or hp==0:
      temp+=1
  if temp>2 or temp==2:
    return True
  else:
    return False

def checkaihp():#checks the ai hp if dead then returns 
  temp=False
  for i in range(2):
    hp=getaihp(i)
    if hp<0 or hp==0:
      temp+=2
  for i in range(4):
    hp=getaihp(i+2)
    if hp<0 or hp==0:
      temp+=1
  if temp>2 or temp==2:
    return True
  else:
    return False

def space(word,size):#thanks to @sslroean(i think that is his username) for this part
  nstr="";cout=0
  word = str(word)
  for i in word:
    nstr+=i
    cout+=1
    if cout==size:
      break
  if len(nstr) < size:
    diff = size - len(nstr)
    nstr2 = " " * diff
    nstr = nstr2 + nstr
  return nstr

def aidamage(bpart,damage):# damages the ai body part with x damage
  if checkaihp()==True:
    print("=========")
    print("!YOU WIN!")
    print("=========")
    time.sleep(3)
    endgame()
  else:
    chance=random.randint(0,100)
    temp=aibpart.get(bpart)
    aibodyparthp=temp[0]
    dodge=int(temp[1])
    if chance<dodge:
      print(f"==========================")
      print(f"==dodged no damage taken==")
      print(f"==========================")
    if chance>dodge:
      critc=random.randint(0,100)
      if critc>70:
        print("===!critical hit!===")
        updatediai(bpart,aibodyparthp-(damage*1.35),0)
        print("=======================")
        print("==take "+str(damage*1.5)+" damage")
        print("=======================")
      if critc<70 and critc>10:
        print("==normal hit==")
        updatediai(bpart,aibodyparthp-damage,0)
        print("=======================")
        print("==take "+str(damage)+" damage")
        print("=======================")
      if critc<10:
        print("=weak hit!=")
        updatediai(bpart,aibodyparthp-(damage*0.8),0)
        print("=======================")
        print("==take "+str(damage*0.6)+" damage")
        print("=======================")

def playerdamage(bpart,damage):
  if checkhp()==True:
    endgame()
  else:
    chance=random.randint(0,100)
    temp=bpartstat.get(bpart)
    bodyparthp=int(temp[0])
    dodge=int(temp[1])
    if chance<dodge:
      print(f"========================================")
      print(f"=====dodged no damage taken to the "+str(bpart)+"=====")
      print(f"========================================")
    if chance>dodge:
      critc=random.randint(0,100)
      if critc>70:
        print("critical hit!")
        updatedi(bpart,bodyparthp-(damage*1.35),0)
        print("=======================")
        print("==deal "+str(damage*1.5)+" damage")
        print("=======================")
      if critc<70 and critc>10:
        print("normal hit")
        updatedi(bpart,bodyparthp-damage,0)
        print("=======================")
        print("==deal "+str(damage)+" damage")
        print("=======================")
      if critc<10:
        print("weak hit!")
        updatedi(bpart,bodyparthp-(damage*0.8),0)
        print("=======================")
        print("==deal "+str(damage*0.6)+" damage")
        print("=======================")
    
def displaydevhp():
  print("=====player====")
  for i in range(len(bpartstat)):
    x=getfpart(i)
    print(x,bpartstat[x])
  print("=====ai=====")
  for i in range(len(aibpart)):
    x=aigetpart(i)
    print(x,aibpart[x])
  
def hp():
  colourli=[]
  li=[]
  for i in range(6):
    x=gethp(i)
    li.append(x)
  for i in range(6):
    x=colour(i)
    colourli.append(x)
  #==================================================================================
  #                                i warn you do not scroll down if you want to keep your sanity
  #                                         scroll down to 412 for nice looking code
  #==================================================================================
  aihead=getaihp(0)
  aibody=getaihp(1)
  ailarm=getaihp(2)
  airarm=getaihp(3)
  ailleg=getaihp(4)
  airleg=getaihp(5)

  aiheadc=aicolour(0)
  aibodyc=aicolour(1)
  ailarmc=aicolour(2)
  airarmc=aicolour(3)
  aillegc=aicolour(4)
  airlegc=aicolour(5)
  #print(getmaxhp(0))

  print(f"             {colourli[-6]}# # #{w}              |"+f"              {aiheadc}# # #{w}")
  print(f"           {colourli[-6]}#  "+space(li[-6],2)+f"/ #{w}             |"+f"            {aiheadc}#  "+str(aihead)+"/ #"+f"{w}")
  print(f"           {colourli[-6]}#  "+str(getmaxhp(0))+f"  #{w}             |"+f"            {aiheadc}#  "+str(getaimaxhp(0))+f"  #{w}")#str(gethp(0))
  print(f"             {colourli[-6]}# # #{w}              |"+f"              {aiheadc}# # #{w}")#===========================head============
  print("                                |"+"     ")
  print(f"             {colourli[-5]}# # #{w}              {w}|"+f"              {aibodyc}# # #{w}")
  print(f"   {colourli[-4]}# # #   {colourli[-5]}#       #   {colourli[-3]}# # #    {w}|"+f"    {ailarmc}# # #{w}"+f"{w}   {aibodyc}#       #{w}   {airarmc}# # #{w}")
  print(f"   {colourli[-4]}#   #   {colourli[-5]}#  body #   {colourli[-3]}#   #    {w}|"+f"    {ailarmc}#   #{w}   {aibodyc}#  body #{w}   {airarmc}#   #{w}")
  print(f"  {colourli[-4]}#larm#   {colourli[-5]}#  "+space(li[-5],3)+f"/ #  {colourli[-3]}#rarm#    {w}|"+f"   {ailarmc}#larm#{w}   {aibodyc}#  "+space(aibody,3),"/#  "+f"{airarmc}#rarm#{w}")
  print(f"   {colourli[-4]}#"+space(li[-4],2)+f"/#   {colourli[-5]}#  "+str(getmaxhp(1))+f"  #   {colourli[-3]}#"+space(li[-3],2)+f"/#    {w}|"+f"    {ailarmc}#"+space(ailarm,2)+"/#"+f"{w}   {aibodyc}#  "+str(getmaxhp(1))+f"  #{w}   {airarmc}#"+space(airarm,2)+f"/#{w}")
  print(f"   {colourli[-4]}#"+space(str(getmaxhp(2)),2)+f" #   {colourli[-5]}#       #   {colourli[-3]}#"+space(str(getmaxhp(3)),2)+f" #    {w}|"+f"    {ailarmc}#"+space(str(getaimaxhp(2)),2)+f" #{w}   {aibodyc}#       #{w}   {airarmc}#"+space(str(getaimaxhp(3)),2)+f" #{w}")
  print(f"   {colourli[-4]}#   #   {colourli[-5]}#       #   {colourli[-3]}#   #    {w}|"+f"    {ailarmc}#   #{w}   {aibodyc}#       #{w}   {airarmc}#   #{w}")
  print(f"   {colourli[-4]}# # #   {colourli[-5]}#       #   {colourli[-3]}# # #    {w}|"+f"    {ailarmc}# # #{w}   {aibodyc}#       #{w}   {airarmc}# # #{w}")#
  print(f"           {colourli[-5]}#       #            {w}|"+f"            {aibodyc}#       #{w}")
  print(f"             {colourli[-5]}# # #              {w}|"+f"              {aibodyc}# # #{w}")

  #=====================legs=================
  print(f"                                {w}|"+f"     ")
  print(f"       {colourli[-2]}# # #       {colourli[-1]}# # #{w}        |"+f"        {aillegc}# # #{w}       {airlegc}# # #{w}")
  print(f"       {colourli[-2]}#   #       {colourli[-1]}#   #        {w}|"+f"        {aillegc}#   #{w}       {airlegc}#   #{w}")
  print(f"       {colourli[-2]}#lleg#      {colourli[-1]}#rleg#       {w}|"+f"        {aillegc}#lleg#{w}      {airlegc}#rleg#{w}")
  print(f"       {colourli[-2]}#"+space(li[-2],2)+f"/#       {colourli[-1]}#"+space(li[-1],2)+f"/#        {w}|"+f"        {aillegc}#"+space(ailleg,2)+"/#"+f"{w}       {airlegc}#"+space(airleg,2)+"/#"+f"{w}")
  print(f"       {colourli[-2]}#"+space(str(getmaxhp(4)),2)+f" #       {colourli[-1]}#"+space(str(getmaxhp(5)),2)+f" #        {w}|"+f"        {aillegc}#"+space(str(getaimaxhp(4)),2)+f" #{w}       {airlegc}#"+space(str(getaimaxhp(5)),2)+f" #{w}")
  print(f"       {colourli[-2]}#   #       {colourli[-1]}#   #        {w}|"+f"        {aillegc}#   #{w}       {airlegc}#   #{w}")
  print(f"       {colourli[-2]}# # #       {colourli[-1]}# # #        {w}|"+f"        {aillegc}# # #{w}       {airlegc}# # #{w}")
def crit(critc):
  ncritc=critc+random.randint(-15,150)
  if ncritc>70:
    print("=============")
    print("CRITICAL Hit!")
    print("=============")
    return 1.35
  if ncritc<70 and ncritc>10:
    print("==========")
    print("Normal hit")
    print("==========")
    return 1
  if ncritc<10:
    print("=========")
    print("weak hit!")
    print("=========")
    return 0.75

def lowbp():
  for i in range(6):
    hp=gethp(i)
    max=getmaxhp(i)
    temp=int((hp/max)*100)
    if temp<25 or temp==25:
      return i

def aimove():
  if checkhp()==True:
    winround()
    print("you have died")
    print("resart the game im too lazy to make it restart by it self")
    time.sleep(999)
  else:
    print("AI's turn:")
    moved=False
    for i in range(6):
      hp=gethp(i)
      max=getmaxhp(i)
      temp=int((hp/max)*100)
    for i in range(6):
      if moved==False:
        hp=gethp(i)
        max=getmaxhp(i)
        temp=int((hp/max)*100)
        if temp<35 and temp>0:
          playerdamage(str(getfpart(i)),20)
          moved=True
    if moved==False:
      ai=random.randint(1,6)
      if ai==1 and getaihp(0)>0:
        playerdamage("head",20)#add wepon and wepon damage
        moved=True
        ai=random.randint(1,6)
        moved=True
      if ai==2 and getaihp(1)>0:
        playerdamage("body",20)
        moved=True
      if ai==3 and getaihp(2)>0:
        playerdamage("larm",20)
        moved=True
      if ai==4 and getaihp(3)>0:
        playerdamage("rarm",20)
        moved=True
      if ai==5 and getaihp(4)>0:
        playerdamage("lleg",20)
        moved=True
      if ai==6 and getaihp(5)>0:
        playerdamage("rleg",20)
        moved=True
    if moved==False:
      aimove()



def playermove():
  hp()
  if checkaihp()==True:
    endgame()
  if checkaihp()!=True:
    print("where would you like to attack:")
    print("head, body, larm, rarm, lleg, rleg")
    option=str(input())
    option=option.lower()
    if option=="rule"or option=="rules":
      rules()
    try:
      aidamage("ai"+option,20)
    except:
      print("===================")
      print("invalid body part")
      print("try again")
      print("===================")
      playermove()
while True:
  while checkaihp()==False and checkhp()==False:
    #just testing some functions
    #playerdamage("head",20)
    #playerdamage("body",20)
    #playerdamage("larm",20)
    #playerdamage("rarm",20)
    #playerdamage("lleg",20)
    #playerdamage("rleg",20)
    #aidamage("aihead",20)
    #aidamage("aibody",20)
    #aidamage("ailleg",20)
    #aidamage("airleg",20)
    #aidamage("ailarm",20)
    #aidamage("airarm",20)
    playermove()
    aimove()

  #print(checkhp())
  #print(checkaihp())



  if checkaihp()==True or checkhp()==True:
    #displaydevhp()
    hp()
    time.sleep(3)
    restart()

