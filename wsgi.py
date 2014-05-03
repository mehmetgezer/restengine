from wsgiref.simple_server import make_server

from restengine import RestEngine



base_url = "/api/v1"
api = ["/users/",  # retrieve all users, put user(s)
       "/users/numeric:id",  # retrieve user by numeric id
       "/users/:name/:surname/cars",  # retrieve user(s) by name and surname, patch user(s)
       "/users/numeric:id/cars",
       "/users/numeric:id/cars/:motor",
       "/users/:id/cars/numeric:id",
       "/users/:id/cars/:model"]


#===============================================================================

wsgi = make_server('', 8080, RestEngine(base_url, api))
print("Serving on port 8080...")
wsgi.serve_forever()
# Serve until process is killed
