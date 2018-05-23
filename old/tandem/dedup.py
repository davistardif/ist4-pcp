def dedup(gens):
    """
    (list of strings) gen
    deduplicates a list of binary strings by one iteration
    """
    reduced = []
    done = True
    found_reduction = False
    for gen in gens:
        for i in range(0,len(gen)):
            for j in range(2, len(gen)+1-i, 2):
                if gen[i:i+j/2] == gen[i+j/2:i+j]:
                    done = False
                    found_reduction = True
                    reduced.append(gen[:i+1]+gen[i+j/2+1:])
        if not found_reduction:
            reduced.append(gen)
        found_reduction = False
    if done:
        return gens, True
    else:
        return reduced, False

def get_seed(gen):
    """
    string gen
    deduplicates a list of binary strings by one iteration until no more
    deduplications are possible, and then simplifies the list of possible
    seeds
    """
    done = False
    gens = [gen]
    while not done:
        gens, done = dedup(gens)
    print gen + ":", list(set(gens))

get_seed("30121013012101212")
get_seed("123032123032303")
get_seed("120312031230321230323031212")
