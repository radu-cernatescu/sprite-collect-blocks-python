import pygame
import random

# Define some colors
BLACK    = (   0,   0,   0)
white    = ( 255, 255, 255)
red      = ( 255,   0,   0)
blue     = (0,0,255)
green    = (0,255,0)

# This class represents the ball
# It derives from the "Sprite" class in Pygame
class Block(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self) #Python 2.7 version


        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """

    # -- Methods
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super(Player,self).__init__()

        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(blue)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0

    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y

    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y

# Initialize Pygame
pygame.init()

# Set the height and width of the screen
screen_width=700
screen_height=400
screen=pygame.display.set_mode([screen_width,screen_height])

# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'RenderPlain.'
good_block_list = pygame.sprite.RenderPlain()
bad_block_list = pygame.sprite.RenderPlain()

# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.RenderPlain()

for i in range(50):
    # This represents a block
    block = Block(red,20,15)

    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)

    # Add the block to the list of objects
    bad_block_list.add(block)
    all_sprites_list.add(block)

for i in range(50):
    # This represents a block
    block = Block(green, 20, 15)

    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)

    # Add the block to the list of objects
    good_block_list.add(block)
    all_sprites_list.add(block)



# Create a red player block
player = Player(20, 15)
all_sprites_list.add(player)

#Loop until the user clicks the close button.
done=False

# Used to manage how fast the screen updates
clock=pygame.time.Clock()

score = 0

font = pygame.font.SysFont('Calibri', 25, True, False)

# -------- Main Program Loop -----------
while done==False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Set the speed based on the key pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)

        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)

    all_sprites_list.update()
    # Clear the screen
    screen.fill(white)

    # See if the player block has collided with anything.
    good_blocks_hit_list = pygame.sprite.spritecollide(player, good_block_list, True)
    bad_blocks_hit_list = pygame.sprite.spritecollide(player, bad_block_list, True)

    # Check the list of collisions.

    if len(bad_blocks_hit_list) > 0:
        score -=len(bad_blocks_hit_list)
    elif len(good_blocks_hit_list) > 0:
        score +=len(good_blocks_hit_list)

    text = font.render("Score:"+str(score),True,BLACK)

    screen.blit(text, [0,0])
    # Draw all the spites
    all_sprites_list.draw(screen)

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

pygame.quit()