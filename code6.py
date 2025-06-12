import ugame
import stage

import constants

def game_scene():

    # the image banks for CircuitPy
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    
    # button states get initialized as "button_up" (not pressed)
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]

    # set up the sounds
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    
    # sets the background to image 0 in the image bank with 10x8 of size 16x16
    background = stage.Grid(image_bank_background, 10, 8)
    
    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)

    alien = stage.Sprite(image_bank_sprites, 9, int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2), 16)
    
    # creates a stage for the background
    # alse sents the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # sets the layers to show up in the order of ship, alien, background
    game.layers = [ship] + [alien] + [background]
    game.render_block()
    
    
    
    while True:
        game.render_sprites([ship])
        game.tick()
        # get user input
        keys = ugame.buttons.get_pressed()

        # button 'A' (will be used to shoot)
        if keys & ugame.K_X:
            print("A")
        if keys & ugame.K_O != 0:
            if b_button == constants.button_state["button_up"]:
                b_button= constants.button_state["button_just_pressed"]
            elif b_button == constants.button_state["button_just_pressed"]:
                b_button = constants.button_state["button_still_pressed"]
        else:
            if b_button == constants.button_state["button_still_pressed"]:
                b_button = constants.button_state["button_released"]
            else:
                b_button = constants.button_state["button_up"]
        if keys & ugame.K_START:
            print("Start")
        if keys & ugame.K_SELECT:
            print("Select")

        # Move right
        if keys & ugame.K_RIGHT:
            ship.move(ship.x + 1, ship.y)
        else:
            if ship.x <= 0:
                ship.move(166, ship.y)

        # Move left
        if keys & ugame.K_LEFT:
            ship.move(ship.x - 1, ship.y)
        else:
            if ship.x >=160:
                ship.move(-6, ship.y)

        # Move up
        if keys & ugame.K_UP:
            ship.move(ship.x, ship.y - 1)
        else:
            if ship.y >= 110:
                ship.move(ship.x, 110)
        
        # Move down
        if keys & ugame.K_DOWN:
            ship.move(ship.x, ship.y + 1)
        else:
            if ship.y <= 70:
                ship.move(ship.x, 70)
        
        #update game Logic
        if  b_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)
        
        # redraw sprites
        game.render_sprites([ship] + [alien])
        game.tick()

if __name__ == "__main__":
    game_scene()