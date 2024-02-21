import marimo

__generated_with = "0.2.5"
app = marimo.App()

@app.cell

def pong_game_cell(mo):
    import time

    # initial setup
    canvas_width, canvas_height = 40, 20
    user = {'x': 1, 'y': canvas_height // 2 - 2, 'width': 2, 'height': 4, 'score': 0}
    com = {'x': canvas_width - 3, 'y': canvas_height // 2 - 2, 'width': 2, 'height': 4, 'score': 0}
    ball = {'x': canvas_width // 2, 'y': canvas_height // 2, 'velocityX': 1, 'velocityY': 1}
    move_direction = 1  # Direction for paddle fyi: 1 for down, -1 for up

    # create and return the current game board
    def create_board():
        
        board_html = '<div style="border: 2px solid lime; background-color: darkgreen; color: lime; font-family: monospace; font-size: 24px; text-align: center; padding: 10px; border-radius: 10px;">'  #basic pong board design
        board_html += 'marimo plays pong<br><br>'
        board_html += '<div style="background-color: black; color: white; white-space: pre; text-align: center;">'
        for y in range(canvas_height):
            for x in range(canvas_width):
                if x == ball['x'] and y == ball['y']:
                    
                    board_html += '<span style="color: lime; font-size: 24px;">ⵔ</span>'
                elif (user['x'] <= x < user['x'] + user['width'] and user['y'] <= y < user['y'] + user['height']) or \
                     (com['x'] <= x < com['x'] + com['width'] and com['y'] <= y < com['y'] + com['height']):
                    
                    board_html += '|'
                else:
                   
                    board_html += '&nbsp;'
            board_html += '<br>'  
        
        board_html += '</div>'
        board_html += f'<div style="font-size: 28px;">Score: {user["score"]} - {com["score"]}</div>'
        
        board_html += '</div>'
        return board_html
    



    def update_game():
        global move_direction
        # ball position
        import random
        ball['x'] += ball['velocityX']
        ball['y'] += ball['velocityY']
        
        # ball collision 
        if ball['y'] <= 0 or ball['y'] >= canvas_height - 1:
            ball['velocityY'] = -ball['velocityY']
        
        # collision check
        if ball['x'] == user['x'] + 1 and user['y'] <= ball['y'] <= user['y'] + user['height']:
            ball['velocityX'] = -ball['velocityX']
        
        # com paddle collision chk
        if ball['x'] == com['x'] - 1 and com['y'] <= ball['y'] <= com['y'] + com['height']:
            ball['velocityX'] = -ball['velocityX']
        
        # Ball reset if it goes past paddle (scoring)
        if ball['x'] < 0:
            com['score'] += 1
            reset_ball()
        elif ball['x'] > canvas_width - 1:
            user['score'] += 1
            reset_ball()
        
        # randomly decide if the user paddle will miss
        if random.random() < 0.1:  # 10% chance to miss
            pass  # user paddle does nothing, simulating a miss
        else:
            # mv user paddle in a simple pattern
            user['y'] += move_direction
            if user['y'] <= 0 or user['y'] + user['height'] >= canvas_height:
                move_direction = -move_direction  # Change direction at bounds
        
        # rnd decide if the com paddle will miss
        if random.random() < 0.1:  # 10% chance to miss
            pass  # Com paddle does nothing, simulating a miss
        else:
            # "ai" for com paddle 
            if com['y'] + com['height'] // 2 < ball['y']:
                com['y'] = min(com['y'] + 1, canvas_height - com['height'])
            elif com['y'] + com['height'] // 2 > ball['y']:
                com['y'] = max(com['y'] - 1, 0)

    def reset_ball():
        ball['x'], ball['y'] = canvas_width // 2, canvas_height // 2
        ball['velocityX'], ball['velocityY'] = 1, 1  # reset velo
    # Function to animate the game for a given number of steps
    def animate_game(steps, delay=0.1):
        for _ in range(steps):
            update_game()
            board_html = create_board()
            mo.output.replace(mo.Html(board_html))
            time.sleep(delay) 
            
    # Start the animation
    animate_game(2000)  # adjust this to set play duration 

    return 

if __name__ == "__main__":
    app.run()


@app.cell
def __():
    import marimo as mo
    
    return (

        mo
        
    )


if __name__ == "__main__":
    app.run()
    
## App author/layout/design(https://github.com/vrtnis/)
## Inspired by Pong