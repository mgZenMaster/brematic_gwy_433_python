import socket

C_REPEAT = 15
C_PAUSE = 5600
C_TUNE = 350
C_BAUD = 25
C_SPEED = 16

HEAD = "TXP:0,0,{},{},{},{},1,".format(C_REPEAT, C_PAUSE, C_TUNE, C_BAUD)
TAIL = "1,1,{},".format(C_SPEED)
PORT = 49880
HI = "3,1,3,1,"
LO = "3,3,1,1,"
ON = "1,3,1,3,3,"
OFF = "3,1,1,3,1,"


def get_id(string):
    retid = ""
    for bit in string:
        if bit == "1":
            retid += HI
        elif bit == "0":
            retid += LO
        else:
            raise Exception("Invalid bit: {}".format(bit))
    return retid


def char_to_id(char):
    char = char.upper()
    if char == "A":
        return get_id("10000")
    elif char == "B":
        return get_id("01000")
    elif char == "C":
        return get_id("00100")
    elif char == "D":
        return get_id("00010")
    else:
        raise Exception("Invalid unit: {}".format(char))


def send(ip, system, unit, state):
    if state.upper() == "ON":
        statecode = ON
    elif state.upper() == "OFF":
        statecode = OFF
    else:
        raise Exception("Invalid state: {}".format(state))

    ids_code = get_id(system) + char_to_id(unit)
    message = HEAD + ids_code + "3," + statecode + TAIL + ";"
    print(message)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.sendto(message.encode(), (ip, PORT))
