def knapSack(values, volumes, capacity):
    assert len(values) == len(volumes)

    for x in volumes:
        assert x == round(x)

    # totals is a dictionary of total volumes to highest (known) total values
    totals = {0: 0}
    max_value = 0

    for value, volume in zip(values, volumes):
        for total_volume, total_value in list(totals.items()):
            new_volume = total_volume + volume
            new_value = total_value + value
            if new_volume <= capacity and new_value > totals.get(new_volume, 0):
                totals[new_volume] = new_value
                if new_value > max_value:
                    max_value = new_value
        
    return max_value