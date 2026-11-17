def share_for(total_paise, people, person):
    base = total_paise // people
    extra = total_paise % people
    if person <= extra:
        return base + 1
    return base


def as_rupees(paise):
    return str(paise // 100) + " rupees " + str(paise % 100) + " paise"


rupees = int(input("Bill rupees: "))
paise = int(input("Bill paise: "))
total_paise = rupees * 100 + paise

people = int(input("How many people are sharing? "))

if people < 1:
    print("There must be at least 1 person to split the bill.")
else:
    print("Bill:", as_rupees(total_paise))
    shares_sum = 0
    for person in range(1, people + 1):
        share = share_for(total_paise, people, person)
        shares_sum = shares_sum + share
        print("Person", person, "pays", share, "paise (" + as_rupees(share) + ")")
    print("Sum of shares:", shares_sum, "paise")
    if shares_sum == total_paise:
        print("Check passed: the shares add up to the bill.")
    else:
        print("Check FAILED: the shares do not add up to the bill.")
