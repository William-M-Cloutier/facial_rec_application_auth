import win32gui
import win32con
import os
import face

secret_folder = "ProjectIdea"
path =  r"D:\Users\17608\Desktop\ProjectIdea"
global END
END = False

def winEnumHandler( hwnd, ctx ):
    global END
    if win32gui.IsWindowVisible( hwnd ):
        if os.path.basename(path) in win32gui.GetWindowText(hwnd):
            # print(win32gui.GetWindowText(hwnd))
            win32gui.PostMessage(hwnd,win32con.WM_CLOSE,0,0)
            print("Please wait. Confirming Facial Identity.")
            result = face.auth_verification()

            if result:
                os.startfile(path)
                print("Huzza. Enjoy your Files")
                END = True
            else:
                print("Unauthorized User.")
            # os.startfile(path)
            # print(os.path.dirname(path))

while not END:
    win32gui.EnumWindows( winEnumHandler, None )