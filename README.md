# Fakemon Collage Creator
This is a EXE, (with an included Python script that it was built from), that creates a Fakemon Collage of your own Fakedex. It is almost entirely customizable, and with it includes the .py file for you to mess with if you wish to alter anything I hard-coded.

Here is an example of what the finished product of my Fakedex looks like: https://cdn.discordapp.com/attachments/470716268874563584/742941921126908054/204405709054410752.png

# Setting Up
1. Open a Spreadsheet editor of your choice. I highly recommend Google Spreadsheets due to how versatile and lightweight it is.

2. You should see an empty, gridded document. On the left side, you should see numbers going downwards. Go to Line 1, and add the following headers, in any order you want:
* N
* Name
* FormName
* Type1
* Type2
* Tag
* Image

If you set up the headers right, you should see column A with "N", column B with "Name", and so on.

3. Fill out your sheet with your Fakemon. Each Fakemon represents a row. Here is what each one represents:
* N: This is the Fakemon's Index Number. You can completely disregard adding anything here. If you don't want it to show up in the collage, add an "E".
* Name: The name of your Fakemon. Do not include the Form Name here!
* FormName: The Fakemon's Form Name. For example, Mega Venusaur would have "Mega" here.
* Tag: This one is the most important on getting the collage to look nice. A Tag represents which stage of evolution this Fakemon exists in. The following tags can be used:
  * 1: This Fakemon does not evolve.
  * 2base: This Fakemon is the first stage of a 2 stage line. This means it can evolve once. ie: Meowth
  * 2final: This Fakemon is the last stage of a 2 stage line. This means it evolved only once. ie: Persian
  * 3base, 3mid, and 3final: Read how 2base and 2final work. This is for 3-staged Fakemon
  * (if it's empty or it's not one of the above): The collage will treat your Fakemon as having no evolution.
* Image: This is also important. You have to provide a DIRECT image link to your Fakemon. Uploading it to imgur and copying the DIRECT image link is the common method. Additionally using Discord Image Links works as well. You want the link that ends with ".png" or ".jpg" or something similar.

4. After you filled out your Fakedex, go to File -> Download -> Comma-Seperated Values (.csv) and save it somewhere.

5. Run the CollageCreator.exe, (or the python file if you have knowledge in Python), and load up the CSV file. If it all works out, then you did it right. Congrats.

# Optional Stuff
The collage creator comes with a folder called "Collage Files" that you can completely personalize your own collages. The things you can change are the following:
* logo.png: This can be any size and shape, (but preferably around the default example logo.png)
* the "t" files: These should be self explanatory. These are the background type images that each Fakemon is placed on. These images must be 600x600 to work correctly, and Type 2 will always overlap Type 1.
* nomon.png: This is what is displayed when no image is supplied or there is an error transcribing and image link.
* font.tff: This is the font used for the names. As of now, there is no way to change the size of the font yet, so I recommend leaving this alone unless you find a font that somehow works at the same size.
