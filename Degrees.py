def RAtoDegrees(RA):
    RA = RA.split(':')
    return (float(RA[0]) + float(RA[1])/60 + float(RA[2])/3600) * 15

def DecToDegrees(Dec):
    Dec = Dec.split(':')
    if '-' in Dec[0]:
        return (float(Dec[0]) - float(Dec[1])/60 - float(Dec[2])/3600)
    else:
        return (float(Dec[0]) + float(Dec[1])/60 + float(Dec[2])/3600)
    
def RAtoRads(RA): pass