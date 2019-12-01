from ZstudentDAO import studentDAO

# We put in the data we get passed up from the json

#create
latestid = studentDAO.create(('Eilish', 22))

#find by id
result = studentDAO.findByID(latestid); # needs to be made into json object
print (result)

#update
studentDAO.update(('Liam',23,latestid))
result = studentDAO.findByID(latestid);
print (result)

#getall
allStudents = studentDAO.getAll()
for student in allStudents:
  print(student)

#delete
studentDAO.delete(latestid)