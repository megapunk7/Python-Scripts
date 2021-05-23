baneshworChwok = {'minbhawan': 'red', 'oldBaneshwor' : 'green'}

def switchLights(chowk):
    for key in chowk.keys():
        if chowk[key] == 'red':
            chowk[key] = 'green'
        elif chowk[key] == 'green':
            chowk[key] = 'yellow'
        elif chowk[key] == 'yellow':
            chowk[key] = 'red'
    assert 'red' in chowk.keys(), "One of the lights must be Red"

print(baneshworChwok)
switchLights(baneshworChwok)
print(baneshworChwok)