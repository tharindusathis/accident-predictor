import util

DATA = [
    {
        
            "longitude": -1.455565,
            "latitude": 53.419588,
            "cluster_1": 13739.0
    },
    {
            "longitude": -2.1692720000000003,
            "latitude": 53.38852900000001,
            "cluster_1": 34395.0
    },
    {
            "longitude": -2.241664,
            "latitude": 53.48017900000001,
            "cluster_1": 8191.0
    },
    {
            "longitude": 0.0583039999999999,
            "latitude": 51.424728,
            "cluster_1": 2807.0
    },
    {
            "longitude": -4.063975,
            "latitude": 51.745943,
            "cluster_1": 30490.0
    },
    {
            "longitude": -1.473296,
            "latitude": 53.360611,
            "cluster_1": 13918.0
    },
    {
            "longitude": 1.374845,
            "latitude": 52.110725,
            "cluster_1": 45579.0
    },
    {
            "longitude": -0.123377,
            "latitude": 51.568425,
            "cluster_1": 702.0
    },
    {
            "longitude": -2.004398,
            "latitude": 52.614487,
            "cluster_1": 15789.0
    },
    {
            "longitude": -0.032725,
            "latitude": 51.512354,
            "cluster_1": 1260.0
    }
]


def test_clusters():
    print("Start Test")
    
    total = 0
    correct = 0

    for data in DATA:
        total += 1

        got = util.get_cluster(data['latitude'],data['longitude'])
        actual = data['cluster_1']

        print("{0}\t{1}\t{2}".format(total, got, actual))

        if got == actual:
            correct += 1
        
    assert correct == total



def test_dummy_weather_data():
    print("Start Test")
    
    for _ in range(5):
      
        got = util.get_weather_data(1,123)
        # print(got)
        
    assert 1 == 1



