# Convert IPv4 address into binary. An Ipv4 address is a 32 bit number divided into 4 octets. Each octet is equal to 8 bits 4 * 8 = 32.
octet1 = int(input("Please enter octet 1 of IP address: "))
octet2 = int(input("Please enter octet 2 of IP address: "))
octet3 = int(input("Please enter octet 3 of IP address: "))
octet4 = int(input("Please enter octet 4 of IP address: "))

byte1 = ["0", "0", "0", "0", "0", "0", "0", "0"]
byte2 = ["0", "0", "0", "0", "0", "0", "0", "0"]
byte3 = ["0", "0", "0", "0", "0", "0", "0", "0"]
byte4 = ["0", "0", "0", "0", "0", "0", "0", "0"]

# octet 1

if octet1 >= 128 or octet1 - 128 == 0:
    octet1 -= 128
    byte1[0] = "1"
if octet1 >= 64 or octet1 - 64 == 0:
    octet1 -= 64
    byte1[1] = "1"
if octet1 >= 32 or octet1 - 32 == 0:
    octet1 -= 32
    byte1[2] = "1"
if octet1 >= 16 or octet1 - 16 == 0:
    octet1 -= 16
    byte1[3] = "1"
if octet1 >= 8 or octet1 - 8 == 0:
    octet1 -= 8
    byte1[4] = "1"
if octet1 >= 4 or octet1 - 4 == 0:
    octet1 -= 4
    byte1[5] = "1"
if octet1 >= 2 or octet1 - 2 == 0:
    octet1 -= 2
    byte1[6] = "1"
if octet1 >= 1 or octet1 - 1 == 0:
    octet1 -= 1
    byte1[7] = "1"

# octet 2

if octet2 >= 128 or octet2 - 128 == 0:
    octet2 -= 128
    byte2[0] = "1"
if octet2 >= 64 or octet2 - 64 == 0:
    octet2 -= 64
    byte2[1] = "1"
if octet2 >= 32 or octet2 - 32 == 0:
    octet2 -= 32
    byte2[2] = "1"
if octet2 >= 16 or octet2 - 16 == 0:
    octet2 -= 16
    byte2[3] = "1"
if octet2 >= 8 or octet2 - 8 == 0:
    octet2 -= 8
    byte2[4] = "1"
if octet2 >= 4 or octet2 - 4 == 0:
    octet2 -= 4
    byte2[5] = "1"
if octet2 >= 2 or octet2 - 2 == 0:
    octet2 -= 2
    byte2[6] = "1"
if octet2 >= 1 or octet2 - 1 == 0:
    octet2 -= 1
    byte2[7] = "1"

# octet 3
if octet3 >= 128 or octet3 - 128 == 0:
    octet3 -= 128
    byte3[0] = "1"
if octet3 >= 64 or octet3 - 64 == 0:
    octet3 -= 64
    byte3[1] = "1"
if octet3 >= 32 or octet3 - 32 == 0:
    octet3 -= 32
    byte3[2] = "1"
if octet3 >= 16 or octet3 - 16 == 0:
    octet3 -= 16
    byte3[3] = "1"
if octet3 >= 8 or octet3 - 8 == 0:
    octet3 -= 8
    byte3[4] = "1"
if octet3 >= 4 or octet3 - 4 == 0:
    octet3 -= 4
    byte3[5] = "1"
if octet3 >= 2 or octet3 - 2 == 0:
    octet3 -= 2
    byte3[6] = "1"
if octet3 >= 1 or octet3 - 1 == 0:
    octet3 -= 1
    byte3[7] = "1"

# octet 4

if octet4 >= 128 or octet4 - 128 == 0:
    octet4 -= 128
    byte4[0] = "1"
if octet4 >= 64 or octet4 - 64 == 0:
    octet4 -= 64
    byte4[1] = "1"
if octet4 >= 32 or octet4 - 32 == 0:
    octet4 -= 32
    byte4[2] = "1"
if octet4 >= 16 or octet4 - 16 == 0:
    octet4 -= 16
    byte4[3] = "1"
if octet4 >= 8 or octet4 - 8 == 0:
    octet4 -= 8
    byte4[4] = "1"
if octet4 >= 4 or octet4 - 4 == 0:
    octet4 -= 4
    byte4[5] = "1"
if octet4 >= 2 or octet4 - 2 == 0:
    octet4 -= 2
    byte4[6] = "1"
if octet4 >= 1 or octet4 - 1 == 0:
    octet4 -= 1
    byte4[7] = "1"

print(
    byte1[0]
    + byte1[1]
    + byte1[2]
    + byte1[3]
    + byte1[4]
    + byte1[5]
    + byte1[6]
    + byte1[7]
    + ".",
    end="",
)
print(
    byte2[0]
    + byte2[1]
    + byte2[2]
    + byte2[3]
    + byte2[4]
    + byte2[5]
    + byte2[6]
    + byte2[7]
    + ".",
    end="",
)
print(
    byte3[0]
    + byte3[1]
    + byte3[2]
    + byte3[3]
    + byte3[4]
    + byte3[5]
    + byte3[6]
    + byte3[7]
    + ".",
    end="",
)
print(
    byte4[0]
    + byte4[1]
    + byte4[2]
    + byte4[3]
    + byte4[4]
    + byte4[5]
    + byte4[6]
    + byte4[7],
    end="",
)
