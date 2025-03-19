import pygame

# initalize game
pygame.init()
clock = pygame.time.Clock()
running = True

# Caption
pygame.display.set_caption("Ping Pong Game")

# Screen dimensions
Width = 1280
Height = 720
screen = pygame.display.set_mode((Width, Height))

# ball position
#ball_pos = pygame.Vector2(Width /2, Height /2 )

###Initalize Objects

# Ball
ball_x = Width / 2
ball_y = Height / 2

ball_xspeed = 5
ball_yspeed = 5

## Paddles
Paddle_width = 10
Paddle_Height = 100

# 20 leftmost side of screen, (random height)
paddle1_x = 20
paddle1_y = Height / (Paddle_Height / 2) + 300

# 1280 - 30 = 1250 right side of screen, (random height)
paddle2_x = Width - 30
paddle2_y = Height / (Paddle_Height / 2) + 300

paddle_speed = 5

# Score
score1, score2 = 0, 0
font = pygame.font.Font(None, 38)

### Main loop
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #### Game Logic
    # Handle input
    keys = pygame.key.get_pressed()
    # LHS paddle
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= paddle_speed
    if keys[pygame.K_s] and paddle1_y < Height - Paddle_Height:
        paddle1_y += paddle_speed
    
    #RHS paddle
    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle2_y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle2_y < Height - Paddle_Height:
        paddle2_y += paddle_speed

    # Move ball
    ball_x += ball_xspeed
    ball_y += ball_yspeed

    # Ball collision with Top and bottom of screen
    if ball_y -15 <= 0 or ball_y + 15 >= Height: # either top (0) or bottom (Height) collision
        ball_yspeed = -ball_yspeed

    # Ball collision with paddles
    # check if the ball is in bounds
    if (paddle1_x -15 <= ball_x <= paddle1_x + Paddle_width +15 and
        paddle1_y -15 <= ball_y <= paddle1_y + Paddle_Height +15) or \
        (paddle2_x -15 <= ball_x <= paddle2_x + Paddle_width +15 and
        paddle2_y -15 <= ball_y <= paddle2_y + Paddle_Height +15):
        ball_xspeed = -ball_xspeed


    # Ball collision with Sides of screen
    if ball_x -15 <= 0 or ball_x + 15 >= Width:
        # Scoring, make sure you know which side the ball went out on to add the correct score
        if ball_x - 15<= 0: # exits left side
            score1 +=1
            ball_xspeed = -ball_xspeed
            ball_yspeed = -ball_yspeed
            ball_x = Width / 2
            ball_y = Height / 2
        elif ball_x +15 >= Width: # exits right side
            score2 += 1
            ball_xspeed = -ball_xspeed
            ball_yspeed = -ball_yspeed
            ball_x = Width / 2
            ball_y = Height / 2
    # Game render
    screen.fill("black")
    pygame.draw.circle(screen, "white", (ball_x, ball_y), 12)
    pygame.draw.rect(screen, "white", (paddle1_x, paddle1_y, Paddle_width, Paddle_Height), 10)
    pygame.draw.rect(screen, "white", (paddle2_x, paddle2_y, Paddle_width, Paddle_Height), 10)
    score_text = font.render(f"{score1} - {score2}", True, "white")
    screen.blit(score_text, (Width // 2 - score_text.get_width() // 2, 20))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS

pygame.quit()