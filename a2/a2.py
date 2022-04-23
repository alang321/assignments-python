def char_to_idx(char):
    return ord(char.upper()) - ord('A')


def read_freq_file(path):
    freqs_en = 26 * [0]

    f = open(path, "r")
    for line in f.readlines():
        idx = char_to_idx(line.split()[0])
        val = float(line.split()[1])

        freqs_en[idx] = val
    f.close()

    sum_freq = sum(freqs_en)
    freqs_en = [i/sum_freq for i in freqs_en]
    return freqs_en


def freq_from_txt(txt):
    freqs = 26 * [0]

    for char in txt:
        if 'A' <= char.upper() <= 'Z':
            idx = char_to_idx(char)
            freqs[idx] += 1

    sum_freq = sum(freqs)
    freqs = [i / sum_freq for i in freqs]
    return freqs


def ceaser_cipher(txt, shift):
    char_array = list(txt)
    for char_idx in range(len(char_array)):
        char = char_array[char_idx]
        if 'A' <= char.upper() <= 'Z':
            idx = char_to_idx(char)
            shited_idx = (idx + shift) % 26

            if 'A' <= char <= 'Z':
                char_array[char_idx] = chr(ord('A') + shited_idx)
            else:
                char_array[char_idx] = chr(ord('a') + shited_idx)
    shifted_txt = ''.join(char_array)
    return shifted_txt


def calc_diff(freq_a, freq_b):
    freq_diff = 0
    for i in range(len(freq_a)):
        freq_diff += abs(freq_a[i] - freq_b[i])
    return freq_diff


def find_shift(txt, freqs):
    freq_diffs = [0] * 26
    for shift in range(26):
        shifted_txt = ceaser_cipher(txt, shift)
        freqs_txt = freq_from_txt(shifted_txt)
        freq_diffs[shift] = calc_diff(freqs, freqs_txt)

    return freq_diffs.index(min(freq_diffs))


def file_to_string(path):
    f = open(path, "r")
    txt = f.read()
    f.close()
    return txt


def string_to_file(path, txt):
    f = open(path, "w")
    f.write(txt)
    f.close()


freqs_en = read_freq_file("ch-freq-en.txt")

file_paths = ["secret_files/secret0.txt",
              "secret_files/secret1.txt",
              "secret_files/secret2.txt",
              "secret_files/secret3.txt",
              "secret_files/secret4.txt",
              "secret_files/secret5.txt",
              "secret_files/secret6.txt"]

deciphered_file_paths = ["secret_files/secret0_deciphered.txt",
                         "secret_files/secret1_deciphered.txt",
                         "secret_files/secret2_deciphered.txt",
                         "secret_files/secret3_deciphered.txt",
                         "secret_files/secret4_deciphered.txt",
                         "secret_files/secret5_deciphered.txt",
                         "secret_files/secret6_deciphered.txt"]


for fil_idx in range(len(file_paths)):
    txt = file_to_string(file_paths[fil_idx])
    optshift = find_shift(txt, freqs_en)
    deciphered_txt = ceaser_cipher(txt, optshift)
    string_to_file(deciphered_file_paths[fil_idx], deciphered_txt)

    print("File:", file_paths[fil_idx], " Shiftkey:", optshift, " New File:", deciphered_file_paths[fil_idx])

input()

print("Freq. sum:", sum(read_freq_file("ch-freq-en.txt")))
print("Ceaser Test 1:", ceaser_cipher('Hello World!', 5))
print("Ceaser Test 2:", ceaser_cipher('Your mother was a hamster', -7))
print("getfreq() Test:", freq_from_txt("Come see the violence inherent in the system!! Help Help I'm being oppressed!!")[:5])
freqs = freq_from_txt("Come see the violence inherent in the system!! Help Help I'm being oppressed!!")
print("calcdiff() Test:", calc_diff(freqs, freqs_en))
print("findshift() Test:", find_shift(file_to_string("secret_files/testdata.txt"), freqs_en))
