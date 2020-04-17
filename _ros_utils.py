# from playsound import playsound

def indata():
    file = None
    with open('_input.txt', 'r') as f:
        file = f.read()
    print('Inputs Read')
    return file

def outdata(out):
    with open('_output.txt', 'w') as f:
        f.write(out)
    print('Outputs Saved')
    # playsound('ping.wav')