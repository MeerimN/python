lst1 = {"notepads": 3, "pens": 5, "pencils": 2, "folders": 5, "organizer": 4}
lst2 = {"pens": 2, "pencils": 3, "folders": 4}

combined = {}

for key, value in lst1.items():
    combined[key] = value

for key, value in lst2.items():
    if key in combined:
        combined[key] += value
    else:
        combined[key] = value

print(combined)