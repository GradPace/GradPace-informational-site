.PHONY: help dev dev-docker compose-deploy compose-up compose-down compose-logs compose-restart k8s-apply k8s-deploy k8s-rollback k8s-logs k8s-restart k8s-down clean test deploy sync add install

NAMESPACE = gradpace-info
REGISTRY_IMAGE = ghcr.io/gradpace/gradpace-informational-site/flask-app

# k8s-deploy pins to this tag instead of :latest - a :latest update can no-op
# if the cluster doesn't see the tag string itself change, even though the
# digest behind it moved. CI passes TAG=sha-<short sha>. Defaults to latest
# for manual use.
TAG ?= latest

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

dev: ## Run Flask development server locally
	cd website && uv run python main.py

dev-docker: ## Run Flask in Docker for development
	docker compose -f docker-compose.development.yml up

# Docker Compose production commands
compose-deploy: ## Pull latest image and deploy with docker compose
	@export $$(grep -v '^#' .env.production | xargs) && \
	docker compose -f docker-compose.production.ghcr.yml --env-file .env.production pull && \
	docker compose -f docker-compose.production.ghcr.yml --env-file .env.production up -d && \
	docker image prune -af

compose-up: ## Start services with docker compose (updates web if image changed)
	@export $$(grep -v '^#' .env.production | xargs) && \
	docker compose -f docker-compose.production.ghcr.yml --env-file .env.production pull web && \
	docker compose -f docker-compose.production.ghcr.yml --env-file .env.production up -d web && \
	docker image prune -af

compose-down: ## Stop and remove docker compose services
	docker compose -f docker-compose.production.ghcr.yml --env-file .env.production down

compose-logs: ## View logs from docker compose services
	docker compose -f docker-compose.production.ghcr.yml --env-file .env.production logs -f

compose-restart: ## Restart docker compose services
	docker compose -f docker-compose.production.ghcr.yml --env-file .env.production restart

logs: ## View logs from running containers
	docker compose -f docker-compose.production.ghcr.yml --env-file .env.production logs -f

k8s-apply: ## Apply/update the k8s manifests (namespace, deployment, service, ingress)
	kubectl apply -f k8s/

k8s-deploy: ## Force a fresh pull + redeploy on k3s. Pass TAG=<tag> to pin a build (defaults to latest)
	kubectl set image deployment/web web=$(REGISTRY_IMAGE):$(TAG) -n $(NAMESPACE)
	kubectl rollout status deployment/web -n $(NAMESPACE)

k8s-rollback: ## Roll the web deployment back to its previous version on k3s
	kubectl rollout undo deployment/web -n $(NAMESPACE)

k8s-logs: ## Tail logs from the web deployment on k3s
	kubectl logs -f deployment/web -n $(NAMESPACE)

k8s-restart: ## Force a rolling restart on k3s
	kubectl rollout restart deployment/web -n $(NAMESPACE)

k8s-down: ## Remove everything in the k8s namespace
	kubectl delete namespace $(NAMESPACE)

clean: ## Clean up Python cache and Docker resources
	find . -type d -name __pycache__ -exec rm -r {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	docker system prune -af

install: ## Install Python dependencies
	cd website && uv sync

test: ## Run tests (when implemented)
	cd website && uv run pytest

deploy: ## Alias for compose-deploy
	@export $$(grep -v '^#' .env.production | xargs) && \
	docker compose -f docker-compose.production.ghcr.yml --env-file .env.production pull && \
	docker compose -f docker-compose.production.ghcr.yml --env-file .env.production up -d && \
	docker image prune -af

sync: ## Sync dependencies to lock file
	cd website && uv sync

add: ## Add a new dependency (usage: make add PACKAGE=flask-cors)
	cd website && uv add $(PACKAGE)
