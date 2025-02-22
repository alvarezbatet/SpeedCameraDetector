with open("radars.txt", "r") as myfile:
    radars = myfile.readlines()[0]
    for radar in radars.split(','):
        radar = radar.split(' ')
        print(radar)