# python3

B = 13
Q = 256

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    input_type = input()
    if input_type[0] == "I":
        return(input().rstrip(), input().rstrip())
    elif input_type[0] == "F":
        path = "./tests/" + "06"
        with open(path, 'r', encoding = 'utf-8') as test:
            return(test.readline().rstrip(), test.readline().rstrip())
    else:
        return
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    # return(input().rstrip(), input().rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_hash(pattern: str) -> int:
    global B, Q
    pattern_len_inHash = len(pattern)
    result = 0
    for i in range(pattern_len_inHash):
        result = (B * result + ord(pattern[i])) % Q
    return result

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    global B, Q
    pattern_len = len(pattern)
    text_len = len(text)
    multiplier = 1
    for i in range(1, pattern_len):
        multiplier = (multiplier * B) % Q
    # and return an iterable variable
    pattern_hash = get_hash(pattern)
    text_hash = get_hash(text[:pattern_len])
    occ = []
    for i in range(text_len - pattern_len + 1):
        if pattern_hash == text_hash:
            if text[i:i+pattern_len] == pattern:
                occ.append(i)
        if i < text_len - pattern_len:
            text_hash = (B * (text_hash - ord(text[i]) * multiplier) + ord(text[i + pattern_len])) % Q
            text_hash = (text_hash + Q) % Q
    return occ


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

