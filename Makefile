.PHONY: install
install:
	poetry install

.PHONY: codegen
codegen:
	poetry run python -m grpc_tools.protoc \
		-I./pb/protos \
		--python_out=./pb \
		--grpc_python_out=./pb \
		./pb/protos/helloworld.proto

.PHONY: up
up:
	poetry run python main.py