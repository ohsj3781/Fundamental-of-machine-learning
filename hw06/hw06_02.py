from collections import Counter
from math import log2
import json

# Mapping data index
index_mapping = {'Outlook': 0, 'Temp': 1, 'Humidity': 2,'Wind':3}
data=[['Sunny','Hot','High','Weak','No'],
      ['Sunny','Hot','High','Strong','No'],
      ['Overcast','Hot','High','Weak','Yes'],
      ['Rain','Mild','High','Weak','Yes'],
      ['Rain','Cool','Normal','Weak','Yes'],

      ['Rain','Cool','Normal','Strong','No'],
      ['Overcast','Cool','Normal','Strong','No'],
      ['Sunny','Mild','High','Weak','No'],
      ['Sunny','Cool','Normal','Weak','Yes'],
      ['Rain','Mild','Normal','Weak','Yes'],

      ['Sunny','Mild','Normal','Strong','Yes'],
      ['Overcast','Mild','High','Strong','No'],
      ['Overcast','Hot','Normal','Weak','Yes'],
      ['Rain','Mild','High','Strong','No']]


def entropy(data):
    # Count the occurrences of each class label in the last column
    labels = [row[-1] for row in data]
    counts = Counter(labels)
    
    # Calculate the total number of elements in the dataset
    total = len(data)
    
    # Calculate the entropy
    entropy = 0
    for count in counts.values():
        probability = count / total
        entropy -= probability * log2(probability)
    return entropy

def split_data(data,index):
    subsets = {}
    for row in data:
        value = row[index]
        if value not in subsets:
            subsets[value] = []
        subsets[value].append(row)
    return subsets

def calc_avg_entropy(subsets):

    total = sum(len(subset) for subset in subsets.values())
    avg_entropy = 0
    for subset in subsets.values():
        subset_entropy = entropy(subset)
        avg_entropy += (len(subset) / total) * subset_entropy
    return avg_entropy

def calc_gain(data, index):
    """
    Calculate the information gain from splitting data on the given index.
    
    Parameters:
    - data: The dataset to split.
    - index: The index of the attribute to split on.
    
    Returns:
    - The information gain from the split.
    """
    subsets = split_data(data, index)
    return entropy(data) - calc_avg_entropy(subsets)

def build_decision_tree(data, index_mapping):
    # Check if all labels are the same
    labels = [row[-1] for row in data]
    if len(set(labels)) == 1:
        return labels[0]  # Return the label if all are the same

    # If no attributes are left to split, return the majority label
    if not index_mapping:
        return Counter(labels).most_common(1)[0][0]

    # Calculate information gain for each attribute
    gains = {index: calc_gain(data, index) for index in index_mapping.values()}
    max_gain = max(gains.values())  # Find the maximum gain
    candidates = [key for key, value in gains.items() if value == max_gain]  # Find all attributes with the same max gain
    if len(candidates) > 1:
        # Choose the attribute with fewer unique values in the dataset
        best_index = min(candidates, key=lambda idx: len(set(row[idx] for row in data)))
    else:
        best_index = candidates[0]

    # Split the data based on the best attribute
    subsets = split_data(data, best_index)
    best_attribute = [key for key, value in index_mapping.items() if value == best_index][0]
    # Create a subtree for each subset
    tree = {best_attribute: {}}
    for value, subset in subsets.items():
        # Remove the used attribute from the index mapping
        new_index_mapping = {key: val for key, val in index_mapping.items() if val != best_index}
        tree[best_attribute][value] = build_decision_tree(subset, new_index_mapping)
    return tree


def main():
    print("Entropy of the dataset:", entropy(data))
    
    tree= build_decision_tree(data, index_mapping)
    print("Decision Tree:")
    print(tree)
    print(json.dumps(tree, indent=4))


if __name__ == "__main__":
    main()
#     main()
    


    