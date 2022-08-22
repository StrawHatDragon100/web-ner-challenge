default:
	@echo "An explicit target is required"
	
install:
	cd $(FRONTEND) && npm install
	cd $(BACKEND) && pip install -r requirements.txt

start:
	export FLASK_PORT=5000
	cd $(FRONTEND) && ng serve --proxy-config src/proxy.conf.json &
	cd $(BACKEND) && flask run
