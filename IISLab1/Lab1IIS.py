from FileReader import FileReader
from PassengerStatistics import PassengerStatistics

fr=FileReader()
ps=PassengerStatistics()
path='titanic.csv'
ps.setPassengers(fr.readFile(path))
sex_cnt=ps.countMaleAndFemale()
survived=ps.countSurvived()
fcp=ps.countFirstClassPassengers()
age_median=ps.countAgeMedianAndMean()
print "Males: ",sex_cnt[0]
print "Females: ",sex_cnt[1]
print "Survived: ",survived,"%"
print "1st class passengers: ",fcp,"%"
print "Age median: ",age_median
print "Age middle: ",age_median