import random

print("🔮 Welcome to Priya Sachidanand Jha's Fortune Teller (21JE0702) 🔮")  
mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").lower()

fortunes = {
    "happy": [
        "Great things await you, Priya! Keep smiling.",
        "Your energy is magnetic today, Priya. 🌞"
    ],
    "sad": [
        "Tough times pass, Priya. Something good is on its way.",
        "Remember, Priya that even rainy clouds clear eventually."
    ],
    "neutral": [
        "Today is a calm sea—perfect to sail forward, Priya!",
        "Balance is power. Keep flowing, Priya. 🌀"
    ],
    "stressed": [
        "Take a deep breath, Priya. You’re stronger than the storm.",
        "The weight you carry today becomes strength tomorrow, Priya."
    ]
}

if mood in fortunes:
    print("✨ Your fortune:", random.choice(fortunes[mood]), "✨")
else:
    print("🔔 Mood not recognized. But fortune still favors the curious. 🔔")