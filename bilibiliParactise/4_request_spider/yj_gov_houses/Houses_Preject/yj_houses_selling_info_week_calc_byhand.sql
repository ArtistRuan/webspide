
-- 删除当天数据
DELETE FROM yj_houses_selling_info_week WHERE data_date = CURRENT_DATE();
-- 插入数据表
INSERT INTO yj_houses.yj_houses_selling_info_week 
(project_name,project_distinct,total_house_num,sold_house_num,week_sold_house_num,house_avg_price,sold_not_house_num,week_sold_not_house_num,not_house_avg_price,data_date)
SELECT
    project_name
    ,MAX(project_distinct) AS project_distinct
    ,MAX(total_house_num) AS total_house_num
    ,MAX(CASE WHEN DATE_FORMAT(data_date,'%Y-%m-%d') = DATE_FORMAT('2021-11-06','%Y-%m-%d') THEN sold_house_num ELSE NULL END) AS sold_house_num
    ,SUM(today_sold_house_num) AS week_sold_house_num
    ,MAX(CASE WHEN DATE_FORMAT(data_date,'%Y-%m-%d') = DATE_FORMAT('2021-11-06','%Y-%m-%d') THEN house_avg_price ELSE NULL END) AS house_avg_price
    ,MAX(CASE WHEN DATE_FORMAT(data_date,'%Y-%m-%d') = DATE_FORMAT('2021-11-06','%Y-%m-%d') THEN sold_not_house_num ELSE NULL END) AS sold_not_house_num
    ,SUM(today_sold_not_house_num) AS week_sold_not_house_num
    ,MAX(CASE WHEN DATE_FORMAT(data_date,'%Y-%m-%d') = DATE_FORMAT('2021-11-06','%Y-%m-%d') THEN not_house_avg_price ELSE NULL END) AS not_house_avg_price
    ,DATE_SUB(CURRENT_DATE(),INTERVAL + 1 DAY) AS data_date
FROM yj_houses.yj_houses_selling_info_day WHERE YEARWEEK(DATE_FORMAT(data_date,'%Y-%m-%d'),1) = YEARWEEK(DATE_FORMAT('2021-11-06','%Y-%m-%d'),1)
    GROUP BY project_name ORDER BY project_name
;
