# 기본 라이브러리라 파이썬 설치시 자동으로 설치됩니다!
# random 모듈은 랜덤한 숫자를 생성할 때 사용합니다.
import random
import os
import platform
import sys

# 게임에 사용될 단어 목록
words = ['Apple', 'Elephant', 'Guitar', 'Sunshine', 'Ocean', 'Mountain', 'Butterfly',
        'Harmony', 'Adventure', 'Whisper', 'Radiant', 'Universe', 'Tranquil', 'Jubilant',
        'Eloquent', 'Serendipity', 'Zephyr', 'Effervescent', 'Blossom', 'Enigma', 'Symphony',
        'Cascade', 'Luminous', 'Quest', 'Ethereal', 'Delight', 'Resilient', 'Velvet', 'Quasar',
        'Jubilee', 'Nebula', 'Mystique', 'Cascade', 'Kaleidoscope', 'Twilight', 'Pinnacle', 'Cacophony',
        'Incandescent', 'Ponder', 'Ineffable', 'Whimsical', 'Mellifluous', 'Ephemeral', 'Velvet', 'Halcyon',
        'Blossom', 'Enchant', 'Serene', 'Utopia', 'Mirage', 'Labyrinth', 'Aegis', 'Enthrall', 'Ineffable',
        'Mesmerize', 'Quaint', 'Petrichor', 'Mellifluous', 'Elysium', 'Halcyon', 'Illuminate', 'Euphoria',
        'Ethereal', 'Bliss', 'Sonorous', 'Solitude', 'Delicate', 'Paradigm', 'Whimsy', 'Grace', 'Effulgent',
        'Cascade', 'Enrapture', 'Pinnacle', 'Ineffable', 'Cherish', 'Enigma', 'Symphony', 'Luminescent', 'Inquisitive',
        'Radiance', 'Lullaby', 'Utopia', 'Nebula', 'Tranquility', 'Velvet', 'Synchrony', 'Enchant', 'Zephyr', 'Quintessence',
        'Ponder', 'Serenity', 'Blissful', 'Ethereal', 'Cascade', 'Mellifluous', 'Luminous', 'Resplendent', 'Uplift', 'Panorama'
        ]

# 행맨 그림
hangman_pics = [
    """
     ------
     |    |
     |
     |
     |
     |
     |
     |
     |
    ---""",
    """
     ------
     |    |
     |    |
     |
     |
     |
     |
     |
     |
    ---""",
    """
     ------
     |    |
     |    |
     |    ⚲
     |
     |
     |
     |
     |
    ---""",
    """
     ------
     |    |
     |    |
     |    ⚲
     |   ╲
     |
     |
     |
     |
    ---""",
    """
     ------
     |    |
     |    |
     |    ⚲
     |   ╲|
     |
     |
     |
     |
    ---""",
    """
     ------
     |    |
     |    |
     |    ⚲
     |   ╲|╱
     |
     |
     |
     |
    ---""",
    """
     ------
     |    |
     |    |
     |    ⚲
     |   ╲|╱
     |    |
     |
     |
     |
    ---""",
    """
     ------
     |    |
     |    |
     |    ⚲
     |   ╲|╱
     |    |
     |   ╱ 
     |
     |
    ---""",
    """
     ------
     |    |
     |    |
     |    ⚲
     |   ╲|╱
     |    |
     |   ╱ ╲
     |
     |
    ---""",
    """
     ------
     |    |
     |    |
     |    ⚲
     |   ╱|╲
     |    |
     |   ╱ ╲
     |
     |
    ---""",
    
]

hangman_pics_results = [
    """     ------
     |    |
     |    |
     |    
     |    
     |   
     |    
     |   
     |  〉⏤⏤〈〄
    ---""",
    """     ------
     |    |
     |    |
     |
     |
     |
     |    ⚲
     |   ╲|╱
     |    |
     |   ╱ ╲
    ---""",
]

class HangmanGame:
    def init(self):
        self.word = random.choice(words).lower()
        self.guess = set()
        self.use = []
        self.attempts = 0
        self.maxlife = self.life = len(hangman_pics) # 전체 목숨

    def main(self):
        isdone = False
        b_choice = -1
        while not isdone:
            menu = ['1. 게임시작', '2. 게임방법', '3. 게임종료']
            choice_set = {1, 2, 3}
            choice = self.choice_number(menu, choice_set) if b_choice == -1 else b_choice
            if choice == 1:
                b_choice = self.play()
                if b_choice == 3:
                    isdone = True
            elif choice == 2:
                menu = ['##기본규칙',
                        '- 예상하는 알파벳 한개를 입력',
                        '- 만약 한개가 아닌 여러개를 입력할 경우 한번에 처리',
                        '##특수입력',
                        '- [숫자] [단어] 입력 가능',
                        '- [00]: 메인메뉴',
                        '- [99]: 게임종료',
                        '- [11 단어]: 단어 맞추면 승리, 기회 소비',
                        '\n1. 게임시작 2. 메인메뉴']
                choice_set = {1, 2}
                b_choice = self.choice_number(menu, choice_set)
                if b_choice == 2:
                    b_choice = -1 
            else:
                sys.exit('\n\n왜 그냥가? ㅠㅠ')

            if isdone:
                sys.exit('\n\n즐거웠어?')

    
    def play(self):
        # 행맨 시작
        self.init()
        while self.life > 0 :
            corrects = self.get_corrects()
            if corrects == self.word:
                break
            self.clear_terminal()
            print('남은 목숨:', self.life)
            print(hangman_pics[self.maxlife - self.life])
            print('정답: ', self.get_corrects())
            print('입력 현황:', self.use, '\n\n')

            user_input = input('글자를 추측해보세요: ').lower().split()

            if len(user_input) == 0:
                continue
            if user_input[0] == '00':
                return -1
            elif user_input[0] == '99':
                return 3
            elif user_input[0] == '11':
                if user_input[1] == self.word:
                    self.attempts += 1
                    break
            else:
                for c in user_input[0]:
                    if c in self.word and not c in self.guess:
                        self.guess.add(c)
                    else:
                        self.life -= 1
                    self.attempts += 1
                    if not c in self.use:
                        self.use.append(c)
                    if self.life == 0:
                        break
        result = ''
        if self.life > 0:
            result += '축하합니다!!\n' + hangman_pics_results[1]
        else:
            result += '아쉽네요 ㅜㅜ\n' + hangman_pics_results[0]
        
        menu = [f'{result}\n\n정답: {self.word} || 시도횟수: {self.attempts}', f'시도내역: {self.use}\n\n', '1. 다시하기 | 2. 메인메뉴 | 3. 종료하기']
        choice_set = {1, 2, 3}
        choice = self.choice_number(menu, choice_set)
        return -1 if choice == 2 else choice
    
    # 단두대 밑에 표시할 글자표
    def get_corrects(self):
        result = ''
        if len(self.guess) == 0:
            return '_' * len(self.word)
        
        return ''.join(c if c in self.guess else '_' for c in self.word)
    
    # 터미널 깔끔하게 지우기
    def clear_terminal(self):
        os.system('cls') if platform.system() == 'Windows' else os.system('clear')
        print('H A N G M A N\n\n')

    # 번호 선택하기
    def choice_number(self, menu, choice_set):
        correct = False
        while not correct:
            try:
                self.clear_terminal()
                choice = int(input('{0}\n입력 >> '.format("\n".join(menu))))
                if not choice in choice_set:
                    raise
                else:
                    return choice
            except:
                self.print_input_error('정확한 번호만 입력해주세요')
                
    # 화면표시를 clear이후에 하기 때문에 경고를 읽을 수 있게 input으로 표시
    def print_input_error(self, message):
        input(f'!! {message} !!\n- 확인(any) -')


if __name__ == "__main__":
    game = HangmanGame()
    game.main()
