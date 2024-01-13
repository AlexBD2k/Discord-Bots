from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    #some base case responses
    if lowered == '':
        return 'you seem very quiet'
    
    elif 'hello' in lowered:
        return 'Hi! how are you?'
    
    elif 'bye' in lowered:
        return 'see you later!'
    #roll the dice minigame feature
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1,6)}'
    
    else: 
        return choice('I dont understand, can you repeat?','What are you talking about?','I didn\'t catch that say again please')
