from FileReader import FileReader
import statistics
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
		return [numpy.median(self.passengers),numpy.mean(self.passengers)]