################################
# Sangay Deki
# 1ECE
# 02230107
################################
# REFERENCES
#https://www.youtube.com/watch?v=5cU1ILGy6dM
#https://stackoverflow.com/questions/70781614/python-rock-paper-scissors-game
#https://www.youtube.com/watch?v=y5gc-y2b5NY
################################
# SOLUTION
# Your Solution Score:
# 50169
################################

def read_input(input_file):
    P = []
    with open(input_file, 'r') as file:
        for line in file: 
            opponent_choice, outcome = line.split()
            P.append((opponent_choice, outcome))
    return P

def calculate_score(matches):
    final_score = 0
    for opponent_move, result in matches:
        if result == 'X': #have to lose (0)
            if opponent_move == 'A': #(rock) therefore need to choose scissor(3)
                final_score += 3  # 3+0
            elif opponent_move == 'B': #(paper) therefore need choose rock(1)
                final_score += 1 # 1+0
            elif opponent_move == 'C': #(scissor) therefore need to choose paper(2)
                final_score += 2 # 2+0
        elif result == 'Y': #have to tie(3), opponent_move = my move
            if opponent_move == 'A': # rock(1)
                final_score += 4  # 1+3
            elif opponent_move == 'B': #paper(2)
                final_score += 5  # 2+3
            elif opponent_move == 'C': #scissor(3)
                final_score += 6  # 3+3
        elif result == 'Z': #have to win(6)
            if opponent_move == 'A': #rock, therefore need to choose paper(2)
                final_score += 8  # 2+6
            elif opponent_move == 'B': #paper, therefore need to choose scissor (3)
                final_score += 9  # 3+6
            elif opponent_move == 'C': #scissor, therefore need to choose rock (1)
                final_score += 7 # 1+6
    print(f"The total score is: {final_score}")

input_file = "CSF101-CAP/input_7_cap1.txt"  # Replace with your input file path
calculate_score(read_input(input_file))
