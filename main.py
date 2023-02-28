import re

def test(character):
    tree = {}
    num = 0

    if character in kb:
        return True
    else:
        facts = [k.replace("=>"+character, "") for k in kb if k[-1] == character]
        if len(facts) > 0:
            for f in facts:
                if "^" in f:
                    fact = f.replace("^", "")
                    tree[num] = [l for l in fact]
                    num += 1
                elif "v" in f:
                    fact = f.replace("v", "")
                    for l in fact:
                        tree[num] = l
                        num += 1
            for n in range(num):
                x = list(map(test, tree[n]))
                if False not in x:
                    kb.append(character)
                    return True
        return False

print("This is an extended propositional backward chaining system.\nYour knowledge base can only accept facts like:\n"
      "P1^P2^...^PK => P, or\nP1vP2v...VPK => P, or\nP.\n"
      "Enter your knowledge base. Type 'nil' to finish input.")

kb = []
while True:
    line = input()
    if line == 'nil':
        break
    pattern = r'^[a-zA-Z](([\^v][a-zA-Z])*(=>))?[a-zA-Z]?'
    match = re.fullmatch(pattern, line)
    if match is not None:
        kb.append(line)
    else:
        print("Invalid proposition")
print("You finished your input. You can now test your system. Exit the system with 'quit'")
while True:
    line = input()
    if line == 'quit':
        break
    else:
        print(test(line))


# TEST CASES:

# AvB=>E
# A^B=>D
# D^E=>F
# B^E=>F
# A
# B
# C


# A^B^C^D=>F
# BvEvG=>F
# H^I=>A
# J^K=>B
# UvTvW=>J
# I^J^T=>P
# I^J^F=>Q
# H
# I
# K
# D
# W
# C

#
# a^b=>c
# cvd=>f
# fvgvhvp=>x
# x^y=>z
# a
# b
# y