build-docker-test:
	docker build -t azamuku-test ./azamuku

test-unit: build-docker-test
	docker run azamuku-test nose2 -v -A unit

test-integration: build-docker-test
	docker-compose -f docker-compose.dev.yml up --build -d
	docker-compose -f docker-compose.dev.yml run web nose2 -v -A integration
	docker-compose -f docker-compose.dev.yml stop

test-coverage: build-docker-test
	docker-compose -f docker-compose.dev.yml up --build -d
	docker-compose -f docker-compose.dev.yml run web nose2 -v -A integration -A unit --with-coverage --coverage-report html
	docker-compose -f docker-compose.dev.yml stop

test: test-unit test-integration
