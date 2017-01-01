import re

number_matcher = re.compile('\d+')
target_matcher = re.compile('to.*?\d+')
bot_id_matcher = re.compile('bot \d+')

def get_numbers(text):
    return list(map(int, number_matcher.findall(text)))

def get_bots(text):
    return bot_id_matcher.findall(text)

def get_targets(text):
    return list(map(lambda s: s.replace('to ', ''), target_matcher.findall(text)))

class Bot:
    '''A Bot accepts a microchip or an instruction'''
    def __init__(self, bot_id):
        self.bot_id = bot_id
        self.values = []
        self.instructions = []

    def accept_microchip(self, value):
        self.values.append(value)
        
    def accept_instruction(self, instruction):
        self.instructions.append(instruction)

    def is_ready(self):
        #Bot is ready when it has 2 microchips and knows what to do with them
        return len(self.values) == 2 and len(self.instructions) > 0
    
    def process_instructions(self):
        #Bot processes instructions when ready to return more instructions of type 'value <v> goes to <>'
        if self.is_ready():
            self.values.sort()
            instruction = self.instructions.pop(0)
            return [ 'value {} goes to {}'.format(self.values.pop(0), target) for target in get_targets(instruction) ]

        return None

def process_instructions(instructions, value1, value2):
    bots = {}
    output_bins = {}

    while len(instructions) > 0:
        instruction = instructions.pop(0)
        target = ''

        #We accept instructions of type:
        #1) value <v> goes to <target>
        #2) bot <b> gives low to <target 1> and high to <target 2>
        #The latter is instruction by the bot and is processed by the bot itself
        if instruction.startswith('value'):
            target = get_targets(instruction)[0]
            value = get_numbers(instruction)[0]
        elif instruction.startswith('bot'):
            target = get_bots(instruction)[0]
            value = None
        else:
            print('Ignoring instruction: ', instruction)
            continue

        if target.startswith('bot'):
            if not target in bots:
                bots[target] = Bot(target)

            bot = bots[target]

            if value is not None:
                bot.accept_microchip(value)
            else:
                bot.accept_instruction(instruction)

            if bot.is_ready():
                pending_instructions = bot.process_instructions()
                values = list(map(lambda i : get_numbers(i)[0], pending_instructions))
                if value1 in values and value2 in values:
                    return target

                instructions += pending_instructions

        elif target.startswith('output'):
            if not target in output_bins:
                output_bins[target] = []

            if value is not None:
                output_bins[target].append(value)
                
        
        else: print('Ignoring instruction:', instruction)
    
    return None

def main():
    #instructions = ['value 5 goes to bot 2', 'bot 2 gives low to bot 1 and high to bot 0', 'value 3 goes to bot 1', 'bot 1 gives low to output 1 and high to bot 0', 'bot 0 gives low to output 2 and high to output 0', 'value 2 goes to bot 2']
    #print(process_instructions(instructions, 2, 5))

    instructions = open('input10.txt').read().strip().split('\n')
    print(process_instructions(instructions, 17, 61))

if __name__ == '__main__':
    main()
