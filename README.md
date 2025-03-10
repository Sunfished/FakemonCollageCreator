# Fakemon Collage Creator
This is a EXE, (with an included Python script that it was built from), that creates a Fakemon Collage of your own Fakedex. It is almost entirely customizable, and with it includes the .py file for you to mess with if you wish to alter anything I hard-coded.

Here is an example of what the finished product of my Fakedex looks like: https://cdn.discordapp.com/attachments/470716268874563584/742941921126908054/204405709054410752.png

# Disclaimer
For some users, using the EXE will trigger responses from anti-virus programs due to how I converted the .py file into an .exe. I can assure you there isn't a virus, and you can run as many tests on it with online programs if you're worried. If you're still wary about using the EXE, then the only other method is to install python and the required libraries, both of which I won't detail here. Use Google!

# Setting Up
If you have any trouble with any of the steps, especially with steps 2 and 3, feel free to view my own spreadsheet as an example here: https://docs.google.com/spreadsheets/d/1_HaGh0U4GXMOpMDbTmB6zm9DqHrm2DHQWYVhaYdBZlY/edit#gid=0

1. Open a Spreadsheet editor of your choice. I highly recommend Google Spreadsheets due to how versatile and lightweight it is.

2. You should see an empty, gridded document. On the left side, you should see numbers going downwards. Go to Line 1, and add the following headers, in any order you want:
* N
* Name
* FormName
* Type1
* Type2
* Tag
* Image

3. Fill out your sheet with your Fakemon. Each Fakemon represents a row. Here is what each one represents:
* N: This is the Fakemon's Index Number. You can completely disregard adding anything here. If you don't want it to show up in the collage, add an "E".
* Name: The name of your Fakemon. Do not include the Form Name here! Any Fakemon without a name will be ignored by the tool, so add a placeholder name.
* FormName: The Fakemon's Form Name. For example, Mega Venusaur would have "Mega" here.
* Tag: This one is the most important on getting the collage to look nice. A Tag represents which stage of evolution this Fakemon exists in. The following tags can be used:
  * 1: This Fakemon does not evolve.
  * 2base: This Fakemon is the first stage of a 2 stage line. This means it can evolve once. ie: Meowth
  * 2final: This Fakemon is the last stage of a 2 stage line. This means it evolved only once. ie: Persian
  * 3base, 3mid, and 3final: Read how 2base and 2final work. This is for 3-staged Fakemon
  * (if it's empty or it's not one of the above): The collage will treat your Fakemon as having no evolution.
* Image: This is also important. You have to provide a DIRECT image link to your Fakemon. Uploading it to imgur and copying the DIRECT image link is the common method. Additionally using Discord Image Links works as well. You want the link that ends with ".png" or ".jpg" or something similar.

4. After you filled out your Fakedex, go to File -> Download -> Comma-Seperated Values (.csv) and save it somewhere.

5. Run the CollageCreator.exe, (or the python file if you have knowledge in Python), and load up the CSV file. If it all works out, then you did it right. Congrats. If the program crashes without any warning, then you messed up somewhere. I'd recommend re-reading the above steps.

# Optional Stuff
The collage creator comes with a folder called "Collage Files" that you can completely personalize your own collages. The things you can change are the following:
* logo.png: This can be any size and shape, (but preferably around the default example logo.png). If you don't want a logo, just delete the file.
* the "t" files: These should be self explanatory. These are the background type images that each Fakemon is placed on. These images must be 600x600 to work correctly, and Type 2 will always overlap Type 1.
* nomon.png: This is what is displayed when no image is supplied or there is an error transcribing and image link.
* font.tff: This is the font used for the names. As of now, there is no way to change the size of the font yet, so I recommend leaving this alone unless you find a font that somehow works at the same size.

# Something Went Wrong!

1. **All my images are missing!** - Make sure you're using direct image links. They should end with a file extension such as ".png" or ".jpg".
1. **My evolutions are split up in different rows!** - Make sure you tag them correctly. View my example document to see how I did it.
1. **Some Fakemon don't show up?** - Only Fakemon with names show up. Please add a temporary placeholder name.

If your issue isn't listed here, or you absolutely can't figure out what you did wrong, feel free to open an issue.
