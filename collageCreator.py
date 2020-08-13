import tkinter as tk
from tkinter import filedialog
import PIL
from PIL import Image
import csv
import math
from PIL import ImageFont
from PIL import ImageDraw
import requests
from io import BytesIO
import re
print("Finished Imports")

def toLit(word):
    return str(word).lower()

def getCol(header, name):
    for i in range(len(header)):
        if header[i].lower().replace(" ","") == name.lower().replace(" ",""):
            return i
    print("failed to find col: " + str(name))
    return -1

def isBaseForm(tag):
    if tag == "1" or tag == "2base" or tag == "3base" or tag == "L":
        return True
    return False

def printTest(family, nameCol, formCol):
    for i in range(len(family)):
        for ii in range(len(family[i])):
            fName = ""
            if formCol != -1 and family[i][ii][formCol]:
                fName = "-"+family[i][ii][formCol]
            print(family[i][ii][nameCol]+fName)
        print()

def printCollage(collageList,nameCol):
    for row in collageList:
        for fam in row:
            l = ""
            for mon in fam:
                l += mon[nameCol] + " "
            print(l)
        print()

def createCollage(dex, headers):

    # Set up headers
    numCol = getCol(headers,"n")
    nameCol = getCol(headers,"name")
    formCol = getCol(headers,"formname")
    imageCol = getCol(headers,"image")
    tagCol = getCol(headers,"tag")
    type1Col = getCol(headers,"type1")
    type2Col = getCol(headers,"type2")

    # Set up Values
    dataFiles = 'Collage Files/'
    maxPerRow = 9 #This is how many mons can appear per row. skips to next row if exceeds
    imageSize = 200
    fontSize = 15
    
    # Sort Fakemon into family groups
    families = []
    family = [] # This temporarily holds the family to append to families[]
    tagScope = "" # Use this to know which tag was previously used
    for i in range(1,len(dex)):

        tag = dex[i][tagCol]
        name = dex[i][nameCol]

        # Ignore mons with no name or tag
        if name == "" or tag == "":
            continue

        # Ignore special characters
        if numCol != -1 and "e" in dex[i][numCol].lower():
            continue

        # Start a new family if we're looking at a new base stage
        if isBaseForm(tag):

            if len(family) == 0:
                print("new base: " + dex[i][nameCol])
                family.append(dex[i])

            else:
                print("family of " + str(len(family))+ "\n")
                families.append(family.copy())
                family.clear()
                family.append(dex[i])
                print("new base: " + dex[i][nameCol])

        else:
            family.append(dex[i])

    # Add the final one if possible
    if len(family) > 0:
        print("family of " + str(len(family))+ "\n")
        families.append(family)

    # printTest(families,nameCol,formCol)

    # Sort Each one into rows based on sizes.
    collageList = []
    collageRow = []
    for row in families:

        # Count how many we have in the current row
        rowCount = 0
        if len(collageRow) != 0:
            for fam in collageRow:
                for mon in fam:
                    rowCount += 1

        # If the row we're going to add is smaller than the max, then add
        if rowCount + len(row) <= maxPerRow:
            collageRow.append(row)

        # Otherwise, add the current row and make a new one
        else:
            # Print Row Info
            rowStr = ""
            for fam in collageRow:
                for mon in fam:
                    rowStr += mon[nameCol] + " "
            print(rowStr)
            collageList.append(collageRow.copy())
            collageRow.clear()
            collageRow.append(row)

    # Add the final row
    if len(collageRow) > 0:
        collageList.append(collageRow.copy())

    print()

    # Create Image
    logoImage = ""
    logoHeight = 0
    logoWidth = 0
    try:
        logoImage = Image.open(dataFiles + "logo.png").convert("RGBA")
        logoHeight = logoImage.height
        logoWidth = logoImage.width
        print("Logo Found")
    except Exception:
        print("Could not open logo.png")
    collageHeight = len(collageList)
    collageWidth = maxPerRow
    collageImage = Image.new('RGB', (collageWidth*imageSize,collageHeight*imageSize+logoHeight),(255, 255, 255))
    colCur = 0

    # Set up Draw info
    draw = ImageDraw.Draw(collageImage)
    font = ImageFont.truetype(dataFiles + "font.ttf", fontSize)
    shadowcolor = "white"
    borderSize = 2

    # Add in Logo and Credits if a logo exists
    if logoHeight > 0:
        
        logoX = math.floor(((imageSize*collageWidth)-logoWidth)/2)
        logoY = 0
        logoLoc = (logoX,logoY)
        collageImage.paste(logoImage,logoLoc,logoImage)

    for row in range(collageHeight):

        # Used to determine the row offset data
        monCount = 0
        for family in collageList[row]:
            for mon in range(len(family)):
                monCount+=1

        xOffset = math.floor(((imageSize*collageWidth)-(monCount*imageSize))/2)
        print("Row #" + str(row+1) + " - Offset: " + str(xOffset))
        
        for family in collageList[row]:
            
            for mon in family:

                # Open the Type Backgrounds if we can
                try:
                    t1 = toLit(mon[type1Col])
                    t2 = toLit(mon[type2Col])
                    primary = Image.open(dataFiles + "t_" + t1 + ".png")
                    secondary = Image.open(dataFiles + "t_" + t1 + "2.png").convert("RGBA")
                    if t2 and " ".join(re.findall("[a-zA-Z]+", t2)) != "":
                        secondary = Image.open(dataFiles + "t_" + t2 + "2.png").convert("RGBA")
                except Exception:
                    print("Forced a Continue")
                    continue

                # Try to open the image link
                # If we fail, or one isn't provided, we use nomon instead
                monImage = ""
                try:
                    response = requests.get(mon[imageCol])
                    monImage = Image.open(BytesIO(response.content)).convert("RGBA")
                except Exception:
                    print("Image not found for " + mon[nameCol])
                    monImage = Image.open(dataFiles + "nomon.png")

                # Thumbnail the images
                tileSize = (imageSize,imageSize)
                primary.thumbnail(tileSize)
                secondary.thumbnail(tileSize)
                monImage.thumbnail(tileSize)

                # Create the location for the tile to paste
                tileX = colCur*imageSize + xOffset
                tileY = row*imageSize + logoHeight
                tileLoc = (tileX,tileY)

                # Create the location for the mon image to paste
                monXOff = math.floor((imageSize-monImage.width)/2)
                monYOff = math.floor((imageSize-monImage.height)/2)
                monX = tileX + monXOff
                monY = tileY + monYOff
                monLoc = (monX,monY)

                # Paste tiles and image
                collageImage.paste(primary,tileLoc,primary)
                collageImage.paste(secondary,tileLoc,secondary)
                collageImage.paste(monImage,monLoc,monImage)

                # Concat name information
                name = mon[nameCol]
                if name == "":
                    name = "???"
                if formCol != -1 and mon[formCol]:
                    name += "-" + mon[formCol]

                # Draw text with border
                x = tileX + 2
                y = tileY + 2
                nameLoc = (x,y)
                text = name
                
                # thin border
                draw.text((x-borderSize, y), text, font=font, fill=shadowcolor)
                draw.text((x+borderSize, y), text, font=font, fill=shadowcolor)
                draw.text((x, y-borderSize), text, font=font, fill=shadowcolor)
                draw.text((x, y+borderSize), text, font=font, fill=shadowcolor)

                # thicker border
                draw.text((x-borderSize, y-borderSize), text, font=font, fill=shadowcolor)
                draw.text((x+borderSize, y-borderSize), text, font=font, fill=shadowcolor)
                draw.text((x-borderSize, y+borderSize), text, font=font, fill=shadowcolor)
                draw.text((x+borderSize, y+borderSize), text, font=font, fill=shadowcolor)

                # Draw Text
                draw.text(nameLoc,name,(0,0,0),font=font)

                print("Added " + mon[nameCol])
                colCur += 1

        # Reset the column
        colCur = 0
        print()

    return collageImage

# Main Program Test
dex = []
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
with open(file_path, 'r', encoding="utf-8") as f:
    reader = csv.reader(f)
    dex = list(reader)

headers = dex[0]
collageImage = createCollage(dex,headers)
collageImage.save("output.png")
a = input("Done")
