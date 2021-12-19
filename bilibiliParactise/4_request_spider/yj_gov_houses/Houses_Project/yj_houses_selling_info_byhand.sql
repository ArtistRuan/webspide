
-- 删除当天数据
DELETE FROM yj_houses.yj_houses_selling_info WHERE data_date = '2021-12-17';
-- 插入数据表
INSERT INTO yj_houses.yj_houses_selling_info (
project_name
,project_address
,project_builder
,project_distinct
,project_total_builder_area
,project_area
,total_house_num
,total_area
,house_num
,house_area
,not_house_num
,not_house_area
,sold_house_num
,sold_house_area
,house_avg_price
,sold_not_house_num
,sold_not_house_area
,not_house_avg_price
,data_date
)
select 
project_name
,project_address
,project_builder
,project_distinct
,project_total_builder_area
,project_area
,total_house_num
,total_area
,house_num
,house_area
,not_house_num
,not_house_area
,sold_house_num
,sold_house_area
,house_avg_price
,sold_not_house_num
,sold_not_house_area
,not_house_avg_price
,'2021-12-17' as data_date
from yj_houses.yj_houses_selling_info
where data_date = '2021-12-19'