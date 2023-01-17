def roman_to_int(self, s: str) -> int:
    val = {'I':1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    var = 0

    for i in range(len(s)):
        if i+1 < len(s) and val[s[i]] < val[s[i+1]]:
            var -= val[s[i]]
        else:
            var += val[s[i]]
    return var
