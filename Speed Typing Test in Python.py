import time

def calculate_typing_speed(start_time, end_time, text):
    total_time = end_time - start_time
    words_typed = len(text.split())
    typing_speed = words_typed / total_time * 60
    return typing_speed

def run_speed_typing_test():
    text = "The quick brown fox jumps over the lazy dog."
    print("Type the following text:")
    print(text)

    input("Press Enter to start the timer. Type the text and press Enter again when finished.")

    start_time = time.time()

    user_input = input()

    end_time = time.time()

    typing_speed = calculate_typing_speed(start_time, end_time, user_input)

    print("Typing speed:", round(typing_speed, 2), "words per minute")

run_speed_typing_test()
