member = input("Enter a new member.")

file = open('members.txt', 'a')
file.write(f"\n{member}")
file.close()