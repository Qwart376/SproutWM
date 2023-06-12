#Version 1.2.0
import pygetwindow
import keyboard
import ctypes

workspaceDictionary = {
    'workspace1': {
        'windows': [],
        'mode': ''
    },
    'workspace2': {
        'windows': [],
        'mode': ''
    },
    'workspace3': {
        'windows': [],
        'mode': ''
    },
    'workspace4': {
        'windows': [],
        'mode': ''
    },
    'workspace5': {
        'windows': [],
        'mode': ''
    },
    'workspace6': {
        'windows': [],
        'mode': ''
    },
    'workspace7': {
        'windows': [],
        'mode': ''
    },
    'workspace8': {
        'windows': [],
        'mode': ''
    },
    'workspace9': {
        'windows': [],
        'mode': ''
    }
}

windowList = []
globalWindows = []
currentWorkspace = 1
switchMode = 1


#assigns all present at start to workspace1, besides windows ones
for object in pygetwindow.getAllWindows():
    if ('title=\"\"' in str(object)) or ('title=\"Settings\"' in str(object)) or ('title=\"Program Manager\"' in str(object)):
        globalWindows.append(object)
    else:
        workspaceDictionary['workspace1']['windows'].append(object)
        windowList.append(object)

#assigns windows to workspace
def Assign(requestWorkspace):
    requestSpace = workspaceDictionary['workspace' + str(requestWorkspace)]['windows']
    assign = pygetwindow.getActiveWindow()
    #if item is in requested list
    if assign in requestSpace:
        return
    #if item wasn't assigned before
    elif any(assign in sublist for sublist in [windowList, globalWindows]) == False:
        requestSpace.append(assign)
        windowList.append(assign)
        if requestWorkspace != currentWorkspace:
            assign.hide()
    #scan entire dictionary for item and handle it
    else:
        for key, work in workspaceDictionary.items():
            for list, values in work.items():
                for value in values:
                    if value == assign:
                        dictKey = workspaceDictionary[key][list]
                        dictKey.remove(assign)
        requestSpace.append(assign)
        if requestWorkspace != currentWorkspace:
            assign.hide()


#switches view to workspace
def SetActive(requestSwitch):
    global currentWorkspace
    requestedWorkspace = workspaceDictionary['workspace' + str(requestSwitch)]['windows']
    if currentWorkspace == requestSwitch:
        return
    else:
        currentWorkspace = requestSwitch
        for windowX in windowList:
            windowX.hide()
        for windowY in requestedWorkspace:
            windowY.show()

#assigns window to workspace without removing it from previous one
def MultiAssign(requestWork):
    req = workspaceDictionary['workspace' + str(requestWork)]['windows']
    assignM = pygetwindow.getActiveWindow()
    #if item is in requested list
    if assignM in req:
        return
    else:
        req.append(assignM)

def ColumnSplit(requestA):
    listerA = workspaceDictionary['workspace' + str(currentWorkspace)]['windows']
    windowsA = len(listerA)
    xA, yA = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)
    columnSizeA = (xA / windowsA) + 12 #pading on right side
    staleA = 0 - 7 #padding on the left corner
    for windowA in listerA:
        if windowA.isMinimized == True:
            windowA.restore()
        windowA.resizeTo(int(columnSizeA), int(yA + 5)) #gap on the bottom corner
        windowA.moveTo(int(staleA), 0)
        staleA += columnSizeA - 12 #gap between windows
    
def VerticalSplit(requestB):
    listerB = workspaceDictionary['workspace' + str(currentWorkspace)]['windows']
    windowsB = len(listerB)
    xB, yB = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)
    columnSizeB = (yB / windowsB) + 6
    staleB = 0
    for windowB in listerB:
        windowB.resizeTo(int(xB) + 10, int(columnSizeB)) #gap on the right
        windowB.moveTo(-5, int(staleB))
        staleB += columnSizeB - 8  #gap between windows

def Quit():
    for windowQ in windowList.items():
        windowQ.show()
        windowQ.minimize()
    for activeQ in workspaceDictionary['workspace' + str(currentWorkspace)]['windows']:
        activeQ.restore()

keyboard.add_hotkey('alt + shift + 1', lambda: Assign('1'))
keyboard.add_hotkey('alt + shift + 2', lambda: Assign('2'))
keyboard.add_hotkey('alt + shift + 3', lambda: Assign('3'))
keyboard.add_hotkey('alt + shift + 4', lambda: Assign('4'))
keyboard.add_hotkey('alt + shift + 5', lambda: Assign('5'))
keyboard.add_hotkey('alt + shift + 6', lambda: Assign('6'))
keyboard.add_hotkey('alt + shift + 7', lambda: Assign('7'))
keyboard.add_hotkey('alt + shift + 8', lambda: Assign('8'))
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
keyboard.add_hotkey('alt + 0', lambda: SetActive('0'))

keyboard.add_hotkey('alt + ctrl + 1', lambda: MultiAssign('1'))
keyboard.add_hotkey('alt + ctrl + 2', lambda: MultiAssign('2'))
keyboard.add_hotkey('alt + ctrl + 3', lambda: MultiAssign('3'))
keyboard.add_hotkey('alt + ctrl + 4', lambda: MultiAssign('4'))
keyboard.add_hotkey('alt + ctrl + 5', lambda: MultiAssign('5'))
keyboard.add_hotkey('alt + ctrl + 6', lambda: MultiAssign('6'))
keyboard.add_hotkey('alt + ctrl + 7', lambda: MultiAssign('7'))
keyboard.add_hotkey('alt + ctrl + 8', lambda: MultiAssign('8'))
keyboard.add_hotkey('alt + ctrl + 9', lambda: MultiAssign('9'))

keyboard.add_hotkey('alt + shift + d', lambda: ColumnSplit(0))
keyboard.add_hotkey('alt + shift + c', lambda: VerticalSplit(0))

keyboard.add_hotkey('alt + r', RestoreWE)

keyboard.wait('alt + shift + q', Quit)