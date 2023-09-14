import cdstoolbox as ct

@ct.application(title='Hello World!')
@ct.output.figure()
@ct.output.download()
def application():

    data = ct.catalogue.retrieve(
        'seasonal-monthly-single-levels',
        {
            'originating_centre': 'ecmwf',
            'variable': '2m_temperature',
            'product_type': 'ensemble_mean',
            'year': '2018',
            'month': ['02'],
            'leadtime_month': ['1'],
        }
    )

    fig = ct.cdsplot.geomap(
        data, pcolormesh_kwargs={'cmap': 'RdBu_r'}, title='Mean {long_name}',
        projection=ct.cdsplot.crs.Robinson()
    )

    return fig, data
