#Version 1.1.0 (Barebones)
import pygetwindow
import keyboard

workspaceDictionary = {
    'workspace1': [],
    'workspace2': [],
    'workspace3': [],
    'workspace4': [],
    'workspace5': [],
    'workspace6': [],
    'workspace7': [],
    'workspace8': [],
    'workspace9': []
}
currentWorkspace = 1

for object in pygetwindow.getAllWindows():
    workspaceDictionary['workspace1'].append(object)

def Assign(requestWorkspace):
    reqSpace = workspaceDictionary['workspace' + str(requestWorkspace)]
    wwspace = workspaceDictionary['workspace' + str(currentWorkspace)]
    assign = pygetwindow.getActiveWindow()
    #if item is in requested list
    if assign in reqSpace:
        return
    #if item isn't in entire dictionary
    elif bool(filter(lambda x: assign in x, [workspaceDictionary])) == False:
        reqSpace.append(assign)
        assign.minimize()
    #scan entire dictionary for item and handle it
    else:
        for key, items in workspaceDictionary.items():
            if assign in items:
                dictKey = workspaceDictionary[key]
                dictKey.remove(assign)
                reqSpace.append(assign)
                if dictKey == wwspace:
                    assign.minimize()
                else:
                    break
                
                    
def SetActive(requestSwitch):
    global currentWorkspace
    useSpace = workspaceDictionary['workspace' + str(requestSwitch)]
    if currentWorkspace == requestSwitch:
        return
    else:
        currentWorkspace = requestSwitch
        for windowX in pygetwindow.getAllWindows():
            windowX.minimize()
        for windowY in useSpace:
            windowY.restore()
            
            
def Controls():
    keyboard.add_hotkey('alt + shift + 1', lambda: Assign('1'))
    keyboard.add_hotkey('alt + shift + 2', lambda: Assign('2'))
    keyboard.add_hotkey('alt + shift + 3', lambda: Assign('3'))
    keyboard.add_hotkey('alt + shift + 4', lambda: Assign('4'))
    keyboard.add_hotkey('alt + shift + 5', lambda: Assign('5'))
    keyboard.add_hotkey('alt + shift + 6', lambda: Assign('6'))
    keyboard.add_hotkey('alt + shift + 7', lambda: Assign('7'))
    keyboard.add_hotkey('atl + shift + 8', lambda: Assign('8'))
    keyboard.add_hotkey('alt + shift + 9', lambda: Assign('9'))
    
    keyboard.add_hotkey('alt + 1', lambda: SetActive('1'))
    keyboard.add_hotkey('alt + 2', lambda: SetActive('2'))
    keyboard.add_hotkey('alt + 3', lambda: SetActive('3'))
    keyboard.add_hotkey('alt + 4', lambda: SetActive('4'))
    keyboard.add_hotkey('alt + 5', lambda: SetActive('5'))
    keyboard.add_hotkey('alt + 6', lambda: SetActive('6'))
    keyboard.add_hotkey('alt + 7', lambda: SetActive('7'))
    keyboard.add_hotkey('alt + 8', lambda: SetActive('8'))
    keyboard.add_hotkey('alt + 9', lambda: SetActive('9'))

    keyboard.wait('alt + shift + q')
    
Controls()