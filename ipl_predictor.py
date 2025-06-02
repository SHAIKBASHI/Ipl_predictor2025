import random

# Tuple of IPL 2025 teams
teams = ("Mumbai Indians", "Chennai Super Kings", "Royal Challengers Bangalore",
         "Kolkata Knight Riders", "Rajasthan Royals", "Sunrisers Hyderabad",
         "Lucknow Super Giants", "Gujarat Titans", "Punjab Kings", "Delhi Capitals")

# Randomly select a team as the "winner"
predicted_winner = random.choice(teams)

print("🏏 Welcome to the IPL 2025 Winner Predictor!")
print("🤖 Our expert AI prediction says...")
print(f"🎉 {predicted_winner} will win the IPL 2025 Trophy! 🏆")
