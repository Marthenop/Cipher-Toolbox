from Modules import Broadcast,ClrTrm,Furthark,PixelatedNightmare,Rando,Sarra,Somnium

while __name__ in '__main__':
    Begining = input('Enter your command now. (Enter Help for a list of commands)\n\n')
    ClrTrm.clear()

    match Begining:

        case "Help":
            ClrTrm.clear()
            print("Current commands are:\nRando\nSarra\nBroadcast\nHER\nExit\n")
            input("")
            ClrTrm.clear()
        
        case "Rando":
            Rando.begin()

        case "Somnium":
            Somnium.begin()

        case "Sarra":
            Sarra.begin()

        case "Broadcast":
            Broadcast.begin()

        case "HER":
            PixelatedNightmare.begin()
            
        case "Hare":
            HareTrick.begin()
            
        case "Exit":
            exit()
