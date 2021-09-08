### SQL Basic Cheatsheet

语句后加`;`

##### 模式定义

类型

`char(n)` 定长字符串

`varchar(n)` 最大长度为n的变长字符串

`int` 整数

`smallint` 小整数

`numeric(p, d)` p(precision)位数，小数点有d(dot)位

`real,double precision` 浮点数，双精度浮点数

`float(n)` 精度至少为n位数的浮点数

```sql
create table r
    (A1 D1,
    A2 D2,
    A3 D3,
    ...,
    An Dn,
    <完整性约束1>,
    ...,
    <完整性约束k>);
```

A(attribute)为属性

D(domain)为域，指定类型和限制

完整性约束：

主键:`primary key(Aj1, Aj2, ..., Ajm)`

外键:`foreign key(Ak1, Ak2, ..., Akn) references s`

非空:`not null`

`drop table r` 删除表

`delete from r` 删除表中数据

`alter table r add A D` 为表r添加属性，A为名称，D为类型

`alter table r drop A` 删除表r的属性A

##### 查询

```sql
select c1, c2 from t
```

从t中查询c1,c2

***

```sql
select * from t
```

从t中查询所有属性

***

```sql
select distince c1 from t
```

从表中查询去重后的c1

***

```sql
select c1 from t
where condition
```

在condition条件下查询c1

***

通式

```sql
select A1, A2, ..., An
from r1, r2, ..., rn
where P
```

r(relation)关系，P(predicate)谓词

理解：

```python
for t1 in r1:
    for t2 in r2:
        ...
        for tn in rn:
            将t1, t2, ..., tn连接成t
            将满足P的元组t加入到结果中
```

1.为from子句列出的关系产生笛卡尔积
2.在1的结果上应用谓词
3.根据select输出指定的属性

***

更名运算`as`可以运用到`from`中，也可以运用到`select`中

```sql
old-name as new-name
```

***

单引号标识字符串，两个单引号表示字符串内的单引号

`%`可以用来匹配任意字串
`_`可以用来匹配任意一个字符

使用`like`来表达模式

```sql
where name like '%Comp%'
```

***

```sql
select c1, c2 from t
order by c1 asc, c2 desc
```

c1属性升序排序，c2降序，优先级从左到右

```sql
select c1, c2 from t
order by c1
limit n offset of
```

偏移量为of，选择接下来的n行

***