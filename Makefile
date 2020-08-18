.PHONY: install
install:
	poetry install

.PHONY: codegen
codegen:
	poetry run python -m grpc_tools.protoc \
		-I./src/pb/protos \
		--python_out=./src/pb \
		--grpc_python_out=./src/pb \
		./src/pb/protos/*.proto

.PHONY: up
up:
	docker-compose up --build

.PHONY: down
down:
	docker-compose down