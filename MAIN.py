import pygame, time, sys
from replit import audio
pygame.init()
screen = pygame.display.set_mode((620, 550))

#background music, might sound glitchy and slow down the program
#I recommand playing without music, as the game will load faster
#bg_music = audio.play_file("Nyan Cat.mp3")
#bg_music.set_loop(3)

def get_attacked(position, name, position_mon):
  #when the cats get too close to the monsters, we lose one life
  global life, attack
  attack = False
  if abs(position[0] - position_mon[0]) < 60 and abs(position[1] - position_mon[1]) < 60:
    attack = True
  if attack == True:
    life -= 1
    if life < 0:
      life = 0
    print(name, "was attacked by a monster :( Try again.", life, "life(s) left.")
    new_position = [0, 10]
    return new_position
  else:
    return position
    
def get_fish(positon1, position2):
  global fish_count
  if abs(position1[0] - position_fish[0]) < 50 and abs(position1[1] - position_fish[1]) < 50:
    fish_count += 1
  if abs(position2[0] - position_fish[0]) < 50 and abs(position2[1] - position_fish[1]) < 50:
    fish_count += 1
  if fish_count >= 2:
    return True
  else:
    fish_count = 0
    return False

basicfont = pygame.font.SysFont(None, 30)
def text_message_b(words, pos1, pos2):
  #text funtion, print text on screen, black text
  screen_text = basicfont.render(words, True, black)
  screen.blit(screen_text, [pos1, pos2])

#white text
def text_message_w(words, pos1, pos2):
  screen_text = basicfont.render(words, True, white)
  screen.blit(screen_text, [pos1, pos2])

#small text
def text_message_s(words, colour, pos1, pos2):
  basicfont = pygame.font.SysFont(None, 20)
  screen_text = basicfont.render(words, True, colour)
  screen.blit(screen_text, [pos1, pos2])

def move_cats():
  pressed_keys = pygame.key.get_pressed()
  if pressed_keys[pygame.K_a]:
    position1[0] -= 0.6
  if pressed_keys[pygame.K_d]:
    position1[0] += 0.6
  if pressed_keys[pygame.K_w]:
    position1[1] -= 0.6
  if pressed_keys[pygame.K_s]:
    position1[1] += 0.6
  if pressed_keys[pygame.K_LEFT]:
    position2[0] -= 0.6
  if pressed_keys[pygame.K_RIGHT]:
    position2[0] += 0.6
  if pressed_keys[pygame.K_UP]:
    position2[1] -= 0.6
  if pressed_keys[pygame.K_DOWN]:
    position2[1] += 0.6
  pygame.event.pump()

def show_life(life):
  #heart/life function
  heart = pygame.image.load("heart.png")
  heart = pygame.transform.scale(heart, (30, 30))
  #print one heart for each life left
  if life > 2:
    screen.blit(heart, (375,0))
  if life > 1:
    screen.blit(heart, (340,0))
  if life > 0:
    screen.blit(heart, (305,0)) 

def no_more_life():
  screen.fill(white)
  screen.blit(losing, (100, 150))
  text_message_b("Game over! no more lifes left.", 100, 80)
  text_message_b("To try again, press key 'r'", 100, 100)
  text_message_b("To quit, press escape", 100, 120)
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_r:
        reset_all()
      if event.key == pygame.K_ESCAPE:
        pygame.display.quit()
        sys.exit()

def no_more_time():
  screen.fill(white)
  screen.blit(losing, (100, 150))
  text_message_b("Game over! Time's up!", 100, 80)
  text_message_b("To try again, press key 'r'", 100, 100)
  text_message_b("To quit, press escape", 100, 120)
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_r:
        reset_all()
      if event.key == pygame.K_ESCAPE:
        pygame.display.quit()
        sys.exit()

#load monster
def monster_set(start_pos, speed, move):
  monster = pygame.image.load("monster.png")
  monster = pygame.transform.scale(monster, (80, 60))
  if "y" in move:
    if start_pos[1] < 350:
      start_pos[1] += 0.7
    else:
      start_pos[1] = 30
  if "x" in move:
    if start_pos[0] < 350:
      start_pos[0] += 0.7
    else:
      start_pos[0] = 30
  if "z" in move:
    if start_pos[1] < 350:
      start_pos[1] += 0.7
    else:
      start_pos[1] = 100
    if start_pos[0] < 350:
      start_pos[0] += 0.7
    else:
      start_pos[0] = 100
  screen.blit(monster, tuple(start_pos))

#reset game variables
def reset_all():
  global position1, position2, life, time_left, fish_count, start_time
  position1 = [0, 10]
  position2 = [0, 100]
  life = 3
  time_left = 1
  fish_count = 0
  start_time = time.time()

#exit game
def game_exit():
  for event in pygame.event.get(): 
    if event.type == pygame.KEYDOWN:       
      if event.key == pygame.K_ESCAPE:
        pygame.display.quit()
        sys.exit()

#loading and adjusting images
background = pygame.image.load("background.jpg")
fish = pygame.image.load("fish.png")
success = pygame.image.load("success.png")
losing = pygame.image.load("lose cat.png")
fish = pygame.transform.scale(fish, (150, 120))
success = pygame.transform.scale(success, (400, 400))
losing = pygame.transform.scale(losing, (200, 200))
losing = pygame.transform.rotate(losing, 22)

#variables set up:
pick_count = 0
choice = []
black = (0,0,0)
white = (255, 255, 255)
#starting positions
position1 = [0, 10]
position2 = [0, 100]
position_mon1 = [200, 30]
position_mon2 = [330, 250]
position_mon3 = [250, 300]
position_mon4 = [0, 180]
position_fish = [400, 300]
#life and time counting
life = 3
time_limit = 30
time_left = 1
fish_count = 0

class gamestage():
  def __init__(self):
    self.state = "intro"

  def stage_manager(self):
    if self.state == "intro":
      self.intro()
    if self.state == "instructions":
      self.instructions()
    if self.state == "level1":
      self.level1()
    if self.state == "level2":
      self.level2()
    if self.state == "level3":
      self.level3()

  def intro(self):
    screen.blit(background, (0,0))
    pygame.draw.rect(screen, (255, 255, 255), ((0, 0), (610, 120)))
    basicfont = pygame.font.SysFont(None, 50)
    title1 = basicfont.render("Lazy Cats", True, (0,225,225))
    title2 = basicfont.render("Lazy Cats", True, (0,0,25))
    screen.blit(title1, (200, 20))
    screen.blit(title2, (202, 22))
    text_message_b("Welcome! Pick TWO cats of your choice:  (press keyboard) " , 10, 80)
    pygame.draw.rect(screen, (255, 151, 33), ((100, 190), (150, 70)))
    text_message_b("Mimi" , 145, 210)
    text_message_s("Press key 'm' ", black, 145, 230)
    pygame.draw.rect(screen, (199, 199, 199), ((300, 190), (150, 70)))
    text_message_b("Lucy" , 350, 210)
    text_message_s("Press key 'l' ", black, 350, 230)
    pygame.draw.rect(screen, (61, 204, 255), ((100, 280), (150, 70)))
    text_message_b("Jackie" , 145, 300)
    text_message_s("Press key 'j' ", black, 145, 320)
    pygame.draw.rect(screen, (0, 0, 0), ((300, 280), (150, 70)))
    text_message_w("Ninja" , 350, 300)
    text_message_s("Press key 'n' ", white, 350, 320)

    mimi = pygame.image.load("mimi.png")
    lucy = pygame.image.load("lucy.png")
    jackie = pygame.image.load("jackie.png")
    ninja = pygame.image.load("ninja.png")
    mimi = pygame.transform.scale(mimi, (100, 75))
    lucy = pygame.transform.scale(lucy, (100, 75))
    jackie = pygame.transform.scale(jackie, (100, 75))
    ninja = pygame.transform.scale(ninja, (100, 75))
    screen.blit(mimi, (42, 190))
    screen.blit(lucy, (252, 190))
    screen.blit(jackie, (44, 280))
    screen.blit(ninja, (252, 280))

    global cat1_name, cat2_name, pick_count, choice, cat1, cat2
    cat1_name = ""
    cat2_name = ""
    for event in pygame.event.get(): 
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_m:
          choice.append ("mimi")
          pick_count += 1
        if event.key == pygame.K_l:
          choice.append ("lucy")
          pick_count += 1
        if event.key == pygame.K_j:
          choice.append ("jackie")
          pick_count += 1
        if event.key == pygame.K_n:
          choice.append ("ninja")
          pick_count += 1
    if pick_count >= 2:
      if choice[0] == "mimi":
        cat1_name = "mimi"
        cat1 = mimi
      elif choice[0] == "lucy":
        cat1_name = "lucy"
        cat1 = lucy
      elif choice[0] == "jackie":
        cat1_name = "jackie"
        cat1 = jackie
      elif choice[0] == "ninja":
        cat1_name = "ninja"
        cat1 = ninja
      if choice[1] == "mimi":
        cat2_name = "mimi"
        cat2 = mimi
      elif choice[1] == "lucy":
        cat2_name = "lucy"
        cat2 = lucy
      elif choice[1] == "jackie":
        cat2_name = "jackie"
        cat2 = jackie
      elif choice[1] == "ninja":
        cat2_name = "ninja"
        cat2 = ninja

    if cat1_name != "" and cat2_name != "":
      self.state = "instructions"

  def instructions(self):
    screen.fill(white)
    text_message_b("Instructions:" , 10, 10)
    text_message_b("Use 'asdw' to control "+ cat1_name, 100, 40)
    text_message_b("Use arrow keys to control "+ cat2_name , 100, 70)
    text_message_b("Get both cats to the fish before time runs out!" , 100, 100)
    text_message_b("Avoid monsters, they will hurt your cats." , 100, 130)
    text_message_b("When you are ready to start, press key 'y'", 100, 200)
    text_message_s("I dare you to beat all three levels...",black, 100, 230)
    text_message_b("To quit game, press 'escape'", 100, 300)
    
    for event in pygame.event.get(): 
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_y:
          self.state = "level1"
          global start_time
          start_time = time.time()
        if event.key == pygame.K_ESCAPE:
            pygame.display.quit()
            sys.exit()

  def level1(self):
    global cat1, cat2, cat1_name, cat2_name, fish, success, losing, life, time_limit, start_time, time_left, position1, position2, position_mon1, position_fish, fish_count

    #long pressing on keys to move cat sprites
    move_cats()
  
    #reset cat possition if attacked
    position1 = get_attacked(position1, cat1_name, position_mon1)
    position2 = get_attacked(position2, cat2_name, position_mon1)

    #time remaining calculations, use int no decimals
    passed_time = int(time.time() - start_time)
    if time_left != 0:
      time_left = time_limit - passed_time

    #situation for winning
    if get_fish(position1, position2) == True:
      #bg_music.paused
      #audio.play_file("yay.mp3") 
      screen.fill(white)
      screen.blit(success, (100, 20))
      text_message_b("To move on to the next level, press key 'y'", 100, 20)
      text_message_b("To quit, press key 'Escape'", 150, 420)
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_y:
            #reset variables, move to next level
            reset_all()
            self.state = "level2"
          if event.key == pygame.K_ESCAPE:
            pygame.display.quit()
            sys.exit()
      
    #situation for losing (dead or no time)
    elif life <= 0:
      no_more_life()
    elif time_left == 0:
      no_more_time()
  
    # Normal playing situation, recolour background, displays the sprites, display time and hearts 
    else:
      screen.blit(background, (0,0))
      monster_set(position_mon1, 0.7, "y")
      screen.blit(fish, tuple(position_fish))
      screen.blit(cat1, tuple(position1))
      screen.blit(cat2, tuple(position2))
      pygame.draw.rect(screen, (255, 151, 33), ((220, 0), (420, 35)))
      text_message_w("Level 1", 230, 10)
      text_message_b("Time Remaining: " +str(time_left), 416, 10)
      show_life(life)
    #exit game if press escape
    game_exit()

  def level2 (self):
    global cat1, cat2, cat1_name, cat2_name, fish, success, losing, life, time_limit, start_time, time_left, position1, position2, position_mon1, position_mon2, position_mon3, position_mon4, position_fish
    #function to move
    move_cats()

    #reset cat possition if attacked
    position1 = get_attacked(position1, cat1_name, position_mon1)
    position2 = get_attacked(position2, cat2_name, position_mon1)
    position1 = get_attacked(position1, cat1_name, position_mon2)
    position2 = get_attacked(position2, cat2_name, position_mon2)
    position1 = get_attacked(position1, cat1_name, position_mon3)
    position2 = get_attacked(position2, cat2_name, position_mon3)
    position1 = get_attacked(position1, cat1_name, position_mon4)
    position2 = get_attacked(position2, cat2_name, position_mon4)

    #time remaining calculations, use int no decimals
    passed_time = int(time.time() - start_time)
    if time_left != 0:
      time_left = time_limit - passed_time

    #situation for winning
    if get_fish(position1, position2) == True:
      screen.fill(white)
      screen.blit(success, (100, 20))
      text_message_b("To move on to the next level, press key 'y'", 100, 20)
      text_message_b("To quit, press key 'Escape'", 150, 420)
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_y:
            #reset variables, move to next level
            reset_all()
            self.state = "level3"
          if event.key == pygame.K_ESCAPE:
            pygame.display.quit()
            sys.exit()

    #situation for losing (dead or no time)
    elif life <= 0:
      no_more_life()
    elif time_left == 0:
      no_more_time()

    # Normal playing situation, recolour background, displays the sprites, display time and hearts 
    else:
      screen.blit(background, (0,0))
      monster_set(position_mon1, 2, "y")
      monster_set(position_mon2, 2, "y")
      monster_set(position_mon3, 2, "x")
      monster_set(position_mon4, 2, "x")
      screen.blit(fish, tuple(position_fish))
      screen.blit(cat1, tuple(position1))
      screen.blit(cat2, tuple(position2))
      pygame.draw.rect(screen, (255, 151, 33), ((220, 0), (420, 35)))
      text_message_w("Level 2", 230, 10)
      text_message_b("Time Remaining: " +str(time_left), 416, 10)
      show_life(life)

    game_exit()
  
  def level3 (self):
    global cat1, cat2, cat1_name, cat2_name, fish, success, losing, life, time_limit, start_time, time_left, position1, position2, position_mon1, position_mon2, position_mon3, position_mon4, position_fish
    #function to move
    move_cats()

    #reset cat possition if attacked
    position1 = get_attacked(position1, cat1_name, position_mon1)
    position2 = get_attacked(position2, cat2_name, position_mon1)
    position1 = get_attacked(position1, cat1_name, position_mon2)
    position2 = get_attacked(position2, cat2_name, position_mon2)
    position1 = get_attacked(position1, cat1_name, position_mon3)
    position2 = get_attacked(position2, cat2_name, position_mon3)
    position1 = get_attacked(position1, cat1_name, position_mon4)
    position2 = get_attacked(position2, cat2_name, position_mon4)

    #time remaining calculations, use int no decimals
    passed_time = int(time.time() - start_time)
    if time_left != 0:
      time_left = time_limit - passed_time

    #situation for winning
    if get_fish(position1, position2) == True:
      screen.fill(white)
      screen.blit(success, (100, 20))
      text_message_b("You have earned to Ultimate Victory  Badge!", 100, 20)
      text_message_b("To quit, press key 'Escape'", 150, 420)

    #situation for losing (dead or no time)
    elif life <= 0:
      no_more_life()
    elif time_left == 0:
      no_more_time()

    # Normal playing situation, recolour background, displays the sprites, display time and hearts 
    else:
      screen.blit(background, (0,0))
      monster_set(position_mon1, 2, "y")
      monster_set(position_mon2, 2, "z")
      monster_set(position_mon3, 2, "x")
      monster_set(position_mon4, 2, "z")
      screen.blit(fish, tuple(position_fish))
      screen.blit(cat1, tuple(position1))
      screen.blit(cat2, tuple(position2))
      pygame.draw.rect(screen, (255, 151, 33), ((220, 0), (420, 35)))
      text_message_w("Level 3", 230, 10)
      text_message_b("Time Remaining: " +str(time_left), 416, 10)
      show_life(life)

    game_exit()

game_stage = gamestage()

while True:  
  #go to stage class manager
  game_stage.stage_manager()
  #keeps the program running and updating
  pygame.display.update()
