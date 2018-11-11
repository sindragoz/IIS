from FileReader import FileReader
import numpy
import math
from scipy.stats import linregress
from collections import Counter
import operator

class PassengerStatistics(object):

	passengers=[]
	def setPassengers(self,passList):
		self.passengers=passList
        pass

	def countMaleAndFemale(self):
		male_cnt=0
		female_cnt=0
		for p in self.passengers:
			if(p['Sex']=="male"):
				male_cnt+=1
			else:
				female_cnt+=1
		return [male_cnt,female_cnt]

	def countSurvived(self):
		survived=0
		for p in self.passengers:
			survived+=int(p['Survived'])
		return round(100*float(survived)/float(len(self.passengers)),2)

	def countFirstClassPassengers(self):
		fcp=0
		for p in self.passengers:
			if(int(p['Pclass'])==1):
			  fcp+=1
		return round(100*float(fcp)/float(len(self.passengers)),2)

	def countAgeMedianAndMean(self):
		ages=[]
		for p in self.passengers:
			if(p['Age']!=''):
			  ages.append(int(float(p['Age'])))
		return [int(numpy.median(ages)),int(numpy.mean(ages))]
	
	def CountCorellation(self):
		sibsp=[]
		parch=[]
		for p in self.passengers:
			sibsp.append(int(p['SibSp']))
			parch.append(int(p['Parch']))
		return round(float(linregress(sibsp, parch).rvalue),4)

	def findMostPopularFemaleName(self):
		fnames=[]
		for p in self.passengers:		
			if(p['Sex']=='female'):
				if(("Mrs" in p['Name'])&(not "Miss" in p['Name'])):				
					if('(' in p['Name']):
						fnames.append(p['Name'].split(',')[1].split('.')[1].split('(')[1].split(' ')[0].replace(')','').replace(' ',''))					
					else:
						fnames.append(p['Name'].split(',')[1].split('.')[0].replace(')','').replace(' ',''))
				elif ("Dr." not in p['Name']):
					fnames.append(p['Name'].split(',')[1].split('.')[1].split(' ')[1].replace(')','').replace(' ',''))
				else:
					fnames.append(p['Name'].split(',')[1].split('.')[1].split(' ')[1].replace(')','').replace(' ',''))
		return max(Counter(fnames).iteritems(), key=operator.itemgetter(1))[0]