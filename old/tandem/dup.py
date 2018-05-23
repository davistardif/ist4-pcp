class Dup(object):
    """
    Dup is a binary string that can be duplicated recursively
    """
    def __init__(self, val_in, distance_in):
        """
        seed_in: (string) starting seed for string
        self.distance: (int) how many mutations/duplications from seed
        self.val: (string) string after mutating/duplicating string
        """
        assert (type(val_in) == str), "val_in must be string"
        assert (type(distance_in) == int), "distance_in must be int"
        self.parent = None
        self.val = val_in
        self.distance = distance_in
    def duplicate(self, i, j):
        """
        i: (int) starting index for substring to duplicate
        j: (int) ending index for substring to duplicate
        tandem duplicates a substring of self.val and increases distance by 1
        """
        assert (type(i) == type(j) == int), "i and j must be int"
        assert (0 <= i <= j <= len(self.val)), "i and j not in bounds"
        d = Dup(self.val[:j+1] + self.val[i:j+1] + self.val[j+1:],  \
            self.distance + 1)
        d.set_parent(self)
        return d
    def set_parent(self, d):
        """
        d: (dup) the string that self was duplicated from
        (used to get tree of duplications)
        """
        assert (type(d) == Dup), "parent must be of type Dup"
        self.parent = d
    def get_family_tree(self):
        """
        returns the path of duplications from the seed string to self
        """
        tree = [self]
        descendant = self
        while descendant.parent != None:
            tree.append(descendant.parent)
            descendant = descendant.parent
        return tree[::-1]
    def __str__(self):
        """
        returns the value of the string and the distance from the seed
        """
        return "(" + self.val + " ; " + str(self.distance) + ")"


def generate_duplicates(intermediates, target):
    """
    intermediates = [list of dup]
    target  = (string) the target string
    this method generates all possible ways to tandem duplicate given
    intermediates so they can still be tandem duplicated to the target later
    """
    intermediates_out = []
    done = True
    for d in intermediates:
        for i in range(0, len(d.val)):
            for j in range(i, len(d.val)):
                e = d.duplicate(i,j)
                if (e.val.count("0") <= target.count("0")) and \
                    (e.val.count("1") <= target.count("1")):
                    intermediates_out.append(e)
                    done = False
                if e.val == target:
                    return [e], True
    if not done:
        return intermediates_out, False
    else:
        return intermediates, True


def find_distance(seed, target):
    """
    seed (string) a binary string seed
    target (string) a binary string target
    Generates all paths from seed to target, and finds the closest one
    """
    seed = Dup(seed, 0)
    intermediates = [seed]
    done = False
    while not done:
        intermediates, done = generate_duplicates(intermediates, target)
    closest = intermediates[0]
    print closest.distance
    for d in closest.get_family_tree(): print d
