phone_book = {}

phone_book["jenny"] = "8675309"
phone_book["emergency"] = "911"


print(phone_book["jenny"])

print("jenny" in phone_book)

voted = {}

def check_voter(name) :
    if name in voted:
        print("kick")
    else:
        voted[name] = True
        print("voted")


check_voter("jenny")
check_voter("mike")
check_voter("mike")