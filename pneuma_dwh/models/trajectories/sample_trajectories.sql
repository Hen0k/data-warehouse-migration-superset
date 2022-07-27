
{{ config(materialized='table') }}


with one_car as (
    select *

        from trajectories
        where unique_id = '20181030_d1_0830_0900_0'
)

select *
from one_car
