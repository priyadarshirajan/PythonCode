def AlpabetDetails(char):
    vowel_count = 0
    space_count = 0
    int_count = 0
    consonent_count = 0
    char_len = len(char)
    for letter in char:
        if letter in "aeiou":
            vowel_count+=1

        elif letter == " ":
            space_count+=1

        elif letter in "0123456789":
            int_count+=1

        else:
            consonent_count+=1
    print(f"Total number of Character in your string {char_len}") 
    print(f"Total number of vowel in your string {vowel_count}") 
    print(f"Total number of space in your string {space_count}") 
    print(f"Total number of integer in your string {int_count}") 
    print(f"Total number of consonent in your string {consonent_count}") 

char = input("Enter your string here :")
AlpabetDetails(char)