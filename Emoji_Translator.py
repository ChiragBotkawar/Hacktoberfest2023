# Emoji Translator 😃
# Convert normal text into emoji-based fun sentences

def emoji_translate(text):
    # Simple emoji dictionary
    emoji_dict = {
        "love": "❤️",
        "happy": "😄",
        "sad": "😢",
        "angry": "😠",
        "pizza": "🍕",
        "dog": "🐶",
        "cat": "🐱",
        "food": "🍔",
        "coffee": "☕",
        "music": "🎵",
        "car": "🚗",
        "party": "🎉",
        "book": "📚",
        "fire": "🔥",
        "sun": "☀️",
        "moon": "🌙",
        "star": "⭐",
        "rain": "🌧️",
        "computer": "💻",
        "python": "🐍",
        "heart": "💖",
        "sleep": "💤",
        "laugh": "😂",
        "cool": "😎",
        "school": "🏫",
        "movie": "🎬",
    }

    words = text.lower().split()
    translated = []

    for word in words:
        if word in emoji_dict:
            translated.append(emoji_dict[word])
        else:
            translated.append(word)
    
    return " ".join(translated)

def main():
    print("🧠 Welcome to Emoji Translator! 😃")
    print("Type a sentence and watch it come alive with emojis!\n")
    
    text = input("Enter your sentence: ")
    result = emoji_translate(text)
    
    print("\n🎨 Emoji Translation:")
    print(result)

if __name__ == "__main__":
    main()
