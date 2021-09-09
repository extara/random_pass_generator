import random
import colorama

colorama.init()


def generate_random_password(length):
    alphabet = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

    join_it = "".join(random.sample(alphabet, (int(length))))

    return join_it



if __name__ == "__main__":
    print(colorama.Fore.RED + 'Hi !\nWelcome to the random password generator')
    while True:
        try:
            pass_length = int(input('Give me your needed password length: '))
            break
        except ValueError:
            print(colorama.Fore.RED + 'Please make sure that you input a number!')
    password = generate_random_password(pass_length)
    print(
        colorama.Fore.LIGHTBLUE_EX + '\nWe provide really high level of security, so your password is shown'
                            ' only once, while generated.'
                            '\nIt is not saved anywhere, so save it in a safe place, AS ALWAYS.\n'
                            'Remember to change it at least once a month! \n\n')
    print(password + "\n\nThank you for using random pass generator")
    print(input("\nHit enter to exit"))
