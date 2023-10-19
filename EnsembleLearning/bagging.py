def randomly_sample(test_table, sample_size)
    return test_table[:, np.random.rand(sample_size)]

def bag_tree(type, table, max_tree_depth, depth, attributes, attribute_vals, mcv, weights)