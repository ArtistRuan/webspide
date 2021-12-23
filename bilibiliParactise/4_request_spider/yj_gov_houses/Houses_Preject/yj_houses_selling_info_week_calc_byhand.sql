/**
*遇到的报错：Truncated incorrect DOUBLE value: '196 套'
*解决方式：
*/


-- 删除当天数据
DELETE FROM yj_houses.yj_houses_selling_info_week WHERE data_date = '2021-12-19';
-- 插入数据表
INSERT INTO yj_houses.yj_houses_selling_info_week 
(project_name,project_distinct,total_house_num,sold_house_num,week_sold_house_num,house_avg_price,sold_not_house_num,week_sold_not_house_num,not_house_avg_price,data_date)
select * from (
SELECT
    a.project_name as project_name
    ,a.project_distinct project_distinct
    ,a.total_house_num AS total_house_num
    ,a.sold_house_num AS sold_house_num
    ,( a.sold_house_num - 0 ) - (b.sold_house_num - 0 ) AS week_sold_house_num
    ,a.house_avg_price AS house_avg_price
    ,a.sold_not_house_num AS sold_not_house_num
    ,( a.sold_not_house_num - 0 ) - (b.sold_not_house_num - 0 ) AS week_sold_not_house_num
    ,a.not_house_avg_price AS not_house_avg_price
    ,a.data_date AS data_date
FROM (select * from yj_houses.yj_houses_selling_info WHERE data_date = '2021-12-19' AND (
    project_name LIKE '%上东新城%'
    OR project_name LIKE '%保利中央公园%'
    OR project_name LIKE '%恒隆共青湖%'
    OR project_name LIKE '%森林湖%'
    OR project_name LIKE '%金山明珠%'
    OR project_name LIKE '%钧明里%'
    OR project_name LIKE '%丰泰上院%'
    -- or project_name like '%绿地城际空间%'
    OR project_name LIKE '%绿地%'
    OR project_name LIKE '%锦峰湖景%'
    OR project_name LIKE '%文华峯境%'
    OR project_name LIKE '%保利公馆%'
    OR project_name LIKE '%淘金湾南区%'
    OR project_name LIKE '%敏捷东樾府%'
    OR project_name LIKE '%美的置业%'
    OR project_name LIKE '%恒隆御景山庄%'
    OR project_name LIKE '%碧桂园凤凰湾%')) a 
left join 
    (select project_name,sold_house_num,sold_not_house_num from yj_houses.yj_houses_selling_info WHERE data_date = '2021-12-18') b 
    on a.project_name = b.project_name
) t;
