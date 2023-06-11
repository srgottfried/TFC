deploy: build up

build:
	docker compose build rasa
	docker compose build rasa-actions
	docker compose build fastapi
	docker compose build rocketchat
	docker compose build mongo

up:
	docker compose up

down:
	docker compose down

init:
	docker cp ./dump mongo:/dump
	docker compose exec mongo mongo --eval 'db.getSiblingDB("rocketchat").rocketchat_settings.update({_id: "Show_Setup_Wizard"},{$set: {"value": "completed"}});'
	docker compose exec mongo mongorestore --drop dump/