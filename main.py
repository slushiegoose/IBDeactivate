# title: gut path proportion calculator
# author: IBDeactivate team
# date: 04/12/21
#version: 1.0
# description:
    # This project outlines how a 2-pill solution can help with Inflammatory bowel disease (IBD).
    # A simple model to simulate how the first pill collects the required data and how the second pill utilise that data.
    # The idea is that it breaks the small intestine length into sections and then calculates the proportion of the gut that is inflammed
    # The gut proportion is then used to calculate the dosage of the drug at that location. This ensures targetted and effective drug delivery.

import random

# Constants
GRAMS_OF_DRUG_PER_PILL = 10
LENGTH_OF_GUT_PATH = 700 #in cm
# Example: GUT_PATH_ARRAY=[0,0,0,1,2,3,1,0,0,0,2,3,1,2,0,0,3,0,3,0] #0=no inflamation, 1=moderate, 2=severe, 3=critical



def create_random_gut_path_array(length: int) -> float:
    """generates a random gut path array (normally would be sent from 1st pill)

    Args:
        length (int): length of array (length of gut path)

    Returns:
        [float]: #0=no inflamation, 1=moderate, 2=severe, 3=critical 
    """
    gut_path_array = []
    for i in range(0, length):
        gut_path_array.append(random.uniform(0, 3))
    return gut_path_array



def calcualte_gut_path_proportion(gut_path_array: float) -> float:
    """calculate the gut path proportion

    Args:
        gut_path_array ([float]): [gut_path_array]

    Returns:
        [float]: [gut_proportion_array]
    """
    gut_proportion_array = []
    for i in range(0, len(gut_path_array)):
        proportion = round(
            ((gut_path_array[i]/sum(gut_path_array))*GRAMS_OF_DRUG_PER_PILL), 3)
        gut_proportion_array.append(proportion)
    return gut_proportion_array


def main():
    gut_path_array = create_random_gut_path_array(LENGTH_OF_GUT_PATH)
    gut_proportion_array = calcualte_gut_path_proportion(gut_path_array)
    print(f"The gut inflamation array recieved is {gut_path_array}")
    print(f"The recommended dosage for each section of gut is {gut_proportion_array}")


if __name__ == '__main__':
    main()
