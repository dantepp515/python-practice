import re;

pattern = "([a-z|0-9]+)@([a-z|\D]+).com|cn$";
str = "hanli@co-mall.com.cn";
m = re.match(pattern , str);
print(m.group());
str = "发送手机号$telphone$给$telphone$";
pattern = "([$]telphone[$])";
m = re.search( pattern , str );
print(re.sub(pattern , "1521069821" , str));
print(re.subn(pattern , "1521069821" , str));