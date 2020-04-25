 only accept POST request at /mock url. body: {"payload":"some_text_as_payload"}
 this service use a random number to decide it the response is 201 (80%) or 400 (20%) in order to mock also broken subscribers
 
To use it with the docker compose configuration in the main project, you need to create the image as:

 docker build -t mockedsubscriber .
 
