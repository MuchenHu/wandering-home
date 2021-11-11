import pgzrun
import random

names = [
    "trash1",
    "trash2",
    "trash3",
    "trash4",
    "trash5",
    "trash6",
    "trash7",
    "trash8",
    "trash9",
    "trash10",
    "trash11",
    "trash12",
    "trash13",
    "trash14",
    "trash15",
    "trash16",
    "trash17",
    "trash18",
]

# 保存正在下落的宝物
things = []

# 玩家、位置和得分初始化
player = Actor("astronaut2r")
player.pos = 90, 365
player.score = 0

# 游戏难度控制参数
player.timel = 300  # 游戏时间限制
player.scorelb = -10  # 第一关分数底线
player.scoregb = 8  # 第一关过关分数线
player.scorelc = -5  # 第二关分数底线
player.scoregc = 16  # 第二关过关分数线
player.scoreld = 0  # 第三关分数底线
player.scoregd = 24  # 第三关过关分数线
player.bchance = 120  # 第一关垃圾多少秒生成一个新垃圾
player.cchance = 45  # 第二关垃圾多少秒生成一个新垃圾
player.dchance = 30  # 第三关垃圾多少秒生成一个新垃圾
player.downvb = 2  # 第一关垃圾下落速度
player.downvc = 3  # 第二关垃圾下落速度
player.downvd = 5  # 第三关垃圾下落速度
player.missb = 2  # 第一关漏一个垃圾扣的分数
player.missc = 2  # 第二关漏一个垃圾扣的分数
player.missd = 2  # 第三关漏一个垃圾扣的分数
player.fetchb = 1  # 第一关捡到一个垃圾得到的分数
player.fetchc = 1  # 第二关捡到一个垃圾得到的分数
player.fetchd = 1  # 第三关捡到一个垃圾得到的分数

# 暂停游戏控制参数
player.pause = 0
# 背景音乐控制参数
player.ma = 0
player.mb = 0
player.mc = 0
player.md = 0
player.me = 0
# 开场动画
player.a1 = 1
player.a11 = 0
player.a12 = 0
player.a13 = 0
player.tip = 0
# 第一关
player.b = 0
player.cnt = 0  # 控制只能撕一次的参数，数值1也是进入下一关的一次性凭证
# 第二关
player.c = 0
player.cnt2 = 0
# 第三关
player.d = 0
player.cnt3 = 0
# 结尾动画
player.e = 0

# 设定窗口
WIDTH = 1300
HEIGHT = 842

# 按钮和星星
buttonal = Actor("buttonal")
buttonal.pos = 738, 200
buttonal.f1 = 0  # 注意这是第一关的标志物
buttonal.f2 = 0
buttonal.f3 = 0
player.l = 0
buttonal.pos = random.randrange(900), random.randrange(840)
star = Actor("star")
star.bottomleft = (WIDTH / 2, -50)
starsm = Actor("starsm")

# a1，开场动画第一幕
planet = Actor("planetbg_intro")
planet.center = 900, 550
planet.angle = 0
astronaut = Actor("astronaut2_intro")
astronaut.center = 790, 250
textbg = Actor("setbg_intro")
textbg.center = 340, 580
rose = Actor("rose_intro")
rose.center = 990, 250

# a2，开场动画第二幕
meteor = Actor("meteorbg")
meteor.center = 900, 60
astronaut2 = Actor("astronaut3_intro")
astronaut2.center = 1100, 430
textbg2 = Actor("setbg2_intro")
textbg2.center = 950, 350
ufo = Actor("ufo_intro")
ufo.center = 900, 700

# a3，开场动画第三幕
astronaut3 = Actor("astronaut_intro_s2")
astronaut3.center = 1100, 580
textbg3 = Actor("setbg3_intro")
textbg3.center = 450, 730
trash1 = Actor("trash6_intro")
trash1.center = 250, 150
trashmix = Actor("trashmix_intro")
trashmix.center = 800, 130
clean = Actor("clean_intro")
clean.center = 350, 160

# 游戏前提示
tipbefostart = Actor("game_start")
tipbefostart.pos = 650, 421

# b，第一关背景
bg1 = Actor("bg1")
bg1.pos = 375, 421
bg2 = Actor("bg2")
bg2.pos = 1120, 421
backup_bg = Actor("bg3")
backup_bg.pos = 1120, 421
obstacle1_1 = Actor("obstacle1_1")
obstacle1_1.pos = 1024, 290
obstacle1_2 = Actor("obstacle1_2")
obstacle1_2.pos = 1024, 1032

# c，第二关背景
bg2_1 = Actor("original_left")
bg2_1.pos = 800, 421
bg2_2 = Actor("original_right")
bg2_2.pos = 800, 421
obstacle2_1 = Actor("obstacle2_1")
obstacle2_1.pos = 840, 200
obstacle2_2 = Actor("obstacle2_2")
obstacle2_2.pos = 1024, 700

# d，第三关背景
bg3_1 = Actor("original_left3")
bg3_1.pos = 651, 421
bg3_2 = Actor("original_right3")
bg3_2.pos = 650, 421
obstacle3_1 = Actor("obstacle3_1")
obstacle3_1.pos = 1100, 210
obstacle3_2 = Actor("obstacle3_2")
obstacle3_2.pos = 860, 650

# e + fail，结尾动画（失败部分）
gameover_bg = Actor("gameover_bg")
gameover_bg.pos = 748, 421
gameover_text = Actor("gameover_text1")
gameover_text.pos = 650, 410
gameover_planet = Actor("gameover_planet")
gameover_planet.pos = 1042, 850
gameover_player = Actor("gameover_player")
gameover_player.pos = 1000, 300
gameover_home = Actor("gameover_home")
gameover_home.pos = 200, 200
gameover_star1 = Actor("star")
gameover_star1.pos = 280, 400
gameover_star2 = Actor("star")
gameover_star2.pos = 440, 200
gameover_star3 = Actor("star")
gameover_star3.pos = 570, 530
gameover_star4 = Actor("star")
gameover_star4.pos = 780, 260
gameover_star5 = Actor("star")
gameover_star5.pos = 1000, 380
scene_count = 0

# e + success，结尾动画（成功部分）
planet_win = Actor("planetbg_intro")
planet_win.center = 900, 550
planet_win.angle = 0
dec_win = Actor("dec")
dec_win.center = 890, 530
astronaut4 = Actor("astronaut_win")
astronaut4.center = 430, 280
bg_win = Actor("bg_win")
bg_win.pos = 650, 421
end_win = Actor("end_win")
end_win.center = 650, 421
text_win = Actor("text_win")
text_win.center = 330, 580
scene_countsuc = 0


# 每次需要刷新窗口的时候，会自动调用draw函数
def draw():
    if player.pause == 0:
        # 清除窗口，设置背景
        screen.clear()
        # 开场动画
        if player.a1 == 1:
            screen.blit("bg_intro", (0, 0))
            planet.draw()
            astronaut.draw()
            rose.draw()
            textbg.draw()
            sounds.buttonal.set_volume(0.5)

        if player.a1 == 2:
            screen.blit("bg2_intro", (0, 0))
            textbg2.draw()
            astronaut2.draw()
            meteor.draw()
            ufo.draw()

        if player.a1 == 3:
            screen.blit("bg3_intro", (0, 0))
            trashmix.draw()
            textbg3.draw()
            astronaut3.draw()
            trash1.draw()
            if astronaut3.image == "astronaut3_intro_s3":
                clean.draw()
            if player.tip:
                tipbefostart.draw()
        # 进入游戏关卡，依次为第一、二、三关场景搭建
        if player.b == 1:
            bg1.draw()
            backup_bg.draw()
            bg2.draw()
            obstacle1_1.draw()
            obstacle1_2.draw()
            # 画上太空垃圾和玩家
            for t in things:
                t.draw()
            player.draw()
            star.draw()
            # 写上通关分数(Goal)和目前的得分(Score)
            # 其中通关分数(Goal)是累计得分
            screen.draw.text(
                "Goal: 8   Score: %d   Lowest Score: -10" % player.score,
                (200, 10),
                fontname="pristina",
                fontsize=40,
                color="purple",
                gcolor="orange",
                owidth=0.5,
                ocolor="peachpuff2",
            )

        if player.c == 1:
            bg2_1.draw()
            bg2_2.draw()
            obstacle2_1.draw()
            obstacle2_2.draw()
            # 画上太空垃圾和玩家
            for t in things:
                t.draw()
            player.draw()
            star.draw()
            # 写上通关分数(Goal)和目前的得分(Score)
            screen.draw.text(
                "Goal: 16   Score: %d   Lowest Score: -5" % player.score,
                (200, 10),
                fontname="pristina",
                fontsize=40,
                color="burlywood",
                gcolor="steel blue",
                owidth=0.5,
                ocolor="ivory2",
            )

        if player.d == 1:
            bg3_1.draw()
            bg3_2.draw()
            obstacle3_1.draw()
            obstacle3_2.draw()
            # 画上太空垃圾和玩家
            for t in things:
                t.draw()
            player.draw()
            star.draw()
            # 写上通关分数(Goal)和目前的得分(Score)
            screen.draw.text(
                "Goal: 24   Score: %d   Lowest Score: 0" % player.score,
                (200, 10),
                fontname="pristina",
                fontsize=40,
                color="cornflower blue",
                gcolor="pale violet red",
                owidth=0.5,
                ocolor="lemon chiffon",
            )

        if player.b == 2:
            bg1.draw()
            backup_bg.draw()
            bg2.draw()
            obstacle1_1.draw()
            obstacle1_2.draw()
            # 画上太空垃圾和玩家
            for t in things:
                t.draw()
            player.draw()
            # 写上通关分数(Goal)和目前的得分(Score)
            screen.draw.text(
                "Goal: 8   Score: %d   Lowest Score: -10" % player.score,
                (200, 10),
                fontname="pristina",
                fontsize=40,
                color="purple",
                gcolor="orange",
                owidth=0.5,
                ocolor="peachpuff2",
            )
            # 当f=1时，隐藏的魔法按钮出现
            if buttonal.f1 == 1:
                buttonal.draw()
            if buttonal.f1 == 2:
                buttonal.draw()
                starsm.draw()
            star.draw()

        if player.c == 2:
            bg2_1.draw()
            bg2_2.draw()
            obstacle2_1.draw()
            obstacle2_2.draw()
            # 画上太空垃圾和玩家
            for t in things:
                t.draw()
            player.draw()
            # 写上通关分数(Goal)和目前的得分(Score)
            screen.draw.text(
                "Goal: 16   Score: %d   Lowest Score: -5" % player.score,
                (200, 10),
                fontname="pristina",
                fontsize=40,
                color="burlywood",
                gcolor="steel blue",
                owidth=0.5,
                ocolor="ivory2",
            )
            # 当f=1时，隐藏的魔法按钮出现
            if buttonal.f2 == 1:
                buttonal.draw()
            if buttonal.f2 == 2:
                buttonal.draw()
                starsm.draw()
            star.draw()

        if player.d == 2:
            bg3_1.draw()
            bg3_2.draw()
            obstacle3_1.draw()
            obstacle3_2.draw()
            # 画上太空垃圾和玩家
            for t in things:
                t.draw()
            player.draw()
            # 写上通关分数(Goal)和目前的得分(Score)
            screen.draw.text(
                "Goal: 24   Score: %d   Lowest Score: 0" % player.score,
                (200, 10),
                fontname="pristina",
                fontsize=40,
                color="cornflower blue",
                gcolor="pale violet red",
                owidth=0.5,
                ocolor="lemon chiffon",
            )
            # 当f=1时，隐藏的魔法按钮出现
            if buttonal.f3 == 1:
                buttonal.draw()
            if buttonal.f3 == 2:
                buttonal.draw()
                starsm.draw()
            star.draw()

        # 此时回收垃圾环节已经结束，不再显示分数
        if player.b == 3:
            bg1.draw()
            backup_bg.draw()
            bg2.draw()
            obstacle1_1.draw()
            obstacle1_2.draw()
            buttonal.draw()
            player.draw()

        if player.c == 3:
            bg2_1.draw()
            bg2_2.draw()
            obstacle2_1.draw()
            obstacle2_2.draw()
            buttonal.draw()
            player.draw()

        if player.d == 3:
            bg3_1.draw()
            bg3_2.draw()
            obstacle3_1.draw()
            obstacle3_2.draw()
            buttonal.draw()
            player.draw()

        # 未能通关（失败的结束动画场景搭建）
        if player.e == 1 and player.score < player.scoregd:
            gameover_bg.draw()
            gameover_text.draw()
            if scene_count == 2:
                gameover_planet.draw()
                gameover_player.draw()
                gameover_home.draw()
            if scene_count >= 3:
                gameover_star1.draw()
                gameover_star2.draw()
                gameover_star3.draw()
                gameover_star4.draw()
                gameover_star5.draw()
       
        # 成功通关（成功的结束动画场景搭建）
        if player.e == 1 and player.score >= player.scoregd:
            bg_win.draw()
            planet_win.draw()
            astronaut4.draw()
            if scene_countsuc == 1:
                dec_win.draw()
                text_win.draw()
            if scene_countsuc >= 2:
                end_win.draw()


# 每一帧都会自动调用update函数
def update():
    # 判断玩家是否暂停
    if player.pause == 0:
        # 控制背景音乐播放
        if player.a1 == 1 and player.ma == 0:
            player.ma += 1
            music.play("guitar")
        if player.b == 1 and player.mb == 0:
            player.mb += 1
            music.stop()
            music.play("trashcolle_bgm_1")
        if player.b == 2:
            music.stop()
        if player.c == 1 and player.mc == 0:
            player.mc += 1
            music.stop()
            music.play("trashcolle_bgm_2")
        if player.c == 2:
            music.stop()
        if player.d == 1 and player.md == 0:
            player.md += 1
            music.stop()
            music.play("trashcolle_bgm_3")
        if player.d == 2:
            music.stop()
        if player.e == 1 and player.score < player.scoregd and player.me == 0:
            player.me += 1
            music.play("gameover")
        if player.e == 1 and player.score >= player.scoregd and player.me == 0:
            player.me += 1
            music.play("ending")

        # 失败条件
        if player.e == 1:
            player.a = 0
            player.b = 0
            player.c = 0
            player.d = 0
            sounds.buttonal.stop()
            sounds.combine.stop()
            sounds.split.stop()
        if player.b == 1 and player.score < player.scorelb:
            player.e = 1
        if player.c == 1 and player.score < player.scorelc:
            player.e = 1
        if player.d == 1 and player.score < player.scoreld:
            player.e = 1
        if player.e == 0:
            clock.schedule(timefailure, player.timel)

        # 判断宇航员是否碰到障碍
        player.ob = [
            obstacle1_1,
            obstacle1_2,
            obstacle2_1,
            obstacle2_2,
            obstacle3_1,
            obstacle3_2,
        ]
        if player.b and (
            player.colliderect(player.ob[0]) or player.colliderect(player.ob[1])
        ):
            player.l = 0
            player.x -= 5
        if player.c and (
            player.colliderect(player.ob[2]) or player.colliderect(player.ob[3])
        ):
            player.l = 0
            player.x -= 5
        if player.d and (
            player.colliderect(player.ob[4]) or player.colliderect(player.ob[5])
        ):
            player.l = 0
            player.x -= 5
        
        # 开场动画第一幕：宇航员浮动状态 + 星球的转动状态
        if player.a1 == 1:
            planet.angle += 0.2
            if planet.angle > 360:
                planet.anlge = 0
            if astronaut.x <= WIDTH - 510 and astronaut.y <= HEIGHT - 590:
                animate(
                    astronaut,
                    tween="linear",
                    duration=2.0,
                    x=WIDTH - 480,
                    y=HEIGHT - 530,
                )
            if astronaut.x >= WIDTH - 490 and astronaut.y <= HEIGHT - 540:
                animate(
                    astronaut,
                    tween="linear",
                    duration=2.0,
                    x=WIDTH - 520,
                    y=HEIGHT - 600,
                )
        
        # 开场动画第二幕：宇航员浮动前进 + 流行划过 + 飞船浮动
        if player.a1 == 2:
            if astronaut2.y <= HEIGHT - 410:
                animate(astronaut2, tween="linear", duration=1.5, y=HEIGHT - 370)
            if astronaut2.y >= HEIGHT - 380:
                animate(astronaut2, tween="linear", duration=1.5, y=HEIGHT - 420)
            if astronaut2.left >= 50:
                astronaut2.left -= 2
            else:
                astronaut2.left -= 0
            animate(meteor, pos=(0, 1000), tween="accelerate", duration=0.2)
            if ufo.y <= HEIGHT - 140:
                animate(ufo, tween="linear", duration=1.5, y=HEIGHT - 110)
            if ufo.y >= HEIGHT - 120:
                animate(ufo, tween="linear", duration=1.5, y=HEIGHT - 150)
        
        # 开场动画第三幕
        if player.a1 == 3:
            # 宇航员的运动
            if astronaut3.y <= HEIGHT - 360:
                animate(astronaut3, tween="linear", duration=1.5, y=HEIGHT - 330)
            if astronaut3.y >= HEIGHT - 350:
                animate(astronaut3, tween="linear", duration=1.5, y=HEIGHT - 370)
            if astronaut3.left >= 50:
                astronaut3.left -= 2.5
            else:
                astronaut3.left -= 0
                astronaut3.image = "astronaut3_intro_s3"
                player.a13 = 1
            # 太空垃圾的转动
            trash1.angle += 0.4
            if trash1.angle > 360:
                trash1.anlge = 0
            if trash1.x <= WIDTH - 1045 and trash1.y <= HEIGHT - 690:
                animate(
                    trash1, tween="linear", duration=2.0, x=WIDTH - 990, y=HEIGHT - 630
                )
            if trash1.x >= WIDTH - 1000 and trash1.y <= HEIGHT - 640:
                animate(
                    trash1, tween="linear", duration=2.0, x=WIDTH - 1025, y=HEIGHT - 670
                )
            trashmix.angle += 0.4
            if trashmix.angle > 360:
                trashmix.anlge = 0
            if trashmix.y <= HEIGHT - 690:
                animate(trashmix, tween="linear", duration=2.0, y=HEIGHT - 630)
            if trashmix.y <= HEIGHT - 640:
                animate(trashmix, tween="linear", duration=2.0, y=HEIGHT - 670)
            if trashmix.left >= 250:
                trashmix.left -= 1.5
            else:
                trashmix.left -= 0
        
        # 游戏关卡中宇航员的浮动
        if player.b or player.c or player.d:
            if player.y <= 410:
                animate(player, tween="linear", duration=1.5, y=435)
            if player.y >= 430:
                animate(player, tween="linear", duration=1.5, y=405)
        
        # 第一关回收垃圾
        if player.b == 1:
            # 平均每秒随机生成一个太空垃圾加入到things列表里
            if random.randrange(player.bchance) == 0:
                # 垃圾下落位置随机
                t = Actor(random.choice(names))
                t.center = random.randrange(776), 0
                things.append(t)
            for t in things:
                # 下降4个像素，可以调节速度
                t.y += player.downvb
                # 如果超出底线，说明没接住，玩家扣分，同时从列表中删除垃圾
                if t.y >= HEIGHT:
                    things.remove(t)
                    player.score -= player.missb
                # 判断是否被玩家接到了
                elif t.colliderect(player):
                    # 玩家接住，加分
                    things.remove(t)
                    player.score += player.fetchb
                    sounds.buttonal1f.play(1)
                # 回收垃圾时不播放寻找魔法按钮的声音
                sounds.buttonal.set_volume(0)

        # 第二关回收垃圾
        if player.c == 1:
            # 平均每秒随机生成一个太空垃圾加入到things列表里
            if random.randrange(player.cchance) == 0:
                # 垃圾下落位置随机
                t = Actor(random.choice(names))
                t.center = random.randrange(636), 0
                things.append(t)
            for t in things:
                # 下降4个像素，可以调节速度
                t.y += player.downvc
                # 如果超出底线，说明没接住，玩家扣分，同时从列表中删除垃圾
                if t.y >= HEIGHT:
                    things.remove(t)
                    player.score -= player.missc
                # 判断是否被玩家接到了
                elif t.colliderect(player):
                    # 玩家接住，加分
                    things.remove(t)
                    player.score += player.fetchc
                    sounds.buttonal1f.play(1)
                # 回收垃圾时不播放寻找魔法按钮的声音
                sounds.buttonal.set_volume(0)

        # 第三关回收垃圾
        if player.d == 1:
            # 平均每秒随机生成一个太空垃圾加入到things列表里
            if random.randrange(player.dchance) == 0:
                # 垃圾下落位置随机
                t = Actor(random.choice(names))
                t.center = random.randrange(656), 0
                things.append(t)
            for t in things:
                # 下降4个像素，可以调节速度
                t.y += player.downvd
                # 如果超出底线，说明没接住，玩家扣分，同时从列表中删除垃圾
                if t.y >= HEIGHT:
                    things.remove(t)
                    player.score -= player.missd
                # 判断是否被玩家接到了
                elif t.colliderect(player):
                    # 玩家接住，加分
                    things.remove(t)
                    player.score += player.fetchd
                    sounds.buttonal1f.play(1)
                # 回收垃圾时不播放寻找魔法按钮的声音
                sounds.buttonal.set_volume(0)

        # update()全局通用，宇航员不可后退到屏幕外
        if player.left <= -15:
            player.left += 6
            player.l = 0

        # 控制player
        if player.left > WIDTH and player.cnt == 1:
            player.left = 6
            player.cnt = 0
            player.b = 0
            player.c = 1
            buttonal.pos = random.randrange(900), random.randrange(840)
        if player.left > WIDTH and player.cnt2 == 1:
            player.left = 6
            player.cnt2 = 0
            player.c = 0
            player.d = 1
            buttonal.pos = random.randrange(900), random.randrange(840)
        if player.left > WIDTH and player.cnt3 == 1:
            player.left = 6
            player.cnt3 = 0
            player.d = 0
            player.e = 1
            buttonal.pos = random.randrange(900), random.randrange(840)
        player.left += player.l
       
        # 不断更新播放声音的大小
        if player.b == 2:
            if buttonal.f1 == 0:
                sounds.buttonal.play()
        if player.c == 2:
            if buttonal.f2 == 0:
                sounds.buttonal.play()
        if player.d == 2:
            if buttonal.f3 == 0:
                sounds.buttonal.play()
            
        # 收集够垃圾，进入本关卡找按钮阶段
        if player.b == 1 and player.score >= player.scoregb:
            player.b = 2
            things.clear()
        if player.c == 1 and player.score >= player.scoregc:
            player.c = 2
            things.clear()
        if player.d == 1 and player.score >= player.scoregd:
            player.d = 2
            things.clear()

        # 结束动画
        # 失败部分
        if player.e == 1 and player.score < player.scoregd:
            gameover_planet.angle += 0.5
            gameover_star1.angle += 0.5
            gameover_star2.angle += 0.5
            gameover_star3.angle += 0.5
            gameover_star4.angle += 0.5
            gameover_star5.angle += 0.5
        # 成功部分
        if player.e == 1 and player.score >= player.scoregd:
            planet_win.angle += 0.2
            if planet_win.angle > 360:
                planet_win.anlge = 0
            if astronaut4.y <= HEIGHT - 560:
                animate(astronaut4, tween="linear", duration=1.5, y=HEIGHT - 530)
            if astronaut4.y >= HEIGHT - 550:
                animate(astronaut4, tween="linear", duration=1.5, y=HEIGHT - 570)
            if astronaut4.left <= 600:
                astronaut4.left += 1.5
            else:
                astronaut4.left -= 0
                astronaut4.image = "astronaut2_win"


# 开始动画用到的函数
def set_text():
    textbg.image = "settext_intro"
    player.a11 = 1

def set_text2():
    textbg2.image = "settext2_intro"
    player.a12 = 1

def set_text3():
    textbg3.image = "settext3_intro"


# 空间撕裂函数
# 第一关
def bgsplit1():
    # 左右图片都更换为撕开后的，包括back_bg
    bg1.image = "bg_left"
    bg2.image = "bg_right"
    backup_bg.image = "bg_right"
    # 撕开
    sounds.split.play()
    backup_bg.left += 20
    bg2.left += 20
    obstacle1_1.left += 20
    obstacle1_2.left += 20
    clock.schedule_unique(bgsplit2, 0.5)

def bgsplit2():
    bg2.top -= 240
    obstacle1_1.top -= 240
    obstacle1_2.top -= 240
    clock.schedule_unique(bgsplit3, 0.5)

def bgsplit3():
    sounds.combine.play()
    bg2.left -= 20
    backup_bg.left -= 20
    obstacle1_1.left -= 20
    obstacle1_2.left -= 20

# 第二关
def bgsplit2_1():
    # 左右图片都更换为撕开后的，包括back_bg
    bg2_1.image = "left"
    bg2_2.image = "right"
    # 撕开
    sounds.split.play()
    bg2_1.left -= 20
    bg2_2.left += 20
    obstacle2_1.left -= 20
    obstacle2_2.left += 20
    clock.schedule_unique(bgsplit2_2, 0.5)

def bgsplit2_2():
    animate(bg2_1, tween="linear", duration=0.5, x=800 - 20 + 70, y=421 - 80)
    animate(obstacle2_1, tween="linear", duration=0.5, x=840 - 20 + 70, y=200 - 100)
    animate(bg2_2, tween="linear", duration=0.5, x=800 + 20 - 70, y=421 + 80)
    animate(obstacle2_2, tween="linear", duration=0.5, x=1024 + 20 - 70, y=650 + 150)
    clock.schedule_unique(bgsplit2_3, 0.5)

def bgsplit2_3():
    sounds.combine.play()
    bg2_1.left += 20
    bg2_2.left -= 20
    obstacle2_1.left += 20
    obstacle2_2.left -= 20


# 第三关
def bgsplit3_1():
    # 左右图片都更换为撕开后的，包括back_bg
    bg3_1.image = "left3"
    bg3_2.image = "right3"
    # 撕开
    sounds.split.play()
    bg3_1.left -= 20
    bg3_2.left += 20
    obstacle3_1.left += 20
    obstacle3_2.left -= 20
    clock.schedule_unique(bgsplit3_2, 0.5)

def bgsplit3_2():
    animate(bg3_1, tween="linear", duration=0.5, x=651 - 20 + 70, y=421 + 80)
    animate(obstacle3_1, tween="linear", duration=0.5, x=1100 + 20 - 70, y=200 - 90)
    animate(bg3_2, tween="linear", duration=0.5, x=650 + 20 - 70, y=421 - 80)
    animate(obstacle3_2, tween="linear", duration=0.5, x=820 - 20 + 70, y=580 + 180)
    clock.schedule_unique(bgsplit3_3, 0.5)

def bgsplit3_3():
    sounds.combine.play()
    bg3_1.left += 20
    bg3_2.left -= 20
    obstacle3_1.left -= 20
    obstacle3_2.left += 20


# 结束动画（失败部分）用到的函数
def change_scene1():
    gameover_home.image = "gameover_nohome"
    clock.schedule_unique(change_scene2, 0.5)

def change_scene2():
    gameover_home.image = "gameover_rose"


# 超时导致失败
def timefailure():
    player.e = 1
    sounds.buttonal.stop()
    sounds.combine.stop()
    sounds.split.stop()


# 得到两点间的距离
def get_distance(pos1, pos2):
    dis = (((pos1[0] - pos2[0]) ** 2) + ((pos1[1] - pos2[1]) ** 2)) ** (0.5)
    return dis


# 键盘控制宇航员运动
def on_key_down(key):
    if key == key.P and (player.pause == 0 or player.pause == 1):
        player.pause += 1
    if key == key.P and player.pause == 2:
        player.pause = 0

    if player.a1 == 1:
        set_text()
    if player.b or player.c or player.d:
        if key == key.A:
            player.l = -5
            player.image = "astronaut2l"
        elif key == key.D:
            player.l = 5
            player.image = "astronaut2r"
        elif key == key.S:
            player.l = 0


# 移动鼠标寻找魔法按钮
def on_mouse_move(pos):
    dis = get_distance(buttonal.pos, pos)
    if player.b == 2 or player.c == 2 or player.d == 2:
        if dis >= 900:
            sounds.buttonal.set_volume(0.05)
        elif 700 <= dis < 900:
            sounds.buttonal.set_volume(0.1)
        elif 500 <= dis < 700:
            sounds.buttonal.set_volume(0.2)
        elif 400 <= dis < 500:
            sounds.buttonal.set_volume(0.3)
        elif 300 <= dis < 400:
            sounds.buttonal.set_volume(0.4)
        elif 200 <= dis < 300:
            sounds.buttonal.set_volume(0.55)
        elif 100 <= dis < 200:
            sounds.buttonal.set_volume(0.75)
        elif 50 <= dis < 100:
            sounds.buttonal.set_volume(0.95)
        elif 0 <= dis < 50:
            sounds.buttonal.set_volume(1)


# 点击鼠标所触发的一系列操作
def on_mouse_down(pos, button):
    # 场景切换
    if player.e == 1 and player.score < player.scoregd:
        global scene_count
        if gameover_bg.collidepoint(pos):
            scene_count += 1
            if scene_count == 1:
                gameover_text.image = "gameover_text2"
            elif scene_count == 2:
                gameover_text.image = "gameover_text3"
                clock.schedule_unique(change_scene1, 1)
            else:
                gameover_text.image = "theend"
    if player.e == 1 and player.score >= player.scoregd:
        global scene_countsuc
        if bg_win.collidepoint(pos):
            scene_countsuc += 1
    # 寻找按钮
    dis = get_distance(buttonal.pos, pos)
    if buttonal.f3 == 2:
        player.d = 3
        buttonal.f3 = 0
    if buttonal.f2 == 2:
        player.c = 3
        buttonal.f2 = 0
    if buttonal.f1 == 2:
        player.b = 3
        buttonal.f1 = 0
    # 游戏规则说明
    if player.a13 == 1 and player.tip == 7:
        player.a1 = 0
        player.a13 = 0
        player.b = 1
        player.tip = -1
    if player.a13 == 1 and player.tip == 6:
        player.tip = 7
        tipbefostart.image = "game_rule6"
    if player.a13 == 1 and player.tip == 5:
        player.tip = 6
        tipbefostart.image = "game_rule5"
    if player.a13 == 1 and player.tip == 4:
        player.tip = 5
        tipbefostart.image = "game_rule4"
    if player.a13 == 1 and player.tip == 3:
        player.tip = 4
        tipbefostart.image = "game_rule3"
    if player.a13 == 1 and player.tip == 2:
        player.tip = 3
        tipbefostart.image = "game_rule2"
    if player.a13 == 1 and player.tip == 1 and tipbefostart.collidepoint(pos):
        player.tip = 2
        tipbefostart.image = "game_rule1"
    if player.a13 == 1 and player.tip == 0:
        textbg3.image = "nothing"
        player.tip = 1
    # 开场动画切换
    if player.a12 == 1:
        player.a1 = 3
        player.a12 = 0
        set_text3()
    if player.a1 == 2:
        set_text2()
        astronaut2.image = "astronaut_intro_s2"
    if player.a11 == 1:
        player.a1 = 2
        player.a11 = 0
    if player.a1 == 1:
        set_text()
    # 寻找到按钮后的星星动画
    if player.b == 2:
        if buttonal.f1 == 1:
            animate(star, tween="bounce_end", duration=4.5, pos=buttonal.pos)
            starsm.pos = player.pos
            sounds.biubiu.play(1)
            buttonal.f1 = 2
            animate(starsm, tween="bounce_end", duration=3.5, pos=buttonal.pos)
        if 0 <= dis <= 100 and button == mouse.LEFT and buttonal.f1 == 0:
            buttonal.f1 = 1
    if player.c == 2:
        if buttonal.f2 == 1:
            animate(star, tween="bounce_end", duration=4.5, pos=buttonal.pos)
            starsm.pos = player.pos
            sounds.biubiu.play(1)
            buttonal.f2 = 2
            animate(starsm, tween="bounce_end", duration=3.5, pos=buttonal.pos)
        if 0 <= dis <= 100 and button == mouse.LEFT and buttonal.f2 == 0:
            buttonal.f2 = 1
    if player.d == 2:
        if buttonal.f3 == 1:
            animate(star, tween="bounce_end", duration=4.5, pos=buttonal.pos)
            starsm.pos = player.pos
            sounds.biubiu.play(1)
            buttonal.f3 = 2
            animate(starsm, tween="bounce_end", duration=3.5, pos=buttonal.pos)
        if 0 <= dis <= 100 and button == mouse.LEFT and buttonal.f3 == 0:
            buttonal.f3 = 1
    # 点击按钮触发撕裂
    if player.b == 3:
        if buttonal.collidepoint(pos) and player.cnt == 0:
            player.cnt += 1
            bgsplit1()
    if player.c == 3:
        if buttonal.collidepoint(pos) and player.cnt2 == 0:
            player.cnt2 += 1
            bgsplit2_1()
    if player.d == 3:
        if buttonal.collidepoint(pos) and player.cnt3 == 0:
            player.cnt3 += 1
            bgsplit3_1()


pgzrun.go()
