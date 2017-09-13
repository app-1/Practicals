
COLOUR_NAMES = {'ALICE BLUE': '#f0f8ff', 'ANTIQUE_WHITE': '#faebd7', 'ANTIQUE WHITE1': '#ffefdb',
                'ANTIQUE WHITE2': '#eedfcc', 'ANTIQUE WHITE3': '#cdc0b0', 'ANTIQUE WHITE': '#8b8378',
                'AQUA MARINE1': '#7fffd4', 'AQUA MARINE2': '#76eec6', 'AQUA MARINE4': '#458b74', 'AZURE1': '#f0ffff'}

colour_name = input('Enter colour name: ').upper()
while colour_name != '':
    if colour_name in COLOUR_NAMES:
        print(COLOUR_NAMES[colour_name])
    else:
        print('Invalid name')
    colour_name = input('Enter colour name: ').upper()
