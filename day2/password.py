from collections import Counter

def split_policy_and_passwords(pw_input):
    """
    Checks if a password is valid
    >>> split_policy_and_passwords(['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc'])
    [['1-3', 'a', 'abcde'], ['1-3', 'b', 'cdefg'], ['2-9', 'c', 'ccccccccc']]
    """
    return [[i.replace(':', '') for i in pw.split()] for pw in pw_input]
    

def get_policy(policy_list):
    """
    returns the min and max value for the letter in the password
    >>> get_policy('1-3')
    [1, 3]
    """
    return [int(i) for i in policy_list.split('-')]


def check_policy(policy_pw):
    """
    This checks if the password policy is being followed
    >>> check_policy(['1-3', 'a', 'abcde'])
    True
    """
    policy = get_policy(policy_pw[0])
    value = policy_pw[1]
    pw_count = dict(Counter(policy_pw[2]))

    try:
        if policy[0] <= pw_count[value] <= policy[1]:
          return True
        else:
            return False
    except:
        return False


def check_policy_pt2(policy_pw):
    """
    This checks if the password policy is being followed
    >>> check_policy_pt2(['1-3', 'a', 'abcde'])
    True
    >>> check_policy_pt2(['1-3', 'b', 'cdefg'])
    False
    >>> check_policy_pt2(['2-9', 'c', 'ccccccccc'])
    False
    """
    policy = get_policy(policy_pw[0])
    value = policy_pw[1]
    pos_count = [1 for n, i in enumerate(policy_pw[2], start=1) 
                 if i == value and n in policy]

    if sum(pos_count) == 1:
        return True
    else:
        return False


def main():
    pol_pws = split_policy_and_passwords(open('pwds.txt', 'r'))
    total = []
    for i in pol_pws:
        status = check_policy_pt2(i)
        total.append(status)
    
    print(sum(total))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
