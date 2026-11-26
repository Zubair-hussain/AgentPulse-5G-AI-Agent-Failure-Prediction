// Match the portable Python predictor with no remote inference calls.
export function predict(record, model, schema) {
  const features = schema.features;
  if (JSON.stringify(model.features) !== JSON.stringify(features)) {
    throw new Error('Model schema mismatch');
  }
  if (!record || typeof record !== 'object' || Array.isArray(record) ||
      Object.keys(record).length !== features.length ||
      features.some(key => !Object.hasOwn(record, key))) {
    throw new Error('Exactly the documented features are required');
  }
  let linear = 0;
  features.forEach((key, i) => {
    const value = record[key];
    const [low, high] = schema.ranges[key];
    if (typeof value !== 'number' || !Number.isFinite(value) ||
        value < low || (high !== null && value > high)) {
      throw new Error(`Invalid ${key}`);
    }
    linear += model.coef[i] * (value - model.mean[i]) / model.scale[i];
  });
  const z = Math.max(-700, Math.min(700, model.intercept + linear));
  const risk = 1 / (1 + Math.exp(-z));
  return {failure_risk: risk, threshold: model.threshold, flagged: risk >= model.threshold};
}
