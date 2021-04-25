all: test image

test:
	bats src/test/test.bats

image: Dockerfile
	docker build -t cdeutsch/configtemplate:latest .

push: image
	docker push cdeutsch/configtemplate:latest
	docker push cdeutsch/configtemplate:$(git describe --tags --abbrev=0)
