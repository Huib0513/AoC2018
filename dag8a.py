#!python3

#tree = open('testinput.dag8').read().split(' ')
tree = open('input.dag8').read().split(' ')
print(tree, len(tree))

# Yuck, globale variabele...
index = 0

def verwerkNode():
    global index

    resultaat = 0
    # Lees header
    aantalkids = int(tree[index])
    aantalmetas = int(tree[index + 1])
    index += 2
    kindwaarde = []
    print("Header gelezen: " + str(aantalkids) + " kinderen en " + str(aantalmetas) + " meta-informatie.")

    # Verwerk kinderen
    for kind in range(aantalkids):
        print("Child number " + str(kind + 1))
        kindwaarde.append(verwerkNode())

    if aantalkids == 0:
        # Verwerk metadata
        for meta in range(aantalmetas):
            resultaat += int(tree[index])
            index += 1
    else:
        for meta in range(aantalmetas):
            ref = int(tree[index])
            if ref <= aantalkids:
                resultaat += kindwaarde[(ref-1)]
            index += 1
    print("Waarde node: " + str(resultaat) + ", kindwaarde: " + str(kindwaarde))
    return resultaat


# Main loop
totaalmeta = 0 + verwerkNode()

print("Het winnende nummer is: " + str(totaalmeta))
