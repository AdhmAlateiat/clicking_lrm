import tkinter as tk
import random

# Function to increase the score when the button is clicked
def increment_score():
    global score, click_multiplier
    score += 1 * click_multiplier
    score_label.config(text=f"Score: {score}")

# Function to buy a score multiplier upgrade
def buy_multiplier():
    global score, click_multiplier, multiplier_price
    if score >= multiplier_price:
        score -= multiplier_price
        click_multiplier += 1
        multiplier_price *= 2
        update_upgrade_labels()

# Function to buy an auto-clicker upgrade
def buy_auto_clicker():
    global score, auto_clickers, auto_clicker_price
    if score >= auto_clicker_price:
        score -= auto_clicker_price
        auto_clickers += 1
        auto_clicker_price *= 2
        update_upgrade_labels()
        auto_click()

# Function to update the upgrade labels
def update_upgrade_labels():
    multiplier_label.config(text=f"Score Multiplier x{click_multiplier} (Cost: {multiplier_price} points)")
    auto_clicker_label.config(text=f"Auto-Clickers x{auto_clickers} (Cost: {auto_clicker_price} points)")

# Function for auto-clickers to automatically click the button
def auto_click():
    increment_score()
    root.after(auto_clicker_interval, auto_click)

# Initialize variables
score = 0
click_multiplier = 1
multiplier_price = 10
auto_clickers = 0
auto_clicker_price = 50
auto_clicker_interval = 1000  # Auto-clickers click every 1 second

# Create the main window
root = tk.Tk()
root.title("Clicking Game with Upgrades")

# Create a label to display the score
score_label = tk.Label(root, text=f"Score: {score}")
score_label.pack()

# Create a button to click
button = tk.Button(root, text="Click me!", command=increment_score)
button.pack()

# Create upgrade buttons and labels
multiplier_label = tk.Label(root, text=f"Score Multiplier x{click_multiplier} (Cost: {multiplier_price} points)")
multiplier_label.pack()
multiplier_button = tk.Button(root, text="Buy Score Multiplier", command=buy_multiplier)
multiplier_button.pack()

auto_clicker_label = tk.Label(root, text=f"Auto-Clickers x{auto_clickers} (Cost: {auto_clicker_price} points)")
auto_clicker_label.pack()
auto_clicker_button = tk.Button(root, text="Buy Auto-Clicker", command=buy_auto_clicker)
auto_clicker_button.pack()

# Move the button to a random position initially
x = random.randint(0, 300)
y = random.randint(0, 300)
button.place(x=x, y=y)

# Use a timer to move the button periodically
def move_button():
    x = random.randint(0, 300)
    y = random.randint(0, 300)
    button.place(x=x, y=y)
    root.after(2000, move_button)

move_button()

# Start the auto-clickers
for _ in range(auto_clickers):
    auto_click()

# Start the main loop
root.mainloop()
