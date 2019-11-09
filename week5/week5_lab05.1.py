
# Lab05.1_CURL

# curl google.com

# 2 
# curl -i google.com

# 3
# curl http://dummy.restapiexample.com/api/v1/employees
# curl http://dummy.restapiexample.com/api/v1/employee/2202

# 4
# curl -X DELETE http://dummy.restapiexample.com/api/v1/delete/1000

# 5
# curl -i -d “{\"name\":\"jj\",\"salary\":\"123\",\"age\":\"23\"}” H “Content-Type: application/json” -X POST
# http://dummy.restapiexample.com/api/v1/create 

# 6
# curl -d “{\"name\":\"Mary\",\"salary\":\"12000\",\"age\":99}” -H “Content-Type: application/json” -X PUT
# http://dummy.restapiexam ple.com/api/v1/update/2202