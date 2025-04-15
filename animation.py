#
# Machine Problem 5
#
# Alan Khanim
#
# Description: Description: This script uses the cs1graphics module to create an 
#              animated graphics scene featuring a sunny landscape with animated bears.
#              The scene includes a bright sun with radiating rays, fluffy white clouds,
#              a green tree with colorful ornaments, and two animated bears. 
#              The first bear enters the scene with a bouncy walk animation while
#              roaring its presence. A second bear then appears and performs a similar 
#              animated walk across the scene. The bears engage in a short conversation before
#              the second bear turns around and exits the scene with the same bouncy walking
#              animation.
#

from cs1graphics import *
from time import sleep

paper = Canvas(1000, 600)
paper.setBackgroundColor('skyBlue')

def create_ground():
    #
    # Creates a green Rectangle covering the lower portion of the canvas
    # to represent the ground/grass area.
    #
    # There are no parameters.
    #
    # Returns nothing (adds grass directly to canvas).
    #
    grass = Rectangle(1000, 200, Point(500, 500))
    grass.setFillColor('green')
    grass.setBorderColor('green')
    paper.add(grass)

def create_sun():
    #
    # Creates a sun with radiating rays at the top right of the canvas.
    # The sun consists of a central Circle and 8 ray Path objects.
    #
    # There are no parameters.
    #
    # Returns nothing (adds sun and rays directly to canvas).
    #
    sun = Circle(50, Point(900, 100))
    ray1 = Path(Point(900, 50), Point(925, 25), Point(900, 0))
    ray2 = Path(Point(900, 150), Point(875, 175), Point(900, 200))
    ray3 = Path(Point(850, 100), Point(825, 75), Point(800, 100))
    ray4 = Path(Point(950, 100), Point(975, 125), Point(1000, 100))
    ray5 = Path(Point(925, 125), Point(975, 175))
    ray6 = Path(Point(925, 75), Point(975, 25))
    ray7 = Path(Point(875, 125), Point(825, 175))
    ray8 = Path(Point(875, 75), Point(825, 25))
    sun.setFillColor('yellow')
    ray1.setBorderColor('yellow')
    ray2.setBorderColor('yellow')
    ray3.setBorderColor('yellow')
    ray4.setBorderColor('yellow')
    ray5.setBorderColor('yellow')
    ray6.setBorderColor('yellow')
    ray7.setBorderColor('yellow')
    ray8.setBorderColor('yellow')
    ray1.setBorderWidth(5)
    ray2.setBorderWidth(5)
    ray3.setBorderWidth(5)
    ray4.setBorderWidth(5)
    ray5.setBorderWidth(5)
    ray6.setBorderWidth(5)
    ray7.setBorderWidth(5)
    ray8.setBorderWidth(5)
    sun.setBorderColor('yellow')
    paper.add(ray1)
    paper.add(ray2)
    paper.add(ray3)
    paper.add(ray4)
    paper.add(ray5)
    paper.add(ray6)
    paper.add(ray7)
    paper.add(ray8)
    paper.add(sun)

def create_clouds():
    #
    # Creates three cloud formations using Ellipse and Circle objects.
    # The clouds are positioned at different locations in the sky.
    #
    # There are no parameters.
    #
    # Returns nothing (adds clouds directly to canvas).
    #
    clouds = Layer()
    cloud1 = Ellipse(200, 100, Point(600, 150))
    cloud2 = Circle(50, Point(600, 100))
    cloud3 = Circle(50, Point(650, 100))
    cloud1.setFillColor('white')
    cloud2.setFillColor('white')
    cloud3.setFillColor('white')
    cloud1.setBorderColor('white')
    cloud2.setBorderColor('white')
    cloud3.setBorderColor('white')
    clouds.add(cloud1)
    clouds.add(cloud2)
    clouds.add(cloud3)
    clouds.adjustReference(600, 150)
    clouds1 = clouds.clone()
    clouds1.flip()
    clouds1.moveTo(300, 100)
    clouds2 = clouds.clone()
    clouds2.moveTo(50, 150)
    paper.add(clouds)
    paper.add(clouds1)
    paper.add(clouds2)

def create_tree():
    #
    # Creates a tree with a brown trunk, green foliage, and four
    # colored ornament balls at different positions in the tree.
    #
    # There are no parameters.
    #
    # Returns nothing (adds tree components directly to canvas).
    #

    trunk = Rectangle(50, 100, Point(175, 450))
    trunk.setFillColor('brown')
    tree = Polygon(Point(175, 200), Point(50, 450), Point(300, 450))
    tree.setFillColor('green')
    ball1 = Circle(12.5, Point(200, 300))
    ball1.setFillColor('red')
    ball2 = Circle(12.5, Point(125, 325))
    ball2.setFillColor('blue')
    ball3 = Circle(12.5, Point(225, 375))
    ball3.setFillColor('purple')
    ball4 = Circle(12.5, Point(150, 425))
    ball4.setFillColor('orange')
    paper.add(trunk)
    paper.add(tree)
    paper.add(ball1)
    paper.add(ball2)
    paper.add(ball3)
    paper.add(ball4)

def create_bear():
    #
    # Creates a bear character using multiple shapes (squares, circles,
    # ellipses) combined in a Layer. The bear is initially positioned
    # off-screen left.
    #
    # There are no parameters.
    #
    # Returns the bear Layer object.
    #
    bear = Layer()
    bearbody = Square(100, Point(300, 450))
    bearbody.setFillColor('brown')
    beararm1 = Ellipse(50, 75, Point(375, 425))
    beararm1.setFillColor('brown')
    beararm2 = Ellipse(50, 75, Point(225, 425))
    beararm2.setFillColor('brown')
    bearleg1 = Circle(25, Point(275, 525))
    bearleg1.setFillColor('brown')
    bearleg2 = Circle(25, Point(325, 525))
    bearleg2.setFillColor('brown')
    bearjaw = Ellipse(100, 50, Point(300, 375))
    bearjaw.setFillColor('brown')
    bearhead = Circle(50, Point(300, 350))
    bearhead.setFillColor('brown')
    bearear1 = Circle(25, Point(350, 325))
    bearear1.setFillColor('brown')
    bearear2 = Circle(25, Point(250, 325))
    bearear2.setFillColor('brown')
    beareye1 = Circle(5, Point(325, 325))
    beareye1.setFillColor('black')
    beareye2 = Circle(5, Point(275, 325))
    beareye2.setFillColor('black')
    bearnose = Polygon(Point(300, 375), Point(275, 350), Point(325, 350))
    bearnose.setFillColor('black')
    bear.add(bearbody)
    bear.add(beararm1)
    bear.add(beararm2)
    bear.add(bearleg1)
    bear.add(bearleg2)
    bear.add(bearear1)
    bear.add(bearear2)
    bear.add(bearhead)
    bear.add(bearjaw)
    bear.add(beareye1)
    bear.add(beareye2)
    bear.add(bearnose)
    bear.adjustReference(300, 450)
    bear.moveTo(-100, 450)
    paper.add(bear)
    return bear

def animate_bear_movement(bear):
    #
    # Animates the bear's movement from left to center of screen with
    # a bouncing motion by changing vertical position alternately.
    #
    # bear - The Layer object containing the bear to animate.
    #
    # Returns nothing.
    #
    sleep(2)
    bear.moveTo(-75, 425)
    sleep(0.15)
    bear.moveTo(-50, 450)
    sleep(0.15)
    bear.moveTo(-25, 425)
    sleep(0.15)
    bear.moveTo(0, 450)
    sleep(0.15)
    bear.moveTo(25, 425)
    sleep(0.15)
    bear.moveTo(50, 450)
    sleep(0.15)
    bear.moveTo(75, 425)
    sleep(0.15)
    bear.moveTo(100, 450)
    sleep(0.15)
    bear.moveTo(125, 425)
    sleep(0.15)
    bear.moveTo(150, 450)
    sleep(0.15)
    bear.moveTo(175, 425)
    sleep(0.15)
    bear.moveTo(200, 450)
    sleep(0.15)
    bear.moveTo(225, 425)
    sleep(0.15)
    bear.moveTo(250, 450)
    sleep(0.15)
    bear.moveTo(275, 425)
    sleep(0.15)
    bear.moveTo(300, 450)

def show_bear_text():
    #
    # Displays and then removes a text bubble with the bear's message
    # near the first bear's position.
    #
    # There are no parameters.
    #
    # Returns nothing.
    #
    beartext = Text('RAWR! RAWR! I am a Bear!', 16, Point(350, 275))
    paper.add(beartext)
    sleep(2)
    paper.remove(beartext)

def animate_bear2_movement(bear2):
    #
    # Animates the second bear's movement from right to left center
    # with a bouncing motion similar to the first bear.
    #
    # bear2 - The cloned Layer object containing the second bear.
    #
    # Returns nothing.
    #
    bear2.moveTo(1095, 425)
    sleep(0.15)
    bear2.moveTo(1065, 450)
    sleep(0.15)
    bear2.moveTo(1035, 425)
    sleep(0.15)
    bear2.moveTo(1005, 450)
    sleep(0.15)
    bear2.moveTo(975, 425)
    sleep(0.15)
    bear2.moveTo(945, 450)
    sleep(0.15)
    bear2.moveTo(915, 425)
    sleep(0.15)
    bear2.moveTo(885, 450)
    sleep(0.15)
    bear2.moveTo(855, 425)
    sleep(0.15)
    bear2.moveTo(825, 450)

def show_bear2_text():
    #
    # Displays and returns a text bubble with the second bear's message
    # near its position.
    #
    # There are no parameters.
    #
    # Returns the Text object for later removal.
    #
    bear2text = Text('RAWR! RAWR! I am also a Bear!', 16, Point(700, 275))
    paper.add(bear2text)
    return bear2text 

def show_conversation(bear2text):
    #
    # Manages the conversation sequence between the two bears by
    # displaying and removing text bubbles in sequence.
    #
    # bear2text - The Text object to remove at start of conversation.
    #
    # Returns nothing.
    #
    sleep(3)
    paper.remove(bear2text)
    beartext1 = Text('This is my territory...', 16, Point(350, 275))
    paper.add(beartext1)
    sleep(2)
    paper.remove(beartext1)
    bear2text1 = Text('My bad', 16, Point(700, 350))
    paper.add(bear2text1)
    sleep(2)
    paper.remove(bear2text1)

def animate_bear2_leaving(bear2):
    #
    # Animates the second bear's exit by flipping it and moving it
    # back to the right edge with bouncing motion.
    #
    # bear2 - The Layer object containing the second bear.
    #
    # Returns nothing.
    #
    bear2.flip()
    bear2.moveTo(825, 450)
    sleep(0.15)
    bear2.moveTo(855, 425)
    sleep(0.15)
    bear2.moveTo(885, 450)
    sleep(0.15)
    bear2.moveTo(915, 425)
    sleep(0.15)
    bear2.moveTo(945, 450)
    sleep(0.15)
    bear2.moveTo(975, 425)
    sleep(0.15)
    bear2.moveTo(1005, 450)
    sleep(0.15)
    bear2.moveTo(1035, 425)
    sleep(0.15)
    bear2.moveTo(1065, 450)
    sleep(0.15)
    bear2.moveTo(1095, 425)
    sleep(0.15)
    bear2.moveTo(1125, 450)


create_ground()
create_sun()
create_clouds()
create_tree()


bear = create_bear()
animate_bear_movement(bear)
show_bear_text()


bear2 = bear.clone()
bear2.moveTo(1125, 450)
paper.add(bear2)
sleep(2)

animate_bear2_movement(bear2)
bear2text = show_bear2_text() 
show_conversation(bear2text)   
animate_bear2_leaving(bear2)