APP_NAME := http-helloworld-python-simple
DOCKER_USER := andreyevbr
IMAGE := $(DOCKER_USER)/$(APP_NAME):latest
CHART_DIR := http-helloworld-python-simple
CHART_PACKAGE := $(APP_NAME)-0.1.0.tgz

.PHONY: all build push

all: build push

build:
	docker build -t $(IMAGE) ./

push:
	docker push $(IMAGE)
