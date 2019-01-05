string = input("Input a string: ")
lstr = list(string)
print(lstr)

dict = {
    "a": lstr.count("a") + lstr.count("A"),
    "b": lstr.count("b") + lstr.count("B"),
    "c": lstr.count("c") + lstr.count("C"),
    "d": lstr.count("d") + lstr.count("D"),
    "e": lstr.count("e") + lstr.count("E"),
    "f": lstr.count("f") + lstr.count("F"),
    "g": lstr.count("g") + lstr.count("G"),
    "h": lstr.count("h") + lstr.count("H"),
    "i": lstr.count("i") + lstr.count("I"),
    "j": lstr.count("j") + lstr.count("J"),
    "k": lstr.count("k") + lstr.count("K"),
    "l": lstr.count("l") + lstr.count("L"),
    "m": lstr.count("m") + lstr.count("M"),
    "n": lstr.count("n") + lstr.count("N"),
    "o": lstr.count("o") + lstr.count("O"),
    "p": lstr.count("p") + lstr.count("P"),
    "q": lstr.count("q") + lstr.count("Q"),
    "r": lstr.count("r") + lstr.count("R"),
    "s": lstr.count("s") + lstr.count("S"),
    "t": lstr.count("t") + lstr.count("T"),
    "u": lstr.count("u") + lstr.count("U"),
    "v": lstr.count("v") + lstr.count("V"),
    "w": lstr.count("w") + lstr.count("W"),
    "x": lstr.count("x") + lstr.count("X"),
    "y": lstr.count("y") + lstr.count("Y"),
    "z": lstr.count("z") + lstr.count("Z"),
}

for k in dict.keys():
    if k in lstr:
        print(k, dict[k])