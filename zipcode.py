from banner import banner

banner("ZIP CODE SORTER", "Blaise")

print("Welcome to the Newaygo County zip code sorter")
zip_code = int(input("Please enter zip code "))


if zip_code == 49309:
    print ("The zip code 49309 is for Bitely")
elif zip_code == 49312:
    print("The zip code 49312 is for Brohman")
elif zip_code == 49337:
    print("The zip code 49337 is for Newaygo and Croton")
elif zip_code == 49412:
    print("The zip code 49412 is for Fremont")
elif zip_code == 49413:
    print("The zip code 49413 is for Fremont")
elif zip_code == 49327:
    print("The zip code 49327 is for Grant")
elif zip_code == 49349:
    print("The zip code 49349 IS FOR White Cloud")
else:
    print(f"The zip code {zip_code} is not in Newaygo County")

input("Would You like to enter another zip code (Y/N)?")