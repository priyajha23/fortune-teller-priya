print("🔮 Welcome to Priya Sachidanand Jha's Fortune Teller (21JE0702) 🔮")  
mood = input("How are you feeling today? (happy/sad/neutral): ").lower()

if mood == "happy":
    print("✨ Your fortune: Great things await you, Priya! Keep smiling. ✨")
elif mood == "sad":
    print("💫 Your fortune: Tough times pass, Priya. Something good is on its way. 💫")
elif mood == "neutral":
    print("🌟 Your fortune: Today is a calm sea—perfect to sail forward, Priya! 🌟")
else:
    print("🔔 Mood not recognized. But fortune still favors the curious. 🔔")