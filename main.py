def tally(input):
    # Variables init
    cost = 0
    start_at = 0
    num_soda = 0
    num_popcorn = 0
    num_combo = 0

    # Keeps count of each number of items.
    for item in input:
        # Keeps count of every item
        if item[11:] =='soda':
            num_soda += 1
        elif item[11:] == 'popcorn':
            num_popcorn += 1

    # Keeps count of each combo
    for i in range(len(input)):
        # Takes first item and checks it against the next in the list by incrementing start_at by 1
        start_at += 1

        for j in range(start_at,len(input)):
            # Takes the Previous item and checks it with the next then starts at the next one
            # Ex. [A, B, C, D] = A checks B, C, and D, then B checks, C, and D, and so on
            if input[i][:10] == input[j][:10]:
                if input[i][11:] != input[j][11:]:
                    # Combos is incremented when same date, but different items
                    num_combo += 1
                    break

    # Since a combo has a soda and popcorn, we can subtract number of combos from each item.
    total = (num_soda - num_combo)*2.50 + (num_popcorn - num_combo)*7.00 + num_combo*9.00
    print(total)


tally(["2022-06-01,soda"])

tally(["2021-11-15,popcorn",
       "2021-11-15,popcorn",
       "2021-11-15,soda",
       "2021-11-15,soda", ])

tally(["2019-12-29,popcorn",
    "2020-01-03,popcorn",
    "2020-01-03,soda",
    "2020-01-03,soda",
    "2020-02-22,popcorn",
    "2020-02-22,soda", ])

tally(["2019-12-29,soda",
    "2020-01-03,popcorn",
    "2020-01-03,soda",
    "2020-01-03,soda",
    "2020-02-22,popcorn",
    "2020-02-22,soda",])
