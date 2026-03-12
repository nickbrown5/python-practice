import secrets

# generate password using diceware method
def password_generator(num_of_words):
    diceware_dict = {}
    passphrase = ''
    with open('diceware.txt', 'r') as file:
        for line in file:
            key, value = line.strip().split('\t')
            diceware_dict[key] = value
    for word in range(0, num_of_words):
        diceware_num = ''
        for die in range(0, 5): # 5 dice rolls
            die = secrets.randbelow(6) + 1
            diceware_num += str(die)
        passphrase += diceware_dict[diceware_num] + ' '
    print(passphrase.strip())

if __name__ == '__main__':
    password_generator(7)
