
import pygame

# Initialize pygame and create window
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ping Pong")

# Load images for the ball and paddles
ball_image = pygame.image.load("ball.png")
paddle1_image = pygame.image.load("paddle1.png")
paddle2_image = pygame.image.load("paddle2.png")

# Create rectangles for the ball and paddles
ball = ball_image.get_rect()
paddle1 = paddle1_image.get_rect()
paddle2 = paddle2_image.get_rect()

# Initial position for the ball and paddles
ball.center = (350, 250)
paddle1.center = (50, 250)
paddle2.center = (650, 250)

# Speed of the ball (x, y)
ball_speed = [5, 5]

# Speed of the paddles (x, y)
paddle1_speed = [0, 5]
paddle2_speed = [0, 5]

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        paddle1.y -= paddle1_speed[1]
    if keys[pygame.K_DOWN]:
        paddle1.y += paddle1_speed[1]
    if keys[pygame.K_w]:
        paddle2.y -= paddle2_speed[1]
    if keys[pygame.K_s]:
        paddle2.y += paddle2_speed[1]

    # Keep the paddles inside the window
    if paddle1.y < 0:
        paddle1.y = 0
    if paddle1.y > 400:
        paddle1.y = 400
    if paddle2.y < 0:
        paddle2.y = 0
    if paddle2.y > 400:
        paddle2.y = 400

    # Move the ball
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Check for collisions with the window edges
    if ball.left < 0 or ball.right > 700:
        ball_speed[0] = -ball_speed[0]
    if ball.top < 0 or ball.bottom > 500:
        ball_speed[1] = -ball_speed[1]

    # Check for collisions with the paddles
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed[0] = -ball_speed[0]

    # Draw everything on the screen
    screen.fill((0, 0, 0))
    screen.blit(ball_image, ball)
    screen.blit(paddle1_image, paddle1)
    screen.blit(paddle2_image, paddle2)
    pygame.display.flip()

# Stop pygame and exit the program
pygame.quit()
