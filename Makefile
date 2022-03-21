M = $(shell printf "\033[34;1m▶\033[0m")

.PHONY: help
help: ## Prints this help message
	@grep -E '^[a-zA-Z_-]+:.?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

######################
### MAIN FUNCTIONS ###
######################

.PHONY: python_build_lambda
python_build_lambda: ## Build the python_lambda docker container
	$(info $(M) Build an instance of lambda for Python)
	@docker build -t mraynov/lambda-python-local -f docker/Dockerfile.python .


.PHONY: python_start_lambda
python_start_lambda: ## Start the python_lambda docker container
	$(info $(M) Starting an instance of lambda)
	@docker stack rm python_lambda
	@docker stack deploy -c ./docker/docker-compose-python-swarm.yml python_lambda

.PHONY: python_stop_lambda
python_stop_lambda: ## Stopping running python_lambda instances
	$(info $(M) Stopping lambda instance)
	@docker stack rm python_lambda

.DEFAULT_GOAL := help