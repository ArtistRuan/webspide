drop table yj_houses_selling_info;
create table if not exists yj_houses_selling_info (
id int unsigned auto_increment primary key
,project_name varchar(320)  -- 项目名称
,project_address varchar(1024)  -- 项目座落
,project_builder varchar(1024)  -- 开发商
,project_distinct varchar(100)  -- 所在地区
,project_total_builder_area varchar(100) -- 总建筑面积
,project_area varchar(100)  -- 占地面积
,total_house_num varchar(100)  -- 总套数
,total_area varchar(100)  -- 总面积
,house_num varchar(100)  -- 住宅套数
,house_area varchar(100)  -- 住宅面积
,not_house_num varchar(100) -- 非住宅套数
,not_house_area varchar(100) -- 非住宅面积
,sold_house_num varchar(100)  -- 已售住宅套数
,sold_house_area varchar(100)  -- 已售住宅面积
,house_avg_price varchar(100)  -- 住宅均价	
,sold_not_house_num varchar(100)  -- 已售非住宅套数
,sold_not_house_area varchar(100)  -- 已售非住宅面积
,not_house_avg_price varchar(100)  -- 非住宅均价
,data_date varchar(100)  -- 时间时间
) engine myisam charset utf8;

