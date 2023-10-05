def parse_two_numbers(raw_numbers):
    """
       Utility function to parse input line

       :param str raw_numbers: Space separated numbers. Example: '3 4'
       :return: Parsed two numbers, compacted into list. Example: [3, 4]
       :rtype: list[int, int]
       :raises ValueError: If format of string cannot be parsed into two integer numbers
    """
    try:
        return list(map(int, raw_numbers.split(' ')))
    except Exception:
        raise ValueError('Invalid format. Please check example of usage in the documentation (README.md)')


def find_atod_clusters(number_of_stars, connections):
    """
       Main function, which incorporates the logic of finding atod clusters and calculating their size

       :param int number_of_stars: Number of stars. Example: 5
       :param list[tuple[int, int], ...] connections: Connections between stars. Example: [(1, 2), (2, 3), (4, 5)]
       :return: number of clusters and their sizes (in non-descending order). Example: (2, [1, 2])
       :rtype: tuple[int, list[int, ...]]
    """

    clusters = []  # Each cluster represented in form {'size': int, 'cluster': set()}
    stars_in_clusters = set()  # Let's save stars which are in clusters, to exclude stars out of clusters later

    for conn in connections:
        stars_in_clusters.update(conn)

        _merged_clusters = set(conn)  # First cluster is the connection itself
        _size = 1  # 1 because _merged_clusters contains by default
        _clusters_wo_changes = []  # Clusters without changes - are clusters which haven't been merged
        for cluster in clusters:
            if _merged_clusters.intersection(cluster['stars']):
                # We have to merge clusters because stars from connections could be in different clusters before
                _merged_clusters = _merged_clusters.union(cluster)
                _size += cluster['size']
            else:
                _clusters_wo_changes.append(cluster)

        # Recreate clusters list with new merged cluster
        clusters = [{'size': _size, 'stars': _merged_clusters}, *_clusters_wo_changes]

    # Compute and sort size of clusters
    num_stars_wo_clusters = (number_of_stars - len(stars_in_clusters))
    cluster_sizes = [0] * num_stars_wo_clusters  # Zero to each star which is a standalone cluster
    cluster_sizes.extend([cluster['size'] for cluster in clusters])
    cluster_sizes = list(sorted(cluster_sizes, reverse=False))

    # Compute number of clusters
    num_clusters = len(clusters) + num_stars_wo_clusters

    return num_clusters, cluster_sizes


# Let's separate input/output logic and domain logic to cover domain logic with tests in another module
if __name__ == '__main__':
    print('Please enter input parameters accordingly to documentation')
    # Read numbers of stars and numbers of connections
    num_stars, num_connections = parse_two_numbers(input())

    # Loop to read coordinates of connections
    conns = []  # I assume that we should calculate even duplicate connections. Otherwise - (set) should be used here.
    for _ in range(num_connections):
        first_star, second_star = parse_two_numbers(input())
        conns.append((first_star, second_star))

    # Main function which solves Atod clusters problem
    number_of_clusters, sizes = find_atod_clusters(num_stars, conns)

    print(number_of_clusters)
    for size in sizes:
        print(size)
