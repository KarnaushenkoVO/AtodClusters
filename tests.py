from atod_clusters import find_atod_clusters

ERROR_MESSAGE = 'Wrong number of clusters for the {case}. Expected: {expected}, actual: {actual}'


def test_1_from_description():
    number_of_stars = 5
    connections = [(1, 2), (2, 3), (4, 5)]

    case = '1 from description'
    expected_number_of_clusters = 2
    expected_sizes = [1, 2]

    number_of_clusters, sizes = find_atod_clusters(number_of_stars, connections)
    assert number_of_clusters == expected_number_of_clusters, ERROR_MESSAGE.format(
        case=case,
        expected=expected_number_of_clusters,
        actual=number_of_clusters
    )
    assert sizes == expected_sizes, ERROR_MESSAGE.format(
        case=case,
        expected=expected_sizes,
        actual=sizes
    )


def test_2_from_description():
    number_of_stars = 6
    connections = [(1, 2), (3, 4)]

    case = '2 from description'
    expected_number_of_clusters = 4
    expected_sizes = [0, 0, 1, 1]

    number_of_clusters, sizes = find_atod_clusters(number_of_stars, connections)
    assert number_of_clusters == expected_number_of_clusters, ERROR_MESSAGE.format(
        case=case,
        expected=expected_number_of_clusters,
        actual=number_of_clusters
    )
    assert sizes == expected_sizes, ERROR_MESSAGE.format(
        case=case,
        expected=expected_sizes,
        actual=sizes
    )


def test_merge_needed():
    number_of_stars = 6
    connections = [(1, 2), (3, 4), (1, 4)]

    case = 'merge needed case'
    expected_number_of_clusters = 3
    expected_sizes = [0, 0, 3]

    number_of_clusters, sizes = find_atod_clusters(number_of_stars, connections)
    assert number_of_clusters == expected_number_of_clusters, ERROR_MESSAGE.format(
        case=case,
        expected=expected_number_of_clusters,
        actual=number_of_clusters
    )
    assert sizes == expected_sizes, ERROR_MESSAGE.format(
        case=case,
        expected=expected_sizes,
        actual=sizes
    )


def test_edge_case_max():
    number_of_stars = 10000
    connections = []

    case = 'edge case max'
    expected_number_of_clusters = number_of_stars
    expected_sizes = [0] * number_of_stars

    number_of_clusters, sizes = find_atod_clusters(number_of_stars, connections)
    assert number_of_clusters == expected_number_of_clusters, ERROR_MESSAGE.format(
        case=case,
        expected=expected_number_of_clusters,
        actual=number_of_clusters
    )
    assert sizes == expected_sizes, ERROR_MESSAGE.format(
        case=case,
        expected=expected_sizes,
        actual=sizes
    )


def test_edge_case_min():
    number_of_stars = 1
    connections = []

    case = 'edge case max'
    expected_number_of_clusters = number_of_stars
    expected_sizes = [0]

    number_of_clusters, sizes = find_atod_clusters(number_of_stars, connections)
    assert number_of_clusters == expected_number_of_clusters, ERROR_MESSAGE.format(
        case=case,
        expected=expected_number_of_clusters,
        actual=number_of_clusters
    )
    assert sizes == expected_sizes, ERROR_MESSAGE.format(
        case=case,
        expected=expected_sizes,
        actual=sizes
    )


if __name__ == '__main__':
    test_1_from_description()
    test_2_from_description()
    test_merge_needed()
    test_edge_case_min()
