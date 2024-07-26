import pygame
import random
import mysql.connector
import tkinter as tk
import ttkbootstrap as ttk

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 50
PLAYER_SPEED = 5
OBSTACLE_SPEED = 2

# Initialize Pygame
pygame.init()

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dodger")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Player
player_x = (SCREEN_WIDTH - PLAYER_WIDTH) // 2
player_y = SCREEN_HEIGHT - PLAYER_HEIGHT

# Obstacles
obstacles = []
obstacle_spawn_timer = 100  # Adjust this for obstacle spawn rate

# Score
score = 0

# tkinter window for player name input
root = tk.Tk()
root.title("Enter Your Name")

player_name = ""

def get_player_name():
    global player_name
    player_name = name_entry.get()
    root.destroy()

label = tk.Label(root, text="Enter your name:")
label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

submit_button = tk.Button(root, text="Submit", command=get_player_name)
submit_button.pack()

root.mainloop()

# Define the reset_game function
def reset_game():
    global player_x, player_y, obstacles, score, game_over
    player_x = (SCREEN_WIDTH - PLAYER_WIDTH) // 2
    player_y = SCREEN_HEIGHT - PLAYER_HEIGHT
    obstacles = []
    score = 0
    game_over = False

# Function to exit the game
def exit_game():
    pygame.quit()
    quit()

# Load and display game instructions from a text file
def load_instructions(filename):
    try:
        with open(filename, 'r') as file:
            instructions = file.read()
        return instructions
    except FileNotFoundError:
        print("Instructions file not found.")
        return ""

instructions = load_instructions("instructions.txt")

#function to load and display instructions
def display_instructions():
    instructions = load_instructions("instructions.txt")  # Load instructions from the file
    instructions_window=Tk()
    instructions_window.title("Instructions")
    frame_instructions=Frame(instructions_window)
    frame_instructions.pack()
    label_instructions=Label(frame_instructions,text=instructions)
    label_instructions.pack()
    instructions_window.mainloop()

##    font = pygame.font.Font(None, 24)
##    text = font.render(instructions, True, (0, 0, 0))
##    screen.blit(text, (10, 100))  # Adjust the position where the instructions are displayed

instructions_displayed = False

# Database connection
def create_connection():
    try:
        connection = mysql.connector.connect(host="localhost",user="root",password="root",database="XIIB1")
        return connection
    except mysql.connector.Error as e:
        print("Error:", e)
        return None

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS scores (id INT AUTO_INCREMENT PRIMARY KEY, score INT)")
    connection.commit()

def insert_score(connection, score):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO scores (score) VALUES (%s)", (score,))
    connection.commit()

# Game loop
running = True
game_over = False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:  # Press "Q" to exit the game
                exit_game()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - PLAYER_WIDTH:
        player_x += PLAYER_SPEED

    if not instructions_displayed:
        display_instructions()
        instructions_displayed = True

    # Spawn obstacles
    if obstacle_spawn_timer <= 0:
        obstacle_x = random.randint(0, SCREEN_WIDTH - OBSTACLE_WIDTH)
        obstacles.append([obstacle_x, 0])
        obstacle_spawn_timer = 100  # Reset the timer
    else:
        obstacle_spawn_timer -= 1

    # Move obstacles
    new_obstacles = []
    for obstacle in obstacles:
        obstacle[1] += OBSTACLE_SPEED
        if obstacle[1] < SCREEN_HEIGHT:
            new_obstacles.append(obstacle)
        else:
            score += 1
    obstacles = new_obstacles

    # Check collision
    for obstacle in obstacles:
        if player_x + PLAYER_WIDTH > obstacle[0] and player_x < obstacle[0] + OBSTACLE_WIDTH and player_y + PLAYER_HEIGHT > obstacle[1] and player_y < obstacle[1] + OBSTACLE_HEIGHT:
            game_over = True

    # Check if the player wants to start a new game
    if game_over:
        if keys[pygame.K_r]:  # For example, you can use the "R" key to start a new game
            reset_game()  # Call the reset_game function to reset the game

    # Clear the screen
    screen.fill(WHITE)

    # Draw player
    pygame.draw.rect(screen, RED, (player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT))

    # Draw obstacles
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, (obstacle[0], obstacle[1], OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)

    if game_over:
        # Insert score into the database
        connection = create_connection()
        if connection:
            create_table(connection)
            insert_score(connection, score)
            connection.close()

        # Game over screen
        font = pygame.font.Font(None, 72)
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2 - 50))
        pygame.display.update()
        pygame.time.delay(2000)  # Display game over message for 2 seconds
        game_over = False
        obstacles = []
        player_x = (SCREEN_WIDTH - PLAYER_WIDTH) // 2
        player_y = SCREEN_HEIGHT - PLAYER_HEIGHT
        score = 0

pygame.quit()
