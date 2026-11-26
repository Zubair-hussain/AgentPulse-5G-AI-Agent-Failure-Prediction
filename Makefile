.PHONY: test validate train predict
validate:
	python -m tools.validate_data
test:
	python -m pytest -q
train:
	python -m agentpulse.train
predict:
	python -m agentpulse.predict examples/telemetry.json
