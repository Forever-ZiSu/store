S1="T血";S2="衬衫";S3="风衣";S4="牛仔裤";S5="皮草";S6="羽绒服"
J1=65.8;J2=49.3;J3=96.8;J4=86.3;J5=135.9;J6=253.6
l1=63+45+129+63+58+48+63;l2=120;l3=43+25+43+60+43+78;l4=60+72+35+90+60+60+140;l5=63+24+63+57;l6=10+69+140+10+10
zl=l1+l2+l3+l4+l5+l6
z1=J1*l1;z2=J2*l2;z3=J3*l3;z4=J4*l4;z5=J5*l5;z6=J6*l6
zsum=z1+z2+z3+z4+z5+z6
print("总销售额：",zsum)
print("所有服装平均每日销售数量：",(l1+l2+l3+l4+l5+l6)/28)
print(S1,"平均每日销售数量：",l1/7)
print(S2,"平均每日销售数量：",l2/1)
print(S3,"平均每日销售数量：",l3/6)
print(S4,"平均每日销售数量：",l4/7)
print(S5,"平均每日销售数量：",l5/4)
print(S6,"平均每日销售数量：",l6/5)
print("每个种类月销售量占比：")
print(S1,"：",l1/zl)
print(S2,"：",l2/zl)
print(S3,"：",l3/zl)
print(S4,"：",l4/zl)
print(S5,"：",l5/zl)
print(S6,"：",l6/zl)