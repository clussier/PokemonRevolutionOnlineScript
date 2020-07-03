#RyanWalk:6/24/20:BattleDetect.py
import pyscreenshot
import ImageComp
from matplotlib.image import imread
from PIL import Image
import pytesseract
import cv2
#d
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR/tesseract.exe'
sideMargin = 0.2037037037
movesetRegionLeftStart = 0.629629629
verticalMargin= 0.1866666666

def Bat():
    """
    Grabs screenshot of active screen and compares the battle options section area to a screenshot of
    a battle and calculate the difference in pixels.

    The area that the function crops to get the battle options section will differ depending on screen
    resolution. You can adjust the spot with the left, top, right, and bottom, variables

    :return: the meansquare error difference of the two cropped photos
    """
    #Screenshot the active screen
    im = pyscreenshot.grab()

    #Calculate spot of battle pane (specifically the battle options area)
    width, height = im.size
    left = (1 - sideMargin*1.6) * width
    top = verticalMargin * height * 3.5
    right = (1 - sideMargin) * width
    bottom = (1 - verticalMargin*1.5) * height

    #Croping the battle options section from the screenshot
    img1 = im.crop((left,top,right,bottom))
    img1 = img1.convert('LA')
    img1.save("battletest.png")

    #Croping the battle options section from a battle image
    img2 = Image.open(r"C:\Users\cluss\PyCharmProjects\PokemonRevolution\Images\BurnedTowerTop.png").convert('LA')
    img2 = img2.crop((left,top,right,bottom))
    img2.save("ABattle1.png")

    #Converting to numpy
    base = imread(r"C:\Users\cluss\PyCharmProjects\PokemonRevolution\ABattle1.png")
    new = imread(r"C:\Users\cluss\PyCharmProjects\PokemonRevolution\battletest.png")

    #Compare new screenshot w battle screenshot using mean squared error
    dif = ImageComp.mse(base, new)
    print("Battle Screen: "+ str(dif))
    return dif

def Cropn():
    """
    Crops the section for which the name of the pokemon appears in a battle screen.
    Note that there is no perfect value for left that will correctly crop the name for
    every pokemon in Pokemon Revolution online. You will have to adjust your name database
    based off your values for left. (For instance, I have 'haunter' saved as 'aaunter' because the
    'h' is cropped off with teh current settings)

    The area that the function crops to get the battle options section will differ depending on screen
    resolution. You can adjust the spot with the left, top, right, and bottom, variables
    """
    #grab the wild pokemons name
    im = pyscreenshot.grab()
    #Calculate spot of battle pane
    width, height = im.size
    left   = 0.459800000 * width
    top    = 0.200000000 * height
    right  = 0.666666667 * width
    bottom = 0.266666667 * height
    im = im.crop((left,top,right,bottom))
    im = im.convert('LA')
    im.save("name.png")

def CheckIfOnLoginScreen():
    """
    Crops Login area to check if on homesecreen. Returns True if on homescreen and False if not

    The area that the function crops to get the battle options section will differ depending on screen
    resolution. You can adjust the spot with the left, top, right, and bottom, variables
    """
    #grab the wild pokemons name
    im = pyscreenshot.grab()
    #Calculate spot of battle pane
    width, height = im.size
    left   = 0.259800000 * width
    top    = 0.200000000 * height
    right  = 0.666666667 * width
    bottom = 0.466666667 * height
    im = im.crop((left,top,right,bottom))
    im = im.convert('LA')
    im.save("HomescreenTest.png")

    im2 = Image.open(r"C:\Users\cluss\PyCharmProjects\PokemonRevolution\Images\Homescreen.png")
    im2 = im2.crop((left,top,right,bottom))
    im2 = im2.convert('LA')
    im2.save("ALogin1.png")

    #Converting to numpy
    base = imread(r"C:\Users\cluss\PyCharmProjects\PokemonRevolution\ALogin1.png")
    new = imread(r"C:\Users\cluss\PyCharmProjects\PokemonRevolution\HomescreenTest.png")

    #Compare new screenshot w battle screenshot using mean squared error
    dif = ImageComp.mse(base, new)
    print("Login Screen: " + str(dif))
    if dif < .1:
        return True
    return False

def CropHealth():
    """
    Crops the section for which the health of the pokemon appears in a battle screen.
    Note that there is no perfect value for left that will correctly crop the health for
    every pokemon in Pokemon Revolution online. You will have to adjust your name database
    based off your values for left. (For instance, I have 'haunter' saved as 'aaunter' because the
    'h' is cropped off with teh current settings)

    The area that the function crops to get the battle options section will differ depending on screen
    resolution. You can adjust the spot with the left, top, right, and bottom, variables
    """
    #Screenshot the active screen
    im = pyscreenshot.grab()
    #Calculate the spot of the healthbar
    width, height = im.size
    left   = 0.610000000 * width
    top    = 0.648000000 * height
    right  = 0.630000000 * width
    bottom = 0.652000011 * height
    im = im.crop((left,top,right,bottom))
    im = im.convert('RGB')
    im.save("healthbar.png")
def Read():
    name = cv2.imread(r"C:\Users\cluss\PycharmProjects\PokemonRevolution\name.png")
    text = pytesseract.image_to_string(name)
    text = text.lower()
    text = text.strip()
    text = text.split()
    text.insert(0,' ')
    text = text[int(len(text))-1]
    if text != " " and text != "sf.":
        print(text)
        return text
