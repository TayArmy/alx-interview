def canUnlockAll(boxes):
    keys = set([0])  # Start with the key to the first box
    unlocked = [False] * len(boxes)  # Keep track of which boxes are unlocked
    unlocked[0] = True  # The first box is initially unlocked

    while keys:
        box = keys.pop()
        for key in boxes[box]:
            if key < len(boxes) and not unlocked[key]:
                unlocked[key] = True
                keys.add(key)

    return all(unlocked)  # Check if all boxes are unlocked
