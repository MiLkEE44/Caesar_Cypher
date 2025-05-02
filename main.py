import art
print(art.logo)
#Imported art and the alphabet 
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# If the user types 'decode', the shift in the for loop is reversed by multiplying by 1. 
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
#Each letter in that's not in the word from the text input gets added to output_text
#Then the shifted position is the alphabet text location + the number from shift_amount. 
#The modulo keeps everything within the alphabet's range
#After the shift, the new letter is appended to output_text. 
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")
#A while loop that continues the game unless 'no' is typed. 
should_continue = True
#The inputs from the user asking for the word he wants to encode and the shift amount he wants. 
while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
#calling the function and putting the inputs into the function 
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
#Choice to end the loop 
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'. \n").lower()
    if restart == 'no':
        should_continue = False
        print("Goodbye")
