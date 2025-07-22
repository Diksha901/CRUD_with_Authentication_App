#  CRUD,Authentication with FASTAPI 

This project focuses on developing a CRUD Application where Users can register themselves , create ,update , delete and read blogs. 
The project also develops an authentication feature to permit only the authorized user  to alter our database .   

---

##  Files in This Repository

- *`blog`* — The directory containing all the routes , functions to connect to our database , models of our tables , schemas etc.
- `main.py` - Contains API routes and our FASTAPI instance (app=FastAPI())
- `config.py` - Contains Settings() class to get access to confidential information like SECRET_KEY to get JWT Token and variables necessary for our database setup .
- `oauth2.py` - Contains Functions to authenticate the user using JWT tokens and the get_user_functionality to only allow authorized user
- `hashing.py` - Uses passlib to hash the password entered by the user
- *`routers`* - Directory containing files in which actual CRUD Functions are written such as **blog.py** ,**user.py**,**authenticate.py**,**like.py**
- *`db`* - Directory containing files in which we have specified structures of our tables(**models.py**) , pydantic models(**schemas.py**) and how to connect to the database (**database.py**)
- `requirements.txt` - The list of dependencies(python,sqlalchemy,psycopg2 ...etc.)  requirerd to run the application 
- `README.md` — You’re reading it!

# Project Structure :
fastapi_project/

  
--->`blog/`

------> main.py 

------>config.py

------>oauth2.py

------>hashing.py

------>`routers/`

       ---->authentication.py
       
       ---->blog.py
       
       ---->like.py
       
       ---->user.py
       
------>`db/`

       ---->models.py
       
       ---->schemas.py
       
       ----> database.py
       
---->venv(gitignored) 

---->requirements.txt

---->README.md


---

##  APIs Implemented

1. **/login : Post Request**
   - To get the JWT token to be authorized to alter the database
   - To perform all different operation on blogs and users , a person needs to login first
2. **/user/create:Post Request**
   - To create a user in the database with name,email and password .
   - Validate the datatypes of name,email and password using pydantic.

3. **/user/{id}:Get Request**
   - To get a user and the blogs he/she has created.
   - Doesn't show password to maintain data integrity.

4. **/blogs/blogs: Post Request**
   - Helps the authenticated user to create a blog .

5. **/blogs/all : Get Request**
   - To get all the blogs in the database .
   - Uses ShowUser pydantic model from schemas.py to show the blog title, content and the creator of the blog.

6. **/blogs/{id} : Get Request**
   - To get a blog by its id

7. **/blogs/ :Get Request**
   - To get a blog using a matching keyword in the blog title
   - Has offset(to skip rows) , limit(to show a specified number of rows from the table) functionality too .

8. **/blogs/display/likes :Get Request** 
    - To get how many upvotes or likes a blog has got 

9. **/blogs/{id} :Put Request** 
    - To update a blog's title and content
    - Only allows the owner of the blog to update the blog 

10. **/blogs/{id} :Delete Request** 
    - To delete a blog 
    - Only the owner of the blog can delete the blog
      
11. **/likes/: Post Request**
    - Submits an upvote or like to the blog
    - Can downvote too if dir = 0 
---


##  TechStack 

> `FastAPI` : to develop the app as an FastAPI instance and to use APIRouter so the code in main .py is not cluttered

> `PostgreSQL` : Database to create and store the tables(blogs,users,likes from models.py) and their data

> `SQLAlchemy` : To setup the database session in python and to access the database in the application.

> `Pydantic` : BaseModel to validate the datatypes of various fields being used in the schema.py


  

---
