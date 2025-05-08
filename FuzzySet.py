class FuzzySet:
    def __init__(self, membership={}):
        self.membership = membership

    def max(self):
        return max(self.membership.values())

    def min(self):
        return min(self.membership.values())

    def complement(self):
        complement_A = {i : 1 - j for i, j in self.membership.items()}
        return FuzzySet(complement_A)

    def union(self, other):
        union_AB = {}
        for i, j in self.membership.items():
            if i in other.membership.keys():
                union_AB[i] = max(j, other.membership[i])
            else:
                union_AB[i] = j
            
        for i, j in other.membership.items():
            if i not in self.membership.keys():
                union_AB[i] = j
        return FuzzySet(union_AB)
    
    def intersection(self, other):
        intersection_AB = {}
        for i, j in self.membership.items():
            if i in other.membership.keys():
                intersection_AB[i] = min(j, other.membership[i])
            else:
                intersection_AB[i] = 0
            
        for i, j in other.membership.items():
            if i not in self.membership.keys():
                intersection_AB[i] = 0
        return FuzzySet(intersection_AB)
    
    def display(self):
        for element, membership in self.membership.items():
            print(f"Element: {element}, Membership: {membership}")


if __name__ == "__main__":
    
    membership_A = {1: 0.0, 2: 0.4, 3: 0.7, 4: 1.0, 5: 0.8}
    fuzzy_A = FuzzySet(membership_A)
    
    membership_B = {1: 0.5, 2: 0.3, 3: 0.8, 4: 0.9, 6: 0.6}
    fuzzy_B = FuzzySet(membership_B)

    print("Fuzzy Set A:")
    fuzzy_A.display()
    
    print("\nFuzzy Set B:")
    fuzzy_B.display()
    
    print("\nMax of Fuzzy Set A:", fuzzy_A.max())
    print("Max of Fuzzy Set B:", fuzzy_B.max())
    
    print("\nMin of Fuzzy Set A:", fuzzy_A.min())
    print("Min of Fuzzy Set B:", fuzzy_B.min())
    
    complement_A = fuzzy_A.complement()
    print("\nComplement of Fuzzy Set A:")
    complement_A.display()

    union_AB = fuzzy_A.union(fuzzy_B)
    print("\nUnion of Fuzzy Set A and B:")
    union_AB.display()

    intersection_AB = fuzzy_A.intersection(fuzzy_B)
    print("\nIntersection of Fuzzy Set A and B:")
    intersection_AB.display()
