import csv
class FileReader(object):

	def csv_reader(self,file_obj):
		passengersList=[]
		reader = csv.DictReader(file_obj, delimiter=',')
		for row in reader:
		  passengersList.append(row)
		return passengersList

	def readFile(self,path):
	 with open("titanic.csv" , "r") as f_obj:
	   lis=self.csv_reader(f_obj)
	 return lis
