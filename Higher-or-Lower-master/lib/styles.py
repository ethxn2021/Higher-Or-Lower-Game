from termcolor import colored 

welcomeMessage = r"""
  _____                       _______ _            _   _                 _               
 / ____|                     |__   __| |          | \ | |               | |              
| |  __ _   _  ___  ___ ___     | |  | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
| | |_ | | | |/ _ \/ __/ __|    | |  | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
| |__| | |_| |  __/\__ \__ \    | |  | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
 \_____|\__,_|\___||___/___/    |_|  |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                         
"""

welcomeMessage = colored(welcomeMessage,"blue")







higherMessage = r"""
 _    _ _       _               
| |  | (_)     | |              
| |__| |_  __ _| |__   ___ _ __ 
|  __  | |/ _` | '_ \ / _ \ '__|
| |  | | | (_| | | | |  __/ |   
|_|  |_|_|\__, |_| |_|\___|_|   
           __/ |                
          |___/      
"""

higherMessage = colored(higherMessage,"yellow")


lowerMessage = r"""
 _                            
| |                           
| |     _____      _____ _ __ 
| |    / _ \ \ /\ / / _ \ '__|
| |___| (_) \ V  V /  __/ |   
|______\___/ \_/\_/ \___|_|      
"""

lowerMessage = colored(lowerMessage,"yellow")




gameOverMessage = r"""
  _____                         ____                 _ _ _ 
 / ____|                       / __ \               | | | |
| |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __| | | |
| | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__| | | |
| |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |  |_|_|_|
 \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|  (_|_|_)    
"""

gameOverMessage = colored(gameOverMessage,"red")






correctMessage = r"""
  _____                         _   
 / ____|                       | |  
| |     ___  _ __ _ __ ___  ___| |_ 
| |    / _ \| '__| '__/ _ \/ __| __|
| |___| (_) | |  | | |  __/ (__| |_ 
 \_____\___/|_|  |_|  \___|\___|\__|
 """

correctMessage = colored(correctMessage,"green")

theMenu = """
1. Start
2. Rules
3. Quit
""".replace(" ","")

theMenu = colored(theMenu,"yellow") + "\nOption:"
