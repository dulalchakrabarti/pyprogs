import cdsapi

c = cdsapi.Client()

c.retrieve(
    'seasonal-original-single-levels',
    {
        'originating_centre':'ecmwf',
        'system':'5',
        'variable':[
            '10m_u_component_of_wind','10m_v_component_of_wind','2m_dewpoint_temperature',
            '2m_temperature','total_cloud_cover'
        ],
        'year':'2019',
        'month':'10',
        'day':'01',
        'leadtime_hour':[
            '492','516','540',
            '564','588'
        ],
        'format':'grib'
    },
    'multi.grib')
