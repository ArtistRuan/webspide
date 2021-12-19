
-- 删除当天数据
DELETE FROM yj_houses.yj_houses_selling_info_day WHERE data_date = '2021-12-19';
-- 插入数据表
INSERT INTO yj_houses.yj_houses_selling_info_day (project_name,total_house_num,sold_house_num,today_sold_house_num,sold_not_house_num,today_sold_not_house_num,project_distinct,house_avg_price,not_house_avg_price,data_date)
SELECT a.project_name,
a.total_house_num  -- 总套数
,a.sold_house_num AS sold_house_num  -- 累计已售住宅套数
,(a.sold_house_num - b.sold_house_num) AS today_sold_house_num  -- 本日已售住宅套数
,a.sold_not_house_num AS sold_not_house_num  -- 累计已售非住宅套数
,(a.sold_not_house_num - b.sold_not_house_num) AS today_sold_not_house_num  -- 本日已售非住宅套数
,a.project_distinct  -- 所在地区
,a.house_avg_price  -- 住宅均价
,a.not_house_avg_price  -- 非住宅均价
,a.data_date  -- 数据批次时间
FROM 
(SELECT DISTINCT 
                project_name
                ,project_distinct  -- 所在地区
                ,total_house_num  -- 总套数
                ,sold_house_num + 0 AS sold_house_num  -- 已售住宅套数
                ,house_avg_price  -- 住宅均价
                ,sold_not_house_num + 0 AS sold_not_house_num  -- 已售非住宅套数
                ,not_house_avg_price  -- 非住宅均价
                ,data_date
            FROM yj_houses.yj_houses_selling_info WHERE data_date = '2021-12-19'
            AND (
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
OR project_name LIKE '%碧桂园凤凰湾%') ORDER BY project_name,data_date ) a 
LEFT JOIN 
(
    SELECT DISTINCT 
                project_name
                ,total_house_num  -- 总套数
                ,sold_house_num + 0 AS sold_house_num  -- 已售住宅套数
                ,house_avg_price  -- 住宅均价
                ,sold_not_house_num + 0 AS sold_not_house_num  -- 已售非住宅套数
                ,not_house_avg_price  -- 非住宅均价
                ,data_date
            FROM yj_houses.yj_houses_selling_info WHERE data_date = '2021-12-18'
            AND (
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
    OR project_name LIKE '%碧桂园凤凰湾%') ORDER BY project_name,data_date
) b ON a.project_name = b.project_name;