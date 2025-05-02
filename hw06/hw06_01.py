def calc_entropy(lst):
    """
    Calculate the entropy of a list of values.
    
    Parameters:
    - lst: A list of values.
    
    Returns:
    - The entropy of the list.
    """
    from collections import Counter
    from math import log2

    # Count the occurrences of each value in the list
    counts = Counter(lst)
    
    # Calculate the total number of elements in the list
    total = len(lst)
    
    # Calculate the entropy
    entropy = 0
    for count in counts.values():
        probability = count / total
        entropy -= probability * log2(probability)
    
    return entropy

def calc_avg_entropy(lst_1, lst_2):
    sum=len(lst_1)+len(lst_2)

    
    return (len(lst_1)/sum)*calc_entropy(lst_1)+(len(lst_2)/sum)*calc_entropy(lst_2)

def calc_gain(lst_0, lst_1, lst_2):
    """
    Calculate the information gain from splitting lst_0 into lst_1 and lst_2.
    
    Parameters:
    - lst_0: The original list of values.
    - lst_1: The first split of the list.
    - lst_2: The second split of the list.
    
    Returns:
    - The information gain from the split.
    """
    return calc_entropy(lst_0) - calc_avg_entropy(lst_1, lst_2)

def main():
    """
    Main function to demonstrate the calc_entropy function.
    """
    # Example list of values
    lst_0=['T','T','T','T','T','F','F','F']
    lst_1=['T','T','T','T','F']
    lst_2=['T','F','F']
    
    # Calculate and print the entropy
    print(f"Entropy of lst_0 : {calc_entropy(lst_0):.4f}")
    print(f"Entropy of lst_1 : {calc_entropy(lst_1):.4f}")
    print(f"Entropy of lst_2 : {calc_entropy(lst_2):.4f}")

    # Calculate and print the average entropy
    print(f"Average entropy of lst_1 and lst_2 : {calc_avg_entropy(lst_1, lst_2):.4f}")

    # Calculate and print the information gain
    print(f"Information gain from splitting lst_0 into lst_1 and lst_2 : {calc_gain(lst_0, lst_1, lst_2):.4f}")
if __name__ == "__main__":
    main()