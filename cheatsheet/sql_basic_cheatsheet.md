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
limit n offset k
```

偏移量为k，选择接下来的n行

***

交，并，差

```sql
(select * from t1) 
union
(select * from t2)
```

```sql
(select * from t1)
intersect
(select * from t2)
```

```sql
(select * from t1)
except
(select * from t2)
```

上面的三个都是多重集的运算，如果需要去重，则使用`union all`,`intersect all`,`except all`即可

***

null value

涉及到空值的任何比较运算的结果都视为`unknown`

涉及到空值的算术表达式的结果都为空

对于布尔运算，只有`false and unknown = false`和`true or unknown = true`，其他的结果也都为`unknown`

`null = null`的结果为`unknown`，而非true

去重时，如果两个值非空且相等，或都为空则视为相同

***

聚集函数

```sql
select aggregate(c1) from t
```

```sql
select aggregate(distinct c1) from t
```

```sql
select aggregate(c1), c2 from t
group by c2
```

对于普通的属性，在含有聚合运算的语句中，他们要么是聚合运算的参数，要么在`group by`中出现

```sql
select c1, aggregate(c2) from t
group by c1
having condition
```

`having`语句用于对分组限定条件，其中可以用聚合函数

`having`中的没有被聚集的属性必须要出现在`group by`中，因为having是对组进行判断，而非单个元组

运算序列：

1. 使用from得到关系
2. 将where中的谓词应用到1中的关系上
3. 使用group by对2中的关系进行分组
4. 将having应用到3中的每个分组中
5. 根据select语句进行输出

对于空值的聚集，除了`count(*)`外所有的聚集函数都将忽略空值

***

`in`和`not in`用来测试元组是否在给定的集合中

```sql
select c1 from t
where c1 [not] in value_list
```

`some(any)`和`all`用于集合比较

对应特称量词和全称量词

```sql
select c1 from t
where c1 > all value_list
```

大于所有的value_list中的值

```sql
select c1 from t
where c1 > some value_list
```

大于任意一个value_list中的值即可


`exists`用来测试集合是否为空集

exists当作为参数的子查询非空时为true，否则为false

`unique`用来测试集合中是否有重复元组

当作为参数的子查询中无重复元组时，unique为true，否则为false

***

`with`用于临时定义关系

```sql
with t2(val) as 
    (select v from t2)
select t2.val t1.val from t1, t2
```

with中，后一个语句可以使用前一个语句中定义的关系的属性

***

数据库的修改

```sql
delete from r
where P
```

删除r中满足P的元组

delete每次只能作用与一个关系，所以当需要在多个关系中删除元组的时候，我们需要多条指令

```sql
insert into r
    values(v1, v2, ...)
```

用于在r中插入元组，同时可以在插入的时候指定属性

```sql
insert into r(Aj1, Aj2, ...)
    values(vj1, vj2, ...)
```

```sql
update r
set a = b
```

更新r中的元组，同样可以应用谓词

可以使用case语句配合更新

```sql
case
    when p1 then res1
    when p2 then res2
    ...
    else res0
end
```

