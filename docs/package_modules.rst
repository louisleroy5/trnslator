Modules
=======

IDF Class
---------

.. currentmodule:: translater.idfclass

.. autosummary::
    :template: autosummary.rst
    :nosignatures:
    :toctree: reference/

    load_idf
    IDF
    run_eplus
    OutputPrep

.. _templates_label:


Schedule Module
---------------

.. currentmodule:: translater.schedule

.. autosummary::
    :template: autosummary.rst
    :nosignatures:
    :toctree: reference/

    Schedule


EnergyDataFrame
---------------

.. currentmodule:: translater.energydataframe

.. autosummary::
    :template: autosummary.rst
    :nosignatures:
    :toctree: reference/

    EnergyDataFrame.set_unit
    EnergyDataFrame.discretize_tsam
    plot_energydataframe_map


EnergySeries
------------

.. currentmodule:: translater.energyseries

.. autosummary::
    :template: autosummary.rst
    :nosignatures:
    :toctree: reference/

    EnergySeries.from_sqlite
    EnergySeries.unit_conversion
    EnergySeries.concurrent_sort
    EnergySeries.normalize
    EnergySeries.ldc_source
    EnergySeries.source_side
    EnergySeries.discretize_tsam
    EnergySeries.discretize
    EnergySeries.plot3d
    EnergySeries.plot2d
    EnergySeries.p_max
    EnergySeries.p_max
    EnergySeries.monthly
    EnergySeries.capacity_factor
    EnergySeries.bin_edges
    EnergySeries.time_at_min
    EnergySeries.bin_scaling_factors
    EnergySeries.duration_scaling_factor
    EnergySeries.ldc
    EnergySeries.nseries
    save_and_show
    plot_energyseries
    plot_energyseries_map


Report Data
-----------

.. currentmodule:: translater.reportdata

.. autosummary::
    :template: autosummary.rst
    :nosignatures:
    :toctree: reference/

    ReportData.from_sql_dict
    ReportData.from_sqlite
    ReportData.heating_load
    ReportData.filter_report_data
    ReportData.sorted_values



IDF to BUI module
-----------------

.. currentmodule:: translater.trnsys

.. autosummary::
    :template: autosummary.rst
    :nosignatures:
    :toctree: reference/

    convert_idf_to_trnbuild
    get_idf_objects
    clear_name_idf_objects
    zone_origin
    closest_coords
    parse_window_lib
    choose_window
    trnbuild_idf



Utils
-----

.. currentmodule:: translater.utils

.. autosummary::
    :template: autosummary.rst
    :nosignatures:
    :toctree: reference/

    config
    validate_trnsys_folder
    log
    load_umi_template_objects
    umi_template_object_to_dataframe
    get_list_of_common_umi_objects
    newrange
    date_transform
    weighted_mean
    top
    copy_file
    piecewise
    rmse
    checkStr
    write_lines
    load_umi_template
    check_unique_name
    angle
    float_round
    timeit
    lcm
    recursive_len
    rotate
    parallel_process