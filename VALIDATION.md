# Release validation

Source syntax and notebook code cells are checked on Python 3.11 and 3.12 by the included workflow. These source checks do not run training, databases, paid model providers, or external simulations. Additional runtime checks are recorded below when executed.

Full historical experiment reproduction is separate from source validation. No new benchmark result is inferred from syntax checks.

## Complete notebook execution

Fresh execution reports a high-minus-low alcohol difference of 1.5598 percentage points, Welch 95% CI [1.4850, 1.6346], and pooled-SD Cohen’s d of 1.5782. The directional Welch p-value is approximately 8.68×10⁻²⁶⁵.

All 16 code cells executed successfully in an isolated CPU process. No model-provider calls were made. Source/input hashes and dependency versions are recorded in `results/reproduction.json`. The raw inputs and raw execution logs are not distributed.
