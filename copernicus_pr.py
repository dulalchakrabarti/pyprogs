import cdsapi

c = cdsapi.Client()

c.retrieve(
    'seasonal-original-single-levels',
    {
        'format': 'grib',
        'originating_centre': 'ecmwf',
        'system': '5',
        'variable': 'total_precipitation',
        'year': '2020',
        'month': '08',
        'day': '01',
        'leadtime_hour': '2400',
        'area': [
            40, 60, 0,
            100,
        ],
    },
    'download.grib')
