import os
import time
import json
import pyperclip
import pyautogui

File = 'Source/Key.txt'

with open ('Source/Data.json', 'r') as DataFile:
    JsonData = json.load (DataFile)

Keys = {
    '56': 'alt',
    '100': 'alt_gr',
    '108': 'arrow_down',
    '105': 'arrow_left',
    '106': 'arrow_right',
    '103': 'arrow_up',
    '14': 'backspace',
    '58': 'caps_lock',
    '15': 'tab',
    '29': 'control',
    '97': 'control_right',
    '127': 'task', # idk what the name is
    '125': 'windows',
    '111': 'delete',
    '102': 'home',
    '107': 'end',
    '28': 'enter',
    '1': 'escape',
    '59': 'f1',
    '60': 'f2',
    '61': 'f3',
    '62': 'f4',
    '63': 'f5',
    '64': 'f6',
    '65': 'f7',
    '66': 'f8',
    '67': 'f9',
    '68': 'f10',
    '87': 'f11',
    '88': 'f12',
    '82': 'num0',
    '79': 'num1',
    '80': 'num2',
    '81': 'num3',
    '75': 'num4',
    '76': 'num5',
    '77': 'num6',
    '71': 'num7',
    '72': 'num8',
    '73': 'num9',
    '69': 'num_lock',
    '98': 'num_slash',
    '55': 'num_star',
    '74': 'num_dash',
    '78': 'num_plus',
    '96': 'num_enter',
    '83': 'num_comma',
    '109': 'page_down',
    '104': 'page_up',
    '119': 'pause_break',
    '70': 'print_screen',
    '99': 'scroll_lock',
    '42': 'shift',
    '54': 'shift_right',
    '57': 'space',
    '30': 'a',
    '48': 'b',
    '46': 'c',
    '32': 'd',
    '18': 'e',
    '33': 'f',
    '34': 'g',
    '35': 'h',
    '23': 'i',
    '36': 'j',
    '37': 'k',
    '38': 'l',
    '50': 'm',
    '49': 'n',
    '24': 'o',
    '25': 'p',
    '16': 'q',
    '19': 'r',
    '31': 's',
    '20': 't',
    '22': 'u',
    '47': 'v',
    '17': 'w',
    '45': 'x',
    '21': 'y',
    '44': 'z',
    '41': 'half',
    '11': '0',
    '2': '1',
    '3': '2',
    '4': '3',
    '5': '4',
    '6': '5',
    '7': '6',
    '8': '7',
    '9': '8',
    '10': '9',
    '12': 'plus',
    '27': 'arrow',
    '43': 'star',
    '53': 'dash',
    '52': 'dot',
    '51': 'comma',
}

def Main ():
    with open (File, 'r') as KeyFile:
        KeyData = KeyFile.read ()

        if '+' in KeyData:
            KeysList = KeyData.split ('+')
            KeysList.reverse ()
            KeyList = []
            for Key in KeysList: KeyList.append (Keys[Key])
            KeyString = '+'.join (KeyList)

            print (f'- {KeyString}')
            HandleKeyPress (KeyString)

        else:
            print (f'- {Keys[KeyData]}')
            HandleKeyPress (Keys[KeyData])

        with open ('Data.json', 'w') as DataFile:
            json.dump (JsonData, DataFile)

def HandleKeyPress (Key):
    if (Key in ('num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'num7', 'num8', 'num9')): ClipboardSystem (Key)
    if (Key in ('num0+num1', 'num0+num2', 'num0+num3', 'num0+num4', 'num0+num5', 'num0+num6', 'num0+num7', 'num0+num8', 'num0+num9')): ClipboardSystem (Key)



###################
# Macro Functions #
###################

def ClipboardSystem (Key):
    # num0 + numX = instant clear the clipboard of that numkey
    if 'num0' in Key:
        Keys = Key.split ('+')
        JsonData['Clipboard'][Keys[1]] = ''

    else:
        Selection = os.popen ('xsel').read ()
        SelectedClipboard = JsonData['Clipboard'][Key]

        if (SelectedClipboard == '' and Selection.strip () not in ('', ' ')):
            JsonData['Clipboard'][Key] = Selection

        if (SelectedClipboard.strip () not in ('', ' ')):
            pyperclip.copy (SelectedClipboard)
            pyautogui.hotkey ('ctrl', 'v')

        else:
            return



################
# Run Function #
################

if __name__ == '__main__':
    Main ()
