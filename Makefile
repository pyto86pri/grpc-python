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
	poetry run python src/main.py

.PHONY: aioup
aioup:
	poetry run python src/aio/main.py