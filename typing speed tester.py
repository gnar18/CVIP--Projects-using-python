import time

def typing_speed_test():
    prompt_text = "The quick brown fox jumps over the lazy dog."
    print("Type the following text:")
    print(prompt_text)
    
    input("Press Enter when you are ready to start typing.")
    
    start_time = time.time()
    user_input = input("Type the text here: ")
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    words_per_minute = (len(prompt_text.split()) / elapsed_time) * 60
    
    print(f"\nTime taken: {elapsed_time:.2f} seconds")
    print(f"Words per minute: {words_per_minute:.2f}")

typing_speed_test()
