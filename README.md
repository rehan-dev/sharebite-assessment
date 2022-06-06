# sharebite-assessment
Restaurant Menu Python Flask Based API 

## Way to run this API Application
1. Install python 
2. Add virtual enviroment using python -m venv env
3. Activate env 
4. pip install requirement.txt

# API ENDPOINTS


1. http://127.0,0.1:5000/api/v1/sections   - REST API GET, POST, PUT, DELETE
2. http://127.0,0.1:5000/api/v1/items      - REST API GET, POST, PUT, DELETE - Add section id in json post request in order to associate section with items
3. http://127.0,0.1:5000/api/v1/modifiers  - REST API GET, POST, PUT, DELETE
4. http://127.0,0.1:5000/api/v1/mappers    - ONLY POST - Map items and mappers using ids {'item_id': 1, 'modifier_id':2}
5. http://127.0,0.1:5000/api/v1/menu       - ONLY GET - Show all the data as you want in you assessment.
