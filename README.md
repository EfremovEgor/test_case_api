
## Clone repo
    git clone https://github.com/EfremovEgor/test_case_api.git
# Run Docker Container
API used to get currency exchange rates: https://freecurrencyapi.com/docs/latest
API_KEY for tests:

    fca_live_htROcuQggEMP9IO0Een3mhkRvI2R2XFCVtI1icZY

change API_KEY in src/settings.py if needed

    docker compose up --build -d
Swagger Docs http://localhost:8000/api	

# Run tests(On your machine)
Change THIS_API_URL in tests/setting.py if needed. 
Change API_KEY in tests/setting.py if needed

    cd tests
    pip install -r requirements.txt
	python3 currency_exchange_test.py

