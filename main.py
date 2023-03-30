import UIManager


# Doesnt work because UIManager runs tkinter windows which prevents anything below the import from running 
# Until the tkinter windows have been closed 
# UIManager.statWindow.health.configure(text='It Works')
print('Program Closed.')