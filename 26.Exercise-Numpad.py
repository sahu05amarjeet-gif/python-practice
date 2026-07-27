num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))


for pad in num_pad:
    for pad_ in pad:
        print(pad_, end=" ")
    print()