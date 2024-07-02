
import pygame

pygame.init()


Win_size = 800
screen = pygame.display.set_mode((Win_size, Win_size))
pygame.display.set_caption("PingPong")
weiss = (255, 255, 255)
yposition_one = 300
yposition_two = 300
ball_speed_x = 7
ball_speed_y = 7
ball_position_x = 400
ball_position_y = 350
ball_radius = 25
schriftart = pygame.font.SysFont("Arial", 45)
score_one = 0
score_two = 0
clock = pygame.time.Clock()
ball_image = pygame.image.load("360_F_213338964_UxvKyZZINlNBO8VhfbjnyZuXK7tn3qiO-removebg-preview.png")
ball_image = pygame.transform.scale(ball_image, (89, 70))
backround_image = pygame.image.load("9a906af8741da53f2a945bb1f1250338_der-verkauf-des-grundstuecks-des-volksparkstadions-bringt-dem-hsv-235-millionen-euro-ein.jpg")
backround_image = pygame.transform.scale(backround_image,  (800, 800))
screen.blit(backround_image, (0, 0))
Tor = pygame.mixer.Sound("hsv-torhymne.mp3")
Tor.set_volume(0.1)
Tor_2 = pygame.mixer.Sound("vollig-losgelost_5GLukLJ.mp3")
Tor_2.set_volume(0.1)
wirtz = pygame.image.load("florian-wirtz-bei-deutschland-spiel-getty-removebg-preview.png")
wirtz = pygame.transform.scale(wirtz, (50, 150))
glatzel = pygame.image.load("195115-removebg-preview.png")
glatzel = pygame.transform.scale(glatzel, (50, 150))





def steuerung(yposition_one, yposition_two, boddy_one, boddy_two):
    keys = pygame.key.get_pressed()
    if boddy_one.colliderect(line_top):  #Wenn boddy one or two mit der oberen oder unteren linie kollidiert dann wird die position zurückgesetzt
        yposition_one = 0
    if boddy_one.colliderect(line_bottom):
        yposition_one = 640
    if boddy_two.colliderect(line_top):
        yposition_two = 0
    if boddy_two.colliderect(line_bottom):
        yposition_two = 640


    if keys[pygame.K_s]:
        yposition_one += 10
    if keys[pygame.K_w]:
        yposition_one -= 10
    if keys[pygame.K_UP]:
        yposition_two -= 10
    if keys[pygame.K_DOWN]:
        yposition_two += 10







    return yposition_one, yposition_two #werden aktualisiert zurückgeben

def gravity_ball(score_one, score_two, boddy_one, boddy_two):
    global ball_position_x, ball_position_y, ball_speed_x, ball_speed_y, ball_radius
    ball_position_x += ball_speed_x
    ball_position_y += ball_speed_y

    if ball_position_x - ball_radius <= 0:
        ball_position_x = 400
        ball_position_y = 350
        ball_speed_x = 7
        ball_speed_y = 7
        score_two += 1
        Tor.stop()
        Tor_2.stop()
        Tor.play(0)
    if ball_position_x + ball_radius >= Win_size:
        ball_position_x = 400
        ball_position_y = 350
        ball_speed_x = -ball_speed_x
        ball_speed_y = -ball_speed_y
        score_one += 1
        Tor.stop()
        Tor_2.stop()
        Tor_2.play(0)

    ball_rect = pygame.Rect(ball_position_x - ball_radius, ball_position_y - ball_radius, ball_radius * 2, ball_radius * 2) #Rechteck für ball, um collidieren zu können
    if ball_rect.colliderect(boddy_one) or ball_rect.colliderect(boddy_two): # ball kollidiert mit den körpern
        ball_speed_x = -ball_speed_x
    if ball_rect.colliderect(line_bottom) or ball_rect.colliderect(line_top): # ball kollidiert mit den linien (rechtecken)
        ball_speed_y = -ball_speed_y




    return score_one, score_two #werden aktualisiert zurückgeben





def draw_score(score_one, score_two):
    text_one = schriftart.render(f"Tore:{score_one}", True, (255, 0, 0))
    screen.blit(text_one, (640, 10))

    text_two = schriftart.render(f"Tore:{score_two}", True, (0, 0, 255))
    screen.blit(text_two, (10, 10))








run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    clock.tick(60)

    pygame.time.delay(22)

    screen.fill((0, 0, 0))

    boddy_one = pygame.draw.rect(screen, (weiss), (10, yposition_one, 50, 150)) # sind vorm hintergrund, damit man die blöcke nicht sieht
    boddy_two = pygame.draw.rect(screen, (weiss), (760, yposition_two, 50, 150))



    screen.blit(backround_image, (0, 0)) # hintergrund gezeichnet



    screen.blit(wirtz, (10, yposition_one)) # wirtz und glatzel gezeichnet
    screen.blit(glatzel, (760, yposition_two))
    line_left = pygame.draw.line(screen, (weiss), (0, 0), (0, 800), (2))
    line_right = pygame.draw.line(screen, (weiss), (798, 0), (798, 800), (2))
    line_top = pygame.draw.rect(screen, (weiss), (0, 1, 800, 2))
    line_bottom = pygame.draw.rect(screen, (weiss), (0, 798, 800, 2))
    ball = pygame.draw.circle(screen, (weiss), (ball_position_x, ball_position_y), ball_radius, 0, )
    screen.blit(ball_image, (ball_position_x - 43, ball_position_y - 35))

    yposition_one, yposition_two = steuerung(yposition_one, yposition_two, boddy_one, boddy_two)  # yposition_one und yposition_two werden der Funktion übergeben, damit sie aktualiesiert werden


    score_one, score_two = gravity_ball(score_one, score_two, boddy_one, boddy_two) #score_one und score_two werden der Funktion übergeben, damit sie aktualiesiert werden
    draw_score(score_two, score_one)





    pygame.display.update()


