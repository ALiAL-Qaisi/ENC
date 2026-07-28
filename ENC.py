#!/usr/bin/env python3
import random

LESS = "\\000"
LAYERS = 3


def generate_key(max_attempts=100000):
    rnd = random.Random()

    for _attempt in range(1, max_attempts + 1):
        try:
            AB = rnd.randint(1, 283)
            AC = rnd.randint(1, 283)
            AD = rnd.randint(1, 283)
            AE = rnd.randint(1, 283)
            AF = rnd.randint(1, 283)

            Mk = rnd.randint(62, 737)
            Mk2 = rnd.randint(62, 157)

            ALII = [None] + [Mk + rnd.randint(1, 10) for _ in range(9999)]
            ALII3 = [None] + [Mk + rnd.randint(1, 10) for _ in range(9999)]
            ALII2 = [None] + [Mk2 + rnd.randint(1, 10) for _ in range(99)]

            A = (ALII2[1] + ALII2[2] + ALII[26] + ALII2[2] + ALII[26] + ALII[58]
                 + ALII[77] + ALII[42] + ALII[53] + ALII[25] + ALII2[2] + ALII[26]
                 + ALII2[2] + ALII[26] + ALII[58] + ALII[77])
            B = ALII[A]

            A2 = (ALII2[52] + ALII2[27] + ALII2[68] + ALII3[73] + ALII2[54]
                  + ALII2[2] + ALII[26] + ALII2[2] + ALII[26] + ALII2[25] + ALII2[53]
                  + ALII3[73] + ALII2[54] + ALII2[28] + ALII3[84] + ALII2[99])
            B2 = ALII[A2]

            A3 = (ALII2[47] + ALII2[31] + ALII2[83] + ALII3[73] + ALII2[54]
                  + ALII2[28] + ALII3[84] + ALII2[99] + ALII2[2] + ALII[26]
                  + ALII2[2] + ALII[26] + ALII[58] + ALII[77])
            B3 = ALII3[A3]

            A4 = (ALII2[68] + ALII3[73] + ALII2[54] + ALII2[28] + ALII3[84]
                  + ALII2[99] + ALII2[2] + ALII[26] + ALII2[2] + ALII[26]
                  + ALII[58] + ALII[77])
            B4 = ALII[A4]

            A5 = (ALII2[35] + ALII2[25] + ALII2[53] + ALII2[52] + ALII2[27]
                  + ALII2[68] + ALII3[73] + ALII2[54] + ALII2[2] + ALII[26]
                  + ALII2[2] + ALII[26])
            B5 = ALII[A5]

            A6 = (ALII2[35] + ALII2[2] + ALII[26] + ALII[58] + ALII[77]
                  + ALII2[2] + ALII[26] + ALII[58] + ALII[77])
            B6 = ALII[A6]

            A7 = (ALII2[63] + ALII2[72] + ALII3[36] + ALII2[99] + ALII2[2]
                  + ALII[26] + ALII2[2] + ALII[26] + ALII[58] + ALII[77])
            B7 = ALII[A7]

            A8 = (ALII2[53] + ALII2[74] + ALII2[53] + ALII2[31] + ALII2[83]
                  + ALII3[73] + ALII2[54] + ALII2[28] + ALII3[84] + ALII2[99]
                  + ALII2[2] + ALII[26] + ALII2[2] + ALII[26] + ALII[58] + ALII[77]
                  + ALII2[28] + ALII3[84] + ALII2[99])
            B8 = ALII3[A8]

            A9 = (ALII2[28] + ALII3[84] + ALII2[99] + ALII2[2] + ALII[26]
                  + ALII[58] + ALII[77])
            B9 = ALII[A9]

            C = (ALII3[1] + ALII3[2] + ALII[26] + ALII3[2] + ALII[26] + ALII[58]
                 + ALII[77] + ALII[42] + ALII[53] + ALII[25] + ALII3[2] + ALII[26]
                 + ALII3[2] + ALII[26] + ALII[58] + ALII[77])
            G = ALII[C]

            C2 = (ALII3[52] + ALII3[27] + ALII3[68] + ALII3[73] + ALII3[54]
                  + ALII3[2] + ALII[26] + ALII3[2] + ALII[26] + ALII3[25] + ALII3[53]
                  + ALII3[73] + ALII3[54] + ALII3[28] + ALII3[84] + ALII3[99])
            G2 = ALII[C2]

            C3 = (ALII3[47] + ALII3[31] + ALII3[83] + ALII3[73] + ALII3[54]
                  + ALII3[28] + ALII3[84] + ALII3[99] + ALII3[2] + ALII[26]
                  + ALII3[2] + ALII[26] + ALII[58] + ALII[77])
            G3 = ALII3[C3]

            C4 = (ALII3[68] + ALII3[73] + ALII3[54] + ALII3[28] + ALII3[84]
                  + ALII3[99] + ALII3[2] + ALII[26] + ALII3[2] + ALII[26]
                  + ALII[58] + ALII[77])
            G4 = ALII[C4]

            C5 = (ALII3[35] + ALII3[25] + ALII3[53] + ALII3[52] + ALII3[27]
                  + ALII3[68] + ALII3[73] + ALII3[54] + ALII3[2] + ALII[26]
                  + ALII3[2] + ALII[26])
            G5 = ALII[C5]

            C6 = (ALII3[35] + ALII3[2] + ALII[26] + ALII[58] + ALII[77]
                  + ALII3[2] + ALII[26] + ALII[58] + ALII[77])
            G6 = ALII[C6]

            C7 = (ALII3[63] + ALII3[72] + ALII3[36] + ALII3[99] + ALII3[2]
                  + ALII[26] + ALII3[2] + ALII[26] + ALII[58] + ALII[77])
            G7 = ALII[C7]

            G8 = ALII3[9999]
            G9 = ALII[9999]

            for v in (B, B2, B3, B4, B5, B6, B7, B8, B9,
                      G, G2, G3, G4, G5, G6, G7, G8, G9):
                if v is None:
                    raise IndexError

            M = G + G2 + C + C2 + A + B * 3 + B2
            M2 = G3 + C3 + G4 + C4 + A2 * B2 + 352 + A3
            M3 = G5 + G6 + C5 + C6 + A3 + B3 + B4 * A4 + 926 // A5 + B5
            M4 = G7 + C7 + C + G8 + A4 + B4 * 836 // 436 + B5 + A5
            O = A + B * 3 + B2 + G + G2 + C + C2 * A9 + B9 + B8 + B9 + A8 + A7
            O2 = A2 * B2 + 800 + A3 + G3 + C3 + G4 + C4
            O3 = A3 + B3 + B4 * A4 + 482 // A5 + B5 + G5 + G6 + C5 + C6
            MO = M + O + M2 + M3 + O3 * O2

            KAY = (G + G2 * G3)
            KAY2 = (O3 + G8 + G7 * G9)
            KAY3 = (G3 + M4 * G9)
            KAY5 = (G + G5 + KAY + G9 * KAY3)
            KAY6 = (G8 + G3 + MO * KAY2 - G6 + KAY5)

            key = [None, (AB + AC * AD) - AE, AC, AD * 2, AE + AD, AF]
            KY1 = (key[5] + key[2] + key[1] * key[4]) - key[1]
            KY2 = (key[2] + key[3] * 1) - key[4]
            KY3 = (key[3] + key[1] * key[2]) + key[4]
            KY4 = (key[1] + key[2] * key[5] * key[5]) + key[1]
            KY5 = (key[1] + key[5] - key[3]) + key[4]
            KY6 = (key[5] + key[2] + key[1] * key[4]) - key[1]
            KY7 = (key[2] + key[3] * 1) - key[4]
            KY8 = (key[5] + key[1] * key[2]) + key[3]
            KY9 = (key[3] + key[4] - key[1] * key[2]) + key[5]
            KY10 = (key[5] + key[1] - key[2]) + key[3]

            LOVE = [None, KY1, KY2, KAY5, KAY6, KY5, KY6, KY7, KY8, KY9, KY10,
                   KY9, KY7, KY5, KY4, KY3, KY10, KY5, KY4, KY2, KAY3, KY1, KY9]

            CONST = (LOVE[1] + LOVE[2] - LOVE[6] + LOVE[3] - LOVE[8] * LOVE[4]
                     + LOVE[7] - LOVE[5] * LOVE[10] + LOVE[9] * LOVE[11] + LOVE[12]
                     + LOVE[13] + LOVE[14] + LOVE[15] - LOVE[16] - LOVE[17]
                     - LOVE[18] - LOVE[19] - LOVE[20])

            KEY = [None]
            for i in range(1, len(LOVE)):
                KEY.append((LOVE[i] + CONST) % 256)

            return KEY

        except IndexError:
            continue

    raise RuntimeError("Failed to generate a valid key after many attempts")


def preprocess(text):
    return text.replace("\\n", "\n").replace("\\t", "\t")


def encrypt_layer(values, KEY):
    out = []
    for idx, v in enumerate(values):
        i = idx + 1
        out.append((v - KEY[4] - (KEY[7] + i) * (KEY[9] + i)) % 256)
    return out


def decrypt_layer(values, KEY):
    out = []
    for idx, v in enumerate(values):
        i = idx + 1
        out.append((v + KEY[4] + (KEY[7] + i) * (KEY[9] + i)) % 256)
    return out


def to_lua_table(values):
    fields = []
    for idx, v in enumerate(values):
        i = idx + 1
        fields.append("[" + str(i) + "]=\"" + (LESS * v) + "\"")
    return "{" + ",".join(fields) + "}"


def main():
    line = "=" * 72
    print(line)
    print("Encryption By ALI AL-QAISI (@XU_UQ)")
    print(line)

    text = input("\nEnter the text to encrypt: ")

    keys = [generate_key() for _ in range(LAYERS)]

    values = list(preprocess(text).encode("utf-8"))
    for KEY in keys:
        values = encrypt_layer(values, KEY)

    print()
    for n, KEY in enumerate(keys, start=1):
        print()
        print("Key" + str(n) + " = " + to_lua_table(KEY[1:]))
    print()
    print("\nALI = " + to_lua_table(values) + "\n")
    print()
    check = list(values)
    for KEY in reversed(keys):
        check = decrypt_layer(check, KEY)
    recovered = bytes(check).decode("utf-8", errors="replace")
    ok = (recovered == preprocess(text))
    print(line)


if __name__ == "__main__":
    main()
                               
