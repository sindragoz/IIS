from FileReader import FileReader
from PassengerStatistics import PassengerStatistics

fr=FileReader()
ps=PassengerStatistics()
path='titanic.csv'
ps.setPassengers(fr.readFile(path))
sex_cnt=ps.countMaleAndFemale()
survived=ps.countSurvived()
fcp=ps.countFirstClassPassengers()
ages=ps.countAgeMedianAndMean()
corr=ps.CountCorellation()
popular_fem_name=ps.findMostPopularFemaleName()
print "Males: ",sex_cnt[0]
print "Females: ",sex_cnt[1]
print "Survived: ",survived,"%"
print "1st class passengers: ",fcp,"%"
print "Age median: ",ages[0]
print "Age middle: ",ages[1]
print "Pierce corellation: ", corr
print "Most popular name: ", popular_fem_name