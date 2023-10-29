class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        substitute_table = {}

        #Updating hash table with blank spaces
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            substitute_table[letter] = ' '
        
        #updating the keys to the position of geven key on their index
        key_index = 0
        for letter in key:
            if letter != ' ' and  substitute_table[letter] == ' ':
                substitute_table[letter] = chr(ord('a') + key_index)
                key_index += 1
        
        decode_msg = ''

        for letter in message:
            if letter == ' ':
                decode_msg += ' '
            else:
                decode_msg += substitute_table[letter]
        
        return decode_msg










        