__author__ = 'robin.hall'

class Locker:

    # Create a closed locker
    def __init__(self, n):

        self.LockerNumber = n
        self.Open = 0

    # Open or close the door
    def OpenOrClose(self):

        self.Open = abs(self.Open - 1)

#Make a list of a load of closed lockers
schoolLockers = [Locker(n) for n in range(1, 1001)]

#Loop through all pupils
for p in range(0, len(schoolLockers)):

    #Loop through all lockers
    for n in range(0, len(schoolLockers)):

        #Is the locker number a multiple of the pupil number ( locker mod pupil = 0 )
        if schoolLockers[n].LockerNumber % (p+1) == 0:

            #Open/close the door
            schoolLockers[n].OpenOrClose()

#Loop through all lockers
for n in range(0, len(schoolLockers)):

    #Is it open
    if schoolLockers[n].Open == 1:

        #Print its number
        print(schoolLockers[n].LockerNumber, schoolLockers[n].LockerNumber ** 0.5 )








