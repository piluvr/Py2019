cidrlist =["128.0.0.0","192.0.0.0","224.0.0.0","240.0.0.0","248.0.0.0","252.0.0.0","254.0.0.0","255.0.0.0","255.128.0.0","255.192.0.0","255.224.0.0","255.240.0.0","255.248.0.0","255.252.0.0","255.254.0.0","255.255.0.0","255.255.128.0","255.255.192.0","255.255.224.0","255.255.240.0","255.255.248.0","255.255.252.0","255.255.254.0","255.255.255.0","255.255.255.128","255.255.255.192","255.255.255.224","255.255.255.240","255.255.255.248","255.255.255.252","255.255.255.254","255.255.255.255"]
ipinput=input("input an ip with cider (ex:xxx.xxx.xxx.xxx/xx): ")
cidr1,cidr = ipinput.split('/')
ipinput=ipinput[:-(len(ipinput)-ipinput.index('/'))]
first, second, third, fourth = str(ipinput).split('.')
first1, second1, third1, fourth1 = str(cidrlist[int(cidr)-1]).split('.')
final=((int(first) & int(first1)))
final2=((int(second) & int(second1)))
final3=((int(third) & int(third1)))
final4=((int(fourth) & int(fourth1)))
'''
final=final[2:]
final2=final2[2:]
final3=final3[2:]
final4=final4[2:]
'''
print(bin(final)+'.'+bin(final2)+'.'+bin(final3)+'.'+bin(final4))
print(str(final)+'.'+str(final2)+'.'+str(final3)+'.'+str(final4))
