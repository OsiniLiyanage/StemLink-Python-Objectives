
def clean_words(txt):
    clean_txt = ""
    for char in txt:
        if char not in ".,!?;:\"'()[]{}":
            clean_txt = clean_txt + char
  
    wrds = clean_txt.lower().split()
    return wrds


def word_frequency(wrds):
    freq = {}
    for w in wrds:
        if w in freq:
            freq[w] = freq[w] + 1
        else:
            freq[w] = 1
    return freq


def filter_long_words(wrds, min_len=5):
    result = filter(lambda x: len(x) >= min_len, wrds)
    return list(result)


def sort_by_frequency(freq_dict):
    sorted_items = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_items


def capitalize_words(wrds):
    caps = map(str.capitalize, wrds)
    return list(caps)


def find_word_positions(wrds, target):
    pos_list = []
    for idx, w in enumerate(wrds):
        if w == target:
            pos_list.append(idx)
    return pos_list


def generate_report(txt):
    print("===== TEXT ANALYSIS TOOLKIT =====")
    print("Analyzing text:")
    print(f'"{txt}"')
    
    words = clean_words(txt)
    
    if len(words) == 0:
        print("No words found!")
        return
    
    print("===== WORD STATISTICS =====")
    print(f"Total words: {len(words)}")
    
    freq = word_frequency(words)
    print(f"Unique words: {len(freq)}")
    
    print("Word frequencies (sorted by count):")
    sorted_freq = sort_by_frequency(freq)
    for i, item in enumerate(sorted_freq, 1):
        word = item[0]
        count = item[1]
        times_word = "time" if count == 1 else "times"
        print(f"{i}. {word}: {count} {times_word}")
    
    print("===== FILTERED WORDS (length >= 5) =====")
    long_wrds = filter_long_words(words, 5)
    seen = []
    unique_long = []
    for w in long_wrds:
        if w not in seen:
            seen.append(w)
            unique_long.append(w)
    
    for i, w in enumerate(unique_long, 1):
        positions = find_word_positions(words, w)
        if len(positions) == 1:
            pos_str = f"position: {positions[0]}"
        else:
            pos_str = f"positions: {', '.join(map(str, positions))}"
        print(f"{i}. {w} (appears at {pos_str})")
    
    print("===== TRANSFORMATIONS =====")
    caps = capitalize_words(words)
    print(f"Capitalized: {caps}")
    
 
    alpha = sorted(words)
    print(f"Sorted alphabetically: {alpha}")
    longest = max(words, key=len)
    shortest = min(words, key=len)
    print(f"Longest word: {longest} ({len(longest)} letters)")
    print(f"Shortest word: {shortest} ({len(shortest)} letters)")


def main(): 
    sample_text = "Python is amazing! Python makes programming fun. Python is powerful."
    generate_report(sample_text)


main()