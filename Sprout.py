#Version 1.0.0
import pygetwindow
import keyboard

workspace1 = []
workspace2 = []
workspace3 = []
workspace4 = []
workspace5 = []
workspace6 = []
workspace7 = []
workspace8 = []
workspace9 = []

currentWorkspace = 1

#Assing all titles at start to workspace1
for object in pygetwindow.getAllWindows():
    workspace1.append(object)

def Popper(popName):
    match currentWorkspace:
        case 1:
            workspace1.remove(popName)
        case 2:
            workspace2.remove(popName)
        case 3:
            workspace3.remove(popName)
        case 4:
            workspace4.remove(popName)
        case 5:
            workspace5.remove(popName)
        case 6:
            workspace6.remove(popName)
        case 7:
            workspace7.remove(popName)
        case 8:
            workspace8.remove(popName)
        case 9:
            workspace9.remove(popName)
        case other:
            return
            

#Assign active window to workspace
def AssignWorkspace1():
    assign = pygetwindow.getActiveWindow()
    if assign in workspace1:
        return
    else:
        Popper(assign)
        workspace1.append(assign)
        assign.minimize()
    
def AssignWorkspace2():
    assign = pygetwindow.getActiveWindow()
    if assign in workspace2:
        return
    else:
        Popper(assign)
        workspace2.append(assign)
        assign.minimize()
    
def AssignWorkspace3():
    assign = pygetwindow.getActiveWindow()
    if assign in workspace3:
        return
    else:
        Popper(assign)
        workspace3.append(assign)
        assign.minimize()
    
def AssignWorkspace4():
    assign = pygetwindow.getActiveWindow()
    if assign in workspace4:
        return
    else:
        Popper(assign)
        workspace4.append(assign)
        assign.minimize()
    
def AssignWorkspace5():
    assign = pygetwindow.getActiveWindow()
    if assign in workspace5:
        return
    else:
        Popper(assign)
        workspace5.append(assign)
        assign.minimize()
    
def AssignWorkspace6():
    assign = pygetwindow.getActiveWindow()
    if assign in workspace6:
        return
    else:
        Popper(assign)
        workspace6.append(assign)
        assign.minimize()
    
def AssignWorkspace7():
    assign = pygetwindow.getActiveWindow()
    if assign in workspace7:
        return
    else:
        Popper(assign)
        workspace7.append(assign)
        assign.minimize()
    
def AssignWorkspace8():
    assign = pygetwindow.getActiveWindow()
    if assign in workspace8:
        return
    else:
        Popper(assign)
        workspace8.append(assign)
        assign.minimize()
    
def AssignWorkspace9():
    assign = pygetwindow.getActiveWindow()
    if assign in workspace9:
        return
    else:
        Popper(assign)
        workspace9.append(assign)
        assign.minimize()

#Moving the pseudo view to another workspace    
def SetActive1():
    global currentWorkspace
    if currentWorkspace == 1:
        return
    else:
        currentWorkspace = 1
        for window in pygetwindow.getAllWindows():
            window.minimize()
        for y in workspace1:
            y.restore()

def SetActive2():
    global currentWorkspace
    if currentWorkspace == 2:
        return
    else:
        currentWorkspace = 2
        for x in pygetwindow.getAllWindows():
            x.minimize()
        for y in workspace2:
            y.restore()

def SetActive3():
    global currentWorkspace
    if currentWorkspace == 3:
        return
    else:
        currentWorkspace = 3
        for x in pygetwindow.getAllWindows():
            x.minimize()
        for y in workspace3:
            y.restore()

def SetActive4():
    global currentWorkspace
    if currentWorkspace == 4:
        return
    else:
        currentWorkspace = 4
        for x in pygetwindow.getAllWindows():
            x.minimize()
        for y in workspace4:
            y.restore()

def SetActive5():
    global currentWorkspace
    if currentWorkspace == 5:
        return
    else:
        currentWorkspace = 5
        for x in pygetwindow.getAllWindows():
            x.minimize()
        for y in workspace5:
            y.restore()

def SetActive6():
    global currentWorkspace
    if currentWorkspace == 6:
        return
    else:
        currentWorkspace = 6
        for x in pygetwindow.getAllWindows():
            x.minimize()
        for y in workspace6:
            y.restore()

def SetActive7():
    global currentWorkspace
    if currentWorkspace == 7:
        return
    else:
        currentWorkspace = 7
        for x in pygetwindow.getAllWindows():
            x.minimize()
        for y in workspace7:
            y.restore()

def SetActive8():
    global currentWorkspace
    if currentWorkspace == 8:
        return
    else:
        currentWorkspace = 8
        for x in pygetwindow.getAllWindows():
            x.minimize()
        for y in workspace8:
            y.restore()

def SetActive9():
    global currentWorkspace
    if currentWorkspace == 9:
        return
    else:
        currentWorkspace = 9
        for x in pygetwindow.getAllWindows():
            x.minimize()
        for y in workspace9:
            y.restore()

#Hotkeys
def Controls():
    keyboard.add_hotkey('alt + shift + 1', AssignWorkspace1)
    keyboard.add_hotkey('alt + shift + 2', AssignWorkspace2)
    keyboard.add_hotkey('alt + shift + 3', AssignWorkspace3)
    keyboard.add_hotkey('alt + shift + 4', AssignWorkspace4)
    keyboard.add_hotkey('alt + shift + 5', AssignWorkspace5)
    keyboard.add_hotkey('alt + shift + 6', AssignWorkspace6)
    keyboard.add_hotkey('alt + shift + 7', AssignWorkspace7)
    keyboard.add_hotkey('alt + shift + 8', AssignWorkspace8)
    keyboard.add_hotkey('alt + shift + 9', AssignWorkspace9)
    
    keyboard.add_hotkey('alt + 1', SetActive1)
    keyboard.add_hotkey('alt + 2', SetActive2)
    keyboard.add_hotkey('alt + 3', SetActive3)
    keyboard.add_hotkey('alt + 4', SetActive4)
    keyboard.add_hotkey('alt + 5', SetActive5)
    keyboard.add_hotkey('alt + 6', SetActive6)
    keyboard.add_hotkey('alt + 7', SetActive7)
    keyboard.add_hotkey('alt + 8', SetActive8)
    keyboard.add_hotkey('alt + 9', SetActive9)
    
    keyboard.wait('alt + shift + q')
    
Controls()