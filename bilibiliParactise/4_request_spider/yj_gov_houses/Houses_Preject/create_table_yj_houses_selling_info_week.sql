drop table if exists yj_houses_selling_info_week;
create table if not exists yj_houses_selling_info_week (
id int unsigned auto_increment primary key comment '主键id'
,project_name varchar(320)  comment '项目名称'
,project_distinct varchar(100)  comment '所在地区'
,total_house_num varchar(100) comment '总套数'
,sold_house_num varchar(100)  comment '已售住宅套数'
,week_sold_house_num varchar(100)  comment '本周已售住宅套数'
,house_avg_price varchar(100)  comment '住宅均价'	
,sold_not_house_num varchar(100)  comment '已售非住宅套数'
,week_sold_not_house_num varchar(100)  comment '本周已售非住宅套数'
,not_house_avg_price varchar(100)  comment '非住宅均价'
,data_date varchar(100)  comment '数据批次时间'
) engine myisam comment '阳江商品房成交周表（含阳江江城及阳东）' charset utf8;

