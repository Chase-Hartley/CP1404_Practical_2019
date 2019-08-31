
COLOUR_HEX = {"ALICEBLUE": "#f0f8ff", "BLACK": "#000000", "DARK": "#e9967a",
              "FLORALWHITE": "#fffaf0", "GOLD": "#ffd700", "GREEN": "#00ff00",
              "KHAKI": "#f0e68c", "LAVENDER": "#e6e6fa0",
              "LIGHTCORAL": "##f08080", "MAGENTA": "#ff00ff"}

for i in COLOUR_HEX:
    print("{:<20}".format(i))

colour_choice = input("\nPlease select a colour from the list: ").upper()

while colour_choice != "":
    if colour_choice in COLOUR_HEX:
        print("{}'s hex code is {}".format(colour_choice, COLOUR_HEX[colour_choice]))
    else:
        print("Invalid short state")
    colour_choice = input("\nPlease select a colour from the list: ").upper()


