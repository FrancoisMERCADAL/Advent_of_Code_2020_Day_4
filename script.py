FILE_NAME = 'passports.txt'
PASSPORT_TEMPLATE = {
            'byr': None,
            'iyr': None,
            'eyr': None,
            'hgt': None,
            'hcl': None,
            'ecl': None,
            'pid': None,
            'cid': None
        }
MEASURE_SYSTEMS = ['cm','in']
EYE_COLORS = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

# PART 1
def valid_passport_count_part1(file):
    valid_passport_count = 0
    test_passport = PASSPORT_TEMPLATE
    for line in file:
        if line == '\n' or line == ' ':
            # check dictionary
            test_passport.pop('cid', None)
            res = None in test_passport.values()
            if res == False:
                valid_passport_count += 1
            test_passport = {
                'byr': None,
                'iyr': None,
                'eyr': None,
                'hgt': None,
                'hcl': None,
                'ecl': None,
                'pid': None,
                'cid': None
            }
        else:
            # form a dictionary
            key_values_array = line.split(' ')
            for i in range(len(key_values_array)):
                key_value = key_values_array[i].split(':')
                test_passport[key_value[0]] = key_value[1].rstrip('\n')
    return valid_passport_count

def passport_part1():
    file = open(FILE_NAME, "r")
    valid_passport_count = valid_passport_count_part1(file)
    file.close()
    return valid_passport_count

# PART 2
def check_byr_value(test_passport):
    key = 'byr'
    result = True
    value = int(test_passport[key])
    if value < 1920 or value > 2002:
        result = False
    return result

def check_iyr_value(test_passport):
    key = 'iyr'
    result = True
    value = int(test_passport[key])
    if value < 2010 or value > 2020:
        result = False
    return result

def check_eyr_value(test_passport):
    key = 'eyr'
    result = True
    value = int(test_passport[key])
    if value < 2020 or value > 2030:
        result = False
    return result

def check_hgt_value(test_passport):
    key = 'hgt'
    result = True
    measure_system = test_passport[key][-2:]
    try:
        hgt_value = int(test_passport[key][:-2])
    except ValueError:
        return False
    if measure_system not in MEASURE_SYSTEMS:
        return False
    if measure_system == MEASURE_SYSTEMS[0]:
        if hgt_value < 150 or hgt_value > 193:
            result = False
    elif measure_system == MEASURE_SYSTEMS[1]:
        if hgt_value < 59 or hgt_value > 76:
            result = False
    return result

def check_hcl_value(test_passport):
    key = 'hcl'
    first_char = test_passport[key][0]
    value = test_passport[key][1:]
    if first_char != '#' or len(value) != 6:
        return False
    else:
        for char in value:
            if char.isdigit() == True or char in ['a','b','c','d','e','f']:
                continue
            else:
                return False
    return True

def check_ecl_value(test_passport):
    key = 'ecl'
    if test_passport[key] in EYE_COLORS:
        return True
    else:
        return False

def check_pid_value(test_passport):
    key = 'pid'
    if len(test_passport[key]) == 9 and test_passport[key].isdigit() == True:
        return True
    else:
        return False

def check_dictionary(test_passport):
    check_array = [
        check_byr_value(test_passport), check_iyr_value(test_passport), check_eyr_value(test_passport), 
        check_hgt_value(test_passport), check_hcl_value(test_passport), check_ecl_value(test_passport), 
        check_pid_value(test_passport)
    ]
    if False in check_array:
        return False
    else:
        return True

def valid_passport_count_part2(file):
    valid_passport_count = 0
    test_passport = PASSPORT_TEMPLATE
    for line in file:
        if line == '\n' or line == ' ':
            # check dictionary
            test_passport.pop('cid', None)
            no_none_dict = None in test_passport.values()
            if no_none_dict == False:
                are_values_valid = check_dictionary(test_passport)
            if are_values_valid == True:
                valid_passport_count += 1
            test_passport = {
                'byr': None,
                'iyr': None,
                'eyr': None,
                'hgt': None,
                'hcl': None,
                'ecl': None,
                'pid': None,
                'cid': None
            }
            are_values_valid = False
        else:
            # form a dictionary
            key_values_array = line.split(' ')
            for i in range(len(key_values_array)):
                key_value = key_values_array[i].split(':')
                test_passport[key_value[0]] = key_value[1].rstrip('\n')
    return valid_passport_count

def passport_part2():
    file = open(FILE_NAME, "r")
    valid_passport_count = valid_passport_count_part2(file)
    file.close()
    return valid_passport_count

# TESTS
## PART 1
print(passport_part1())
# OUTPUT: 254

## PART 2
print(passport_part2())
# OUTPUT: 184
