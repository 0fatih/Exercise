# Asagida kullanilan yontem Regex'lerden daha kolay.

user_input = 'Bu\nmetinde\tbazi\nbosluklar var...\r\n'

character_map = {
    ord('\n') : ' ',
    ord('\t') : ' ',
    ord('\r') : None
}

print(user_input.translate(character_map))
