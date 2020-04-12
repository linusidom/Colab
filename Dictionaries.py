#Print print_me from the dictionary
d1 = {'k1':'print_me'}
d2 = {'k1':{'k2':'print_me'}}
d3 = {'k1':[{'nested_key':['37',['print_me']]}]}
sim_d3 = d3['k1'][0]['nested_key'][1]
print(d1['k1'])
print(d2['k1']['k2'])
print(*sim_d3)
