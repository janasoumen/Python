from pyLogFunctions import *
method_list = ['=>REGISTER','=>INVITE','RTCP out 30','RTCP out 28','Partial Service Detection', 'Received Data state is -------->UP','Received Data state is -------->DOWN']

for methods in method_list:
  print(methods,"=====>",isPresent(methods), "=" ,  isCount(methods))



  

