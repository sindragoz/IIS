from sklearn.linear_model import LinearRegression, Ridge, Lasso, RandomizedLasso
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import RFE, f_regression
import numpy as np 

#���������� �������� ������: 750 �����-���������� � 14 ��������-���������
np.random.seed(0)
size = 750
X = np.random.uniform(0, 1, (size, 14))
#������ �������-�����: ������������� �������� ��������
Y = (10 * np.sin(np.pi*X[:,0]*X[:,1]) + 20*(X[:,2] - .5)**2 +
 10*X[:,3] + 5*X[:,4]**5 + np.random.normal(0,1))
#��������� ����������� ���������
X[:,10:] = X[:,:4] + np.random.normal(0, .025, (size,4)) 
#�������� ������
lr = LinearRegression() 
lr.fit(X, Y)
#��������� ������
ridge = Ridge(alpha=7)
ridge.fit(X, Y)
#�����
lasso = Lasso(alpha=.05)
lasso.fit(X, Y) 
#��������� �����
rdl=RandomizedLasso()
rdl.fit(X, Y) 
names = ["x%s" % i for i in range(1,15)] 

#����������� ���������� ���������
lr = LinearRegression()
lr.fit(X, Y)
rfe = RFE(lr)
rfe.fit(X,Y)

#���������� ��������� ���������� ���������
rfr=RandomForestRegressor()
rfr.fit(X,Y)

#�������� ����������
f = f_regression(X, Y, center=True) 

def rank_to_dict(ranks, names):
 ranks = np.abs(ranks)
 minmax = MinMaxScaler()
 ranks = minmax.fit_transform(np.array(ranks).reshape(14,1)).ravel()
 ranks = map(lambda x: round(x, 2), ranks)
 return dict(zip(names, ranks)) 

ranks={}
ranks["Linear reg"] = rank_to_dict(lr.coef_, names)
ranks["Ridge"] = rank_to_dict(ridge.coef_, names)
ranks["Lasso"] = rank_to_dict(lasso.coef_, names) 
ranks["Randomized Lasso"] = rank_to_dict(rdl.all_scores_, names) 
ranks["RFE"] = rank_to_dict(rfe.ranking_, names) 
#ranks["F regression"] = rank_to_dict(pval, names) 
ranks["F regression"] = rank_to_dict(f[1:14:1], names) 

mean = {}
for key, value in ranks.iteritems():
 for item in value.iteritems():
  if(item[0] not in mean):
   mean[item[0]] = 0
  mean[item[0]] += item[1]
for key, value in mean.iteritems():
 res=value/len(ranks)
 mean[key] = round(res, 2)
mean = sorted(mean.iteritems(), key=lambda (x, y): y, reverse=True)
print "MEAN"
print mean

for key, value in ranks.iteritems():
 ranks[key] = sorted(value.iteritems(), key=lambda (x, y): y, reverse=True)
for key, value in ranks.iteritems():
 print key
 print value