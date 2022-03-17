import RPi.GPIO as RT

dac = [26, 19, 13, 6, 5, 11, 9, 10]

RT.setmode(RT.BCM)
RT.setup (dac, RT.OUT)

def dtob(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

try:
    while (1):
        var = input ("Write an integer number in range 0..255:")
        if var == 'q':
            break
        elif var.isdigit () is False:
            try:
                var = int (var)
                if var < 0:
                    print ("Negative number")
                    continue

            except ValueError:
                try:
                    var = float (var)
                except ValueError:
                    print ("A string")
                    continue
                
                print ("Float number")
                continue

        var = int (var)
        if var > 255:
            print ("Out of range")
            continue
        else:
            print ("voltage", var*3.3/256)
            RT.output (dac, dtob(var))
        
finally:
    RT.output (dac, 0)
    RT.cleanup ()
