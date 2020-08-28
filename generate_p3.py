import string
import random

## Display error message
def display_error(message):
    print('\n==================================')
    print('ERROR:\n{0}').format(message)
    print('==================================\n')

## Generate Key
def generate_key(qty, n):
    key = []

    for i in range(int(qty)):
        generated_key = ''

        for _ in range(int(n)):
            if int(_) % 4 == 0 and int(_) != 0:
                generated_key += '-'
            generated_key += ''.join(random.choice(string.ascii_uppercase + string.digits))
        
        key.append(generated_key)

    return key

## Generate SQL
def generate_SQL(table, keys):
    SQL = ''

    for i, val in enumerate(keys):
        SQL += 'INSERT INTO "{0}" ("invite", "is_revoked", "created_at", "updated_at") VALUES (\'{1}\', \'0\', NULL, NULL);'.format(table, val)
    
    return SQL



if __name__ == '__main__':

    ## Get how many keys to generate
    quantity = input('How many keys do you want generate? ')

    while quantity.isdigit() == False:
        display_error('The quantity has to be a number')
        quantity = input('How many keys do you want generate? ')


    ## Get how long option
    key_chars = input('How long the key has to be? ')

    while key_chars.isdigit() == False:
        display_error('The key chars has to be a number')
        key_chars = input('How long the key has to be? ')

    ## Generate the keys
    keys = generate_key(quantity, key_chars)


    ## Get generate SQL option
    generate_sql = input('Generate SQL? [y/n]')

    while str(generate_sql) != 'y' and str(generate_sql) != 'n':
        display_error('The option has to be "y" or "n"')
        generate_sql = input('Generate SQL? [y/n] ')

    ## If user want to generate SQL
    if generate_sql == 'y':
        table_name = input('Enter table name? ')
        SQL = generate_SQL(table_name, keys)

        print('\n'+SQL)
    else:
        print('\n')
        for i, val in enumerate(keys):
            print(val)

input()