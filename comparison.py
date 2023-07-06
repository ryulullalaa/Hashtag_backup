import hashlib

stored_hashes = [
    "022d06d1b7983d0d3189cf150d7490dd0938fb1f00a337f692d702ee75c39575", 
    "069846ff6799955eea05aee1a005d87fbce6f2f8394fc464b821dee23f7aac3e",
    "2bcc3cac0ef207c15f820a3e98f7a0389dce7b147c8595d2bf3b3d7d65af29f9",
    "3f9c221f9767452aca4eb97a8ce9b896b401bc4add47a8604063e5753be159bd",
    "59d797509d63fd7f6b2a73590d08439a6014ff5f8f19a0e56636714dce2a0a5d",
    "639641f0a922739ac81964fc670066e3c23c28c3162e210cad9299902dc24680",
    "65b3a3378771535bedd7afe2836147559a87e4562eaef3ab5d72c8d1b4c07968",
    "684d1eb67102d6bd970738cb1c408b0cfac2671587e4372469fd7e258d45cb63",
    "6b44786c8979b39b2541dc4fecb1e5c1a52058cfb04744c1de9b79f12c997ba9",
    "86131a9f697d3ae15020ef4dc2fec85ab88e7514d4143fbd99a3109677ab9bd0",
    "91dfc1ac6fdc7d4de7e5279a450d031a666365972263afb5d29eed9c80687515",
    "9dbf8600f7fadb4a856b5d3c7d65330581b5275e2b7906f8b26f980b4ec57782",
    "a69ce5ab70dd11a4660eb2dec57db3fdc29d3ff9889239d5c5a1a003f7e6c60a",
    "ab4734e00e9774a7e533a13617146ce758ef4ce4bbb5254429ce62507cbae3dc",
    "ae52e3c850a445024be45248d5fa3ce9a9721d6d7c955f96a641df03acd01c5f",
    "c885ac7be78e19bf6208e9133e86ed82adae556c6af7b6506e854435b7954bd5",
    "ea3fc2cdbc595398544d0a302df7d010f1f4cbce6fd1be5fba137b6275ad0b4f",
    "f66c05bb10f20de0887d90b4793f13126f2bc6a2abe1ecd1b7305b56ce8816f4"
]

# Prompt the user for the hashes all at once, separated by spaces
hash_input = input("Enter all hashes you want to check, separated by spaces: ")

input_hashes = hash_input.split(' ')

# For each input hash...
for input_hash in input_hashes:
    # We'll check if the input hash is in the list of stored hashes.
    if input_hash in stored_hashes:
        print(f"The input hash '{input_hash}' matches a stored hash.")
    else:
        print(f"The input hash '{input_hash}' does not match any stored hashes.")

import hashlib

# Prompt the user for the hashes all at once, separated by line breaks
hash_input = input("Enter all hashes you want to check, separated by line breaks: ")

input_hashes = hash_input.split('\n')

# Open the file in append mode
with open("input_hashes.txt", "a") as file:
    # For each input hash...
    for input_hash in input_hashes:
        # We'll check if the input hash is in the list of stored hashes.
        if input_hash in stored_hashes:
            print(f"The input hash '{input_hash}' matches a stored hash.")
        else:
            print(f"The input hash '{input_hash}' does not match any stored hashes.")
        
        # Write the input hash to the file, followed by a newline
        file.write(input_hash + "\n")
