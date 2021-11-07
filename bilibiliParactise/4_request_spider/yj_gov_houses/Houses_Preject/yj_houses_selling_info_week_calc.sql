DELIMITER $$

USE `yj_houses`$$

DROP PROCEDURE IF EXISTS `yj_houses_selling_info_week_calc`$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `yj_houses_selling_info_week_calc`()
BEGIN
-- 删除当天数据
DELETE FROM yj_houses_selling_info_week WHERE data_date = CURRENT_DATE();
-- 插入数据表
INSERT INTO yj_houses.yj_houses_selling_info_week 
(project_name,project_distinct,total_house_num,sold_house_num,week_sold_house_num,house_avg_price,sold_not_house_num,week_sold_not_house_num,not_house_avg_price,data_date)
SELECT
    project_name
    ,MAX(project_distinct) AS project_distinct
    ,MAX(total_house_num) AS total_house_num
    ,MAX(CASE WHEN DATE_FORMAT(data_date,'%Y-%m-%d') = CURRENT_DATE() THEN sold_house_num ELSE NULL END) AS sold_house_num
    ,SUM(today_sold_house_num) AS week_sold_house_num
    ,MAX(CASE WHEN DATE_FORMAT(data_date,'%Y-%m-%d') = CURRENT_DATE() THEN house_avg_price ELSE NULL END) AS house_avg_price
    ,MAX(CASE WHEN DATE_FORMAT(data_date,'%Y-%m-%d') = CURRENT_DATE() THEN sold_not_house_num ELSE NULL END) AS sold_not_house_num
    ,SUM(today_sold_not_house_num) AS week_sold_not_house_num
    ,MAX(CASE WHEN DATE_FORMAT(data_date,'%Y-%m-%d') = CURRENT_DATE() THEN not_house_avg_price ELSE NULL END) AS not_house_avg_price
    ,CURRENT_DATE() AS data_date
FROM yj_houses_selling_info_day WHERE YEARWEEK(DATE_FORMAT(data_date,'%Y-%m-%d'),1) = YEARWEEK(NOW(),1)
    GROUP BY project_name ORDER BY project_name
;
END$$

DELIMITER ;