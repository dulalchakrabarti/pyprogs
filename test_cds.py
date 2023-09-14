import cdsapi

c = cdsapi.Client()

c.retrieve(
    'seasonal-monthly-single-levels',
    {
        'format':'grib',
        'originating_centre':'ecmwf',
        'system':'5',
        'variable':'2m_temperature',
        'product_type':[
            'ensemble_mean','monthly_maximum','monthly_mean',
            'monthly_minimum','monthly_standard_deviation'
        ],
        'year':'2019',
        'month':'10',
        'leadtime_month':[
            '1','2','3',
            '4','5','6'
        ]
    },
    'download.grib')
